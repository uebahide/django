from django import forms
from FormApp.models import Student, Class

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        class_choices = [(c.id, c.name) for c in Class.objects.all()]
        self.fields['student_class'].choices = class_choices

