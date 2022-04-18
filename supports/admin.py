from django.contrib import admin
from .models import Faq#,Ans

#admin.site.register(Faq)

#class AnsInline(admin.TabularInline):


@admin.register(Faq)
class FqaModelAdmin(admin.ModelAdmin):
    list_display = (
'writer',
'created_at',
'modifier',
'modified_date',
    )
    search_fields = ('category','writer','modifier')
    search_help_text = '카테고리, 작성자, 수정자 검색'
    readonly_fields = ('created_at','modified_date',)
    #inlines = [AnsInline]
    