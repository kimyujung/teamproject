from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=20, blank='TRUE')
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to = 'images/', blank="TRUE")
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100] #본문 내용 100글자 상한 선으로 return 

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name='comments')
    writer = models.CharField(max_length=20, blank='TRUE')
    contents = models.CharField(max_length=200)

    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return self.contents