from django.urls import path, include
from . import views
from .views import (
    HomePageView,
    AboutPageView,
    MyAccountPageView,
    PaymentDetailsPageView,
    PrintOrdersPageView,
    ReviewPageView,
    CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView,
    DocumentListView, DocumentDetailView, DocumentCreateView, DocumentUpdateView, DocumentDeleteView,
   
)




urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('myaccount/', MyAccountPageView.as_view(), name='myaccount'),
    path('paymentdetails/', PaymentDetailsPageView.as_view(), name='paymentdetails'),
    path('printorders/', PrintOrdersPageView.as_view(), name='printorders'),
    path('review/', ReviewPageView.as_view(), name='review'),


   
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),

    
    path('documents/', DocumentListView.as_view(), name='document_list'),
    path('documents/<int:pk>/', DocumentDetailView.as_view(), name='document_detail'),
    path('documents/create/', DocumentCreateView.as_view(), name='document_create'),
    path('documents/<int:pk>/edit/', DocumentUpdateView.as_view(), name='document_update'),
    path('documents/<int:pk>/delete/', DocumentDeleteView.as_view(), name='document_delete'),

 
    

]