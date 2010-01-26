import os, sys
from google.appengine.ext import webapp
from google.appengine.api import users
from google.appengine.ext.webapp import template
import config

class RequestHandler(webapp.RequestHandler):
	def __init__(self):
		#sys.path.insert(0, config.APP_ROOT_DIR)
		#sys.path.insert(1, os.path.join(config.APP_ROOT_DIR, 'util'))
		sys.path.insert(0, '/home/berryp/webapps/berryphillips/util')

	def authenticate(func):
		def callf(request, *args, **kwargs):
			if not users.get_current_user():
				request.redirect(users.create_login_url(request.uri))
		return callf

	def get_template(self, template_name):
		return os.path.join(os.path.dirname(__file__), 'templates', template_name)

	def render_template(self, template_name, template_vars):
		template_path = self.get_template(template_name)
		template.register_template_library('django.contrib.markup.templatetags.markup')
		return template.render(template_path, template_vars)

	def render_to_response(self, template_name, template_vars):
		self.response.out.write(self.render_template(template_name, template_vars))
