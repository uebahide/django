from django import forms
from .models import BookModel
from datetime import datetime


class BookForm(forms.ModelForm):

    class Meta:
        model = BookModel
        fields = ('title', 'description', 'price')

    def save(self):
        obj = super(BookForm, self).save(commit=False)
        obj.created_at = datetime.now()
        obj.updated_at = datetime.now()
        obj.save()
        return obj