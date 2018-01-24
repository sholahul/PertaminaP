from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^InputDisplay/$', views.InputDisplay,name="InputDisplay"),

    url(r'^DisplayInformation1/$', views.DisplayInformation1,name="DisplayInformation1"),
    url(r'^DisplayInformation2/$', views.DisplayInformation2,name="DisplayInformation2"),
    url(r'^DisplayInformation3/$', views.DisplayInformation3,name="DisplayInformation3"),
    url(r'^DisplayInformation4/$', views.DisplayInformation4,name="DisplayInformation4"),
    url(r'^DisplayInformation5/$', views.DisplayInformation5,name="DisplayInformation5"),
]