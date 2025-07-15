from django.forms import ModelForm
from .models import Page

#日記のページ用のフォーム
class PageForm(ModelForm):
    class Meta:
        model = Page
        #ユーザーが入力する項目
        fields = ["title", "body","page_date","picture"]
                