from django import forms

from .models import Payment

class PaymentForm(forms.ModelForm):
    
    class Meta:
        # course_name = [('course_name', 'web - price: 500'), ('jj', 'JJ - price: 500'), ('pp', 'PP - price: 500'),]
  
        model = Payment
        # course_name = "1, 2, 4"
        fields = ("name", "course_name", "amount", "email", "creditors_address", "phone", "message")
        
        
        