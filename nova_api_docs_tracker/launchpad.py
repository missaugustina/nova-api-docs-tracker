from launchpadlib.credentials import Credentials
from launchpadlib.launchpad import Launchpad

# class to set up and return a launchpad client
credentials = Credentials("nova-api-docs-tracker")
request_token_info = credentials.get_request_token(web_root="production")
launchpad = Launchpad(credentials, service_root="production")

base_url = 'https://api.launchpad.net'
version = '1.0'


# create bug
def create_bug(params):
    url = '/'.join(base_url, version, 'bugs')
    bug_id = 1

    params['ws.op'] = 'createBug'
    print "PARAMS: %(params)s" % {'params': params}

    # get token info
    # post to url

    return bug_id

