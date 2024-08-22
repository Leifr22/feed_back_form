from django import forms
from .models import Feedback

# class FeedbackForm(forms.Form):
#     name=forms.CharField(label='Имя',max_length=7, min_length=2, error_messages={
#         'max_length': 'Слишком много символов',
#         'min_length': 'Слишком мало символов',
#          'required': 'Укажите хотя бы один символ'})
#     surname=forms.CharField()
#     feedback=forms.CharField(widget=forms.Textarea())
#     rating=forms.IntegerField(label='Рейтинг', max_value=5, min_value=0)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields='__all__'
        labels={
            'name':'Имя',
            'surname':'Фамилия',
            'feedback':'Отзыв',
            'rating':'Рейтинг',
        }
        error_messages={
            'name':{
               'max_length': 'Слишком много символов',
               'min_length': 'Слишком мало символов',
               'required': 'Не должно быть пустым',
            },
            'surname': {
                'max_length': 'Слишком много символов',
                'min_length': 'Слишком мало символов',
                'required': 'Не должно быть пустым',
            },
            'feedback':{
                'required': 'Не должно быть пустым'
            },
            'rating': {
                'required': 'Не должно быть пустым'
            }
        }