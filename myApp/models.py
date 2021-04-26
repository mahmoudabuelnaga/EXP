from django.db import models

# Create your models here.

class EXP_Report(models.Model):
    PS_IVDATEG      = models.DateField(null=True, blank=True)
    PS_BR_CODE      = models.CharField(max_length=50, null=True, blank=True)
    BR_NAMEA        = models.CharField(max_length=100, null=True, blank=True)
    BR_NAMEL        = models.CharField(max_length=100, null=True, blank=True)
    SM_CODE         = models.CharField(max_length=50, default='null', null=True, blank=True)
    SM_NAME         = models.CharField(max_length=200, null=True, blank=True)
    PRCU_CODE       = models.CharField(max_length=50, default='null', null=True, blank=True)
    PRCU_NAME       = models.CharField(max_length=50, default='null', null=True, blank=True)
    MOBILE          = models.CharField(max_length=50, default='null', null=True, blank=True)
    PRCUCT_NAME     = models.CharField(max_length=50, default='null', null=True, blank=True)
    CT_DISCOUNT     = models.CharField(max_length=50, default=0, null=True, blank=True)
    count           = models.CharField(max_length=50, null=True, blank=True)
    TOTALPRICE      = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    NET_PRICE       = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    POINTS_GAINED   = models.CharField(max_length=50, null=True, blank=True)
    POINTS_USED     = models.CharField(max_length=50, null=True, blank=True)
    POINTS_DISCOUNT = models.CharField(max_length=50, null=True, blank=True)


    def __str__(self):
        return self.SM_NAME