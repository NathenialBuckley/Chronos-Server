from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from chronosapi.models import WatchType


"""Chronos API Watch Type View"""


class WatchTypeView(ViewSet):

    def retrieve(self, pk):
        watchtype = WatchType.objects.get(pk=pk)
        serializer = WatchTypeSeralizer(watchtype)
        return Response(serializer.data)

    def list(self, request):
        watchtype = WatchType.objects.all()
        seralized = WatchTypeSeralizer(watchtype, many=True)
        return Response(seralized.data, status=status.HTTP_200_OK)

    def create(self, request):
        watchtype = WatchType.objects.get(pk=request.data['watchtype'])

        watchtype = WatchType.objects.create(
            label=request.data['label'],
        )
        serializer = WatchTypeSeralizer(watchtype)
        return Response(serializer.data)

    def update(self, request, pk):
        editing_watchtype = WatchType.objects.get(pk=pk)
        editing_watchtype.content = request.data["content"]

        return Response(None, status=status.HTTP_205_RESET_CONTENT)

    def destroy(self, request, pk):
        watchtype = WatchType.objects.get(pk=pk)
        watchtype.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class WatchTypeSeralizer(serializers.ModelSerializer):
    class Meta:
        model = WatchType
        fields = ('id', 'type', 'watchId')
