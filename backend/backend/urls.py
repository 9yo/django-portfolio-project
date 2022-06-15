from django.urls import include, path
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.conf import settings
from users import views as user_views
from contacts import views as contacts_views


router = routers.DefaultRouter()
router.register(r'users', user_views.UserViewSet)
router.register(r'contacts', contacts_views.ContactViewSet)
router.register(r'contact_books', contacts_views.ContactBookViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', user_views.CreateUserView.as_view(), name='user'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
