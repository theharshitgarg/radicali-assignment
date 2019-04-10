# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from policy.models import Policy

admin.site.register(Policy)
