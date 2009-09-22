from django import forms

class ContactForm(forms.Form):
    almacen  = forms.CharField(max_length=100)
    direccion = forms.CharField()
    email = forms.EmailField()
    
class FormularioLineaPedido(forms.Form):
    pass
