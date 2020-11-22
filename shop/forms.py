from django import forms
from .models import Product, Type


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'type'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'description': forms.Textarea(attrs={
            }),
        }

    # remove the help text
    def __init__(self, *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)

        for fieldname in ['name', 'description', 'type']:
            self.fields[fieldname].help_text = None


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'description',
        ]
        widgets = {
            'description': forms.Textarea(attrs={
            }),
        }
