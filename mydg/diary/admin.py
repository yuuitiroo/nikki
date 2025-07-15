from django.contrib import admin
from .models import Page


#管理サイトにページのデータを表示
#dmin.site.register(Page)
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ["id", "created_at", "updated_at"]
