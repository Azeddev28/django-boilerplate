from django.db import models
from api.budgets.models import Budget, CostCenter

from api.companies.models import Classification, Company, Goal



class AccountingEntry(models.Model):
    description = models.CharField(max_length=100, blank=True, null=True)
    type_accounting_entry = models.IntegerField()
    goal = models.ForeignKey(Goal, models.DO_NOTHING, related_name='accounting_entries')
    classification = models.ForeignKey(Classification, models.DO_NOTHING, related_name='accounting_entries')
    observation = models.CharField(max_length=100, blank=True, null=True)
    cost_center = models.ForeignKey(CostCenter, models.DO_NOTHING, related_name='accounting_entries')
    deleted = models.BooleanField()
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True, related_name='accounting_entries')
    budget = models.ForeignKey(Budget, models.DO_NOTHING, related_name='accounting_entries') 

    class Meta:
        db_table = 'accountingentry'


class UnitMeasure(models.Model):
    acronym = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'unitmeasure'
