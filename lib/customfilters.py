from google.appengine.api import users
from google.appengine.ext.webapp.template import create_template_register
register = create_template_register()

@register.filter
def markup(text, format=None):
	""" Render the given text to HTML """
	if format == 'html':
		# Return the text as is
		return text
	elif format == 'textile':
		from lib.textile import textile
		return textile(text)

	# The default markup is Markdown
	from lib import markdown2
	return markdown(text, ['codehilite'])

@register.filter
def signin_url(user, label=None):
	if user:
		if not label:
			label = "sign out"
		return "<a href=\"%s\">%s</a>" % (users.create_logout_url('/'), label)
	else:
		if not label:
			label = "sign in"
		return "<a href=\"%s\">%s</a>" % (users.create_login_url('/'), label)


