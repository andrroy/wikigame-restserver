from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from sites.models import Task

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


class TaskSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Task
		fields = ('start_url', 'end_url')

class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all().filter(start_url = "http://no.m.wikipedia.org/wiki/Dahls_Pils") #### FIX!!!
	serializer_class = TaskSerializer

router.register(r'tasks', TaskViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
