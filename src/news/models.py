from django.db import models

# Create your models here.

class New(models.Model):
    heading_one = models.CharField(max_length=500)
    h1_paragraph1 = models.TextField()
    h1_paragraph2 = models.TextField(blank=True)
    h1_paragraph3 = models.TextField(blank=True)
    image_one = models.ImageField(upload_to='news/news_photos') 
    file_one = models.FileField(upload_to='news/news_files', blank=True)

    heading_two = models.CharField(max_length=500)
    h2_paragraph1 = models.TextField()
    h2_paragraph2 = models.TextField(blank=True)
    h2_paragraph3 = models.TextField(blank=True)
    image_two = models.ImageField(upload_to='news/news_photos') 
    file_two = models.FileField(upload_to='news/news_files', blank=True)

    heading_three = models.CharField(max_length=500)
    h3_paragraph1 = models.TextField()
    h3_paragraph2 = models.TextField(blank=True)
    h3_paragraph3 = models.TextField(blank=True)
    image_three = models.ImageField(upload_to='news/news_photos') 
    file_three = models.FileField(upload_to='news/news_files', blank=True)

    heading_four = models.CharField(max_length=500)
    h4_paragraph1 = models.TextField()
    h4_paragraph2 = models.TextField(blank=True)
    h4_paragraph3 = models.TextField(blank=True)
    image_four = models.ImageField(upload_to='news/news_photos') 
    file_four = models.FileField(upload_to='news/news_files', blank=True)

    heading_five = models.CharField(max_length=500)
    h5_paragraph1 = models.TextField()
    h5_paragraph2 = models.TextField(blank=True)
    h5_paragraph3 = models.TextField(blank=True)
    image_five = models.ImageField(upload_to='news/news_photos') 
    file_five = models.FileField(upload_to='news/news_files', blank=True)

    heading_six = models.CharField(max_length=500)
    h6_paragraph1 = models.TextField()
    h6_paragraph2 = models.TextField(blank=True)
    h6_paragraph3 = models.TextField(blank=True)
    image_six = models.ImageField(upload_to='news/news_photos') 
    file_six = models.FileField(upload_to='news/news_files', blank=True)

    pub_date = models.DateTimeField('Date Published', auto_now_add=True, auto_now=False)

    def __str__(self):
       return str(self.pub_date)

# Create your models here.
