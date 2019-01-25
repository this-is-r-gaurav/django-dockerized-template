from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.contrib import messages


import datetime

from .models import Profile
from .utils import update_avatar_image



