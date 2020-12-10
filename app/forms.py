from django import forms
from django.contrib.auth.models import User
from app.models import MemberInfo

class MemberInfoForm(forms.ModelForm):

    class Meta:
        model = MemberInfo
        fields = ('member_id','first_name','middle_name','last_name','email', 'designation', 'district',\
                  'profile_link_twt','profile_link_fb', \
                  'image','is_featured_member','is_home_featured_member')
