from django.urls import path, include

from api.budgets import urls as budget_urls


urlpatterns = [
    path('', include(budget_urls)),
]
