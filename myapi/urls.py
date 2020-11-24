from django.urls import include, path
from rest_framework import routers
from myapi.views import HeroViewSet

app_name = "myapi"

router = routers.DefaultRouter()
router.register(r'heroes',HeroViewSet)


urlpatterns = [ 
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]
