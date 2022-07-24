from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_categories, name='list_categories'),
    path('categories/new/', views.add_category, name='add_category'),
    path('categories/<int:category_id>/view', views.view_category, name='view_category'),
    path('categories/<int:category_id>/edit', views.edit_category, name='edit_category'),
    path('categories/<int:category_id>/posts/new', views.add_post, name='add_post'),
    path('categories/<int:category_id>/posts/<int:post_id>/view', views.view_post, name='view_post'),
    path('categories/<int:category_id>/posts/<int:post_id>/edit', views.edit_post, name='edit_post'),

    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.category, name='category'),
    path('posts/', views.posts, name='posts'),
    path('posts/<int:post_id>/', views.post, name='post'),
]
