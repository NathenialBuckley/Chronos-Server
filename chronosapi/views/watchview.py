from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from chronosapi.models import Watch, Customer, WatchType
from django.contrib.auth.models import User


class WatchView(ViewSet):
    """Chronos API Watch view"""

    def retrieve(self, request, pk=None):
        watch = Watch.objects.get(pk=pk)
        serialized = WatchSerializer(watch, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        watches = Watch.objects.all()
        serialized = WatchSerializer(watches, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        customer_id = Customer.objects.get(user=request.auth.user)
        watch_type = WatchType.objects.get(pk=request.data["watchTypeId"])
        watch = Watch.objects.create(
            name=request.data['name'],
            watchtype=watch_type,
            price=request.data['price'],
            customer=customer_id,
            image=request.data['image']
        )
        serializer = WatchSerializer(watch)
        return Response(serializer.data)

    def update(self, request, pk):
        editing_watch = Watch.objects.get(pk=pk)
        editing_watch.content = request.data["content"]

        return Response(None, status=status.HTTP_205_RESET_CONTENT)

    def destroy(self, request, pk=None):
        watch = Watch.objects.get(pk=pk)
        watch.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class UserSeralizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class CustomerSeralizer(serializers.ModelSerializer):
    user = UserSeralizer(many=False)

    class Meta:
        model = Customer
        fields = ('id', 'user')


class WatchSerializer(serializers.ModelSerializer):
    customer = CustomerSeralizer(many=False)

    class Meta:
        model = Watch
        fields = ('id', 'name', 'watchtype', 'price', 'customer', 'image')
