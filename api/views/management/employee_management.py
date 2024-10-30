from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from employee.models import Employee
from employee.serializers import EmployeeSerializer
from accounts.permissions.permissions import IsAdmin
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdmin])
def get_employees(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True).data
        return Response({'employees': serializer}, status=status.HTTP_200_OK)