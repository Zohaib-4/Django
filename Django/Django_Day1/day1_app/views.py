from django.http import HttpResponse
from django.template import loader
from . import models

def day1_app(request):
  mymembers = new_table.objects.all().values()
  template = loader.get_template('index.html')
  return HttpResponse(template.render())