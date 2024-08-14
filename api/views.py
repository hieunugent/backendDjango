from django.http import JsonResponse
from rest_framework import generics
from .models import User
from .serializers import UserSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def user_list(request):
    users = User.objects.all().values()
    return JsonResponse(list(users), safe=False)

def add_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        user = User(name=name, email=email)
        user.save()
        return JsonResponse({"message": "User added successfully!"}, status=201)
