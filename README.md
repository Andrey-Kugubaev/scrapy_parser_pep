# Асинхронный парсер PEP

---
![python](https://img.shields.io/badge/Python-3.9-green)
![Scrapy](https://img.shields.io/badge/Scrapy-2.5.1-green)
![Regex](https://img.shields.io/badge/Regex-grey)
![flake8](https://img.shields.io/badge/flake8-4.0.1-green)
---
## Содержание:
- [Введение](#introduction)
- [Парсер документов PEP](#parser-parsing-pep-documents)
- [Инструкция по запуску](#instruction-to-start)

---
### <anchor>Введение</anchor>
Проект по изучению фраемворка Scrapy. В рамках проекта необходимо с помощью Scrapy
получить информацию о статусах документов PEP.

----
### <anchor>Парсер документов PEP</anchor>
Парсер собирает информацию (Number, Name и Status) о документах PEP с сайта
https://peps.python.org/ и сохраняет в файл формата _csv_.
Отдельно парсер подсчитывает количество документов с определенным статусом, подсчитывает
общее количество документов PEP и сохрянает данную информацию в в файл формата _csv_

----
### <anchor>Инструкция по запуску</anchor>
<details>

1. Склонируйту проект `git clone git@github.com:Andrey-Kugubaev/bs4_parser_pep.git`
2. Установите и запустите виртуальное окружение `python -m venv venv` или `python3 -m venv venv`,
далее `source venv/Scripts/activate` или `source venv/bin/activate`
3. Установите зависимости `pip install -r requirements.txt`
4. Запустите парсер `scrapy crawl pep`

</details>