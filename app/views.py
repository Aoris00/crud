from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Customer, Document
from .forms import CustomerForm, DocumentForm


class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'








class CustomerListView(ListView):
    model = Customer
    template_name = 'app/customer_list.html'
    context_object_name = 'customers'

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'app/customer_form.html'
    success_url = reverse_lazy('customer_list')

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'app/customer_form.html'
    success_url = reverse_lazy('customer_list')

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'app/customer_confirm_delete.html'
    success_url = reverse_lazy('customer_list')


class DocumentListView(ListView):
    model = Document
    template_name = 'app/document_list.html'
    context_object_name = 'documents'

class DocumentDetailView(DetailView):
    model = Document
    template_name = 'app/document_detail.html'
    context_object_name = 'document'

class DocumentCreateView(CreateView):
    model = Document
    form_class = DocumentForm
    template_name = 'app/document_form.html'
    success_url = reverse_lazy('document_list')

class DocumentUpdateView(UpdateView):
    model = Document
    form_class = DocumentForm
    template_name = 'app/document_form.html'
    success_url = reverse_lazy('document_list')

class DocumentDeleteView(DeleteView):
    model = Document
    template_name = 'app/document_confirm_delete.html'
    success_url = reverse_lazy('document_list')


class MyAccountPageView(TemplateView):
    template_name = 'app/myaccount.html'

class PaymentDetailsPageView(TemplateView):
    template_name = 'app/paymentdetails.html'

class PrintOrdersPageView(TemplateView):
    template_name = 'app/printorders.html'

class ReviewPageView(TemplateView):
    template_name = 'app/review.html'



    
