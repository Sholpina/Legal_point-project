from django.test import TestCase
from datetime import datetime


# Create your tests here.
def get_current_datetime():
        """
        Returns the current datetime using Python's datetime module.
        """
        return datetime.now().strftime('%b %d %Y')


data_footer = get_current_datetime()
print(data_footer)
