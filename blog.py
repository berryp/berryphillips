import os, cgi, sys, logging
from google.appengine.api import users
from google.appengine.ext import webapp, db
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

import request

class Article(db.Model):
	headline = db.StringProperty()
	slug = db.StringProperty()
	body = db.TextProperty()
	tags = db.ListProperty(basestring)
	draft = db.BooleanProperty()
	publish_date = db.DateTimeProperty()
	
class Image(db.Model):
	image_data = db.BlobProperty()
	mime_type = db.StringProperty()

def secure(func):
	def callf(request, *args, **kwargs):

		if users.get_current_user():
			return func(request, *args, **kwargs)
		else:
			request.redirect(users.create_login_url(request.request.uri))

	return callf

class BlogHandler(request.RequestHandler):
	def get(self):
		from markdown import markdown
	
		body = """
# Well, it had to happen some time!

Here is a snippet of python code

	#!python
	#return the list of the permutations of s
	def get_permutations(s):
		result = []
		if len(s) == 1:
			result.append(s)
			return result

		for i in range(0,len(s)):
			for perm in get_permutations(s.replace(s[i], s[0])[1:]):
				result.append(s[i] + perm)
		return result		

And here is a snippet of CSS

	#!css
	body {
		margin: 0px;
		padding: 0px;
		font-family: Arial, Helvetica, sans-serif;
		font-size: 12px;
		background-color: #DDDDDD;
	}

	pre 					{ padding: 5px; }

	.codehilitetable 		{ border: solid 1px #ccc; }
	.codehilitetable
	.linenos			{ background: #aaaaff; }

	.clearBoth 				{ clear: both; }

	#header 				{ color: #fff; height: 30px; background: #000; }
	#header h1 				{ float: left; padding: 0px 0px 0px 10px; font-size: 120%; font-family: monospace;  }
	#header .greeting 		{ float: right; padding: 5px 10px 0px 0px; font-size: 110%; }

	#main 					{ margin: 30px auto; width: 950px; background: #fff; padding: 10px 20px 10px 20px; }
	#body 					{ float: left; width: 650px; }
	#right 					{ float: right; width: 250px; }


"""
		user = users.get_current_user()
		if user:
			greeting = ("Welcome, %s! (<a href=\"%s\">sign out</a>)" %
						(user.nickname(), users.create_logout_url("/")))
		else:
			greeting = ("<a href=\"%s\">Sign in or register</a>." %
						users.create_login_url("/"))
		if not user:
			body = markdown(body, ['codehilite'])
		#else:
		#	body = "<textarea style=\"height: 300px; width: 600px;\">%s</textarea>" % body
		vars = {
			'body': body,
			'greeting': greeting,
			#'body': sys.path
		}
		self.response.out.write(self.render_template('index.html', vars))
		
