from django import forms

from .models import Post
from django.utils import timezone
from .models import Post_now
from .models import Remote_post
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


class PostForm(forms.ModelForm):
    class Meta:
        model = Post_now
        fields = ('text',)


class RemotePostForm(forms.ModelForm):
    class Meta:
        model = Remote_post
        fields = ('text','time')
        widgets = {
            'time': DateTimePickerInput(format='%m/%d/%Y HH:mm'),  # specify date-format
}


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)