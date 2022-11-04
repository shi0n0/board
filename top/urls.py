from django.contrib import admin
from django.urls import include, path

from ..myoriginal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myoriginal/', include("myoriginal.urls")),
]