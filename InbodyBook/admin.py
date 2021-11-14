from django.contrib import admin
from InbodyBook.models import Institution, InbodyUser, Meachines,IndiaRegions
# Register your models here.
@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display=('id','institution_name','meachine_name','inbodyUser','client_name','client_mobile',
    'client_email','city','state','addr1','addr2','zip_code','start_date',
    'end_date')

@admin.register(InbodyUser)
class InbodyUserAdmin(admin.ModelAdmin):
    list_display=('id','name','email','mobile')

@admin.register(Meachines)
class Meachines(admin.ModelAdmin):
    list_display=('id','meachine_name','region','booked')

@admin.register(IndiaRegions)
class IndiaRegions(admin.ModelAdmin):
    list_display=('id','region')