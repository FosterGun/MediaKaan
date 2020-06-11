from django.conf.urls import url
from . import views

app_name = 'gestionUsuarios'

urlpatterns = [
    url(r'^registro/$', views.register, name='register'),
    url(r'^iniciosesion/$', views.user_login, name='user_login'),
    url(r'^activar/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^olvidopass/$', views.forget_pass, name='forget_pass')
]