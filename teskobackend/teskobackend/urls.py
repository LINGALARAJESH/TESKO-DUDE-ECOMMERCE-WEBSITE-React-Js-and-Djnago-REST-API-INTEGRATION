from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header =" TESKO DUDE ADMIN "
admin.site.site_title =" TESKO DUDE ADMIN "

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include("app.urls")),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
