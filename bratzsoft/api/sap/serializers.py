
from rest_framework import serializers

from bratzsoft.sap.models import AbapUser, Category, Component, Host, LandscapeRole, Note


class AbapUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = AbapUser
        depth = 2
        fields = ['id', 'username', 'sap_system', 'client', 'active']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        depth = 1
        fields = ['id', 'name']


class ComponentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Component
        depth = 1
        fields = ['id', 'name', 'description', 'active']


class HostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Host
        depth = 2
        fields = ['id', 'hostname', 'ipv4', 'active']


class LandscapeRoleSerializer(serializers.ModelSerializer):

    class Meta:

        model = LandscapeRole
        depth = 1
        fields = ['id', 'name', 'active']


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        depth = 1
        fields = ['id', 'number', 'version', 'title', 'component', 'update_date', 'related_product', 'category']
