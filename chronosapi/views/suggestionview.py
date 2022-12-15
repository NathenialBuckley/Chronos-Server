from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from chronosapi.models import Suggestion


class SuggestionView(ViewSet):
    """Chronos API Suggestion View"""

    def retrieve(self, request, pk=None):
        suggest = Suggestion.objects.get(pk=pk)
        serialized = SuggestionSerializer(
            suggest, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self):
        suggest = Suggestion.objects.all()
        serialized = SuggestionSerializer(suggest, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        suggest = Suggestion.objects.get(pk=request.data['suggestion'])

        suggest = Suggestion.objects.create(
            label=request.data['label'],
        )
        serializer = SuggestionSerializer(suggest)
        return Response(serializer.data)

    def update(self, request, pk):
        editing_suggestion = Suggestion.objects.get(pk=pk)
        editing_suggestion.content = request.data["content"]

        return Response(None, status=status.HTTP_205_RESET_CONTENT)

    def destroy(self, request, pk):
        suggest = Suggestion.objects.get(pk=pk)
        suggest.delete()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


class SuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suggestion
        fields = ('id', 'name', 'watchtype', 'price', 'customerId')
