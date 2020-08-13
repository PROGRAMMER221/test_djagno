from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.
def index(request):
    return render(request, 'index.html')

def StudentView(request):
    if request.method == 'POST':
        form = StudentForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm()

    return render(request, 'student.html',{'form':form})

def StudentDisplayView(request):
    context = {
        'student':Student.objects.all()
    }

    return render(request, 'student-display.html',context)