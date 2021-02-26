from __future__ import absolute_import, unicode_literals

from .celery import app as cellery_app


__all__ = ('cellery_app', )