from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_page),
    path('blog/<str:post_id>/',views.blog_page, name='blog_post'),
]
