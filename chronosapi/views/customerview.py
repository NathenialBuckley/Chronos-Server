from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from chronosapi.models import Customer
from django.contrib.auth.models import User


"""Chronos API Cusotmer View"""


class CustomerView(ViewSet):

    def retrieve(self, request, pk):
        post = Customer.objects.get(pk=pk)
        serializer = CustomerSeralizer(post)
        return Response(serializer.data)

    def list(self, request):
        customers = Customer.objects.all()
        seralized = CustomerSeralizer(customers, many=True)
        return Response(seralized.data, status=status.HTTP_200_OK)

    def create(self, request):
        user = User.objects.get(pk=request.data['user'])
        customer = Customer.objects.get(pk=request.data['customers'])

        customer = Customer.objects.create(
            label=request.data['label'],
        )
        serializer = CustomerSeralizer(customer)
        return Response(serializer.data)

    def update(self, request, pk):
        editing_customer = Customer.objects.get(pk=pk)
        editing_customer.content = request.data["content"]

        return Response(None, status=status.HTTP_205_RESET_CONTENT)

    def destroy(self, request, pk):
        customer = Customer.objects.get(pk=pk)
        customer.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class CustomerSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'address', 'city', 'state',
                  'postalCode', 'phone', 'userId')
