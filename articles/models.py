from autoslug import AutoSlugField
from django.db import models
from django.db.models import permalink


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    category_slug = AutoSlugField(populate_from='title')

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return 'view_single_category', None, {'category_slug': self.category_slug}


class Article(models.Model):
    title = models.CharField(max_length=100, unique=True)
    article_slug = AutoSlugField(populate_from='title')
    content = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ManyToManyField(Category)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return 'view_single_article',  None, {'article_slug': self.article_slug}
