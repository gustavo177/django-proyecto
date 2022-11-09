from django import forms

class AgregarTarea(forms.Form):
    # Tipos de formulario
    # https://docs.djangoproject.com/en/4.1/topics/forms/
    tarea=forms.CharField()

class UploadFileForm(forms.Form):
    # Tipos de formulario
    # https://docs.djangoproject.com/en/4.1/topics/forms/
    title = forms.CharField(max_length=50)
    file = forms.FileField()


    