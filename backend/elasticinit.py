from elasticgit import models


class TestStory(models.Model):
    title = models.TextField('The Title')
    author = models.UUIDField('The Author')
    category = models.IntegerField('The Category')
    body = models.TextField('The Story')
    uuid = models.UUIDField('The UUID')
    update_count = models.IntegerField('The Update Count')
    co_authors = models.ListField('The Co-Authors', fields=models.UUIDField)
