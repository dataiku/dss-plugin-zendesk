class ZD(object):
    NEXT_PAGE = "next_page"
    SEARCH_RESULTS = "results"
    BASE_URL = "https://{subdomain}.zendesk.com/api/v2/"
    AFTER_CURSOR = "after_cursor"
    END_OF_STREAM = "end_of_stream"
    TYPE = "type:{}"
    STATUS = "status:{}"
    QUERY = "query={}"


class ZendeskEndpoints(object):
    SEARCH = "search"
    USERS = "users"
    ORGANIZATIONS = "organizations"
    GROUPS = "groups"
    TICKETS = "tickets"
    SATISFACTION_RATINGS = "satisfaction_ratings"
    INCREMENTAL = "incremental/{route}"


class ZendeskResponse(object):
    SEARCH = "results"
    USERS = "users"
    ORGANIZATIONS = "organizations"
    GROUPS = "groups"
    TICKETS = "tickets"
    SATISFACTION_RATINGS = "satisfaction_ratings"
    TICKET_EVENTS = "ticket_events"


zendesk_parameters_whitelist = [
    "zendesk_access_type",
    "oauth_access",
    "token_access",
    "password_access",
    "zendesk_api",
    "zendesk_query_type",
    "zendesk_ticket_status",
    "zendesk_query",
    "zendesk_date_operator_1",
    "zendesk_date_relation_1",
    "zendesk_date_1",
    "zendesk_date_operator_2",
    "zendesk_date_relation_2",
    "zendesk_date_2",
    "zd_satisfaction_ratings_score",
    "zd_satisfaction_ratings_start_time",
    "zd_satisfaction_ratings_end_time",
    "zd_users_role",
    "zd_users_permission_set",
    "zd_incremental_api",
    "zd_incremental_start_time",
    "zd_incremental_end_time"
]
