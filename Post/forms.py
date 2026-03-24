from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget

class PostForm(forms.ModelForm):
    class Meta:
        content = forms.CharField(widget=CKEditorWidget())
        model = Post
        fields = ['title', 'content', 'img', 'active']