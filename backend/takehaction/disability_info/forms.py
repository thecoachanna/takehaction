from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "disability_name",
            "disability_description",
        )

    # def save(self, commit=True):
    #     user = super(NewUserForm, self).save(commit=False)
