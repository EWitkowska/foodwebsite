from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from foodwebsite.settings import EMAIL_HOST_USER

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = 'Website Inquiry' 
			body = {
			'full_name': form.cleaned_data['full_name'], 
			'email': form.cleaned_data['email'], 
            'subject': form.cleaned_data['subject'],
			'message': form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, body['email'], [EMAIL_HOST_USER], fail_silently=False) 
			except BadHeaderError:
				return HttpResponse('Invalid header found')
			return redirect ("food:index")
      
	form = ContactForm()
	return render(request, "contact/contact.html", {'form':form})
