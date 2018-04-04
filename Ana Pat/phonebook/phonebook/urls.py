from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
        url(r'^contact/',
            include('contact.urls'), name="contact"),
        url(r'^admin/', admin.site.urls),
]
