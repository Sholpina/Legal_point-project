from django.db import models


class Blog(models.Model):
        title = models.CharField(max_length=200)
        image = models.ImageField(upload_to='media/blog/images/')
        date = models.DateField()
        description = models.TextField()
        tag = models.CharField(max_length=50)

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
