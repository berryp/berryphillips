import os, cgi, sys, logging
from google.appengine.ext import webapp
from google.appengine.ext.webapp.template import register_template_library
from google.appengine.ext.webapp.util import run_wsgi_app

import config
from handlers import blog

#sys.path.insert(0, config.APP_ROOT_DIR)
#sys.path.insert(1, os.path.join(config.APP_ROOT_DIR, 'util'))
EXTRA_PATHS = []
EXTRA_PATHS.append(os.path.join(os.path.dirname(__file__), 'util'))
sys.path = sys.path + EXTRA_PATHS


register_template_library('lib.customfilters')

ROUTES = [
	('/', blog.BlogHandler),
	('/edit', blog.EditArticleHandler),
]

application = webapp.WSGIApplication(ROUTES, debug=True)

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


def main():
	article = Article(
		title = "First Post",
		body = body

	)

	run_wsgi_app(application)

if __name__ == "__main__":
	main()

