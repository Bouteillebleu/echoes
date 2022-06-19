from django.urls import path, re_path

from . import views
from .views import plain_text as views_plain_text

urlpatterns = [
    # Pages available to everyone.
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    # Pages / endpoints available to those who are logged in.
    # - Plain text visions, volumes, full year.
    path('vision/<int:pk>/text', views_plain_text.show_vision, name="plain_text_vision"),
    re_path('volume/(?P<volume_number>[1-9][0-9]*[a-d])/text', views_plain_text.show_single_volume,
            name="plain_text_single_volume"),
    path('volume/<int:volume_major_number>/text', views_plain_text.show_full_year,
         name="plain_text_full_year")
    # - Previews of visions, volumes, full year?
    # - DOCX (or PDF?) visions, volumes, full year.
    # Pages available to those who are logged in and have edit permissions.
    # - Add the next event
    # - Edit existing vision
    # - Add new vision
]
