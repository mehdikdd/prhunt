from django.contrib import admin
from django.urls import path, include
from . import views as pviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pviews.welcome, name='welcome'),
    path('pr/', include('products.urls')),
]
