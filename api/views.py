from django.contrib.auth.models import User, Group
from rest_framwork import viewsets
from api.serializers import UserSerializer, GroupSerializer

class UserViewSet(views.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(views.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
