from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework import mixins
from articles.models import Article
from articles.serializer import AddEditArticleSerializer, ArticleReadOnlySerialiser


class AddEditModelViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    pass


class AddEditArticlesView(AddEditModelViewSet):
    queryset = Article.objects.all()
    serializer_class = AddEditArticleSerializer


class ArticlesReadOnlyView(ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleReadOnlySerialiser

    def list(self, request):
        queryset = self.queryset
        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
