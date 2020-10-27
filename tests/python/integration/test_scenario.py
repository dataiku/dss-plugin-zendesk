from dku_plugin_test_utils import scenario


def test_run_read_zendesk_groups(client, plugin):
    scenario(client, 'PLUGINTESTZENDESK', 'run_read_zendesk_groups')


def test_run_read_zendesk_incremental(client, plugin):
    scenario(client, 'PLUGINTESTZENDESK', 'run_read_zendesk_incremental')


def test_run_read_zendesk_organizations(client, plugin):
    scenario(client, 'PLUGINTESTZENDESK', 'run_read_zendesk_organizations')


def test_run_read_zendesk_search(client, plugin):
    scenario(client, 'PLUGINTESTZENDESK', 'run_read_zendesk_search')


def test_run_read_zendesk_tickets(client, plugin):
    scenario(client, 'PLUGINTESTZENDESK', 'run_read_zendesk_tickets')


def test_run_read_zendesk_users(client, plugin):
    scenario(client, 'PLUGINTESTZENDESK', 'run_read_zendesk_users')
