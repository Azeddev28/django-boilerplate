from django.contrib import admin

from api.companies.models import Company, Goal, Classification, Filter


admin.site.register(Company)
admin.site.register(Goal)
admin.site.register(Classification)
admin.site.register(Filter)
