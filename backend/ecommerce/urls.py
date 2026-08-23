from django.conf import settings  # pyright: ignore[reportMissingModuleSource]
from django.conf.urls.static import static  # pyright: ignore[reportMissingModuleSource]
from django.contrib import admin  # pyright: ignore[reportMissingModuleSource]
from django.urls import (  # type: ignore
    include,
    path,
)  # pyright: ignore[reportMissingModuleSource]

urlpatterns = [

    path(
        "admin/",
        admin.site.urls
    ),

    path(
        "api/",
        include("store.urls")
    ),
]


if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )