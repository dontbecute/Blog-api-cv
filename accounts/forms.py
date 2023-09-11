from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class Createion(UserCreationForm):
    class Meta(UserCreationForm):
        model= CustomUser
        fields = UserCreationForm.Meta.fields + ("name", )

class Change(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields