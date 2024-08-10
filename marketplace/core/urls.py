from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from core.views import index, contacts

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)