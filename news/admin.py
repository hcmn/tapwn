from django.contrib import admin
from tapwn.news.models import Headline

class HeadlineAdmin(admin.ModelAdmin):
    list_display = ['subject','schedule_content','publication_date',]
    list_display_links = ['subject','schedule_content','publication_date',]
    date_hierarchy = 'publication_date'
    search_fields = ['subject']

admin.site.register(Headline, HeadlineAdmin)