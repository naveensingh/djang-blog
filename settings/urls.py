from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_nested import routers
from django.contrib.staticfiles import views

from articles.views import ArticlesList
from index.IndexView import IndexView

router = routers.SimpleRouter()
router.register(r'articles', ArticlesList)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^api/v1/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', views.serve),
]

# urlpatterns += router.urls
