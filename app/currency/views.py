from django.http.response import HttpResponse

from currency.models import Rate, ContactUs


def rate_list(request):
    results = []
    rates = Rate.objects.all()

    for rate in rates:
        results.append(
            f'ID: {rate.id}, sell:{rate.sell}, buy:{rate.buy}, '
            f'created: {rate.created}, currency_type: {rate.currency_type}, source: {rate.source}<br>'
        )

    return HttpResponse(str(results))

def contactus_list(request):
    results = []
    rates = Rate.objects.all()

    for rate in rates:
        results.append(
            f'ID: {rate.id}, email_from:{rate.email_from}, subject:{rate.subject}, '
            f'created: {rate.created}, message: {rate.message}<br>'
        )

    return HttpResponse(str(results))
