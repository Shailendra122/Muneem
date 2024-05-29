from django import forms
from .models import Account_Data

class DateInput(forms.DateInput):
        input_type='date'

class AccountForm(forms.ModelForm):
    d_o_c_options=(('Debit','Debit'),('Credit','Credit'))
    d_or_c=forms.ChoiceField(choices=d_o_c_options,widget=forms.RadioSelect,label='Debit Or Credit')

    class Meta:
        model=Account_Data
        fields=['d_or_c','name','m_no','date','amount','paid','date_of_transaction']
        
        widgets ={
            'date':DateInput,
            'date_of_transaction':DateInput(),
        }
