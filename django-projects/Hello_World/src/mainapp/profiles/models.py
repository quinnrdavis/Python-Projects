from django.db import models


PREFIX_CHOICES = {
    ('Mr.', 'Mr.'),
    ('Mrs.', 'Mrs.'),
    ('Ms.', 'Ms.'),
    ('Dr.', 'Dr.'),
}


class Profile(models.Model):
    prefix = models.CharField(max_length=60, choices=PREFIX_CHOICES, blank=True, null=True)
    fname = models.CharField(max_length=60, default="", blank=True, null=False)
    lname = models.CharField(max_length=60, default="", blank=True, null=False)
    email = models.CharField(max_length=60, default="", blank=True, null=False)
    username = models.CharField(max_length=60, default="", blank=True, null=False)

    def __str__(self):
        return self.fname
