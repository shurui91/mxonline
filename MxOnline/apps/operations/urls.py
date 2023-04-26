from django.urls import re_path as url
from MxOnline.apps.operations.views import AddFavView, CommentView

urlpatterns = [
    url(r'^fav/$', AddFavView.as_view(), name="fav"),
    url(r'^comment/$', CommentView.as_view(), name="comment"),
]
