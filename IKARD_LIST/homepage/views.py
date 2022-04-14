import re
from django.shortcuts import render
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import redirect
from homepage.forms import LogMessageForm
from homepage.models import LogMessage
from django.views.generic import ListView

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "homepage/about.html")

def contact(request):
    return render(request, "homepage/contact.html")

def hello_there(request, name):
    return render(
        request,
        'homepage/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "homepage/log_message.html", {"form": form})


def tile_view(request):
    return render(request, "homepage/tile_page.html")