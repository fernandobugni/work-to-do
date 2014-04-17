import os
import webapp2

from google.appengine.api import users
from controller.project import project
from model.Project import Project

class MainPage(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()

        if user:
            self.response.headers['Content-Type'] = 'text/plain'
            self.response.write('Hello, ' + user.nickname())
        else:
            self.redirect(users.create_login_url(self.request.uri))

application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/project', project),
    ('/project/new', project),
    ('/project/delete', project)
], debug=True)