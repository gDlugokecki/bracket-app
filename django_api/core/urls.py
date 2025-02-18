"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from ninja import Redoc
from apps.match.api import match_router
from apps.player.api import player_router
from apps.tournament.api import tournament_router
from apps.authentication.api import auth_router
from ninja import NinjaAPI

api = NinjaAPI(docs=Redoc())


@api.get("/hello")
def hello(request):
    return "hello world"


api.add_router("/match/", match_router)
api.add_router("/player/", player_router)
api.add_router("/tournament/", tournament_router)
api.add_router("/auth/", auth_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls),
]
