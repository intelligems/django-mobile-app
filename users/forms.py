from django.contrib.auth.forms import UserChangeForm

from .models import Account


class AccountChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Account
