import os, cgi, sys, logging
from google.appengine.api import users
from google.appengine.ext import webapp, db
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

from django.contrib.markup.templatetags.markup import textile

import request

class BlogHandler(request.RequestHandler):
	def get(self):
		vars = {
			'body': textile("""
				h2. Hey there!
				"""),
		}
		self.response.out.write(self.render_template('index.html', vars))

