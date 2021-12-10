from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Person
from .forms import OwnerRegistration
from django.http import JsonResponse
import json
from django.middleware.csrf import get_token


def get_csrf_token(request):
    return HttpResponse(get_token(request))

# Create your views here

def persondetails(request):
    person = Person.objects.all().select_related('address').select_related(
    'job_detail__job_location').select_related('education_detail__college_address')
    response = []

    for P in person:
       response.append({
        "family_name": P.family_name,
        "first_name": P.first_name,
        "last_name": P.last_name,
        "date_of_birth": P.date_of_birth,
        "blood_group": P.blood_group,
        "age": P.age,
        "gender": P.gender,
        "phone_number": str(P.phone_number),
        "aadhar_card": P.aadhar_card,
        "pan_card": P.pan_card,

        "address": {
            "address_line1": P.address.address_line1,
            "address_line2": P.address.address_line2,
            "landmark": P.address.landmark,
            "city": P.address.city,
            "state": P.address.state,
            "pincode": P.address.pincode,
        },

        "job_detail": {
            "occupation": P.job_detail.occupation,
            "years_of_experience": P.job_detail.years_of_experience,
            "company_name": P.job_detail.company_name,

            "job_location": {
                "address_line1": P.job_detail.job_location.address_line1,
                "address_line2": P.job_detail.job_location.address_line2,
                "landmark": P.job_detail.job_location.landmark,
                "city": P.job_detail.job_location.city,
                "state": P.job_detail.job_location.state,
                "pincode": P.job_detail.job_location.pincode,
            }
        },

        "education_detail": {
            "qualification": P.education_detail.qualification,
            "college": P.education_detail.college,
            "year_of_completion": P.education_detail.year_of_completion,

            "college_address": {
                "area": P.education_detail.college_address.area,
                "city": P.education_detail.college_address.city,
                "state": P.education_detail.college_address.state,
                "pincode": P.education_detail.college_address.pincode,
                "country": P.education_detail.college_address.country,

            }


        }

    })
    
    return JsonResponse(response, safe=False)

class OwnerView:
    @staticmethod
    def create_owner(request):
        if request.method=='POST':
            fm=OwnerRegistration(json.loads(request.body))
            if fm.is_valid():
                return JsonResponse({
                    "success": False,
                    "message": 'Form Validated'
                },safe=False)
            else:
                print(fm.errors.as_json())
                res = HttpResponse(fm.errors.as_json())
                res.headers['Content-Type'] = "application/json"
                return res
        else:
            return JsonResponse({
                "success": False,
                "message": 'Invalid form details'
            },safe=False)
