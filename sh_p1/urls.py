
from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^persons/', include('persons.urls',namespace='persons')),
    url(r'^', include('persons.urls',namespace='persons')),
    url('^', include('django.contrib.auth.urls')),
    #url('^accounts/', include('django.contrib.auth.urls')),
    url('^accounts/', include('accounts.urls',namespace='accounts')),

]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)