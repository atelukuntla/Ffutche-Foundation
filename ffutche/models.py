from django.db import models


class Donation(models.Model):
    contributor_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=20)
    email_id = models.CharField(max_length=250)
    contribution_type = models.CharField(max_length=100)
    quantity = models.IntegerField()
    value = models.IntegerField()

    def __str__(self):
        return self.contributor_name + ' - ' + self.contribution_type
