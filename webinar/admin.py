from django.contrib import admin
from webinar.models import JustUser,JustEdit,Webinar
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(JustUser)
class JustUserAdmin(ImportExportModelAdmin):
    pass

admin.site.register(JustEdit)
admin.site.register(Webinar)