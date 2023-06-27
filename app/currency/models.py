from django.db import models


class Rate(models.Model):
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2, validators=[])
    created = models.DateTimeField()
    currency_type = models.CharField(max_length=3)  # usd, eur
    source = models.CharField(max_length=68)


class ContactUs(models.Model):
    email_from = models.EmailField(max_digits=100)
    created = models.DateTimeField()
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=300)
