from django.conf.urls import url, include


from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter


from .views import UserViewSet, AbapUserViewSet, CategoryViewSet, ComponentViewSet, HostViewSet, LandscapeRoleViewSet, LinkURLViewSet, NoteViewSet



# Create a router and register our viewsets with it.
router = DefaultRouter()
#router.register()
router.register(r'users', UserViewSet)




router.register(r'abapusers', AbapUserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'components', ComponentViewSet)
router.register(r'hosts', HostViewSet)
router.register(r'landscaperoles', LandscapeRoleViewSet)
router.register(r'links', LinkURLViewSet)
router.register(r'notes', NoteViewSet)




helper_patterns = [
    url(r'^', include(router.urls)),
    #url(r'^sap/', include(UserList.as_view()),
    #url(r'^users/', UserList.as_view()),
    #url(r'^users/(?P<pk>[0-9]+)/$', AbapUserDetail.as_view()),


    #url(r'^abapusers/', AbapUserList.as_view()),
    #url(r'^abapusers/(?P<pk>[0-9]+)/$', AbapUserDetail.as_view()),

    #url(r'^categories/', CategoryList.as_view()),
    #url(r'^categories/(?P<pk>[0-9]+)/$', CategoryDetail.as_view()),
]

urlpatterns = helper_patterns
#urlpatterns = format_suffix_patterns(urlpatterns)
