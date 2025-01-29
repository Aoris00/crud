from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Customer, Document, Review
from .forms import CustomerForm, DocumentForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, get_object_or_404
from .models import PrintOrder, Document
from .models import PaymentDetails





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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        
        user = self.request.user
        customer = Customer.objects.filter(email=user.email).first()
        
        context['user_name'] = f"{customer.first_name}" if customer else user.username
        context['user_email'] = user.email
        context['user_phone'] = customer.phone_number if customer else 'N/A'
        
        return context

def payment_details(request):
    if request.method == 'POST':
        payment_method = request.POST['payment_method']
        amount = request.POST['amount']
        status = request.POST['status']
        

        messages.success(request, "Payment details saved successfully!")
        return redirect('myaccount')

    return render(request, 'app/paymentdetails.html')



class SuccessPageView(ListView):
    model = PaymentDetails
    template_name = 'app/payment_details_finished.html'
    success_url = reverse_lazy('payment_success')


class ReviewSuccessPageView(ListView):
    model = Review
    template_name = 'app/review_finished.html'
    success_url = reverse_lazy('review_finished')



class PrintOrdersPageView(ListView):
    model = PrintOrder
    template_name = 'app/printorders.html'
    context_object_name = 'orders'



class ReviewPageView(TemplateView):
    template_name = 'app/review.html'


def print_order_detail(request, order_id):
    order = get_object_or_404(PrintOrder, id=order_id)
    document = order.document  

    context = {
        'order': order,
        'document': document,
    }
    return render(request, 'app/printorders.html', context)

    
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'app/signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is already taken.")
            return render(request, 'app/signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is already in use.")
            return render(request, 'app/signup.html')

        
        user = User.objects.create_user(username=username, email=email, password=password)
        
       
        first_name = request.POST.get('first_name', '')
        phone_number = request.POST.get('phone_number', '')

        customer = Customer.objects.create(
            first_name=first_name, 
            email=email,
            phone_number=phone_number
        )
        
        user.save()
        customer.save()

        login(request, user)
        return redirect('myaccount')

    return render(request, 'app/signup.html')



def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')
