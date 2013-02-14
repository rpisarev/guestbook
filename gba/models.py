from django.db import models

class GuBook(models.Model):
        username = models.CharField(max_length=255)
	email = models.EmailField()
	homepage =  models.URLField(blank = True)
	text = models.TextField()
	image = models.ImageField(upload_to='image', blank = True)
	ip = models.IPAddressField()
	browser = models.CharField(max_length=255)
	date = models.DateTimeField()
	def __unicode__(self):
                return self.text[:10]
	def lst(self):
		return [self.username, '<img src="{{ STATIC_URL }}/static/' + self.image, self.email, self.date, self.homepage, self.text, self.browser, self.ip]

        class Meta:
                ordering = ["date"]

# Create your models here.
