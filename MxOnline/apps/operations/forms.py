import re

from django import forms
from MxOnline.apps.operations.models import UserFavorite


class UserFavForm(forms.ModelForm):
    class Meta:
        model = UserFavorite
        fields = ["fav_id", "fav_type"]