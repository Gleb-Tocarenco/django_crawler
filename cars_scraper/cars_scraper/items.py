from scrapy_djangoitem import DjangoItem
from cars.models import Car

import scrapy


class CarItem(DjangoItem):
   
   django_model = Car