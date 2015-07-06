from elasticgit import EG
from elasticgit.models import Model, IntegerField, TextField

#workspace = EG.workspace('/Users/codieroelf/repositories/backend/mina')
#workspace.setup('Codie Roelf', 'codiebeulaine@gmail.com')


class TestStory(Model):
	title = TextField('The Title')
	author = TextField('The Author')
	category = IntegerField('The Category')
	body = TextField('The Story')