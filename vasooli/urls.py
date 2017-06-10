from django.conf.urls import include
from django.conf.urls import url

from django.conf import settings
from django.contrib import admin
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token

from gale_user import views
from bills import views as bills_view
from authorization.views import (
    LoginView,
    RegisterView
)

router = routers.DefaultRouter()
urlpatterns = router.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-token-auth/', obtain_jwt_token, name='create_token'),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token)
]

urlpatterns += router.urls

urlpatterns += [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-auth/', include('rest_auth.urls')),
]

urlpatterns += [
    url(r'^users/create/$', views.UserCreateView.as_view(), name="user_create"),
    url(r'^users/list/$', views.UsersListView.as_view(), name="users_list"),
    url(r'^users/(?P<pk>\d+)/detail/$', views.UserDetailView.as_view(), name="user_detail"),
    url(r'^users/(?P<pk>\d+)/update/$', views.UserUpdateView.as_view(), name="user_update"),
    url(r'^users/(?P<pk>\d+)/delete/$', views.UserDeleteView.as_view(), name="user_delete"),
    url(r'^users/mybills/$', views.my_bills, name="my_bills"),
]

urlpatterns += [
    url(r'^bill/create/$', bills_view.BillsCreateView.as_view(), name="bills_create"),
    url(r'^bill/list/$', bills_view.BillsListView.as_view(), name="bills_list"),
    url(r'^bill/(?P<pk>\d+)/detail/$', bills_view.BillsDetailView.as_view(), name="bills_detail"),
    url(r'^bill/(?P<pk>\d+)/update/$', bills_view.BillsUpdateView.as_view(), name="bills_update"),
    url(r'^bill/(?P<pk>\d+)/delete/$', bills_view.BillsDeleteView.as_view(), name="bills_delete"),
]

urlpatterns += [
    url(r'^user/login', LoginView.as_view()),
    url(r'^user/register', RegisterView.as_view())
]

if not settings.DEBUG:
    urlpatterns += (
        '',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)
