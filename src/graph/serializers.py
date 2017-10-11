from django.contrib.auth.models import User
from rest_framework import serializers
from graph.models import Graph, GraphData


class GraphDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = GraphData
        fields = ("id", "label", "data")


class GraphSerializer(serializers.ModelSerializer):
    graph_data = GraphDataSerializer(read_only=True, many=True)

    class Meta:
        model = Graph
        fields = ("id", "name", "description", "color_code","single_data", "multipe_data", "graph_data", "date_created")
