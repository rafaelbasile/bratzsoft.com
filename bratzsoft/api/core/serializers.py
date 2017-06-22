from bratzsoft.accounts.models import User

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        depth =  1
        #fields = ['id','username',  'client', 'active']
        exclude = ['password',]
