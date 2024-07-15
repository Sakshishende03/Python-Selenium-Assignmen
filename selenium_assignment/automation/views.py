from django.shortcuts import render

# Create your views here.
from django.core.mail import EmailMessage
from django.shortcuts import render

def send_email(request):
    email = EmailMessage(
        'Python (Selenium) Assignment - Your Name',
        'Please find the attached screenshot of the confirmation page.',
        'sakshishende06@gmail.com',
        ['tech@themedius.ai'],
        cc=['hr@themedius.ai']
    )
    email.attach_file('confirmation_page.png')
    email.send()
    return render(request, 'email_sent.html')
