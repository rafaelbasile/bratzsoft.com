from django.conf.urls import url, include


from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as drf_views
from rest_framework.routers import DefaultRouter


from .views import CustomerViewSet, AbapUserViewSet, CategoryViewSet, ComponentViewSet, HostViewSet, LandscapeRoleViewSet, NoteViewSet, AbapUserList



# Create a router and register our viewsets with it.
corerouter = DefaultRouter()
corerouter.register(r'customers', CustomerViewSet)



# Register SAP Settings
saprouter = DefaultRouter()
saprouter.register(r'abapusers', AbapUserViewSet)
saprouter.register(r'categories', CategoryViewSet)
saprouter.register(r'components', ComponentViewSet)
saprouter.register(r'hosts', HostViewSet)
saprouter.register(r'landscaperoles', LandscapeRoleViewSet)
saprouter.register(r'notes', NoteViewSet)





urlpatterns = [
    
    url(r'^access_token/', drf_views.obtain_auth_token),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(corerouter.urls)),
    url(r'^sap/', include(saprouter.urls)),


]

