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

    machine_west_1 =  Machine.objects.filter(booked =False, region__id=1)
    machine_west_2 = Machine.objects.filter(booked =False, region__id=2)
    machine_north =  Machine.objects.filter(booked =False, region__id=4)
    machine_south = Machine.objects.filter(booked =False, region__id=5)
    machine_east = Machine.objects.filter(booked =False, region__id=6)

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
        'notify':notify,
        'machine_east':machine_east,
        'machine_west_1':machine_west_1,
        'machine_west_2':machine_west_2,
        'machine_north':machine_north,
        'machine_south':machine_south
        })

    return render(request,'form.html',{'Machine_list':Machine_list, 'users':user_list,
    'indian_regions':indian_regions,
    'machine_east':machine_east,
    'machine_west_1':machine_west_1,
    'machine_west_2':machine_west_2,
    'machine_north':machine_north,
    'machine_south':machine_south    
    
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
# def export_to_xl(request):
    
#     # workbook = xlwt.Workbook() 
    
#     # sheet = workbook.add_sheet("Sheet Name")
    
#     # # Applying multiple styles
#     # style = xlwt.easyxf('font: bold 1, color red;')
    
#     # # Writing on specified sheet
#     # sheet.write(0, 0, 'SAMPLE', style)
  
#     # workbook.save("sample.xls")
 
 
#     # response = redirect('/show-record')
#     # return response
 
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="users.xlsx' 

#     wb = xlwt.Workbook(encoding='utf-8')
#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True
#     ws = wb.add_sheet('Booking_records') # this will make a sheet named Users Data
   
#     row = 1
#     col = 0
#     data = Institution.objects.all()
#     for res in data:
#         ws.write(row, col,res.institution_name)
#         ws.write(row, col+1,res.client_name)
#         ws.write(row, col+2,res.client_mobile)
#         ws.write(row, col+3,res.client_email)
#         ws.write(row, col+4,res.city)
#         ws.write(row, col+5,res.state)
#         ws.write(row, col+6,res.addr1)
#         #### if conditon need to be add ### 
#         ws.write(row, col+7,res.addr2)
#         ws.write(row, col+8,res.zip_code)
#         ws.write(row, col+9,res.start_date)
#         ws.write(row, col+10,res.end_date) 
#         ws.write(row, col+11,res.inbodyUser.name)
#         ws.write(row, col+12,res.meachine_name.meachine_name) 

 
 
#     # # Sheet header, first row
#     # row_num = 0

#     # font_style = xlwt.XFStyle()
#     # font_style.font.bold = True

#     # columns = ['Username', 'First Name', 'Last Name', 'Email Address', ]

#     # for col_num in range(len(columns)):
#     #     ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

#     # # Sheet body, remaining rows
#     # font_style = xlwt.XFStyle()

#     # rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
#     # for row in rows:
#     #     row_num += 1
#     #     for col_num in range(len(row)):
#     #         ws.write(row_num, col_num, row[col_num], font_style)

#     wb.save(response)

#     return response
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
