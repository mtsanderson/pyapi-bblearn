import requests

class Learn(object):
    def __init__(self, base_url, secret, key):
        self.base_url = base_url
        self.secret = secret
        self.key = key

        self.api_base_url = '{0}/learn/api/public/v1'.format(self.base_url)
        self.version_endpoint = '{0}/system/version'.format(self.api_base_url)
        self.oauth_endpoint = '{0}/oauth2/token'.format(self.api_base_url)
        self.courses_endpoint = '{0}/courses'.format(self.api_base_url)
        self.terms_endpoint = '{0}/terms'.format(self.api_base_url)
        self.users_endpoint = '{0}/users'.format(self.api_base_url)

        self.token = None
        self.headers = None

    def request_token(self):
        data = {'grant_type': 'client_credentials'}

        if self.token is None:
            r = requests.post(self.oauth_endpoint, data=data,
                            auth=(self.key, self.secret), verify=True)

            if r.status_code == 200:
                self.token = r.json()['access_token']
                self.headers = {'Authorization': 'Bearer {0}'.format(self.token)}
            else:
                print 'Errar'

    def get_system_version(self):
        req_url = self.version_endpoint

        r = requests.get(req_url, headers=self.headers, verify=True)

        return r.json()

    def get_course(self, course_id, fields=None):
        req_url = '{0}/courseId:{1}'.format(self.courses_endpoint, course_id)

        data = {'fields': fields}

        r = requests.get(req_url, params=data, headers=self.headers, verify=True)

        return r.json()

    def get_courses(self, offset=0, limit=10, fields=None):
        req_url = self.courses_endpoint

        data = {'offset': offset, 'limit': limit, 'fields': fields}

        r = requests.get(req_url, params=data, headers=self.headers, verify=True)

        return r.json()

    def create_course(self, course_json, fields=None):
        req_url = self.courses_endpoint

        data = {'fields': fields}

        print req_url

        r = requests.post(req_url, data=course_json, params=data, headers=self.headers, verify=True)

        return r.json()

    def delete_course(self, course_id, removeFiles=True):
        req_url = '{0}/externalId:{1}'.format(self.courses_endpoint, course_id)

        data = {'removeFiles': removeFiles}

        print req_url

        r = requests.delete(req_url, params=data, headers=self.headers, verify=True)

        return r.json()

    def get_terms(self, offset=0, limit=10, fields=None):
        req_url = self.terms_endpoint

        data = {'offset': offset, 'limit': limit, 'fields': fields}

        r = requests.get(req_url, params=data, headers=self.headers, verify=True)

        return r.json()

    def get_term(self, term_id, fields=None):
        req_url = '{0}/externalId:{1}'.format(self.terms_endpoint, term_id)

        data = {'fields': fields}

        r = requests.get(req_url, params=data, headers=self.headers, verify=True)

        return r.json()

    def get_users(self, offset=0, limit=10, fields=None):
        req_url = self.users_endpoint

        data = {'offset': offset, 'limit': limit, 'fields': fields}

        r = requests.get(req_url, params=data, headers=self.headers, verify=True)

        return r.json()

    def create_user(self, user_json, fields=None):
        req_url = self.users_endpoint

        data = {'fields': fields}

        r = requests.post(req_url, data=user_json, params=data, headers=self.headers, verify=True)

        return r.json()

    def delete_user(self, user_id, removeFiles=True):
        req_url = '{0}/userName:{1}'.format(self.users_endpoint, user_id)

        data = {'fields': fields}

        r = requests.delete(req_url, params=data, headers=self.headers, verify=True)

        return r.json()

    def get_user(self, user_id, fields=None):
        req_url = '{0}/userName:{1}'.format(self.users_endpoint, user_id)

        data = {'fields': fields}

        r = requests.get(req_url, params=data, headers=self.headers, verify=True)

        return r.json()
