from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('compress', views.compress, name='compress'),
    path('get_user_images', views.get_user_images, name='get_user_images'),
    path('delete_image/<slug:user>/<slug:image>', views.delete_image, name='delete_image'),
    path('delete_all_for_user/<slug:user>', views.delete_all_for_user, name='delete_all_for_user'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)