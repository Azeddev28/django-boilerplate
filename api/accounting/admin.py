from django.contrib import admin

from api.accounting.models import AccountingEntry, UnitMeasure


admin.site.register(AccountingEntry)
admin.site.register(UnitMeasure)
