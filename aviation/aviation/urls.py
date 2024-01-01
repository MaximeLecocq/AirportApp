"""
URL configuration for aviation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from rest_framework import routers
from airport.views import AirportViewSet,LargeAirportsViewSet,MediumAirportsViewSet,SmallAirportsViewSet,HeliportsViewSet,SeaplaneBasesViewSet,AsiaViewSet,AfricaViewSet,OceaniaViewSet,SouthCentralAmericaViewSet,EuropeViewSet,NorthAmericaViewSet

router = routers.SimpleRouter()

# routers for airport types
router.register('api',AirportViewSet)
router.register('large',LargeAirportsViewSet)
router.register('medium',MediumAirportsViewSet)
router.register('small',SmallAirportsViewSet)
router.register('heliports',HeliportsViewSet)
router.register('seaplane',SeaplaneBasesViewSet)

# routers for continents
router.register('asia',AsiaViewSet)
router.register('africa',AfricaViewSet)
router.register('oceania',OceaniaViewSet)
router.register('southcentralameria',SouthCentralAmericaViewSet)
router.register('europe',EuropeViewSet)
router.register('northamerica',NorthAmericaViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('',include('airport.urls')),
]