from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.db import models
from phone.models import Phone, PhoneBrand
from phone.forms import PhoneForm, BrandForm

# Create your views here.


def index(request):
    return render(request, "index.html")


class PhoneListView(ListView):
    model = Phone
    template_name = 'phone/list.html'  # Specify your template name
    context_object_name = 'phones'  # Name of the context variable to use in the template


def add_phone(request):
    if request.method == "POST":
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('phone:phone-list')
    else:
        form = PhoneForm()

    context = {
        'form': form
    }

    return render(
        request, 'phone/add.html', context
    )


def get_report(request):
    if request.method == "POST":
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.cleaned_data['brand']
            phones = Phone.objects.filter(
                phone_name__brand__name__iexact=brand
            )
    else:
        phones = None
        form = BrandForm()

    korean_brand = PhoneBrand.objects.filter(
        name__iexact="Korea"
    )

    manufacturing_country_nationality = Phone.objects.filter(
        manufacturing_country__iexact=models.F("phone_name__brand__nationality")
    )

    context = {
        'form': form,
        "korean_brand": korean_brand,
        "phones": phones,
        "manufacturing_country_nationality": manufacturing_country_nationality
    }
    return render(request, "report.html", context)
