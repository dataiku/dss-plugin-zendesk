import requests
import re
import logging
from zendesk_constants import ZD

zendesk_response = {
    "search": "results",
    "users": "users",
    "organizations": "organizations",
    "groups": "groups",
    "tickets": "tickets",
    "satisfaction_ratings": "satisfaction_ratings",
    "ticket_events": "ticket_events"
}

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format='zendesk plugin %(levelname)s - %(message)s')


class ZendeskClient():
    def __init__(self, config):
        self.config = config
        self.zendesk_access_type = self.config.get("zendesk_access_type")
        self.zendesk_api = self.config.get("zendesk_api")
        self.connection = self.config.get(self.zendesk_access_type + "_access")
        if self.zendesk_access_type == "token":
            self.zendesk_username = self.connection["zendesk_username"] + "/token"
        else:
            self.zendesk_username = self.connection["zendesk_username"]
        self.zendesk_password = self.connection["zendesk_password"]
        self.auth = (self.zendesk_username, self.zendesk_password)
        self.subdomain = self.connection["zendesk_subdomain"]

    def search(self, search_options):
        args = self.parse_search_options(search_options)
        if args['type'] == "free":
            query = search_options['zendesk_query']
            url = self.get_free_search_query_url(query)
        else:
            url = self.get_search_url(**args)
        data = self.get(url)
        return data

    def any(self, search_options):
        parameters = self.parse_api_options(self.zendesk_api, search_options)
        incremental_api_parameters = self.parse_api_options("incremental", search_options)
        if "api" in incremental_api_parameters and incremental_api_parameters["api"] is True:
            url = self.get_incremental_api_url(incremental_api_parameters)
        else:
            url = self.get_generic_url(parameters)
        data = self.get(url)
        return data

    def get(self, url):
        response = requests.get(url, auth=(self.zendesk_username, self.zendesk_password))
        if response.status_code != 200:
            if response.status_code == 422:
                raise Exception("Query result is over the 1,000 results limit")
            else:
                raise Exception("Error {}".format(response.status_code))
        data = response.json()
        self.update_next_page(data)
        return data[zendesk_response[self.zendesk_api]]

    def update_next_page(self, data):
        if ZD.END_OF_STREAM in data and data[ZD.END_OF_STREAM] is True:
            self.next_page_url = None
            self.after_cursor = None
        else:
            if ZD.NEXT_PAGE in data:
                self.next_page_url = data[ZD.NEXT_PAGE]
            else:
                self.next_page_url = None
            if ZD.AFTER_CURSOR in data:
                self.after_cursor = data[ZD.AFTER_CURSOR]
            else:
                self.after_cursor = None

    def get_next_page(self):
        return self.get(self.next_page_url)

    def has_next_page(self):
        return self.next_page_url is not None

    def with_type(self, type):
        if type is None or type == "":
            return ""
        else:
            return ZD.TYPE.format(type)

    def get_search_query(self, type=None, status=None, first_date=None, last_date=None):
        if self.zendesk_api != "search":
            return []
        search_tokens = []
        if type is not None:
            search_tokens.append(ZD.TYPE.format(type))
        if status is not None:
            search_tokens.append(ZD.STATUS.format(status))
        if first_date is not None:
            search_tokens.append(first_date)
        if last_date is not None:
            search_tokens.append(last_date)
        if len(search_tokens) > 0:
            search_string = ZD.QUERY.format(" ".join(search_tokens))
        else:
            search_string = ""

        return [search_string]

    def get_query_string(self, query_options):
        if isinstance(query_options, list) and len(query_options) > 0:
            return "?" + "&".join(query_options)
        else:
            return ""

    def get_search_url(self, type=None, status=None, first_date=None, last_date=None):
        return self.get_base_url() + self.get_search_edge() + self.get_query_string(self.get_search_query(type, status, first_date, last_date))

    def get_free_search_query_url(self, query):
        return self.get_base_url() + self.get_search_edge() + self.get_query_string(["query=" + query])

    def get_generic_url(self, parameters):
        return self.get_base_url() + self.get_edge_point() + self.get_query_string(self.get_generic_query(parameters))

    def get_incremental_api_url(self, parameters):
        return self.get_base_url() + "incremental/" + self.get_edge_point() + self.get_query_string(self.get_generic_query(parameters))

    def get_search_edge(self):
        return "search.json"

    def get_edge_point(self):
        return self.zendesk_api + ".json"

    def get_base_url(self):
        return ZD.BASE_URL.format(subdomain=self.subdomain)

    def parse_search_options(self, search_options):
        ret = {'type': None, 'status': None, 'first_date': None, 'last_date': None}
        if 'zendesk_date_relation_1' in search_options\
                and 'zendesk_date_operator_1' in search_options\
                and search_options['zendesk_date_operator_1'] != 'none'\
                and 'zendesk_date_1' in search_options:
            ret['first_date'] = search_options['zendesk_date_operator_1'] + search_options['zendesk_date_relation_1'] + search_options['zendesk_date_1']
            if 'zendesk_date_relation_2' in search_options\
                    and 'zendesk_date_operator_2' in search_options\
                    and search_options['zendesk_date_operator_2'] != 'none'\
                    and 'zendesk_date_2' in search_options:
                ret['last_date'] = search_options['zendesk_date_operator_2'] + search_options['zendesk_date_relation_2'] + search_options['zendesk_date_2']
        if 'zendesk_query_type' in search_options:
            ret['type'] = search_options['zendesk_query_type']
            if (ret['type'] == "ticket") and ('zendesk_ticket_status' in search_options):
                ret['status'] = search_options['zendesk_ticket_status']
        return ret

    def get_generic_query(self, parameters={}):
        tokens = []
        for parameter in parameters:
            if parameter == "api":
                continue
            parameter_value = parameters[parameter]
            if isinstance(parameter_value, list):
                if len(parameter_value) == 1:
                    tokens.append("{}={}".format(parameter, parameter_value[0]))
                elif len(parameter_value) > 1:
                    for sub_parameter in parameter_value:
                        tokens.append("{}[]={}".format(parameter, sub_parameter))
            elif (parameter_value is not None) and (parameter_value != ""):
                tokens.append("{}={}".format(parameter, parameter_value))
        return tokens

    def parse_api_options(self, api, search_options):
        pattern = "zd_" + api + "_(.*)"
        parameters = {}
        for search_option in search_options:
            match = re.search(pattern, search_option)
            if match is not None:
                variable_name = match.group(1)
                parameters[variable_name] = search_options[search_option]
        return parameters
