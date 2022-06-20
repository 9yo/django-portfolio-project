from django.urls import include, path, re_path
from django.views.generic import TemplateView
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

urlpatterns = [
    # path('', include('frontend.urls')),
    path('api/', include(router.urls)),
    path('api/', include('contacts.urls')),
    path('auth/register/', user_views.CreateUserView.as_view(), name='user'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh_token/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# urlpatterns += [re_path(r'^', TemplateView.as_view(template_name='index.html'))]
