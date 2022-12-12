from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from chronosapi.models import Review


"""Chronos API Review View"""


class ReviewView(ViewSet):

    def retrieve(self, request, pk):
        post = Review.objects.get(pk=pk)
        serializer = ReviewSeralizer(post)
        return Response(serializer.data)

    def list(self, request):
        reviews = Review.objects.all()
        seralized = ReviewSeralizer(reviews, many=True)
        return Response(seralized.data, status=status.HTTP_200_OK)

    def create(self, request):
        review = review.objects.get(pk=request.data['reviews'])

        review = Review.objects.create(
            label=request.data['label'],
        )
        serializer = ReviewSeralizer(Review)
        return Response(serializer.data)

    def update(self, request, pk):
        editing_review = Review.objects.get(pk=pk)
        editing_review.content = request.data["content"]

        return Response(None, status=status.HTTP_205_RESET_CONTENT)

    def destroy(self, request, pk):
        review = Review.objects.get(pk=pk)
        review.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class ReviewSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'review', 'customerId', 'watchId')
