from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, )

from users.apps import UsersConfig
from users.views import UserCreateView, UserListView, UserDetailView, UserUpdateView, UserDeleteView

app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='create'),
    # path('list/', UserListView.as_view(), name='list'),
    # path('detail/<int:pk>/', UserDetailView.as_view(), name='detail'),
    # path('update/<int:pk>/', UserUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/', UserDeleteView.as_view(), name='delete'),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
