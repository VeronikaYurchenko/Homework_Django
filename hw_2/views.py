from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    html = """
    <h1>Главная страница.</h1>
    <p>Это главная страница домашнего задания к 1-му семинару.</p>
    """
    logger.info("The main page has been loaded.")
    return HttpResponse(html)


def about(request):
    html = """
    <h1>Привет, меня зовут Вероника</h1>
    <p>Я создаю свой первый сайт на Django.<br/>Посмотрите на мой сайт.</p>
    """
    logger.info("The page about yourself has been loaded.")
    return HttpResponse(html)