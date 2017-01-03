from django.db import models

# Create your models here.

class New(models.Model):
    heading_one = models.CharField(max_length=500)
    h1_paragraph1 = models.TextField()
    h1_paragraph2 = models.TextField(blank=True)
    h1_paragraph3 = models.TextField(blank=True)
    image_one = models.ImageField(upload_to='news/news_photos', blank=True) 
    image_two = models.ImageField(upload_to='news/news_photos', blank=True) 
    file_one = models.FileField(upload_to='news/news_files', blank=True)

    pub_date = models.DateTimeField('Date Published', auto_now_add=True, auto_now=False)

    def __str__(self):
       return str(self.heading_one)
