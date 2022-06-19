from rest_framework.routers import DefaultRouter
from .views import ContactViewSet, ContactBookViewSet

router = DefaultRouter()
router.register(r'contacts', ContactViewSet)
router.register(r'contact_books', ContactBookViewSet)
urlpatterns = router.urls
