from django import forms
from .models import TaskUserAssignment,Task

class TaskSubmissionForm(forms.ModelForm):
    like = forms.BooleanField(required=False, label="Liked")
    subscribe = forms.BooleanField(required=False, label="Subscribed")
    follow = forms.BooleanField(required=False, label="Followed")
    comment = forms.BooleanField(required=False, label="Commented")

    class Meta:
        model = TaskUserAssignment
        fields = ['proof_screenshot', 'proof_text', 'proof_video']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'payout', 'deadline', 'created_by', 'users_assigned', 'proof', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter task title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Enter task description'}),
            'payout': forms.NumberInput(attrs={'class': 'form-control'}),
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'created_by': forms.Select(attrs={'class': 'form-select'}),
            'users_assigned': forms.CheckboxSelectMultiple(attrs={'class': 'users-assigned'}),
            'proof': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Optional proof details'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
