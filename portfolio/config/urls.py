from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

admin.site.site_header = "T. Vimala Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Manage portfolio content"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("portfolio.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
elif settings.SERVE_MEDIA:
    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {"document_root": settings.MEDIA_ROOT},
        ),
    ]
