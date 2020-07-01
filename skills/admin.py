from django.contrib import admin

from .models import CreditOptions, Skills

class SkillsAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)
admin.site.register(Skills, SkillsAdmin)

class CreditOptionsAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'crew_position', 'year', 'get_username')
    admin.site.site_header = "Cion Crew Database"

    def get_username(self, obj):
        return obj.user
    get_username.short_description = 'User'
    get_username.admin_order_field = 'user__username'
admin.site.register(CreditOptions, CreditOptionsAdmin)