from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles import views
from articles.urls import articles_router
from index.IndexView import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/articles/', include(articles_router.urls)),
    url(r'^static/(?P<path>.*)$', views.serve),
]

# urlpatterns += router.urls
