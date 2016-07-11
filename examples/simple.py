import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import learn

APP_KEY = 'YOUR API KEY'
APP_SECRET = 'YOUR SECRET'
BASE_URL = 'https://learn.example.com'

# Create new Learn Object and 'login' via token request
LearnApi = learn.Learn(BASE_URL, APP_SECRET, APP_KEY)
LearnApi.request_token()

# Get System version (Requires 3000.3)
# print LearnApi.get_system_version()

# Get a user by username, only returning the user's uuid and studentId fields
user = LearnApi.get_user('user', fields=('uuid, studentId'))

print user

# Return a list of courses with length 10
courses = LearnApi.get_courses(limit=10)

# Print the course id of the 10 courses retrieved
for course in courses['results']:
    print course['courseId']

# Return a list of terms
terms = LearnApi.get_terms()
