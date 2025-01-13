from django.db import models

class RunningModel(models.Model):
    run_date = models.DateField()
    run_id = models.CharField(max_length=100)

    def __str__(self):
        return self.run_date