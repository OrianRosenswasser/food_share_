# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from main.serializers import FoodPostSerializer, RegisterSerializer
from .models import Member, FoodPost
from .forms import MemberForm, FoodPostForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework import generics

# Home Page
def home(request):
    return render(request, 'index.html')

# Register View
@api_view(['GET', 'POST'])
def register(request):
    if request.method == 'GET':
        # If it's a GET request, we could return a registration form (for a front-end interface).
        return Response({"message": "Register page"})

    elif request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Food Feed View
@api_view(['GET'])
def food_feed(request):
    if request.method == 'GET':
        # Get all food posts from the database
        food_posts = FoodPost.objects.all()
        # Serialize the food posts
        serializer = FoodPostSerializer(food_posts, many=True)
        # Return the serialized data as JSON
        return Response(serializer.data)

    elif request.method == 'POST':
        # Create a new food post
        serializer = FoodPostSerializer(data=request.data)
        if serializer.is_valid():
            # Save the new food post and return it
            serializer.save()
            return Response(serializer.data, status=201)  # 201 Created status
        return Response(serializer.errors, status=400) 

# Post Food View
@api_view(['GET', 'POST'])
def post_food_page(request):
    if request.method == 'GET':
        # Get all food posts
        food_posts = FoodPost.objects.all()
        serializer = FoodPostSerializer(food_posts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # Handle the creation of a new food post
        serializer = FoodPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
# Login View (Add actual authentication logic)

@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'GET':
        # Return a login form or message (adjust as necessary)
        return Response({"message": "Login page"})
    
    elif request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Logged in successfully"})
        return Response({"message": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


class FoodPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodPost.objects.all()
    serializer_class = FoodPostSerializer

def index(request):
    # Ensure the path to your build folder is correct
    return render(request, 'index.html')