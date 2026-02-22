from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student, Achievement, Category


# =========================
# DASHBOARD (cards + table)
# =========================
@login_required
def student_list(request):
    students = Student.objects.all()

    active_count = Student.objects.filter(status="Active").count()
    dept_count = Student.objects.values("department").distinct().count()

    context = {
        "students": students,
        "active_count": active_count,
        "dept_count": dept_count,
    }
    return render(request, "myapp2/student_detail.html", context)


# =========================
# STUDENTS PAGE (full list)
# =========================
@login_required
def students_page(request):
    students = Student.objects.all()
    return render(request, "myapp2/students_list.html", {"students": students})


# =========================
# STUDENT DETAIL
# =========================
@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    achievements = student.achievements.all()

    context = {
        "student": student,
        "achievements": achievements
    }
    return render(request, "myapp2/student_single_detail.html", context)


# =========================
# ADD STUDENT
# =========================
@login_required
def add_student(request):
    if request.method == "POST":
        Student.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            register_number=request.POST.get("register_number"),
            course=request.POST.get("course"),
            batch=request.POST.get("batch"),
            department=request.POST.get("department"),
            status=request.POST.get("status", "Active"),
        )
        return redirect("student_list")

    return render(request, "myapp2/student_form.html")


# =========================
# UPDATE ACHIEVEMENT STATUS
# =========================
@login_required
def update_achievement_status(request, pk, status):
    achievement = get_object_or_404(Achievement, pk=pk)
    if status in ["Approved", "Rejected", "Pending"]:
        achievement.status = status
        achievement.save()
    return redirect("student_detail", pk=achievement.student.pk)


# =========================
# DELETE STUDENT (POST only)
# =========================
@login_required
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
    return redirect("student_list")


# =========================
# EDIT STUDENT
# =========================
@login_required
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.register_number = request.POST.get("register_number")
        student.course = request.POST.get("course")
        student.batch = request.POST.get("batch")
        student.department = request.POST.get("department")
        student.status = request.POST.get("status", "Active")
        student.save()
        return redirect("student_list")

    # send student so form can prefill values
    return render(request, "myapp2/student_form.html", {"student": student})
