from launchpadlib.credentials import Credentials
from launchpadlib.launchpad import Launchpad


class LpClient:

    def __init__(self):
        # class to set up and return a launchpad client
        self.credentials = Credentials("nova-api-docs-tracker")
        self.request_token_info = self.credentials.get_request_token(web_root="production")

        self.lp = Launchpad.login_with('nova-api-docs-tracker', 'staging', version='devel')
        # credentials_file ??
        #self.lp = Launchpad(self.credentials, service_root="production")

        self.base_url = 'https://api.launchpad.net'
        self.version = '1.0'

    def test_launchpad(self):
        result = self.lp.people['auggy']
        return result


    # create bug
    def create_bug(self, params):
        url = '/'.join(self.base_url, self.version, 'bugs')
        bug_id = 1

        params['ws.op'] = 'createBug'
        print "PARAMS: %(params)s" % {'params': params}

        # get token info
        # post to url

        return bug_id

