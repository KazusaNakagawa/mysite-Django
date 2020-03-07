from django.forms import ModelForm, TextInput, Textarea

from blog.models import Comment, Reply


class CommentForm(ModelForm):
    class Meta(object):
        model = Comment
        fields = ('author', 'text')
        # bootstrapのform-controlを使用している
        widgets = {
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '名前',
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'コメント内容',
            }),
        }
        # Put label name in placeholder
        labels = {
            'author': '',
            'text': '',
        }


class ReplyForm(ModelForm):
    class Meta(object):
        model = Reply
        fields = ('author', 'text')
        widgets = {
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': '名前',
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': '返信内容',
            }),
        }
        labels = {
            'author': '',
            'text': '',
        }
