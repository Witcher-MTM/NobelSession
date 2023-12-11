from .models import User
from django.forms import ModelForm, TextInput, DateInput, Textarea
from datetime import datetime, date, timedelta


class BankForm(ModelForm):
    class Meta:
        today_date = datetime.now().strftime('%Y-%m-%d')
        model = User
        fields = ["user_name",
                  "user_surname",
                  "user_age",
                  "user_email",
                  "user_hashpass",
                  "bank_id"]
        widgets = {
            "user_name": TextInput(attrs={
                'id': 'user_name',
            }),
            "user_surname": TextInput(attrs={
                'id': 'user_surname',
            }),
            "user_age": DateInput(attrs={
                'id': 'user_age',
                'max': (date.today() - timedelta(days=365 * 18)).isoformat()
            }),
            "user_email": TextInput(attrs={
                'id': 'user_email',
                'type':'email'
            }),
            "user_hashpass": TextInput(attrs={
                'id': 'user_hashpass',
                'type': 'password'
            }),
            "bank_id": TextInput(attrs={
                'id': 'bank_id',
            })
        }