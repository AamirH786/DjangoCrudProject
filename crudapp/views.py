from django.shortcuts import render
from .models import Student
from django.contrib import messages
from django.db.models import Q

def index(request):
    students = Student.objects.all()
    query = ""
    if request.method == 'POST':
        if 'add' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            address = request.POST.get('address')
            Student.objects.create(
                name=name,
                email=email,
                address=address
            )

            messages.success(request, "Record Added Successfully")
            
        elif 'update' in request.POST:
            id = request.POST.get('id')
            name = request.POST.get('name')
            email = request.POST.get('email')
            address = request.POST.get('address')
            try:
                update_student = Student.objects.get(id=id)
                update_student.name = name
                update_student.email = email
                update_student.address = address
                update_student.save()
                messages.success(request, "Record Updated Successfully")
            except Student.DoesNotExist:
                messages.error(request, "Student does not exist.")
            
        elif 'delete' in request.POST:
            id = request.POST.get('id')
            try:
                student = Student.objects.get(id=id)
                student.delete()
                messages.success(request, "Record Deleted Successfully")
            except Student.DoesNotExist:
                messages.error(request, "Student does not exist.")
            
        elif 'search' in request.POST:
            query = request.POST.get('searchquery')
            if query:
                students = Student.objects.filter(Q(name__icontains=query) | Q(email__icontains=query) | Q(address__icontains=query))
    
    context = {'students': students, "query":query}
    return render(request, 'index.html', context=context)
