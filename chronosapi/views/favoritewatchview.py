from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from chronosapi.models import FavoriteWatch, Watch, Customer


"""Chronos API Cusotmer View"""


class FavoriteWatchView(ViewSet):

    def retrieve(self, pk):
        fWatch = FavoriteWatch.objects.get(pk=pk)
        serializer = FavoriteWatchSeralizer(fWatch)
        return Response(serializer.data)

    def list(self, request):
        fwatch = FavoriteWatch.objects.all()
        seralized = FavoriteWatchSeralizer(fwatch, many=True)
        return Response(seralized.data, status=status.HTTP_200_OK)

    def create(self, request):
        customer = Customer.objects.get(user=request.auth.user)
        watch = Watch.objects.get(pk=request.data["id"])
        # fwatch = FavoriteWatch.objects.get(pk=request.data['watches'])

        fwatch = FavoriteWatch.objects.create(
            watch=watch,
            customer=customer
        )

        # fwatch = FavoriteWatch.objects.create(
        #     label=request.data['label'],
        # )
        serializer = FavoriteWatchSeralizer(fwatch)
        return Response(serializer.data)

    def update(self, request, pk):
        editing_fwatch = FavoriteWatch.objects.get(pk=pk)
        editing_fwatch.content = request.data["content"]

        return Response(None, status=status.HTTP_205_RESET_CONTENT)

    def destroy(self, request, pk):
        fwatch = FavoriteWatch.objects.get(pk=pk)
        fwatch.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class WatchSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        fields = ('id', 'name', 'image')


class CustomerSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id',)


class FavoriteWatchSeralizer(serializers.ModelSerializer):
    watch = WatchSeralizer(many=False)
    customer = CustomerSeralizer(many=False)

    class Meta:
        model = FavoriteWatch
        fields = ('id', 'watch', 'customer')
