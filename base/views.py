from django.shortcuts import render
from django.http import JsonResponse
from .serializers import DrinkSerializer
from .models import Drink
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
@api_view(['GET','POST'])
def drink_list(request):

	if request.method == 'GET':
		drinks = Drink.objects.all()
		serializer = DrinkSerializer(drinks, many=True)
		return JsonResponse({'drinks':serializer.data})

	if request.method == 'POST':
		serializer = DrinkSerializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response({'drinks':serializer.data}, status = status.HTTP_201_CREATED)

