from rest_framework import serializers

from api.budgets.models import Budget, Company, Indicator, CompetenceCostCenterStructure


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicator
        fields = '__all__'


class BudgetSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    indicator = IndicatorSerializer()

    class Meta:
        model = Budget
        fields = '__all__'


class CompetenceCostCenterStructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetenceCostCenterStructure
        fields = '__all__'
