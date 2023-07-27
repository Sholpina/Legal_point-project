from django.db import models


class Blog(models.Model):
        title = models.CharField(max_length=100)
        description = models.TextField()
        date = models.DateField()
        image = models.ImageField(upload_to='media/blog/images', null=True, blank=True)
        tag = models.CharField(max_length=50, null=True, blank=True)

        def __str__(self):
                return self.title

# class Tag(models.Model):
#     article = models.ForeignKey(
#         Blog,
#         on_delete=models.CASCADE,
#         related_name="tags",
#         related_query_name="tag",
#     )
#     name = models.CharField(max_length=255)
