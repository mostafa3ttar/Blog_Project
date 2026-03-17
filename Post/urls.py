from django.urls import path, include
# from .views import all_posts, post
from . import views


app_name='Post'

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('<int:id>/', views.post_detail, name='Single-post'),
    
    path('create/', views.create_post, name='create'),
    path('<int:id>/edit/', views.edit_post, name='edit_post'),
    
    path('<int:id>/delete/', views.delete_post, name='delete_post'),
    # path('Post', views.product, name='product'),
]
