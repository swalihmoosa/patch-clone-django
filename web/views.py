import json
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from web.models import Testimonial, Promoter, Faq, Subscribe

def index(request):
    testimonials = Testimonial.objects.all()
    promoters = Promoter.objects.all()
    rent_tracking_faqs = Faq.objects.filter(faq_type="rent_tracking")
    new_deposit_faqs = Faq.objects.filter(faq_type="new_deposit")
    existing_deposit_faqs = Faq.objects.filter(faq_type="existing_deposit")



    context = {
        "testimonials" : testimonials,
        "promoters" : promoters,
        "rent_tracking_faqs" : rent_tracking_faqs,
        "new_deposit_faqs" : new_deposit_faqs,
        "existing_deposit_faqs" : existing_deposit_faqs

    }
    return render(request,"index.html",context=context)


def subscribe(request):
    email = request.POST.get("email")
    if not Subscribe.objects.filter(email=email).exists():
        Subscribe.objects.create(
            email = email
        )

        response_data = {
            "status" : "success",
            "title" : "Successfully Registered",
            "message" : "You are Subscribed to the News Letter"
        }
    else:
        response_data = {
            "status" : "error",
            "title" : "Already Registered",
            "message" : "You are Already Subscribed to the News Letter,no need to Subscribe again"
        }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")