from django import forms

class FinanceForm(forms.Form):
    date = forms.DateTimeField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Date & Time",
        required=True
    )
    howmuch = forms.IntegerField(
        label="How Much?",
        min_value=0,
        required=True
    )
    why = forms.CharField(
        label="Why?",
        max_length=200,
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        required=True
    )
    mode = forms.ChoiceField(
        label="Mode of Payment",
        choices=[
            ('UPI', 'UPI'),
            ('Cash', 'Cash'),
            ('Netbanking', 'Netbanking'),
            ('Debit Card', 'Debit Card'),
            ('Credit Card', 'Credit Card')
        ],
        required=True
    )
