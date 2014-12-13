from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    summary = models.CharField(null=True, blank=True, max_length=250)
    text = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    due_by = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(default=50, null=False, blank=False)
    user = models.ForeignKey(User, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    modified = models.DateTimeField(auto_now=True, null=False, blank=False)

    def __str__(self):
        if self.complete:
            return '{0} - Complete'.format(self.summary)
        else:
            return '{0}'.format(self.summary)