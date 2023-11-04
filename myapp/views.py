from django.http import JsonResponse
from django.shortcuts import render
from .models import Employee
from django.shortcuts import get_object_or_404

from django.http import HttpResponse



def default_view(request):
    return HttpResponse("Welcome to My Project")


def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'myapp/employee_list.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        designation = request.POST.get('designation')
        place = request.POST.get('place')
        salary = request.POST.get('salary')

        if name and dob and designation and place and salary:
            employee = Employee.objects.create(
                name=name,
                dob=dob,
                designation=designation,
                place=place,
                salary=salary
            )

           
            new_employee_data = {
                'name': employee.name,
                'dob': employee.dob,
                'designation': employee.designation,
                'place': employee.place,
                'salary': employee.salary
            }

            return JsonResponse({'success': True, 'new_employee': new_employee_data})
        else:
            return JsonResponse({'success': False, 'errors': 'All fields are required'})

    return render(request, 'myapp/employee_list.html')

def delete_employee(request, employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
        employee.delete()
        return JsonResponse({'success': True})
    except Employee.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Employee not found'})

def get_employee(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    employee_data = {
        'id': employee.id,
        'name': employee.name,
        'dob': employee.dob,
        'designation': employee.designation,
        'place': employee.place,
        'salary': employee.salary,
    }
    return JsonResponse({'success': True, 'employee': employee_data})

def update_employee(request, employee_id):
    if request.method == 'POST':
        employee = get_object_or_404(Employee, pk=employee_id)
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        designation = request.POST.get('designation')
        place = request.POST.get('place')
        salary = request.POST.get('salary')

        if name and dob and designation and place and salary:
            employee.name = name
            employee.dob = dob
            employee.designation = designation
            employee.place = place
            employee.salary = salary
            employee.save()
            return JsonResponse({'success': True, 'employee': {
                'id': employee.id,
                'name': name,
                'dob': dob,
                'designation': designation,
                'place': place,
                'salary': salary
            }})
        else:
            return JsonResponse({'success': False, 'errors': 'All fields are required'})


