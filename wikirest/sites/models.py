from django.db import models


class Task(models.Model):
	start_url = models.URLField(max_length=200)
	end_url = models.URLField(max_length=200)