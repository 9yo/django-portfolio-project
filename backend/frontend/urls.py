import re
from django.urls import path, re_path
from .views import index, render_static_files


urlpatterns = [
    path(r'', index),
    path(r'css/<filename>', render_static_files),
    path(r'js/<filename>', render_static_files),
]
