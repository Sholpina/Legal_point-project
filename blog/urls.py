from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('detail/<int:blog_id>/', views.detail, name='detail'),
    path('dashboard//', views.dashboard, name='dashboard'),
]