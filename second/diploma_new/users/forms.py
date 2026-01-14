from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.forms import ModelForm

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'input'})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        labels = {'first_name': 'Name', 'last_name': 'Surname'}

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['realt','first_name', 'last_name', 'email', 'username', 'phone', 'profile_image']
        labels = {'realt': 'Агентство','first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email', 'phone': 'телефон'}


