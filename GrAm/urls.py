from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.start,name = 'start'),
    url('^home/',views.home,name = 'home'),
    url('^signin/',views.signin,name = 'signin'),
    url('^login/',views.login,name = 'login'),
    url('^/profile/',views.profile, name='profile'),
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)