from django import forms


class AddIndicationsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(AddIndicationsForm, self).__init__(*args, **kwargs)
        self.fields['date'] = forms.DateField(label='Дата снятия показаний')
        self.fields['indications'] = forms.CharField(label='Показания', widget=forms.Textarea)


class SubscribeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SubscribeForm, self).__init__(*args, **kwargs)
        self.fields['email'] = forms.EmailField(label='Email:')
