from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(
            blank=True, null=True)



    def publish(self, author):
        self.published_date = timezone.now()
        self.author = author
        self.save()



    def __str__(self):
        return self.title




class Post_now(models.Model):
    text = models.TextField()


class Remote_post(models.Model):
    text = models.TextField()
    time = models.DateTimeField(blank=True,auto_now=False)


class cryptoBTC_price(models.Model):
    price = models.TextField()

