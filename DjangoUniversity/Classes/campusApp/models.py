from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    name = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_id = models.IntegerField(default="", blank=True, null=False)

    #creates model manager
    object = models.Manager()

    #displays the object output values in the form of a string
    def __str__(self):
        display_course = '{0.name}: {0.state}'
        return display_course.format(self)

    # removes the addded 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campuses"