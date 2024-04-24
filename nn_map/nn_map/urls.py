from django.contrib import admin
from django.urls import path

from map_app.views import MyMapFolium

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MyMapFolium.as_view(template_name='my_nn.html'), name='my_nn')
]
