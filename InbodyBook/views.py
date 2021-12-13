from django.http import request
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Machine,InbodyUser,Institution,IndiaRegions
import json
import xlwt
from django.http import HttpResponse
import time
# Create your views here.
def index(request):
    Machine_list = Machine.objects.filter(booked =False)

    machine_west_1 =  Machine.objects.filter(booked =False, region__region="West 1")
    machine_west_2 = Machine.objects.filter(booked =False, region__region="West 2")
    machine_north =  Machine.objects.filter(booked =False, region__region="North")
    machine_south = Machine.objects.filter(booked =False, region__region="South")
    machine_east = Machine.objects.filter(booked =False, region__region="East")
    
    user_list = InbodyUser.objects.all()
    indian_regions = IndiaRegions.objects.all()
    
    notify="error"
    #### Client ####
    if request.method == "POST":
    
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
        meachine_id_east = request.POST.get("meachine_name_east")
        meachine_id_west_1 = request.POST.get("meachine_name_west_1")
        meachine_id_west_2 = request.POST.get("meachine_name_west_2")
        meachine_id_north = request.POST.get("meachine_name_north")
        meachine_id_south = request.POST.get("meachine_name_south")
        if meachine_id_east:
            meachine_id= meachine_id_east
        if meachine_id_west_1:
            meachine_id=meachine_id_west_1
        if meachine_id_west_2:
            meachine_id=meachine_id_west_2
        if meachine_id_north:
            meachine_id=meachine_id_north
        if meachine_id_south:
            meachine_id=meachine_id_south
        ##### NO Vacent Machines #####
        else:
            print("this is called")
            return render(request,'form.html',{'Machine_list':Machine_list, 'users':user_list,
                'indian_regions':indian_regions,
                'machine_east':machine_east,
                'machine_west_1':machine_west_1,
                'machine_west_2':machine_west_2,
                'machine_north':machine_north,
                'machine_south':machine_south,
                'notify':"error_1",    
                
                })
        # add_region = IndiaRegions.objects.get(id=int(region))
        
        # connect_region_to_meachine = Machine(meachine_name=)
        
        add_user = InbodyUser.objects.get(id=int(user_id))
        Machine.objects.filter(id=int(meachine_id)).update(booked=True)
        add_meachine = Machine.objects.get(id=int(meachine_id))



        add_Institution=Institution(institution_name=institution_name,client_name=client_name,client_mobile=mobile_no,client_email=email,city=city,state=state,
                                            addr1=addr1,addr2=addr2,zip_code=zip_code,start_date=start_date,end_date=end_date,
                                            inbodyUser=add_user,meachine_name=add_meachine)
        add_Institution.save()
        notify="sucess"

 
    return render(request,'form.html',{'Machine_list':Machine_list, 'users':user_list,
    'indian_regions':indian_regions,
    'machine_east':machine_east,
    'machine_west_1':machine_west_1,
    'machine_west_2':machine_west_2,
    'machine_north':machine_north,
    'machine_south':machine_south,
    'notify':notify,    
    
    })

def region(request):
    # arm=request.GET.get('regioon')
    arm=json.loads(request.body)
    print("#############################")
    print(arm)
    return render(request,'form.html')
def show_record(request):
    records = Institution.objects.all()
 
    return render(request,'record.html',{'records':records})

# ***** Export To XL *****
 
import time
def export_to_xl(request):
    response = HttpResponse(content_type='application/ms-excel')
    timestr = time.strftime("%Y%m%d-%H%M%S")
    file_xl_name = "CSV_EXPORT_"+str(timestr)+".xls"
    response['Content-Disposition'] = 'attachment; filename='+str(file_xl_name)

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Institution Name', 'Client Name', 'Client Mobile', 'Client Email','City','State','Address1','Address2','Zip Code','Start Date','End Date','Inbody User','Machine Name']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Institution.objects.all().values_list('institution_name', 'client_name', 'client_mobile', 'client_email','city','state','addr1','addr2','zip_code','start_date','end_date','inbodyUser__name','meachine_name__meachine_name')

    for row in rows:
 
        row_num += 1
        for col_num in range(len(row)):
            if col_num == 9:
                ws.write(row_num, col_num, row[col_num].strftime('%d-%m-%Y'), font_style)
                continue
            if col_num == 10:
                ws.write(row_num, col_num, row[col_num].strftime('%d-%m-%Y'), font_style)
                continue
 
            ws.write(row_num, col_num, row[col_num], font_style)
            
    wb.save(response)

    return response
    
def qrcode(request):
    pass