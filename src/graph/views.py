from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from graph.models import Graph
from graph.serializers import GraphSerializer


class GraphListCreateAPIView(ListCreateAPIView):
    serializer_class = GraphSerializer
    permission_classes = ()

    def get_queryset(self):
        return Graph.objects.all()

    def perform_create(self, serializer):
        serializer.save()


class GraphDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = GraphSerializer
    queryset = Graph.objects.all()
    permission_classes = ()


