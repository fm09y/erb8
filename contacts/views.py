from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from django.contrib import messages

def contact(request):
    if request.method=="POST":
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        
        # FIX 1: Validate empty listing_id
        if listing_id == '' or not str(listing_id).isdigit():
            messages.error(request, 'Invalid listing')
            return redirect(request.META.get('HTTP_REFERER'))
            
        listing_id = int(listing_id)  # FIX 2: Convert to integer
        
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        
        if request.user.is_authenticated:
            # FIX 3: Use .exists() for proper boolean check
            has_contacted = Contact.objects.filter(listing_id=listing_id, user_id=user_id).exists()
            if has_contacted:
                messages.error(request, "You have already made an enquiry")
                return redirect("listings:listing", listing_id=listing_id) 
            
            contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)
            contact.save()
            messages.success(request, "Your request submitted, clinic call back")
        
        return redirect("listings:listing", listing_id=listing_id) 
    
    # FIX 4: Proper indentation for GET requests
    return render(request, "listings/listings.html")

def delete_contact(request, contact_id):
    contact= get_object_or_404(Contact, pk=contact_id)
    print("Deleting contact:", )
    contact.delete()
    # Your delete logic here
    return redirect('accounts:dashboard')

def edit_contact(request, contact_id):
    # Your edit logic here  
    return redirect('accounts:dashboard')
