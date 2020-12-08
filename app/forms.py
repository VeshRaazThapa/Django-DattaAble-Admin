from django import forms
from django.contrib.auth.models import User
from app.models import MemberInfo

class MemberInfoForm(forms.ModelForm):
    class Meta:
        model = MemberInfo
        fields = ('','designation', 'district', 'images','is_featured_member','is_home_featured_member','twitter_link','fb_link')

