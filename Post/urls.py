from django.urls import path, include
# from .views import all_posts, post
from . import views


app_name='Post'

urlpatterns = [
    path('', views.all_posts, name='all_posts'),
    path('<int:id>/', views.post, name='Single-post'),
    # path('Post', views.product, name='product'),
]
