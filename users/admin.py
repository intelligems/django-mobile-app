from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import AccountChangeForm
from .models import Account


class AccountsAdmin(UserAdmin):
    form = AccountChangeForm
    list_display = ('username', 'first_name', 'last_name', 'last_login')


admin.site.register(Account, AccountsAdmin)
