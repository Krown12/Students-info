from django.shortcuts import render,HttpResponse,redirect
from .models import *
# Create your views here.

def index(request):
    return HttpResponse("hello suka")

def home(request):
    return render(request,"index.html")

def aboutus(request):
    employee = [
        {
            "name":"hary",
            "branch":"ceo"
        },
        {
            "name":"sita",
            "branch":"manager"
        },
        {
            "name":"dhyam",
            "branch":"clerk"
        },
    ]
    name = "test"
    
    context = {
        "employee":employee
    }
    
    return render(request,'about-us.html',context)
def blog(request):
    return render(request,'blog.html')

def contactus(request):
    return render(request,'contact-us.html')

def register(request):
    context = {}
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        age = data.get('age') 
        grade = data.get('grade')
        faculty = data.get('faculty')
        description = data.get('description')
        nationality = data.get('nationality') =='on'
        stuimg = request.FILES.get('stuimage')
        print(name,age,faculty,grade)
        
        if name == ''and faculty=='':
            context={
                "error":"all value should be filled properly"
            }

        else:
            students.objects.create(
            name= name,
            age=age,
            faculty=faculty ,
            nationality = nationality,
            stuimg = stuimg,
            grade = grade,
            description = description
                          )
        

    return render(request,'register-id.html', context)
    

def students_info(request):
    info = students.objects.all()
    context = {
        "students":info
    }
    return render(request,"students_info.html",context)

def marked(request,pk):
    
    obj = students.objects.get(pk=pk)
    obj.is_selected=True
    obj.save()
    return redirect('/students-info/')

def edit(request,pk):
    try:
        obj = students.objects.get(id=pk)
        if request.POST == "POST":
            data = request.POST
            new_name = data.get('name')
            new_age = data.get('age')
            new_faculty = data.get('faculty')
            new_grade = data.get('grade')
            new_description = data.get('description')
            new_nationality = data.get('nationality') =='on'
            stuimg = request.FILES.get('stuimage')

            obj.name = new_name
            obj.age = new_age
            obj.faculty = new_faculty
            obj.grade = new_grade
            obj.description= new_description
            obj.nationality = new_nationality
            obj.stuimg=stuimg
            obj.save()
            return redirect("/students-info/")
        context = {
            "obj":obj
            }
        return render(request,"edit.html",context)
    except:
        return obj.DoesNotExist


def delete(request,pk):
    print(pk)
    obj = students.objects.get(pk=pk)
    obj.delete()
    return redirect('/students-info/')

    
