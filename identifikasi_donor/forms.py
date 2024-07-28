from django import forms

class FormIdentifikasiDonor(forms.Form):
    age = forms.IntegerField(label='Age')
    hemoglobin = forms.FloatField(label='Hemoglobin')
    weight = forms.FloatField(label='Weight')
    systolic = forms.IntegerField(label='Systolic Blood Pressure')
    diastolic = forms.IntegerField(label='Diastolic Blood Pressure')
