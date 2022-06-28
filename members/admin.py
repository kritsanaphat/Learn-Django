from django.contrib import admin

from members.models import Members

# Register your models here.
class MembersAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'status','register_at']
    search_fields =  ['firstname','lastname']
    list_filter = ['status']

admin.site.register(Members,MembersAdmin)