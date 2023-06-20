from django.shortcuts import render
from .forms import quoteForm
# Create your views here.
from .models import *
from django.core.mail import send_mail
# Create your views here.

def about_us(request):
    return render(request, "about_us.html")

def our_process(request):
    return render(request,"our_process.html")

def testimonials(request):
    return render(request, "testimonials.html")

def our_work(request):
    # get a collection of all, projects.
    projects = Project.objects.all()



    return render(request, "our_work.html", {'projects': projects})

def project_details(request, pk):
    # get the project, based off of the pk that we passed in.
    project = Project.objects.filter(pk=pk).get()

    # if the project has a link, associated with, it pass bool variable to template to create a button underneath image.
    if project.link != "":
        print("The link for this project is: ", project.link)
        link = True
    else:
        link = False

    # query all of the images belonging to this proejct.
    images = ProjectGallery.objects.filter(project_id=pk)
    return render(request, "project_details.html", {'project': project, 'images': images, 'link': link})



def home(request):

    # render the form, and send out a confirmation e-mail with a "Do Not Reply Heading". Send e-mail to self as well.

    if request.method == 'POST':
        # get the form submitted by user.
        form = quoteForm(request.POST)

        if form.is_valid():
            # do form processing such as sending out the e-mail.
            send_mail(
                 "Thank You For Choosing Prairie Code LLC",
                 "Hello, We Appreciate you for reaching out to us. A representative will soon reach out to you.",
                 "Don't Reply <do_not_reply@domain.example>",
                 [form.cleaned_data['email']],
                 fail_silently=False,
             )

            send_mail(
                "A New Quote Has Been Created",
                "Hello, We Appreciate you for reaching out to us. A representative will soon reach out to you.",
                "Don't Reply <do_not_reply@domain.example>",
                ['prairiecodellc@gmail.com'],
                fail_silently=False,
              )




            form = quoteForm()

    else:
        form = quoteForm()


    return render(request, "index.html", {'form': form})
