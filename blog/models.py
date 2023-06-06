from django.db import models


class Post(models.Model):
    objects = None
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%M/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%M/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'
    # pk : 각 레코드에 대한 고유값으로 이해하면 됌.

    # author: 추후 작성 예정
