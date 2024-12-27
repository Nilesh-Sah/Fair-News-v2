from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    summary=models.TextField()
    affiliation=models.TextField()
    published_date=models.DateTimeField(auto_now_add=True, null=True, blank=True)  #New rows will get the current timestamp automatically. Existing rows will have NULL for this field.
  

    def __str__(self) :
        return self.title
    








