from django.contrib.auth.models import User, Group
from rest_framwork import serializers

class UserSerializers(serializers.HyperlinkdModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializers(serializers.HyperlinkdModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
