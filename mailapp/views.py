from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm
from django.conf import settings

def send_gmail(request):

    if request.method == "POST":
        form = EmailForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']

            full_message = f"Message from {name}\n\n{message}"

            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )

            return render(request, "success.html")

    else:
        form = EmailForm()

    return render(request, "email_form.html", {"form": form})
