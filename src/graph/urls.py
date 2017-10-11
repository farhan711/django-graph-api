from django.conf.urls import url
from graph.views import GraphListCreateAPIView, GraphDetailAPIView

urlpatterns = [
    url(r'^$', GraphListCreateAPIView.as_view(), name="list"),
    url(r'^(?P<pk>[0-9]+)/$', GraphDetailAPIView.as_view(), name="detail"),
]