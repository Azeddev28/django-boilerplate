from django.db import models


class Company(models.Model):
    company_code = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    parameter = models.CharField(max_length=100, blank=True, null=True)
    segment = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'company'


class Goal(models.Model):
    code = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    type_goal = models.IntegerField()

    class Meta:
        db_table = 'goal'


class Classification(models.Model):
    description = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'classification'


class Filter(models.Model):
    description = models.CharField(max_length=100, blank=True, null=True)
    competence = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'filter'
