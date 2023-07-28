from datetime import timezone

from django.db import models


class Blog(models.Model):
        title = models.CharField(max_length=100)
        description = models.TextField()
        date = models.DateField()
        image = models.ImageField(upload_to='media/blog/images', null=True)
        tag = models.CharField(max_length=50, null=True, blank=True)

        def __str__(self):
                return self.title

        # def was_published_recently(self, date):
        #         now = timezone.now()
        #         time_since_publication = now - self.date
        #         return time_since_publication

# class Tag(models.Model):
#     article = models.ForeignKey(
#         Blog,
#         on_delete=models.CASCADE,
#         related_name="tags",
#         related_query_name="tag",
#     )
#     name = models.CharField(max_length=255)
