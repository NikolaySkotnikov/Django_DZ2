from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog_catalog),
    path('category/', views.category_list),
    path('category/<int:cat_id>/', views.category_detail),
]