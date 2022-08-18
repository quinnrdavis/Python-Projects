from django.db import models


# Create your models here.
class UniversityCampus(models.Model):
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campusID = models.IntegerField(default="", blank=True, null=False)

    # creates model manager
    object = models.Manager()

    # displays campus objects by their name in the admin panel
    def __str__(self):
        display_campus = '{0.name}'
        return display_campus.format(self)

    # remove 's' and display model name as 'University Campus'
    class Meta:
        verbose_name_plural = "University Campus"
