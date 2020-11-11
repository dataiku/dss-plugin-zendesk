import pytest
import logging

from dku_plugin_test_utils import dss_scenario


pytestmark = pytest.mark.usefixtures("plugin", "dss_target")
logger = logging.getLogger("dss-plugin-test.zendesk.test_scenario")


def test_run_read_zendesk_groups(user_clients):
    dss_scenario.run("default", user_clients["default"], 'PLUGINTESTZENDESK', 'run_read_zendesk_groups', logger)


def test_run_read_zendesk_incremental(user_clients):
    dss_scenario.run("default", user_clients["default"], 'PLUGINTESTZENDESK', 'run_read_zendesk_incremental', logger)


def test_run_read_zendesk_organizations(user_clients):
    dss_scenario.run("user1", user_clients["user1"], 'PLUGINTESTZENDESK', 'run_read_zendesk_organizations', logger)


def test_run_read_zendesk_search(user_clients):
    dss_scenario.run("user1", user_clients["user1"], 'PLUGINTESTZENDESK', 'run_read_zendesk_search', logger)


def test_run_read_zendesk_tickets(user_clients):
    dss_scenario.run("user1", user_clients["user1"], 'PLUGINTESTZENDESK', 'run_read_zendesk_tickets', logger)


def test_run_read_zendesk_user_clients(user_clients):
    dss_scenario.run("user1", user_clients["user1"], 'PLUGINTESTZENDESK', 'run_read_zendesk_users', logger)
