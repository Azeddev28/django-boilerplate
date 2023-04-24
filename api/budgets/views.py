from rest_framework.mixins import (
    CreateModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    ListModelMixin
)
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet

from api.budgets.models import Budget, CompetenceCostCenterStructure
from api.budgets.serializers import BudgetSerializer, CompetenceCostCenterStructureSerializer


class BudgetViewSet(
    CreateModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def create(self, request, *args, **kwargs):
        if "id" in request.data:
            return self.update(request, *args, **kwargs)

        return super().create(request, *args, **kwargs)


class BudgetListPaginatedView(GenericAPIView, ListModelMixin):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer

    def post(self, request, *args, **kwargs):
        # Call the list method to retrieve the list of objects
        return self.list(request, *args, **kwargs)


class BudgetListView(GenericAPIView, ListModelMixin):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    pagination_class = None
    ordering = 'created_at'

    def post(self, request, *args, **kwargs):
        # Call the list method to retrieve the list of objects
        return self.list(request, *args, **kwargs)


class CompetenceCostCenterStructureViewset(
    CreateModelMixin,
    UpdateModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
    GenericViewSet,
):
    queryset = CompetenceCostCenterStructure.objects.all()
    serializer_class = CompetenceCostCenterStructureSerializer
    
    def create(self, request, *args, **kwargs):
        if "id" in request.data:
            return self.update(request, *args, **kwargs)

        return super().create(request, *args, **kwargs)


class CompetenceCostCenterStructureListPaginatedView(GenericAPIView, ListModelMixin):
    queryset = CompetenceCostCenterStructure.objects.all()
    serializer_class = CompetenceCostCenterStructureSerializer

    def post(self, request, *args, **kwargs):
        # Call the list method to retrieve the list of objects
        return self.list(request, *args, **kwargs)


class CompetenceCostCenterStructureListView(GenericAPIView, ListModelMixin):
    queryset = CompetenceCostCenterStructure.objects.all()
    serializer_class = CompetenceCostCenterStructureSerializer
    pagination_class = None
    ordering = 'created_at'

    def post(self, request, *args, **kwargs):
        # Call the list method to retrieve the list of objects
        return self.list(request, *args, **kwargs)


