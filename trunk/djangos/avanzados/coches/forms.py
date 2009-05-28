from django import forms
from models import Color, Coche

class CocheForm(forms.Form):
    TYPE_CHOICES = [(t.type, t.type) for t in Coche.objects.all()]
    COLOR_CHOICES = (('', '-- choose a vehicle type first --'))
    type = forms.CharField(choices=TYPE_CHOICES, \
        widget=forms.Select(attrs={'onchange':'get_vehicle_color();'}))
    color = forms.CharField(choices=COLOR_CHOICES)