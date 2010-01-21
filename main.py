import os, cgi, sys, logging
#from google.appengine.api import users
from google.appengine.ext import webapp #, db
#from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

import blog

EXTRA_PATHS = []
EXTRA_PATHS.append(os.path.join(os.path.dirname(__file__), 'util'))
sys.path = sys.path + EXTRA_PATHS

ROUTES = [
	('/', blog.BlogHandler),
]

application = webapp.WSGIApplication(ROUTES, debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()

