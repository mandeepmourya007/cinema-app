from django.db import models


# class Cinema(models.Model):
#     name = models.CharField(max_length=200)



class Movie(models.Model):
    STATUS_CHOICES = [
        ('coming_up', 'Coming Up'),
        ('starting', 'Starting'),
        ('running', 'Running'),
        ('finished', 'Finished'),
    ]
    # cinema = models.ForeignKey(Cinema,related_name='movies',related_query_name='movies')
    name = models.CharField(max_length=255)
    protagonists = models.TextField()
    poster = models.ImageField(upload_to='posters/')
    trailer = models.URLField()
    start_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    ranking = models.IntegerField(default=0)

    def __str__(self):
        return self.name
