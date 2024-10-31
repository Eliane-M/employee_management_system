from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from employee.models import Employee
from employee.serializers import EmployeeSerializer
from accounts.permissions.permissions import IsManagement
from rest_framework.response import Response
from rest_framework import status
from base.services.auth import verify_user


#For the list of all employees
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsManagement])
def get_employees(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True).data
        return Response({'employees': serializer}, status=status.HTTP_200_OK)


#For the employee details by ID 
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsManagement])
def get_employee(request, employee_id):
    try:
        employee = Employee.objects.get(employeeId=employee_id)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
    

#For deleting an employee
@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsManagement])
def delete_employees(request):
    if request.method == 'DELETE':
        id = request.data.get('id')
        if id is None:
            return Response({"error": "Employee ID is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            employee = Employee.objects.get(id=id)
            employee.delete()
            return Response({"message": "Employee deleted successfully"}, status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        

#For adding a new employee
@api_view(['POST'])
@permission_classes([IsAuthenticated, IsManagement])
def add_new_employee(request):
    name = request.data.get('name')
    email = request.data.get('email')
    employeeId = request.data.get('employeeId')
    phone_number = request.data.get('phone_number')

    if not name or not email or not employeeId or not phone_number:
        return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

    if Employee.objects.filter(email=email).exists() or Employee.objects.filter(employeeId=employeeId).exists():
        return Response({"error": "An employee with this email or ID already exists"}, status=status.HTTP_409_CONFLICT)

    # Creating the employee
    try:
        employee = Employee(
            name=name,
            email=email,
            employeeId=employeeId,
            phone_number=phone_number
        )
        employee.save()
        return Response({"message": "Employee created successfully"}, status=status.HTTP_201_CREATED)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": f"There was an error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

#For updating an employee
@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsManagement])
def update_employee(request, employee_id):
    try:
        employee = Employee.objects.get(employeeId=employee_id)
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)

    name = request.data.get('name', employee.name)
    email = request.data.get('email', employee.email)
    phone_number = request.data.get('phone_number', employee.phone_number)

    if email != employee.email and Employee.objects.filter(email=email).exists():
        return Response({"error": "An employee with this email already exists"}, status=status.HTTP_409_CONFLICT)

    try:
        employee.name = name
        employee.email = email
        employee.phone_number = phone_number
        employee.save()

        return Response({
            "name": employee.name,
            "email": employee.email,
            "employeeId": employee.employeeId,
            "phone_number": employee.phone_number
        }, status=status.HTTP_200_OK)
    
    except Employee.DoesNotExist:
        return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": f"There was an error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)