from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api.budgets.views import BudgetListView, BudgetViewSet, BudgetListPaginatedView, CompetenceCostCenterStructureListView, CompetenceCostCenterStructureViewset

budget_router = DefaultRouter()
budget_router.register(r'', BudgetViewSet, basename='budget')


completence_cost_center_structure_router = DefaultRouter()
completence_cost_center_structure_router.register(r'', CompetenceCostCenterStructureViewset, basename='budget')


urlpatterns = [
    # Paginated list route
    path('budget/list-paginated/', BudgetListPaginatedView.as_view(), name='budget-paginated'),
    # Whole list route
    path('budget/list/', BudgetListView.as_view(), name='budget-all'),

    # Exclude the list URL from the router-generated URLs
    path('budget/', include(budget_router.urls)),

    path('competenceCostCenterStructure/list/', CompetenceCostCenterStructureListView.as_view(), name='budget-all'),

    # Exclude the list URL from the router-generated URLs
    path('competenceCostCenterStructure/', include(completence_cost_center_structure_router.urls)),
]
