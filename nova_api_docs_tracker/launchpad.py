from launchpadlib.credentials import Credentials
from launchpadlib.launchpad import Launchpad

# class to set up and return a launchpad client

credentials = Credentials("nova-api-docs-tracker")
request_token_info = credentials.get_request_token(web_root="production")
launchpad = Launchpad(credentials, service_root="production")