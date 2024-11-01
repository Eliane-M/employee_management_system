# employee_management_system

A comprehensive RESTful API built using Django and Django REST Framework for managing employee records, including CRUD operations, attendance tracking, and role-based permissions for different users. This system also supports validation for unique email addresses and employee IDs, as well as secure authentication and permission controls.

Features
Employee Management: Create, update, retrieve, and delete employee records with validation for unique identifiers.
Attendance Tracking: Record employees' check-in and check-out times, with options to filter by date range.
Role-Based Access Control: Ensures that only authorized users (with IsManagement permissions) can manage employee records.
Validation: Checks for valid email formats, unique emails, and a properly formatted employee ID.

To test it you will need to first do the following steps

## clone the repo
git clone https://github.com/Eliane-M/employee_management_system.git

## install dependencies
pip install -r requirements.txt

## apply migrations
py manage.py migrate

## then run the server
py manage.py runserver

the secret key used was "gg&$ozfa4k2(u^nt6bs+9^@e#3ebc%vm176mevn8)+xw6o^5#t"
