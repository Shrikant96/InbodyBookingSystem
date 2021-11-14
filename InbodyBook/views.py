from django.http import request
from django.shortcuts import render
from .models import Meachines,InbodyUser,Institution,IndiaRegions
# Create your views here.
def index(request):
    meachines_list = Meachines.objects.filter(booked =False)
    user_list = InbodyUser.objects.all()
    indian_regions = IndiaRegions.objects.all()
    #### Client ####
    if request.method == 'POST':
        user_id = request.POST.get("user_name")
        institution_name = request.POST.get("institution_name")
        client_name = request.POST.get("client_name")
        mobile_no = request.POST.get("mobile_no")
        email = request.POST.get("email")
        city = request.POST.get("city")
        state = request.POST.get("state")
        addr1 = request.POST.get("addr1")
        addr2 = request.POST.get("addr2")
        zip_code = request.POST.get("zip_code")

        # region = request.POST.get("region")

        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        meachine_id = request.POST.get("meachine_name")

        # add_region = IndiaRegions.objects.get(id=int(region))
        
        # connect_region_to_meachine = Meachines(meachine_name=)
        
        add_user = InbodyUser.objects.get(id=int(user_id))
        Meachines.objects.filter(id=int(meachine_id)).update(booked=True)
        add_meachine = Meachines.objects.get(id=int(meachine_id))



        add_Institution=Institution(institution_name=institution_name,client_name=client_name,client_mobile=mobile_no,client_email=email,city=city,state=state,
                                            addr1=addr1,addr2=addr2,zip_code=zip_code,start_date=start_date,end_date=end_date,
                                            inbodyUser=add_user,meachine_name=add_meachine)
        add_Institution.save()
    return render(request,'form.html',{'meachines_list':meachines_list, 'users':user_list,'indian_regions':indian_regions})

def show_record(request):
    records = Institution.objects.all()
    return render(request,'record.html',{'records':records})