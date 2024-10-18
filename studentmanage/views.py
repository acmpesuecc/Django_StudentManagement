from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddStudentForm,AddProfessorForm,AddCourseForm
from .models import Student,Courses,Professor,Scores,Taken,Taughtby

# Create your views here.

def home(request):
#login page is inside home function cause no one can view webpage without first being logged in

    if request.method=='POST':
        '''username=request.POST['username']
        password=request.POST['password']'''
        username = request.POST.get('username', '')
        password = request.POST.get('password', '') 
        #authenticate
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"You have been logged in!")
            return redirect('home')
        else:
            messages.success(request,"You have not been logged in")
            return redirect('home')  
    else:
        return render(request,'home.html')
    
def relations(request):
    scores = Scores.objects.all()
    taken=Taken.objects.all()
    taughtby=Taughtby.objects.all()
    return render(request,'relations.html',{'scores':scores,'taken':taken,'taughtby':taughtby})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect('home')

def register_user(request):
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            messages.success(request,"You have successfully registered...")
            return redirect('home')
    else:
        form=SignUpForm()
        return render(request,'register.html',{'form':form})
    
    return render(request,'register.html',{'form':form})

def student(request):
    student_records=Student.objects.all()
    accurate=[]
    if request.method=="POST":
        searched = request.POST.get('searched')
        accurate=[i for i in student_records if f"{i.rollno}"==searched or i.firstname==searched or i.lastname==searched or f"{i.phoneno}"==searched or i.email==searched]
    return render(request,'student.html',{'student_records':student_records, 'accurate':accurate})

def courses(request):
    course_records=Courses.objects.all()
    accurate=[]
    if request.method=="POST":
        searched = request.POST.get('searched')
        accurate=[i for i in course_records if f"{i.courseid}"==searched or i.coursename==searched or i.semester==searched ]
    return render(request,'courses.html',{'course_records':course_records,"accurate":accurate})

def professor(request):
    professor_records=Professor.objects.all()
    accurate=[]
    if request.method=="POST":
        searched = request.POST.get('searched')
        accurate=[i for i in professor_records if f"{i.profid}"==searched or i.name==searched or f"{i.phoneno}"==searched or i.email==searched]
    return render(request,'professor.html',{'professor_records':professor_records,"accurate":accurate})

def student_record(request,pk):
    if request.user.is_authenticated:
        #look up record
        student_record=Student.objects.get(rollno=pk)
        return render(request,'srecord.html',{'student_record':student_record})
    else:
        messages.success(request,"Login to view")
        return redirect('register')
    
def course_record(request,pk):
    if request.user.is_authenticated:
        #look up record
        course_record=Courses.objects.get(courseid=pk)
        return render(request,'crecord.html',{'course_record':course_record})
    else:
        messages.success(request,"Login to view")
        return redirect('register')
    
def prof_record(request,pk):
    if request.user.is_authenticated:
        #look up record
        prof_record=Professor.objects.get(profid=pk)
        return render(request,'precord.html',{'prof_record':prof_record})
    else:
        messages.success(request,"Login to view")
        return redirect('register')


def delete_srecord(request,pk):
    if request.user.is_authenticated:
        #delete for student
        delete_it=Student.objects.get(rollno=pk)
        delete_it.delete()
        messages.success(request,"Record Deleted Successfully...")
        return redirect('student')
    else:
        messages.success(request,"You must be logged in")
        return redirect('register')
    
def delete_crecord(request,pk):
    if request.user.is_authenticated:
        #delete for course - anything with 401 is deletable
        delete_it=Courses.objects.get(courseid=pk)
        delete_it.delete()
        messages.success(request,"Record Deleted Successfully...")
        return redirect('courses')
    else:
        messages.success(request,"You must be logged in")
        return redirect('register')
    
def delete_precord(request,pk):
    if request.user.is_authenticated:
        #delete for professor - anything starting from 3 is deletabloe
        delete_it=Professor.objects.get(profid=pk)
        delete_it.delete()
        messages.success(request,"Record Deleted Successfully...")
        return redirect('professor')
    else:
        messages.success(request,"You must be logged in")
        return redirect('register')
    
    '''def add_student(request):
   # form=AddStudentForm(request.POST or None)
    if request.method=="POST":
        form=AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Record Added Successfully...")
            return redirect('student')

            add_student = form.save()
            messages.success(request,"Record Added Successfully...")
            return redirect('student') 
        else:
            messages.success(request,"Form INVALID")
            #return redirect('student')
            return render(request, 'add_student.html', {'form': form})
    else:
        form=AddStudentForm()
    return render(request,'add_student.html',{'form':form})'''


def add_student(request):
    new_record=None
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddStudentForm(request.POST)
            if form.is_valid():
                new_record = form.save()  # Saving the form data to a variable named new_record
                messages.success(request, "Record Added successfully.")
                return redirect('student')
        else:
            form = AddStudentForm()

        return render(request, 'add_student.html', {'form': form,'new_record':new_record})
    else:
        messages.error(request, "You must be logged in.")
        return redirect('home')
    
def add_professor(request):
    new_record=None
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddProfessorForm(request.POST)
            if form.is_valid():
                new_record = form.save()  # Saving the form data to a variable named new_record
                messages.success(request, "Record Added successfully.")
                return redirect('professor')
        else:
            form = AddProfessorForm()

        return render(request, 'add_professor.html', {'form': form,'new_record':new_record})
    else:
        messages.error(request, "You must be logged in.")
        return redirect('home')
    
def add_course(request):
    new_record=None
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddCourseForm(request.POST)
            if form.is_valid():
                new_record = form.save()  # Saving the form data to a variable named new_record
                messages.success(request, "Record Added successfully.")
                return redirect('courses')
        else:
            form = AddCourseForm()

        return render(request, 'add_course.html', {'form': form,'new_record':new_record})
    else:
        messages.error(request, "You must be logged in.")
        return redirect('home')

    
def update_srecord(request,pk):
    if request.user.is_authenticated:
        student_record=Student.objects.get(rollno=pk)
        form=AddStudentForm(request.POST or None, instance=student_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been Updated...")
            return redirect('student')
        return render(request, 'update_srecord.html', {'form': form})
    else:
        messages.error(request, "You must be logged in.")
        return redirect('home')
    

def update_precord(request,pk):
    if request.user.is_authenticated:
        prof_record=Professor.objects.get(profid=pk)
        form=AddProfessorForm(request.POST or None, instance=prof_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been Updated...")
            return redirect('professor')
        return render(request, 'update_precord.html', {'form': form})
    else:
        messages.error(request, "You must be logged in.")
        return redirect('home')
    
def update_crecord(request,pk):
    if request.user.is_authenticated:
        course_record=Courses.objects.get(courseid=pk)
        form=AddCourseForm(request.POST or None, instance=course_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been Updated...")
            return redirect('courses')
        return render(request, 'update_crecord.html', {'form': form})
    else:
        messages.error(request, "You must be logged in.")
        return redirect('home')

'''
def student_record(request,pk):
    if request.user.is_authenticated:
        #look up record
        student_record=Student.objects.get(rollno=pk)
        return render(request,'srecord.html',{'student_record':student_record})
    else:
        messages.success(request,"Login to view")
        return redirect('register')


'''