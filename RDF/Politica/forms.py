from django import forms

#from .models import Usuario

class formContacto(forms.Form):

        #cuentanos = forms.CharField(label='Cuentanos', max_length=1000)
        #cuentanos = forms.CharField(required=True)
    
    nombre = forms.CharField(max_length=30)
    email = forms.CharField(max_length=50)
    cuentanos = forms.CharField(max_length=255)

        #fields = ('cuentanos',)

    def clean_cuentanos(self):

        cuentanos = self.cleaned_data.get('cuentanos')
        if cuentanos == str():
            raise forms.ValidationError("Por favor, rellene el campo.")

        return cuentanos

    def clean_nombre(self):

        nombre = self.cleaned_data.get('nombre')
        if nombre == str():
            raise forms.ValidationError("Por favor, rellene el campo.")

        return nombre

    def clean_email(self):

        email = self.cleaned_data.get('email')
        if email == str():
            raise forms.ValidationError("Por favor, rellene el campo.")

        if email.find("@") == -1:
        	raise forms.ValidationError("Por favor, introduzca un email correcto.")

        return email