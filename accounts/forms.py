from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser


class CustomUserCreationForm (UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'age', 'email', )


class CustomUserChangeForm (UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'age', 'email', )
