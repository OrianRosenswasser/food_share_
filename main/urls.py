# urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import FoodPostDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login-page/', views.login, name='login'),
    path('food-post/', views.post_food_page, name='post_food_page'),
    path('food-feed/', views.food_feed, name='food_feed'),
    # Corrected path for FoodPostDetailView
    path('api/food_feed/<int:pk>/', FoodPostDetailView.as_view(), name='food_post_detail'),
    path('', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
