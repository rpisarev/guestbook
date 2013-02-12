from django.db import models

class GuBook(models.Model):
        username = models.CharField(max_length=255)
	email = models.EmailField()
	homepage =  models.URLField(blank = True)
	text = models.CharField()
	image = ImageField(blank = True))
	ip = models.CharField()
	browser = models.CharField()
	date = models.DateField()
	def __unicode__(self):
                return self.text

        class Meta:
                ordering = ["date"]

# Create your models here.
