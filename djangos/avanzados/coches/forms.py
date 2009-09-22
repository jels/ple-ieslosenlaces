from django import forms
from models import Color, Coche

class CocheForm(forms.Form):
    TYPE_CHOICES = [(t.tipo, t.tipo) for t in Coche.objects.all()]
    COLOR_CHOICES = (('', '-- choose a vehicle type first --'))
    tipo = forms.CharField(
        widget=forms.Select(attrs={'onchange':'get_vehicle_color();'},
                            choices=TYPE_CHOICES))
    color = forms.CharField(
        widget=forms.Select(
            choices=COLOR_CHOICES)
        )
    
class PedidoCocheForm(forms.Form):
    NUM_PEDIDO = [(x, x) for x in range(10)]
    cant = forms.IntegerField(widget = forms.Select(choices=NUM_PEDIDO))
    
                    