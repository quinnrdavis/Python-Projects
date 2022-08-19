from django.forms import ModelForm

from .models import Account, Transaction


# creates Account form based on Account model
class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


# creates Transaction form based on Transaction model
class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
