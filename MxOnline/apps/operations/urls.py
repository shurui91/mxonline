from django.urls import re_path as url
from MxOnline.apps.operations.views import AddFavView

urlpatterns = [
    url(r'^fav/$', AddFavView.as_view(), name="fav"),
]
