from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Company, Number, Profile


def index(request):
    company_list = Company.objects.all()
    paginator = Paginator(company_list, 5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {}
    context['company_list'] = company_list
    context['paginator'] = paginator
    context['page'] = page

    return render(request, 'index.html', context)


def show_company(request, company_slug):
    company = get_object_or_404(Company, slug=company_slug)

    return render(request, 'includes/company_item.html', {
        'company': company,
    })


def show_profile(request, company, person_pk):
    person = get_object_or_404(Profile, pk=person_pk, company__slug=company)

    return render(request, 'includes/profile_item.html', {
        'person': person,
    })
