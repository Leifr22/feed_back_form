from django.forms import forms


class GalleryUplads(forms.Form):
    image=forms.FileField()