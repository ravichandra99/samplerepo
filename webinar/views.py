from django.shortcuts import render,HttpResponse
from webinar.forms import UserForm
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from webinar.models import JustEdit

# Create your views here.
class Index(FormView):
    template_name = 'index.html'
    form_class = UserForm
    success_url = '/thanks/'

    def form_valid(self, form):
        to_mail = form.cleaned_data['email']
        e = JustEdit.objects.get(ref = 'asdf')
        sub = e.subject
        msg = e.body
        send_mail(sub ,msg ,'info@codegnan.com',[to_mail],fail_silently=False)
        form.save()
        return super().form_valid(form)

def thanks(request):
	return render(request,'thanks.html')