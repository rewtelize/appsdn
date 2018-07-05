from django import forms


class formRelacion(forms.Form):

    politica = forms.CharField(max_length=255)
    usuario = forms.CharField(max_length=255)

class formPolitica(forms.Form):

    porigen = forms.CharField(max_length=255)
    pdestino = forms.CharField(max_length=255)
    accion = forms.CharField(max_length=255)
    switch = forms.CharField(max_length=255)

class formUsuario(forms.Form):

    nombre = forms.CharField(max_length=255)
    apellidos = forms.CharField(max_length=255)
    correo = forms.CharField(max_length=255)
    usuario = forms.CharField(max_length=255)
    credencial = forms.CharField(max_length=255)

class formAplicacion(forms.Form):

    #archivo = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    #nombre = forms.CharField(max_length=128)
    #descripcion = forms.CharField(max_length=255)
    #archivo = forms.CharField(max_length=255)
    #autor = forms.CharField(max_length=255)
    #archivo = forms.FileField()
    pass

class formConfiguracion(forms.Form):

    #archivo = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    #nombre = forms.CharField(max_length=128)
    #descripcion = forms.CharField(max_length=255)
    #archivo = forms.CharField(max_length=255)
    #autor = forms.CharField(max_length=255)
    #archivo = forms.FileField()
    pass

class formConmutador(forms.Form):
    pass

class formLogin(forms.Form):
    pass

class formRegistro(forms.Form):
    pass
