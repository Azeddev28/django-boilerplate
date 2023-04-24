from django.contrib import admin

from api.budgets.models import Indicator, Budget, CostCenterStructure, CostClassStructure, CostClass, CostCenter


admin.site.register(Indicator)
admin.site.register(Budget)
admin.site.register(CostCenterStructure)
admin.site.register(CostClassStructure)
admin.site.register(CostClass)
admin.site.register(CostCenter)
