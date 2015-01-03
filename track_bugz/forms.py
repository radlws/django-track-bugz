from django import forms
from models import Milestone


class MilestoneSelectForm(forms.Form):

    milestone = forms.ModelChoiceField(queryset=Milestone.objects.all(), widget=forms.Select(
        attrs={'class': 'milestone-select-noneed'}))