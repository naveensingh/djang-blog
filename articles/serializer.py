from rest_framework import serializers
from articles.models import Article, Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(max_length=100)

    class Meta:
        model = Category
        fields = ("title", "category_slug")


class AddEditArticleSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)

    class Meta:
        model = Article
        fields = ("title", "content", "category")


class ArticleReadOnlySerialiser(serializers.HyperlinkedModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Article
        fields = ("title", "content", "category")
