from django.shortcuts import render

# Create your views here.
import csv
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Event, Student, Branch, Blog, AvailableFeatures
from django.views import View
from .forms import BlogForm
from django.core.mail import send_mail


# Create your views here.
# homepage view
class OpenView(View):
    def get(self, request):
        for i in Event.objects.filter(current_status=True):
            if i.warn:
                b = True
                break
        else:
            b = False
        if len(Event.objects.filter(current_status=True)) == 0:
            b = False
        return render(request, 'form/HomePage.html', {'error': Event.objects.filter(current_status=True), 'status': b})


# Register View
class CheckView(View):
    def get(self, request):
        msg = request.session.get('msg', False)
        if msg: del (request.session['msg'])
        context = {'event': Event.objects.all(), 'branch': Branch.objects.all(), 'error': msg}
        return render(request, 'form/register.html', context)

    def post(self, request):
        event = request.POST.get('event')
        student_name = request.POST.get('student_name')
        email_id = request.POST.get('email_p')
        mobile_number = request.POST.get('mobile_number')
        roll_no = request.POST.get('roll_no')
        branch = request.POST.get('branch')
        e = Event.objects.filter(current_status=True)
        a = Student.objects.filter(roll_no=roll_no.strip(), event__current_status=True)
        if len(a) == 0:
            s = Student(event=e.get(event_name=event), student_name=student_name, email_id=email_id.strip(),
                        mobile_number=mobile_number, roll_no=roll_no, branch=Branch.objects.get(branch_name=branch))
            s.save()
            message = send_mail("Successfully Registered for Event",
                                "You Have been Successfully Registered for the " + e.get(
                                    event_name=event).event_name + "\n We want you to be present half hour before "
                                                                   "event will be started\n" + "Event Timing :" +
                                str(e.get(
                                    event_name=event).pub_date.date()) + " " + str(e.get(
                                    event_name=event).pub_date.time()) + "\nEvent Venue: " + e.get(
                                    event_name=event).event_venue + "\nIf any detail is missing in this mail feel "
                                                                    "free to contect us.",
                                "shia.sharma123@gmail.com", [email_id], fail_silently=False)
            if (message):
                request.session['msg'] = "We have sent you a mail"
            else:
                request.session['msg'] = "Student has Registered Successfully"
            return redirect(request.path)
        else:
            for i in a:
                if i.event.event_name == event.strip():
                    b = True
                    break
            else:
                b = False
            if b:
                request.session['msg'] = "Student has Already Registered for the Event"
                return redirect(request.path)
            else:
                s = Student(event=e.get(event_name=event), student_name=student_name, email_id=email_id.strip(),
                            mobile_number=mobile_number, roll_no=roll_no, branch=Branch.objects.get(branch_name=branch))
                s.save()
                message = send_mail("Successfully Registered for Event",
                                    "You Have been Successfully Registered for the " + e.get(event_name=event).event_name + "\n We want you to be present half hour before event will be started\n" + "Event Timing :" +str(e.get(event_name=event).pub_date.date())+" "+str(e.get(event_name=event).pub_date.time())+"\nEvent Venue: " + e.get(event_name=event).event_venue + "\nIf any detail is missing in this mail feel free to contect us.",
                                    "shia.sharma123@gmail.com", [email_id], fail_silently=False)
                if (message):
                    request.session['msg'] = "We have sent you a mail"
                else:
                    request.session['msg'] = "You have Registered For More than One Events"

                return redirect(request.path)


# Event Page View
class EventView(View):
    def get(self, request):
        context = {'event': Event.objects.all()}
        return render(request, 'form/eventdetail.html', context)


# Download Data In CSV Format
class DownloadData(View):
    def get(self, request):
        msg = request.session.get('msg', False)
        if msg: del (request.session['msg'])
        context = {'error': msg}
        return render(request, 'form/download.html', context)

    def post(self, request):
        code = request.POST['eve_code']
        response = HttpResponse(content_type='text/csv')
        writer = csv.writer(response)
        writer.writerow(['Event', 'Student Name', 'Email', 'Mobile No', 'Roll No', 'Branch'])
        a = Student.objects.filter(event__event_code=code.strip())
        if len(a) > 0:
            for stu in a.values_list('event__event_name',
                                     'student_name',
                                     'email_id',
                                     'mobile_number',
                                     'roll_no',
                                     'branch__abbr'):
                writer.writerow(stu)
            response['Content-Disposition'] = 'attachment;filename="data.csv"'
            return response
        else:
            request.session['msg'] = "No Event with this code Exist or No Data Available"
            return redirect(request.path)


# 404 Error Page Not Found View
def view_404(request, exception):
    return render(request, 'form/404.html')


class Blog(View):
    def get(self, request):
        msg = request.session.get('msg', False)
        form = BlogForm()
        if msg: del (request.session['msg'])
        context = {'form': form, 'message': msg}
        return render(request, 'form/blog.html', context)

    def post(self, request):
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            request.session['msg'] = "We Have Got Your Stand"
            return redirect(request.path)
        else:
            request.session['msg'] = "Try Again !"
            return redirect(request.path)

# Create your views here.
