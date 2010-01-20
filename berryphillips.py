import os, cgi, sys, logging
#from google.appengine.api import users
from google.appengine.ext import webapp #, db
#from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app

import blog
"""
DIR_PATH = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))
LIB_PATH = os.path.join(DIR_PATH, "lib")
EXTRA_PATHS = []
for path in os.listdir(LIB_PATH):
    fullpath = os.path.join(LIB_PATH, path)
    if os.path.isdir(fullpath) and not path.startswith("."):
        EXTRA_PATHS.append(fullpath)
sys.path = sys.path + EXTRA_PATHS
"""
application = webapp.WSGIApplication(
									 [('/', blog.BlogHandler)],
									 debug=True)

def main():
	run_wsgi_app(application)

if __name__ == "__main__":
	main()

