from django import forms
from .models import Customer, Document, PrintOrder, PaymentDetails, Review

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'file', 'pages', 'print_quality', 'delivery_address', 'comments']

class PrintOrderForm(forms.ModelForm):
    class Meta:
        model = PrintOrder
        fields = '__all__'

class PaymentDetailsForm(forms.ModelForm):
    class Meta:
        model = PaymentDetails
        fields = '__all__'

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
