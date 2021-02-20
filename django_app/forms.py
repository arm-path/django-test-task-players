from django import forms

from django_app.models import Comments


class CommentsForm(forms.ModelForm):
    """ Форма представления комментарии """

    class Meta:
        model = Comments
        fields = ['player', 'comment_text']
        widgets = {'comment_text': forms.Textarea(attrs={'class': 'form-control', 'rows': "1"})}
