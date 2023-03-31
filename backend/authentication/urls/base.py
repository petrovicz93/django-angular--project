from django.conf.urls import url, include
from django.contrib.auth import get_user_model

from authentication import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', views.UserViewSet)

User = get_user_model()

urlpatterns = [
    url(r'^me/?$', views.UserView.as_view(), name='user'),
    url(
        r'^users/create/?$',
        views.UserCreateView.as_view(),
        name='user-create'
    ),
    url(
        r'^users/createpassword/?$',
        views.UserCreatePasswordView.as_view(),
        name='user-create-password'
    ),
    url(
        r'^users/check-user/?$',
        views.CheckActiveUserView.as_view(),
        name='user-create-password'
    ),
    url(
        r'^users/(?P<pk>\d+)/?$',
        views.GetUserView.as_view(),
        name='user-avatar'
    ),
    url(
        r'^users/check-active-user/?$',
        views.UserCreatePasswordView.as_view(),
        name='user-create-password'
    ),
    url(
        r'^users/jwt/create/?',
        views.ObtainJwtToken.as_view(),
        name='jwt-create'),
    url(
        r'^profile/update/(?P<pk>\d+)/?$',
        views.UserProfileUpdateView.as_view(),
        name='profile-update'
    ),
    url(
        r'^profile/resetpwd/?$',
        views.UserPwdResetView.as_view(),
        name='profile-update'
    ),
    url(
        r'^users/delete/?$',
        views.UserDeleteView.as_view(),
        name='user-delete'
    ),
    url(
        r'^users/activate/?$',
        views.ActivationView.as_view(),
        name='user-activate'
    ),
    url(
        r'^users/upload-avatar/?$',
        views.UploadAvatarView.as_view(),
        name='user-avatar'
    ),
    url(
        r'^{0}/?$'.format(User.USERNAME_FIELD),
        views.SetUsernameView.as_view(),
        name='set_username'
    ),
    url(r'^password/?$', views.SetPasswordView.as_view(), name='set_password'),
    url(
        r'^password/reset/?$',
        views.PasswordResetView.as_view(),
        name='password_reset'
    ),
    url(
        r'^password/reset/confirm/?$',
        views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    url(r'^$', views.RootView.as_view(), name='root'),
    url(r'^', include(router.urls)),
]