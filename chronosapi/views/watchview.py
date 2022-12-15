from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from chronosapi.models import Watch


class WatchView(ViewSet):
    """Chronos API Watch view"""

    def retrieve(self, request, pk=None):
        watch = Watch.objects.get(pk=pk)
        serialized = WatchSerializer(watch, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self):
        watches = Watch.objects.all()
        serialized = WatchSerializer(watches, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        watch = Watch.objects.get(pk=request.data['watches'])

        watch = Watch.objects.create(
            label=request.data['label'],
        )
        serializer = WatchSerializer(watch)
        return Response(serializer.data)

    def update(self, request, pk):
        editing_watch = Watch.objects.get(pk=pk)
        editing_watch.content = request.data["content"]

        return Response(None, status=status.HTTP_205_RESET_CONTENT)

    def destroy(self, request, pk):
        watch = Watch.objects.get(pk=pk)
        watch.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class WatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        fields = ('id', 'name', 'price', 'customerId')
