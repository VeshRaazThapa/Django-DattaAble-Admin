from django import forms
from django.contrib.auth.models import User
from app.models import MemberInfo

class MemberInfoForm(forms.ModelForm):

    class Meta:
        model = MemberInfo
        fields = ('middle_name', 'designation', 'district', 'images','is_featured_member','is_home_featured_member')
        # fields = ('middle_name',)
class UserInfoForm(forms.ModelForm):

    class Meta:
        model = User
        fields = {'email','username','last_name','first_name'}
        # fields = ('username',)