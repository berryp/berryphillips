import os 
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class RequestHandler(webapp.RequestHandler):
	def get_template(self, template_name):
		return os.path.join(os.path.dirname(__file__), 'templates', template_name)

	def render_template(self, template_name, template_vars):
		template_path = self.get_template(template_name)
		template.register_template_library('django.contrib.markup.templatetags.markup')
		return template.render(template_path, template_vars)

