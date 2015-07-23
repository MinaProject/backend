from elasticgit import models


class TestStory(models.Model):
    title = models.TextField('The Title')
    author = models.TextField('The Author')
    category = models.IntegerField('The Category')
    body = models.TextField('The Story')
    uuid = models.UUIDField('The UUID')
