import os, cgi, sys, logging
from datetime import datetime
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

import models
import request
#from util import markdown

class BlogHandler(request.RequestHandler):
	def get(self):
	
		body = """
# Well, it had to happen some time!

Here is a snippet of python code

	:::python
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

	:::css
    body {
        margin: 0px;
        padding: 0px;
        font-family: Arial, Helvetica, sans-serif;
        font-size: 12px;
        background-color: #DDDDDD;
    }

    pre                     { padding: 5px; }

    .codehilitetable        { border: solid 1px #ccc; }
    .codehilitetable
    .linenos                { background: #aaaaff; }

    .clearBoth              { clear: both; }

    #header                 { color: #fff; height: 30px; background: #000; }
    #header h1              { float: left; padding: 0px 0px 0px 10px; font-size: 120%; font-family: monospace;  }
    #header .greeting       { float: right; padding: 5px 10px 0px 0px; font-size: 110%; }

    #main                   { margin: 30px auto; width: 950px; background: #fff; padding: 10px 20px 10px 20px; }
    #body                   { float: left; width: 650px; }
    #right                  { float: right; width: 250px; }
"""
		user = users.get_current_user()
		from markdown import markdown
		vars = {
			'body': markdown(body, ['codehilite']),
			'user': user,
		}
		#self.response.out.write(self.render_template('index.html', vars))
		self.render_to_response('blog/index.html', vars)

class EditArticleHandler(request.RequestHandler):
	def get(self):
		self.render_to_response('blog/index.html', {})

	def post(self):
		article = Article()

		article.title = self.request.get('title')
		article.slug = self.request.get('slug')
		article.body = self.request.get('body')

		article.put()

		self.response.out.write(self.render_template('index.html', vars))


