from django.db import models

class GuBook(models.Model):
        username = models.CharField(max_length=255)
	email = models.EmailField()
	homepage =  models.URLField(blank = True)
	text = models.CharField(max_length=2**16)
	image = models.ImageField(upload_to='img/%Y/%m/%d')
	ip = models.CharField(max_length=20)
	browser = models.CharField(max_length=255)
	date = models.DateTimeField()
	def __unicode__(self):
                return self.text

        class Meta:
                ordering = ["date"]

# Create your models here.
