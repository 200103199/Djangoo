from django.shortcuts import render, redirect
from .forms import EmpForm
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .import models
from .models import *

def add_emp(request):
    if request.method == "GET":
        form = EmpForm()
        return render(request, "myapp/from.html", {"form": form})
    else:
        form = EmpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data.pop("r_salary")
            models.Emp.objects.create(**data)
            return redirect('/admin')
        else:
            clear_errors = form.errors.get("all")
            return render(request, "myapp/from.html", {"form": form, "clear_errors": clear_errors})




# Create your views here.
def book(request):
    object_list = Book.objects.all()
    student_list = Book.objects.all()

    search_query = request.POST.get('search')

    if not search_query:
        search_query = ""
    if request.method == 'POST':
        object_list = Book.objects.filter(student_name__icontains=search_query)

    return render(request, 'polls/book.html', {'object_list': object_list})