from django.db import models
from django.utils import timezone


def user_directory_path(instance, filename):
    print(instance)
    return 'static/images/goods/{}'.format(filename)


class Photo(models.Model):
    # good = models.ForeignKey(Good, on_delete=models.CASCADE, related_name="photos", related_query_name="photo", )
    title = models.CharField(max_length=200)
    alt = models.CharField(max_length=255)
    src = models.ImageField(upload_to=user_directory_path)

    def __str__(self):
        return self.title


class Good(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    photos = models.ManyToManyField(Photo)

    short_desc = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name
