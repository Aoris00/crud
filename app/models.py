from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class MyAccount(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username
    
    
class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    upload_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('printed', 'Printed'), ('delivered', 'Delivered')],
        default='pending'
    )
    pages = models.PositiveIntegerField(blank=True, null=True)
    print_quality = models.CharField(
        max_length=50,
        choices=[('standard', 'Standard'), ('high', 'High')],
        default='standard'
    )
    delivery_address = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} {self.user.username}"
    
    
class PrintOrder(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    document = models.ForeignKey('Document', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[('received', 'Received'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('delivered', 'Delivered')],
        default='received'
    )
    print_type = models.CharField(
        max_length=50,
        choices=[('color', 'Color'), ('black_and_white', 'Black and White')],
        default='black_and_white'
    )
    
    special_instructions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.id} for {self.user.username} - {self.status}"
    
    
class PaymentDetails(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    printorder = models.ForeignKey('PrintOrder', on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(
        max_length=50,
        choices=[('credit_card', 'Credit Card'), ('gcash', 'Gcash'), ('bank_transfer', 'Bank Transfer')],
        default='credit_card'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')],
        default='pending'
    )

    def __str__(self):
        return f"{self.transaction_id} - {self.payment_status}"
    
    
class Review(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    printorder = models.ForeignKey('PrintOrder', on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 5)])
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.rating}"
