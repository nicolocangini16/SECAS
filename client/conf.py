#BASE = "https://lingon.ladok.umu.se"
BASE = "http://localhost"

# If BASE is https these has to be specified
SERVER_CERT = "certs/server.crt"
SERVER_KEY = "certs/server.key"
CA_BUNDLE = None

VERIFY_SSL = False

# information used when registering the client, this may be the same for all OPs

ME = {
    "application_type": "web",
    "application_name": "idpproxy",
    "contacts": ["ops@example.com"],
    "redirect_uris": ["{base}authz_cb"],
    "post_logout_redirect_uris": ["{base}logout_success"],
    "response_types": ["code"]
}

BEHAVIOUR = {
    "response_type": "code",
    "scope": ["openid", "profile", "email", "address", "phone"],
}

ACR_VALUES = ["MULTI_AUTHN"]

# The keys in this dictionary are the OPs short userfriendly name
# not the issuer (iss) name.

CLIENTS = {
    # The ones that support webfinger, OP discovery and client registration
    # This is the default, any client that is not listed here is expected to
    # support dynamic discovery and registration.
    "": {
        "client_info": ME,
        "behaviour": BEHAVIOUR
    },
    #"oictest": {
    #    "srv_discovery_url": "https://oictest.umdc.umu.se:8085/",
    #    "client_info": ME,
    #    "behaviour": BEHAVIOUR
    #},
    # "lingon": {
    #     "srv_discovery_url": "https://lingon.ladok.umu.se:8092/",
    #     "client_info": ME,
    #     "behaviour": BEHAVIOUR,
    #     "verify_ssl": False
    # },
    # Supports OP information lookup but not client registration
    # "google": {
    #     "srv_discovery_url": "https://accounts.google.com/",
    #     "client_registration": {
    #         "client_id": "xxxxxxxxx.apps.googleusercontent.com",
    #         "client_secret": "2222222222",
    #         "redirect_uris": ["{base}google"],
    #     },
    #     "behaviour": {
    #         "response_type": "code",
    #         "scope": ["openid", "profile", "email"]
    #     },
    #     "allow": {
    #         "issuer_mismatch": True
    #     },
    #     "userinfo_request_method": "GET"
    # }
}

# Which type of client
CLIENT_TYPE = 'OIDC'  # one of OIDC/OAUTH2
# Whether an attempt to fetch the userinfo should be made
USERINFO = True
