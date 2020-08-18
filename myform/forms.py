from django import forms

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'act', 'nov', 'dec']
choice_day = [(str(i), str(i)) for i in range(1, 31)]
choice_month = [(str(i+1), months[i]) for i in range(len(months))]
choice_year = [(str(i), str(i)) for i in range(1980, 2021)]

class SampleForm(forms.Form):
    firstname = forms.CharField(max_length=20, label='First name:', required=True)
    lastname = forms.CharField(max_length=20, label='First name:', required=False)
    email = forms.EmailField(max_length=100, label='Email address', required=True)
    phonenum = forms.IntegerField(max_value=99999999999, min_value=6000000000, required=True)
    pswrd = forms.CharField(max_length=20, label='Password', widget=forms.PasswordInput)
    birthday = forms.ChoiceField(choices=choice_day, required=True, label='Birth day')
    bmonth = forms.ChoiceField(choices=choice_month, required=True, label='birth month')
    byear = forms.ChoiceField(choices=choice_year, required=True, label='birth year')