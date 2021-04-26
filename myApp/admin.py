from django.contrib import admin
from .models import EXP_Report

from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(EXP_Report)
class PersonAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['SM_NAME', 'SM_CODE', 'BR_NAMEA', 'BR_NAMEL',
                    'PS_BR_CODE', 'PRCU_NAME', 'PRCUCT_NAME']
    list_filter = ['PS_IVDATEG']

admin.site.site_header = 'Dashboard'