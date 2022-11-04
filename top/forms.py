from django import forms
from .models import Post

#ユーザーが投稿する内容
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('name', 'text',)
