from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import generics, viewsets

from bratzsoft.sap.models import AbapUser, Category, Component, Host, LandscapeRole, LinkURL, Note
from bratzsoft.api.sap.serializers import AbapUserSerializer, CategorySerializer, ComponentSerializer, HostSerializer,LandscapeRoleSerializer, linkURLSerializer, NoteSerializer
from bratzsoft.api.core.serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AbapUserViewSet(viewsets.ModelViewSet):
    queryset = AbapUser.objects.all()
    serializer_class = AbapUserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = UserSerializer

class ComponentViewSet(viewsets.ModelViewSet):
    queryset = Component.objects.all()
    serializer_class = ComponentSerializer

class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer

class LandscapeRoleViewSet(viewsets.ModelViewSet):
    queryset = LandscapeRole.objects.all()
    serializer_class = LandscapeRoleSerializer

class LinkURLViewSet(viewsets.ModelViewSet):
    queryset = LinkURL.objects.all()
    serializer_class = linkURLSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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

class LinkURLList(generics.ListCreateAPIView):
    queryset = LinkURL.objects.all()
    serializer_class = linkURLSerializer

class linkURLDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LinkURL.objects.all()
    serializer_class = linkURLSerializer

class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetail(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
