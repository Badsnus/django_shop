from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('catalog/', include('catalog.urls')),
    path('blog/', include('blog.urls')),
    path('contacts/', include('contacts.urls')),
    path('profile/', include('user_profile.urls')),
    path('send_message/', include('send_message.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
