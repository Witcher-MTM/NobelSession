from .models import Bank
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from datetime import datetime, date, timedelta


class BankForm(ModelForm):
    class Meta:
        today_date = datetime.now().strftime('%Y-%m-%d')
        model = Bank
        fields = ["bank_name",
                  "bank_city",
                  "bank_description",
                  "bank_founder_name",
                  "bank_founder_surname",
                  "bank_founder_birthday",
                  "bank_found_date",
                  "bank_avatar"]
        widgets = {
            "bank_name": TextInput(attrs={
                'class': 'form-input block w-full focus:bg-white',
                'id': 'bank_name',
                'value': ''
            }),
            "bank_city": TextInput(attrs={
                'class': 'form-input block w-full focus:bg-white',
                'id': 'bank_city',
                'value': ''
            }),
            "bank_description": Textarea(attrs={
                'class': 'form-textarea block w-full focus:bg-white',
                'id': 'bank_description',
                'rows': '8',
                'value': ''
            }),
            "bank_founder_name": TextInput(attrs={
                'class': 'form-input block w-full focus:bg-white',
                'id': 'owner_name',
                'value': ''
            }),
            "bank_founder_surname": TextInput(attrs={
                'class': 'form-input block w-full focus:bg-white',
                'id': 'owner_secondname',
                'value': ''
            }),
            "bank_founder_birthday": DateTimeInput(attrs={
                'class': 'form-input block w-full focus:bg-white',
                'id': 'owner_birthday',
                'type': 'date',
                'value': '',
                'max': (date.today() - timedelta(days=365 * 18)).isoformat()
            }),
            "bank_found_date": DateTimeInput(attrs={
                'class': 'form-input block w-full focus:bg-white',
                'id': 'bank_birthday',
                'value': '',
                'type': 'date',
                'max': today_date
            }),

        }