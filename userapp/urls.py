from django.urls import path
from .views import LoginView, LogoutView, UserListView, ProfileAPIView, UserDetailView, BlacklistAllUsersExceptSelfView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('blacklist_all_users/',
         BlacklistAllUsersExceptSelfView.as_view(), name='blacklist-all-users'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('profile/', ProfileAPIView.as_view(), name='user-profile'),
]
