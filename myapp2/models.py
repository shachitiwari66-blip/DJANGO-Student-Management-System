from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    register_number = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=100)
    batch = models.CharField(max_length=20)
    department = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='Active')
    created_at = models.DateTimeField(auto_now_add=True)  # add this

    def __str__(self):
        return f"{self.name} ({self.register_number})"


class Achievement(models.Model):
    # Foreign Keys link tables together
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='achievements') 
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) 
    title = models.CharField(max_length=200) # [cite: 15]
    description = models.TextField() # [cite: 17]
    proof = models.FileField(upload_to='proofs/', blank=True, null=True) 
    date = models.DateField() # [cite: 23]
    status = models.CharField(max_length=10, choices=[('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending')], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True) 