from django.db import models

# Create your models here.
class Test(models.Model):
    test_field = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50, default='set_name')

    def __str__(self):
        return str(self.name)
