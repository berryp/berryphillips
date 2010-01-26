from datetime import datetime
from google.appengine.api import users
from google.appengine.ext import db

import request


class Article(db.Model):
	title = db.StringProperty(required=True)
	slug = db.StringProperty(required=True)
	body = db.TextProperty(required=True)
	tags = db.StringListProperty(default=[])
	published = db.BooleanProperty(), 
	created_date = db.DateTimeProperty(auto_now_add=True)
	published_date = db.DateTimeProperty()
	updated_date = db.DateTimeProperty()
	author = db.UserProperty(required=True)
	format = db.StringProperty(required=True, 
								choices=set(['html', 'markdown', 
											'textile', 'text']))
	allow_comments = db.BooleanProperty()

	def save(self):
		if published and not created_date:
			published_date = datetime.now()
		else:
			updated_date = datetime.now()
		self.put()
	
class Image(db.Model):
	image_data = db.BlobProperty()
	mime_type = db.StringProperty()

