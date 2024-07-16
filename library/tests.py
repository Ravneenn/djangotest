from django.test import TestCase
from library.models import Article, Reporter


# Create your tests here.
Reporter.objects.all()
r = Reporter(full_name="John Smith")
r.save()

print(r.full_name)