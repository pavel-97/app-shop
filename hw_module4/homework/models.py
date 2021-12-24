from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('AdvertisementAuthor', on_delete=models.CASCADE)
    type_of = models.ForeignKey('AdvertisementType', on_delete=models.CASCADE)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class AdvertisementAuthor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    mail = models.EmailField()
    telephone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class AdvertisementType(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
