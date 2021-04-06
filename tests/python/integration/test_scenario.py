from dku_plugin_test_utils import dss_scenario


def test_run_read_zendesk_groups(user_dss_clients):
    dss_scenario.run(user_dss_clients, 'PLUGINTESTZENDESK', 'run_read_zendesk_groups')


def test_run_read_zendesk_incremental(user_dss_clients):
    dss_scenario.run(user_dss_clients, 'PLUGINTESTZENDESK', 'run_read_zendesk_incremental')


def test_run_read_zendesk_organizations(user_dss_clients):
    dss_scenario.run(user_dss_clients, 'PLUGINTESTZENDESK', 'run_read_zendesk_organizations', user="data_scientist_1")


def test_run_read_zendesk_search(user_dss_clients):
    dss_scenario.run(user_dss_clients, 'PLUGINTESTZENDESK', 'run_read_zendesk_search', user="data_scientist_1")


def test_run_read_zendesk_tickets(user_dss_clients):
    dss_scenario.run(user_dss_clients, 'PLUGINTESTZENDESK', 'run_read_zendesk_tickets', user="data_scientist_1")


def test_run_read_zendesk_user_clients(user_dss_clients):
    dss_scenario.run(user_dss_clients, 'PLUGINTESTZENDESK', 'run_read_zendesk_users', user="data_scientist_1")
