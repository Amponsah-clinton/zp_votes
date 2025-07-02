from django.contrib import admin
from .models import Learner, Position, Aspirant, Vote, Staff

class LearnerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'initials', 'grade', 'has_voted', 'password')

admin.site.register(Learner, LearnerAdmin)  
admin.site.register(Position)
admin.site.register(Aspirant)
admin.site.register(Vote)




@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'initials', 'role_or_subject', 'has_voted', 'password')
    search_fields = ('name', 'initials')
    list_filter = ('role_or_subject', 'has_voted', 'title')  # Optional: allow filtering by title
