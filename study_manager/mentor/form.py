from django import forms
from tasks.models import Tasks

class CreatTaskForm(forms.ModelForm):
    class Meta:
        model=Tasks
        fields="__all__"
        exclude=["mentor_id","student_id","situation"]

