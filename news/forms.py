from django.forms import ModelForm
from tapwn.news.models import Headline

class HeadlineForm(ModelForm):
    class Meta:
        model = Headline