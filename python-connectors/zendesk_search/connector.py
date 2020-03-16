import logging
from dataiku.connector import Connector
from zendesk_constants import ZendeskEndpoints, zendesk_parameters_whitelist
from zendesk_client import ZendeskClient

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO,
                    format='zendesk plugin %(levelname)s - %(message)s')


class ZendeskSearchConnector(Connector):

    def __init__(self, config, plugin_config):
        Connector.__init__(self, config, plugin_config)  # pass the parameters to the base class

        logger.info('Init Zendesk plugin')
        self.client = ZendeskClient(config)
        self.search_parameters = self.filter_parameters(config)
        self.zendesk_api = self.config.get("zendesk_api")

    def get_read_schema(self):
        return None

    def generate_rows(self, dataset_schema=None, dataset_partitioning=None,
                      partition_id=None, records_limit=-1):
        if self.zendesk_api == ZendeskEndpoints.SEARCH:
            data = self.client.search(self.search_parameters)
        else:
            data = self.client.any(self.search_parameters)
        while len(data) > 0:
            counter = 0
            for result in data:
                if counter == records_limit:
                    break
                else:
                    counter = counter + 1
                yield (result)
            if self.client.has_next_page():
                data = self.client.get_next_page()
            else:
                break

    def get_writer(self, dataset_schema=None, dataset_partitioning=None,
                   partition_id=None):
        raise Exception("Unimplemented")

    def get_partitioning(self):
        raise Exception("Unimplemented")

    def list_partitions(self, partitioning):
        return []

    def partition_exists(self, partitioning, partition_id):
        raise Exception("unimplemented")

    def get_records_count(self, partitioning=None, partition_id=None):
        raise Exception("unimplemented")

    def filter_parameters(self, parameters):
        filtered_parameters = {}
        for parameter in parameters:
            if parameter in zendesk_parameters_whitelist:
                filtered_parameters[parameter] = parameters[parameter]
        return filtered_parameters


class CustomDatasetWriter(object):
    def __init__(self):
        #  Nested comment explaining why this method is empty.
        pass

    def write_row(self, row):
        """
        Row is a tuple with N + 1 elements matching the schema passed to get_writer.
        The last element is a dict of columns not found in the schema
        """
        raise Exception("unimplemented")

    def close(self):
        #  Nested comment explaining why this method is empty.
        pass
