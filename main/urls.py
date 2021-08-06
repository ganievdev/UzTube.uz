from django.urls import path
from . import views
from .views import MainIndex, CreatePost, video_viewer, PostLike, Search, profileView, delete,http_404

app_name = 'main'

urlpatterns = [

    path('', MainIndex.as_view(),name='index'),
    path('create/', CreatePost.as_view(), name='create'),
    path('video_viewer/<int:id>/', video_viewer, name="video_viewer"),
    path('like/<int:pk>/<str:type>/', PostLike.as_view(), name="postlike"),
    path('search/', Search.as_view(), name='search'),
    path('profile_view/<int:id>/',profileView,name='profile_view'),
    path('delete/<int:id>/',delete,name="delete"),
    path('404/',http_404.as_view(),name="http_404")
]
