from django.contrib import admin
from tapwn.news.models import Headline, Jumbotron

class HeadlineAdmin(admin.ModelAdmin):
    list_display = ['subject','schedule_content','publication_date',]
    list_display_links = ['subject','schedule_content','publication_date',]
    date_hierarchy = 'publication_date'
    search_fields = ['subject']

class JumbotronAdmin(admin.ModelAdmin):
    list_display = ['header_text','schedule_content_start','schedule_content_end','publication_date','affiliate_link',]
    list_display_links = ['header_text','schedule_content_start','schedule_content_end','publication_date','affiliate_link',]
    date_hierarchy = 'publication_date'
    search_fields = ['header_text']

admin.site.register(Headline, HeadlineAdmin)
admin.site.register(Jumbotron, JumbotronAdmin)