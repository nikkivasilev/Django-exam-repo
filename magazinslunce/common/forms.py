from django import forms
from magazinslunce.common.models import ProductRating, ProductComment


class ProductRatingForm(forms.ModelForm):
    class Meta:
        model = ProductRating
        fields = ('rating',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ("text",)
        widgets = {"text": forms.Textarea(attrs={"placeholder": "Add comment..."})}

