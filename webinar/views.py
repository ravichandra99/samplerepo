from django.shortcuts import render,HttpResponse,HttpResponseRedirect,get_object_or_404
from webinar.forms import UserForm
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from webinar.models import JustEdit,Webinar
from django.urls import reverse
import uuid

# Create your views here.
def Index(request):
    w = get_object_or_404(Webinar, id = 1)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            just_id =str(uuid.uuid4())
            form.instance.just_id = just_id
            to_mail = form.cleaned_data['email']
            e = JustEdit.objects.get(ref = 'asdf')
            sub = e.subject
            msg = e.body +'\n'+ just_id
            send_mail(sub ,msg ,'CodeGnan IT SOLUTIONS <info@codegnan.com>',[to_mail],fail_silently=False)
            # redirect to a new URL:
            form.save()
            return HttpResponseRedirect(reverse('webinar:thanks',args=(just_id,)))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'index.html', {'form': form,'w':w})


def thanks(request,just_id):
    w = get_object_or_404(Webinar, id = 1)
    return render(request,'thanks.html',{'w':w,'just_id':just_id})