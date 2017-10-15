from django.shortcuts import render

from rest_framework import generics, viewsets


from bratzsoft.sap.models import AbapUser, Category, Component, Host, LandscapeRole, Note
from bratzsoft.api.sap.serializers import AbapUserSerializer, CategorySerializer, ComponentSerializer, HostSerializer,LandscapeRoleSerializer, NoteSerializer






class AbapUserViewSet(viewsets.ModelViewSet):
    queryset = AbapUser.objects.all()
    serializer_class = AbapUserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

class LandscapeRoleViewSet(viewsets.ModelViewSet):
    queryset = LandscapeRole.objects.all()
    serializer_class = LandscapeRoleSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class AbapUserList(generics.ListCreateAPIView):
    queryset = AbapUser.objects.all()
    serializer_class = AbapUserSerializer


class AbapUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AbapUser.objects.all()
    serializer_class = AbapUserSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = AbapUserSerializer


class ComponentList(generics.ListCreateAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class ComponentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class HostList(generics.ListCreateAPIView):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

class Hostdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

class LandscapeRoleList(generics.ListCreateAPIView):
    queryset = LandscapeRole.objects.all()
    serializer_class = LandscapeRoleSerializer

class LandscapeRoleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LandscapeRole.objects.all()
    serializer_class = LandscapeRoleSerializer


class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetail(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
