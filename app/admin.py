from django.contrib import admin
from .models import Customer, MyAccount, Document, PrintOrder, PaymentDetails, Review

admin.site.register(Customer)
admin.site.register(MyAccount)
admin.site.register(Document)
admin.site.register(PrintOrder)
admin.site.register(PaymentDetails)
admin.site.register(Review)
