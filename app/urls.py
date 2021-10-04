from django.contrib import admin
from django.urls import path, include
from members.views import MemberLoginView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('dgev_admin/sesiones/', include('members.urls')),
                  path('dgev_admin/', include('core.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
