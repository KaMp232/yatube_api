from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as auth_views
from . import views

router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='posts')
router.register('groups', views.GroupViewSet, basename='groups')

urlpatterns = [
        path('api-token-auth/',
         auth_views.obtain_auth_token,
         name='api_token_auth'),
    path('', include(router.urls)),

    path('posts/<int:post_id>/comments/',
         views.CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='post-comments'),

    path('posts/<int:post_id>/comments/<int:pk>/',
         views.CommentViewSet.as_view({
             'get': 'retrieve',
             'put': 'update',
             'patch': 'partial_update',
             'delete': 'destroy'
         }),
         name='post-comment-detail'),
]
