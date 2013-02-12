from django.db import models

class GuBook(models.Model):
        username = models.CharField(max_length=255)
	email = models.EmailField()
	homepage =  models.URLField(blank = True)
	text = models.TextField()
	image = models.ImageField(upload_to='img/%Y/%m/%d', blank = True)
	ip = models.IPAddressField()
	browser = models.CharField(max_length=255)
	date = models.DateTimeField()
	def __unicode__(self):
                return self.text[:10]
	def lst(self):
		return [self.username, self.email, self.text, self.date]

        class Meta:
                ordering = ["date"]

# Create your models here.
