import os
import sys

#  Add stuff to the path to enable exec outside of DSS
plugin_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(os.path.join(plugin_root, 'python-lib'))
from zendesk_client import ZendeskClient

fake_conf = {
    'password_access': {}, 'token_access': {
        'zendesk_password': '6aflxdTXvD9tof68ei1Y60pMphzDtlvjg0UOszBK',
        'zendesk_subdomain': 'dss-testing',
        'zendesk_username': 'alexandre.bourret@dataiku.com'
    }, 'zendesk_date_1': '1hours',
    'zendesk_date_2': '1972-14-04',
    'zendesk_access_type': 'token',
    'zendesk_ticket_status': '*',
    'zendesk_query_type': 'ticket',
    'oauth_access': {},
    'zendesk_query': '',
    'zendesk_date_operator_1': 'created',
    'zendesk_date_relation_1': '<',
    'zendesk_date_operator_2': 'updated', 'zendesk_date_relation_2': '<',
    "zendesk_api": "search",
    'zd_search_foo': 'bar'
}

client = ZendeskClient(fake_conf)


def test_with_type():
    assert client.with_type('bla') == "type:bla"
    assert client.with_type('') == ""
    assert client.with_type(None) == ""


def test_parse_search_options():
    assert client.parse_search_options(fake_conf) == {'first_date': 'created<1hours', 'last_date': 'updated<1972-14-04', 'status': '*', 'type': 'ticket'}


def test_get_search_query():
    search_options = client.parse_search_options(fake_conf)
    assert client.get_search_query(**search_options) == ["query=type:ticket status:* created<1hours updated<1972-14-04"]


def test_get_query_string():
    assert client.get_query_string(["query=type:ticket status:* created<1hours updated<1972-14-04"]) == "?query=type:ticket status:* created<1hours updated<1972-14-04"


def test_get_search_url():
    search_options = client.parse_search_options(fake_conf)
    assert client.get_search_url(**search_options) == "https://dss-testing.zendesk.com/api/v2/search.json?query=type:ticket status:* created<1hours updated<1972-14-04"


def test_parse_api_options():
    assert client.parse_api_options("search", fake_conf) == {'foo': 'bar'}


def test_get_generic_query():
    parameters = client.parse_api_options("search", fake_conf)
    assert client.get_generic_query(parameters) == ['foo=bar']


def test_multiple_get_generic_query():
    conf = {
        'zd_search_role': ["end-user", "agent", "admin"]
    }
    parameters = client.parse_api_options("search", conf)
    assert client.get_generic_query(parameters) == ['role[]=end-user', 'role[]=agent', 'role[]=admin']


def test_array_1_get_generic_query():
    conf = {
        'zd_search_role': ["end-user"]
    }
    parameters = client.parse_api_options("search", conf)
    assert client.get_generic_query(parameters) == ['role=end-user']


def test_get_generic_url():
    parameters = client.parse_api_options("search", fake_conf)
    assert client.get_generic_url(parameters) == "https://dss-testing.zendesk.com/api/v2/search.json?foo=bar"
