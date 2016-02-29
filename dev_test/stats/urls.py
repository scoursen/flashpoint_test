from django.conf.urls import url

from stats import views

urlpatterns = [
    url(r'^get$', views.get_stats),
]
