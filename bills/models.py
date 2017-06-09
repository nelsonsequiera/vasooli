from __future__ import unicode_literals
from django.conf import settings

from django.db import models
from gale_user.models import User as gale_user


class Bill(models.Model):
    user = models.ForeignKey(gale_user)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bill_date = models.DateTimeField(auto_now=True)
    project_id = models.CharField(max_length=1000, null=True)
    description = models.TextField(null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    proof_image = models.ImageField(upload_to=settings.PROOF_IMAGE_DIRECTORY, default='nothing.png')
    manager = models.ForeignKey(gale_user, related_name='+')
    is_save = models.BooleanField(default=False)
    is_submit = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username or ''

    class Meta:
        verbose_name = 'Bill'
        verbose_name_plural = 'Bills'
