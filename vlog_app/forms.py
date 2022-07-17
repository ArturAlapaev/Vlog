from django import forms
from .models import Post, User


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = '__all__' -выбирает все колонки
        fields = ('title', 'img', 'description', 'is_draft')

    def save(self, user_id, commit=True):
        form = super().save(commit=False)
        user = User.objects.get(pk=user_id)
        form.user_id = user
        return form.save()


class EditPostForm(forms.ModelForm):

    img = forms.ImageField(
        required=False
    )

    class Meta:
        model = Post
        fields = ('title', 'img', 'description', 'is_draft', 'is_delete')