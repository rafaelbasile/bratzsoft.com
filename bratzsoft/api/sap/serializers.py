
from rest_framework import serializers

from bratzsoft.sap.models import AbapUser, Category, Component, Host, LandscapeRole, LinkURL, Note

class AbapUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AbapUser
        depth = 1
        fields = ['id','username', 'sid', 'client', 'active']



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        depth = 1
        fields = ['id', 'name']

class ComponentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Component
        depth = 1
        fields =  ['id', 'name', 'description', 'active']

class HostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Host
        depth = 1
        fields = ['id', 'hostname', 'ipv4', 'Customer', 'active']

class LandscapeRoleSerializer(serializers.ModelSerializer):

    class Meta:

        model = LandscapeRole
        depth = 1
        fields = ['id', 'name', 'active']


class linkURLSerializer(serializers.ModelSerializer):

    class Meta:
        model = LinkURL
        depth = 1
        fields = ['id', 'link','Category']

class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        depth = 1
        fields = ['id', 'number', 'version', 'title', 'component', 'update_date', 'related_product', 'category']