from django.db import models

from api.base_models import BaseModel
from api.companies.models import Company, Filter


class Indicator(models.Model):
    description = models.CharField(max_length=100, blank=True, null=True)
    competence = models.IntegerField()
    type_indicator = models.IntegerField()
    percentual = models.IntegerField()
    month = models.IntegerField()
    type_readjustment = models.IntegerField()
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True, related_name='indicators')

    class Meta:
        db_table = 'indicator'


class Budget(BaseModel):
    approach = models.IntegerField()
    automatic_accept_date = models.DateTimeField()
    automatic_accept_email = models.CharField(max_length=100, blank=True, null=True)
    closing_date = models.DateTimeField()
    closing_email = models.CharField(max_length=100, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    competence = models.IntegerField()
    description = models.CharField(max_length=100, blank=True, null=True)
    group_legend = models.IntegerField()
    indicator = models.ForeignKey(Indicator, models.DO_NOTHING, blank=True, null=True, related_name='budgets')
    month_challenge_forecast = models.IntegerField()
    opening_date = models.DateTimeField()
    projection_indicator_id = models.BigIntegerField(blank=True, null=True)
    status_budget = models.IntegerField()
    type_budget = models.IntegerField()
    type_projection = models.IntegerField()

    class Meta:
        db_table = 'budget'


class CostClassStructure(models.Model):
    code = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    type_cost_class = models.IntegerField()
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name='cost_structures')
    is_package = models.BooleanField()
    purpose = models.IntegerField()
    pmso = models.IntegerField()
    indicator_projection = models.ForeignKey(Indicator, models.DO_NOTHING, blank=True, null=True, related_name='cost_structure_projections')
    is_blocked_projection = models.BooleanField()
    is_blocked_base_scenario = models.BooleanField()
    is_blocked_free_account = models.BooleanField()
    is_blocked_activation = models.BooleanField()
    is_blocked_shared = models.BooleanField()
    indicator_classification = models.ForeignKey(Indicator, models.DO_NOTHING, blank=True, null=True, related_name='cost_structure_classifications')
    competence = models.IntegerField()
    is_negative_value = models.BooleanField()
    indicator_material_service = models.ForeignKey(Indicator, models.DO_NOTHING, blank=True, null=True, related_name='cost_structures_material_services')

    class Meta:
        db_table = 'costclassstructure'


class CostClass(BaseModel):
    cost_class_structure = models.ForeignKey(CostClassStructure, models.DO_NOTHING, related_name='cost_classes')
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True, related_name='cost_classes')
    budget = models.ForeignKey(Budget, models.DO_NOTHING, related_name='cost_classes')

    class Meta:
        db_table = 'costclass'


class CompetenceCostCenterStructure(models.Model):
    description = models.CharField(max_length=100, blank=True, null=True)
    competence = models.IntegerField()

    class Meta:
        db_table = 'competencecostcenterstructure'


class CostCenterStructure(models.Model):
    code = models.CharField(max_length=100, blank=True, null=True)
    coverage_code = models.IntegerField()
    description = models.CharField(max_length=100, blank=True, null=True)
    type_cost_center = models.IntegerField()
    coverage = models.IntegerField()
    parent = models.ForeignKey('self', models.DO_NOTHING, related_name='cost_center_structures')
    hierarchy = models.IntegerField(blank=True, null=True)
    deadline_release = models.DateTimeField()
    competence = models.IntegerField()
    activatable = models.BooleanField()
    shared = models.BooleanField()
    competence_cost_center_structure = models.ForeignKey(CompetenceCostCenterStructure, models.DO_NOTHING, related_name='cost_center_structures')

    class Meta:
        db_table = 'costcenterstructure'



class CostCenter(models.Model):
    cost_center_structure = models.ForeignKey(CostCenterStructure, models.DO_NOTHING, related_name='cost_centers')
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True, related_name='cost_centers')
    budget = models.ForeignKey(Budget, models.DO_NOTHING, related_name='cost_centers')

    class Meta:
        db_table = 'costcenter'


class ParametrizationCostClass(models.Model):
    use = models.IntegerField()
    cost_class_code = models.CharField(max_length=100, blank=True, null=True)
    group_cost_class_code = models.CharField(max_length=100, blank=True, null=True)
    module = models.IntegerField()

    class Meta:
        db_table = 'parametrizationcostclass'


class Itemfilter(models.Model):
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True, related_name='item_filters')
    budget = models.ForeignKey(Budget, models.DO_NOTHING, related_name='item_filters')
    cost_center = models.ForeignKey(CostCenter, models.DO_NOTHING, blank=True, null=True, related_name='item_filters')
    filter = models.ForeignKey(Filter, models.DO_NOTHING, related_name='item_filters')

    class Meta:
        db_table = 'itemfilter'


class Permission(models.Model):
    type_permission = models.IntegerField()
    user_network = models.CharField(max_length=100, blank=True, null=True)
    budget = models.ForeignKey(Budget, models.DO_NOTHING, related_name='permissions')
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True, related_name='permissions')
    cost_center = models.ForeignKey(CostCenter, models.DO_NOTHING, blank=True, null=True, related_name='permissions')
    cost_class = models.ForeignKey(CostClass, models.DO_NOTHING, blank=True, null=True, related_name='permissions')

    class Meta:
        db_table = 'permission'
