from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import viewsets
from articles.models import Article
from rest_framework import serializers


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class ArticleListSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'content')


class ArticlesList(viewsets.ViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerialiser

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
