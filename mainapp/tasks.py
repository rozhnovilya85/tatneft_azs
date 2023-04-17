# Create your tasks here

from celery import shared_task
import json
import logging
import pandas as pandas
from django.conf import settings
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time
import os.path
from mainapp.models import AzsDB

logging.basicConfig(filename="log.txt", format="%(asctime)s %(levelname)s %(message)s", level=logging.ERROR)

@shared_task
def spisok_azs():
    print('Работаю')
    options = webdriver.ChromeOptions()
    #настройки браузера
    p = {'download.default_directory':'D:\Учеба\djangoProject\\tatneft_azs\mainapp\management\commands'}
    #добавить параметры в браузер
    options.add_experimental_option('prefs', p)
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    #развернуть браузер
    driver.maximize_window()
    #запустить URL
    driver.get('https://rss.tatneft.ru')
    time.sleep(2)
    #формируем список ссылок из меню для рандомного перемещения по меню
    elements = driver.find_elements(By.CLASS_NAME, "cufon-rp")
    link = []
    for item in elements:
        link.append(item.get_attribute('href'))
    a = 0
    while a != 5:
        driver.get(str(random.choice(link)))
        a = a+1
        time.sleep(2)
    element = driver.find_element(By.XPATH, """/html/body/div[1]/div/div[2]/div/div[1]/div[1]/ul/li[7]/a""")
    element.click()
    time.sleep(2)
    element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div[1]/ul/li[7]/ul/li[2]/a')
    element.click()
    time.sleep(2)
    # функция для загрузки списка азс
    def link_file():
        element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[2]/div/form/table/tbody/tr[1]/td[3]/a')
        element.click()
        time.sleep(10)
    a = False
    b = os.path.isfile(f'{settings.BASE_DIR}\mainapp\management\commands\spisokAZS.xls')
    while a == b:
        try:
            link_file()
            f = open(f'{settings.BASE_DIR}\mainapp\management\commands\spisokAZS.xls')
            f.close()
        except Exception:
            logging.error(str(Exception), exc_info=True)
        b = os.path.isfile(f'{settings.BASE_DIR}\mainapp\management\commands\spisokAZS.xls')
    driver.quit()
    #обрабатываем скаченый файл .xls библиотекой pandas
    df1 = pandas.read_excel(f'{settings.BASE_DIR}\mainapp\management\commands\spisokAZS.xls', sheet_name='Лист1')
    df1.to_json(f'{settings.BASE_DIR}\mainapp\management\commands\\file.json', orient='records', force_ascii=False)
    os.remove(f'{settings.BASE_DIR}\mainapp\management\commands\spisokAZS.xls')

    def load_from_json(file_name):
        with open(f'{settings.BASE_DIR}\mainapp\management\commands\{file_name}.json', 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    #загружаем данные в базу
    azs = load_from_json('file')
    AzsDB.objects.all().delete()
    for item in azs:
        azs_data = AzsDB(
            number_azs=item['Номер АЗС'],
            address=item['Адрес'],
            latitude=item['Координаты GPS (широта)'],
            longitude=item['Координаты GPS (долгота)'],
            DT=item['ДТ'],
            DT_Taneko=item['ДТ ТАНЕКО'],
            DT_winter=item['ДТ (зимнее)'],
            DT_arctic=item['ДТ Арктика']
        )
        azs_data.save()
    os.remove(f'{settings.BASE_DIR}\mainapp\management\commands\\file.json')

