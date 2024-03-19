from django.shortcuts import render, redirect
from django.template.loader import get_template
from .forms import quoteForm
# Create your views here.
from django import forms
from .models import *
from django.core.mail import send_mail, EmailMultiAlternatives


# Create your views here.


def contact_us(request):
    print("Inside of the contact_us view!")
    if request.method == "POST":
        # get the content that was submitted.
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['e-mail']
        content = request.POST['content']

        # need to group the data and send it in an e-mail format. we will
        # make use of client side logic to ensure that all of the data is
        # valid, perhaps just for the e-mail.
        send_mail(
            "Thank You For Choosing Prairie Code LLC",
            "Hello, We Appreciate you for reaching out to us. A "
            "representative will soon reach out to you.",
            "Don't Reply <do_not_reply@domain.example>",
            [email],
            fail_silently=False,
        )
        plaintext = get_template("email/admin_confirmation.txt")
        content = ({
            'user': first_name + last_name,
            'email': email,
            'details': content
        })

        text_content = plaintext.render(content)

        msg = EmailMultiAlternatives("A New Quote Has Been Created",
                                     text_content,
                                     "Don't Reply <do_not_reply@domain.example>",
                                     ['prairiecodellc@gmail.com'])
        msg.send()

        return redirect('Home:success')

    return render(request, "contact_us.html")


def submissionSuuccess(request):
    return render(request, "formSubmitSuccess.html")


def faq(request):
    return render(request, "faq.html")


def about_us(request):
    return render(request, "about_us.html")


def our_process(request):
    return render(request, "our_process.html")


def testimonials(request):
    return render(request, "testimonials.html")


def our_work(request):
    # get a collection of all, projects.
    projects = Project.objects.all()

    return render(request, "our_work.html", {'projects': projects})


def project_details(request, pk):
    # get the project, based off of the pk that we passed in.
    project = Project.objects.filter(pk=pk).get()

    # if the project has a link, associated with, it pass bool variable to
    # template to create a button underneath image.
    if project.link != "":
        print("The link for this project is: ", project.link)
        link = True
    else:
        link = False

    # query all of the images belonging to this proejct.
    images = ProjectGallery.objects.filter(project_id=pk)
    return render(request, "project_details.html",
                  {'project': project, 'images': images, 'link': link})


def home(request):
    # render the form, and send out a confirmation e-mail with a "Do Not Reply Heading". Send e-mail to self as well.

    if request.method == 'POST':
        # get the form submitted by user.
        form = quoteForm(request.POST)

        # check for spam first.

        if form.is_valid():
            # do form processing such as sending out the e-mail.

            # before we can send out the mail we need to make sure that, the details of the form does not contain any blacklisted forms

            if form.check_spam() == 1:
                found_spam = 1
                return render(request, "index.html",
                              {'form': form, 'found_spam': found_spam})
            else:
                found_spam = 0
                return render(request, "index.html",
                              {'form': form, 'found_spam': found_spam})

            send_mail(
                "Thank You For Choosing Prairie Code LLC",
                "Hello, We Appreciate you for reaching out to us. A representative will soon reach out to you.",
                "Don't Reply <do_not_reply@domain.example>",
                [form.cleaned_data['email']],
                fail_silently=False,
            )

            plaintext = get_template("email/admin_confirmation.txt")
            content = ({
                'user': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'details': form.cleaned_data['details']
            })

            text_content = plaintext.render(content)

            msg = EmailMultiAlternatives("A New Quote Has Been Created",
                                         text_content,
                                         "Don't Reply <do_not_reply@domain.example>",
                                         ['prairiecodellc@gmail.com'])
            msg.send()

            form = quoteForm()

            return redirect('Home:home')

    else:
        # print out the form error in the template itself.

        form = quoteForm()
    return render(request, "index.html", {'form': form, })
