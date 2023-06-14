from django.db import models

# Create your models here.
class Project(models.Model):
    thumbnail = models.ImageField(upload_to='projects/')
    name = models.CharField(max_length=45)
    link = models.CharField(max_length=75, blank=True)
    motivation = models.TextField(blank=False)
    capabilities = models.TextField(blank=False)
    my_contributions = models.TextField(blank=False)

    def __str__(self):
        return self.name

class ProjectGallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    caption = models.CharField(max_length=35)

    def __str__(self):
        return str(self.image)
