from django.forms import ModelForm
from quiz.models import Question
from django import forms

from django.utils.safestring import mark_safe


class PlainTextWidget(forms.Widget):
    def render(self, _name, value, _attrs):
        return mark_safe(value) if value is not None else '-'


class QuestionForm(ModelForm):
    text = forms.Field(
        widget=forms.TextInput(attrs={'rows': 4, 'cols': 15}),
    )

    boolfield = forms.TypedChoiceField(
        coerce=lambda x: x == 'True',
        choices=( (True, 'Yes'), (False, 'No')),
        widget=forms.RadioSelect
    )
    # answer = forms.BooleanField()


    def __init__(self, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        self.fields['text'].label = ''  # this removes the label from the form
        self.fields['boolfield'].label = ''

    class Meta:
        model = Question

        fields = ['text', 'answer']
