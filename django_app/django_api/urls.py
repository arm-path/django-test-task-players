from rest_framework.routers import SimpleRouter

from django_app.django_api.views import CommentsViewSet

router = SimpleRouter()
router.register('comments', CommentsViewSet),

urlpatterns = []
urlpatterns += router.urls