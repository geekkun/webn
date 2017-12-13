from tastypie.resources import ModelResource
from theapp.models import Article
from tastypie.authorization import Authorization

class ArticleResource(ModelResource):
    class Meta:
        queryset = Article.objects.all()
        resource_name = 'article'
        authorization = Authorization()