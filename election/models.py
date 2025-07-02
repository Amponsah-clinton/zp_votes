from django.db import models

from django.db import models

import random
from django.db import models

class Learner(models.Model):
    CLASS_CHOICES = [
        ('7A', '7A'),
        ('7B', '7B'),
        ('7C', '7C'),
        ('8A', '8A'),
        ('8B', '8B'),
    ]

    full_name = models.CharField(max_length=100)
    initials = models.CharField(max_length=10, blank=True)
    grade = models.CharField(max_length=10, choices=CLASS_CHOICES)
    has_voted = models.BooleanField(default=False)
    password = models.CharField(max_length=20, editable=False, blank=True)  # new

    def save(self, *args, **kwargs):
        if not self.initials:
            names = self.full_name.strip().split()
            self.initials = ''.join([n[0].upper() for n in names])
        self.initials = self.initials.upper()

        if not self.password:
            self.password = 'zpec' + ''.join(random.choices('0123456789', k=5))

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} ({self.initials}) - {self.grade}"

    class Meta:
        unique_together = ('initials', 'grade')

        
class Position(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Aspirant(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='aspirants/', default='aspirants/placeholder.jpg')

    def __str__(self):
        return f"{self.name} ({self.grade}) - {self.position.name}"


from django.utils import timezone
from django.db import models


from django.db import models

class Vote(models.Model):
    learner = models.ForeignKey('Learner', on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ForeignKey('Staff', on_delete=models.CASCADE, null=True, blank=True)
    position = models.ForeignKey('Position', on_delete=models.CASCADE)
    aspirant = models.ForeignKey('Aspirant', on_delete=models.CASCADE, related_name='votes')
    timestamp = models.DateTimeField(auto_now_add=True)  

    def clean(self):
        if not self.learner and not self.staff:
            raise ValidationError("Vote must be associated with either a learner or a staff.")
        if self.learner and self.staff:
            raise ValidationError("Vote cannot be associated with both learner and staff.")

    def __str__(self):
        return f"{self.learner or self.staff} voted for {self.aspirant} ({self.position})"

    
    
from django.db import models
from django.core.exceptions import ValidationError
import random

class Staff(models.Model):
    TITLE_CHOICES = [
        ('Mr.', 'Mr.'),
        ('Mrs.', 'Mrs.'),
        ('Aunty', 'Aunty'),
        ('Uncle', 'Uncle'),
        ('Sir', 'Sir'),
    ]

    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    name = models.CharField(max_length=100)
    role_or_subject = models.CharField(max_length=100)
    initials = models.CharField(max_length=10, editable=False, unique=True)
    password = models.CharField(max_length=20, editable=False, blank=True)
    has_voted = models.BooleanField(default=False)

    def clean(self):
        if not self.initials and self.name:
            names = self.name.strip().split()
            self.initials = ''.join([n[0].upper() for n in names])

        if not self.password:
            self.password = 'staff' + ''.join(random.choices('0123456789', k=5))

    def save(self, *args, **kwargs):
        self.clean()  
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} {self.name} ({self.initials}) - {self.role_or_subject}"

    class Meta:
        verbose_name_plural = "Staff"
