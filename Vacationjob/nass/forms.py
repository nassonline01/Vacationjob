from django import forms
from .models import TaskUserAssignment

class TaskSubmissionForm(forms.ModelForm):
    like = forms.BooleanField(required=False, label="Liked")
    subscribe = forms.BooleanField(required=False, label="Subscribed")
    follow = forms.BooleanField(required=False, label="Followed")
    comment = forms.BooleanField(required=False, label="Commented")

    class Meta:
        model = TaskUserAssignment
        fields = ['proof_screenshot', 'proof_text', 'proof_video']
