from django import forms

class SubmissionForm(forms.Form):
  taskid = forms.CharField(label='Task id', max_length=100)
  lang = forms.CharField(max_length=10) # change to choice field later
  code = forms.CharField(widget=forms.Textarea)