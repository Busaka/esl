from django.db import models

# Create your models here.
class About(models.Model):

    page = models.CharField(max_length=500)
    paragragh1 = models.TextField(blank=True)
    heading1 = models.CharField(max_length=500)
    paragragh2 = models.TextField(blank=True)
    paragragh3 = models.TextField(blank=True)
    paragragh4 = models.TextField(blank=True)
    heading2 = models.CharField(max_length=500)
    paragragh5 = models.TextField(blank=True)
    paragragh6 = models.TextField(blank=True)
    paragragh7 = models.TextField(blank=True)
    paragragh8 = models.TextField(blank=True)
    paragragh9 = models.TextField(blank=True)
    paragragh10 = models.TextField(blank=True)
    heading3 = models.CharField(max_length=500)
    paragragh11 = models.TextField(blank=True)
    paragragh12 = models.TextField(blank=True)
    heading4 = models.CharField(max_length=500)
    paragragh13 = models.CharField(max_length=500)
    heading5 = models.CharField(max_length=500)
    paragragh14 = models.CharField(max_length=500)
    heading6 = models.CharField(max_length=500)
    paragragh15 = models.CharField(max_length=500)

    def __str__(self):
        return self.page

class TermsAndCondition(models.Model):

    heading1 = models.CharField(max_length=500)
    h1_paragragh1 = models.TextField(blank=True)
    h1_paragragh2 = models.TextField(blank=True)
    h1_paragragh3 = models.TextField(blank=True)
    h1_paragragh4 = models.TextField(blank=True)
    h1_paragragh5 = models.TextField(blank=True)
    h1_paragragh6 = models.TextField(blank=True)
    h1_paragragh7 = models.TextField(blank=True)

    heading2 = models.CharField(max_length=500)
    h2_paragragh1 = models.TextField(blank=True)
    h2_paragragh2 = models.TextField(blank=True)
    h2_paragragh3 = models.TextField(blank=True)
    h2_paragragh4 = models.TextField(blank=True)
    h2_paragragh5 = models.TextField(blank=True)
    h2_paragragh6 = models.TextField(blank=True)
    h2_paragragh7 = models.TextField(blank=True)

    heading3 = models.CharField(max_length=500)
    h3_paragragh1 = models.TextField(blank=True)
    h3_paragragh2 = models.TextField(blank=True)
    h3_paragragh3 = models.TextField(blank=True)
    h3_paragragh4 = models.TextField(blank=True)
    h3_paragragh5 = models.TextField(blank=True)
    h3_paragragh6 = models.TextField(blank=True)
    h3_paragragh7 = models.TextField(blank=True)

    def __str__(self):
        return self.heading1

class Copyright(models.Model):

    heading1 = models.CharField(max_length=500)
    h1_paragragh1 = models.TextField(blank=True)
    h1_paragragh2 = models.TextField(blank=True)
    h1_paragragh3 = models.TextField(blank=True)
    h1_paragragh4 = models.TextField(blank=True)
    h1_paragragh5 = models.TextField(blank=True)
    h1_paragragh6 = models.TextField(blank=True)
    h1_paragragh7 = models.TextField(blank=True)

    heading2 = models.CharField(max_length=500)
    h2_paragragh1 = models.TextField(blank=True)
    h2_paragragh2 = models.TextField(blank=True)
    h2_paragragh3 = models.TextField(blank=True)
    h2_paragragh4 = models.TextField(blank=True)
    h2_paragragh5 = models.TextField(blank=True)
    h2_paragragh6 = models.TextField(blank=True)
    h2_paragragh7 = models.TextField(blank=True)

    heading3 = models.CharField(max_length=500)
    h3_paragragh1 = models.TextField(blank=True)
    h3_paragragh2 = models.TextField(blank=True)
    h3_paragragh3 = models.TextField(blank=True)
    h3_paragragh4 = models.TextField(blank=True)
    h3_paragragh5 = models.TextField(blank=True)
    h3_paragragh6 = models.TextField(blank=True)
    h3_paragragh7 = models.TextField(blank=True)

    def __str__(self):
        return self.heading1

