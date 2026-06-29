from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from . import views

app_name = 'api'

router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='posts')
router.register('groups', views.GroupViewSet, basename='groups')
# Комментарии регистрируем отдельно, т.к. у них есть nested-URL
# Но их будем обрабатывать вручную

urlpatterns = [
    # Эндпоинт для получения токена
    path('v1/api-token-auth/', views.obtain_auth_token),
    # Подключаем роутер для основных эндпоинтов
    path('v1/', include(router.urls)),
]

# Добавляем эндпоинты для комментариев вручную (nested)
from .views import CommentViewSet

# Добавляем после router
urlpatterns += [
    path(
        'v1/posts/<int:post_id>/comments/',
        CommentViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='comment-list'
    ),
    path(
        'v1/posts/<int:post_id>/comments/<int:pk>/',
        CommentViewSet.as_view(
            {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}
        ),
        name='comment-detail'
    ),
]
