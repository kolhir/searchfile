from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50, label="Название")
    file = forms.FileField(label = "Файл")


