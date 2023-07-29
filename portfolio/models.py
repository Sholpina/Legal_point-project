from django.db import models
from datetime import datetime

class Project(models.Model):
        title = models.CharField(max_length=100)
        description = models.CharField(max_length=250)
        image = models.ImageField(upload_to='portfolio/images/')
        url = models.URLField(blank=True)

        def __str__(self):
                return self.title

        # def get_current_datetime(self):
        #         """
        #         Returns the current datetime using Python's datetime module.
        #         """
        #         data_footer = datetime.now().strftime('%b %d %Y')
        #         return data_footer


