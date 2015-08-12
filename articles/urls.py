from rest_framework_nested import routers
from articles.views import AddEditArticlesView, ArticlesReadOnlyView

articles_router = routers.SimpleRouter()
articles_router.register(r"view", ArticlesReadOnlyView)
articles_router.register(r"add-edit", AddEditArticlesView)