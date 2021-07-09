from django import forms
from grader_web.settings import supportedLangs

Langs = [(lang, supportedLangs[lang]['name']) for lang in supportedLangs]
class SubmissionForm(forms.Form):
  taskid = forms.CharField(label='Task id', max_length=100)
  lang = forms.CharField(widget=forms.Select(choices=Langs, attrs={"id":"lang"}))
  code = forms.CharField(widget=forms.Textarea(attrs={"id":"editor"}))

class TaskSubmitForm(forms.Form):
  lang = forms.CharField(widget=forms.Select(choices=Langs, attrs={"id":"lang"}))
  code = forms.CharField(widget=forms.Textarea(attrs={"id":"editor"}))