from bratzsoft.accounts.models import User, Customer

from rest_framework import serializers


class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Customer
        depth =  1
        #fields = ['id','username',  'client', 'active']
        exclude = ['created_at',]
