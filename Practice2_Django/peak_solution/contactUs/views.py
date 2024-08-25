from django.http import HttpResponse
from django.template import loader
from .models import Users

def contactUs(request):
    mymembers = Users.objects.all().values()
    template = loader.get_template('contact.html')
    context = {
      'mymembers': mymembers,
    }
    # template = loader.get_template('contact.html')
    return HttpResponse(template.render(context, request))