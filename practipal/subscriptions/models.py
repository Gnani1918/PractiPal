from django.db import models


class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    monthly_price = models.DecimalField(max_digits=8, decimal_places=2)
    yearly_price = models.DecimalField(max_digits=8, decimal_places=2)
    trial_days = models.PositiveIntegerField(default=0)

    limit_clients = models.PositiveIntegerField(default=0)
    limit_sessions = models.PositiveIntegerField(default=0)
    limit_storage = models.PositiveIntegerField(default=0)
    limit_team_members = models.PositiveIntegerField(default=1)

    option_api_access = models.BooleanField(default=False)
    option_branding = models.BooleanField(default=False)
    option_support = models.BooleanField(default=False)
    option_popular = models.BooleanField(default=False)

    extra_features = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.name
