from import_export import resources
from .models import EXP_Report

class PersonResource(resources.ModelResource):
    class Meta:
        model = EXP_Report