from django.conf.urls import handler404,handler400,handler403,handler500
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name='home'),
]
handler404 = 'main.views.error404'
handler403 = 'main.views.error403'
handler400 = 'main.views.error400'
handler500 = 'main.views.error500'