from django.contrib import admin
from django.urls import path, include
from . import views as pviews
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pviews.welcome, name='welcome'),
    path('pr/', include('products.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
