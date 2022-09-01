from django.shortcuts import render
from django.http import HttpResponse

import logging

# Create your views here.

logger = logging.getLogger(__name__)


def index(request):
    logger.debug('console')
    logger.info('file')
    return HttpResponse('Hello world')
