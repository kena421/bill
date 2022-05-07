from django.contrib import admin

from main.models import ADMIN_MODELS, Profile, Student, Teacher



admin.site.site_header = "School Management"
admin.site.site_title = "School Management"
admin.site.index_title = "School Management"

class TeacherAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
         if db_field.name == 'profile':
             kwargs["queryset"] = Profile.objects.filter(role=Profile.ROLES[1][0])
                #  kwargs["queryset"] = Company.objects.filter(name='Test')
         return super(TeacherAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Teacher, TeacherAdmin)

class StudentAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
         if db_field.name == 'profile':
             kwargs["queryset"] = Profile.objects.filter(role=Profile.ROLES[0][0])
                #  kwargs["queryset"] = Company.objects.filter(name='Test')
         return super(StudentAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Student, StudentAdmin)

CUSTOM_ADMIN = [Teacher, Student]
MODEL_ADMIN = list(set(ADMIN_MODELS) - set(CUSTOM_ADMIN))

for model in MODEL_ADMIN:
    admin.site.register(model)
