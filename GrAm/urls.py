from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.start,name = 'start'),
    url('^home/',views.home,name = 'home'),
    url('^signin/',views.signin,name = 'signin'),
    url('^login/',views.login,name = 'login')
]