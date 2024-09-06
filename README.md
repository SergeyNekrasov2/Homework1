# `Banking operations widget`

Программа создана для фильтрации и сортировки банковских счетов по дате и оплате.

## Project dependencies:
- The program uses the version Python 3.12
- flake8 = "7.1.0"
- black = "24.4.2"
- isort = "5.13.2"
- mypy = "1.11.0"
- pytest = "^8.3.2"

## Функции, которые мы будем использовать в этой версии кода:

- Функция скрывающая номер карты и счета
- Функция сортировки по дате
- Функция фильтрации в операциях по счетам
- Функция скрывающая номер карты и счета.
- Функция сортировки по дате.
- Функция фильтрации в операциях по счетам.
- Функция которая принимает список словарей с банковскими операциями и возвращает ID операции, в которых указана заданная валюта, описание каждой операции.
- Функция - генератор номеров банковских карт.
- Функция financial_transactions, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
- Функция transaction_amount, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях.
- Функция read_csv_transactions, которая считывает данные о финансовых операциях из CSV файла и преобразует их в список словарей
- Функция read_xlsx_transactions, которая считывает данные о финансовых операциях из excel файла и преобразует их в список словарей

## Декораторы:
- Декоратор для логирования вызова функции и записи ее результата в файл или на консоль.

## Логгеры:
- Написаны логи для модулей utils и masks:
financial_transactions_logger, transaction_amount_logger, card_number_logger, mask_account_logger

## Тестирование:

Написаны тесты для имеющиxcя в проекте функций.
Для запуска тестирования необходимо в терминале ввести "pytest"

## Структура проекта
По завершении этого проекта будет добавлен pytest, для запуска тестов и новый функционал

# Инструкция по установке
Чтобы скачать репозиторий:

`git clone https://github.com/SergeyNekrasov2/Homework1.git`

Затем вам необходимо установить основные зависимости для запуска проекта в вашей системе:

```pip install -r requirements.txt```

Подождите, пока наборы данных загрузятся, это может занять некоторое время. 

## Команда проекта:
`Некрасов Сергей` 

## Контакт для связи с командой разработки:
`nekrasov-nekras-nekrasov@mail.ru` 

## Источники
Программа создана при поддержке [skypro@skyeng.ru](https://sky.pro/#giftpopup) 
 ![alt текст](https://static.tildacdn.com/tild3364-3965-4237-b664-363533643431/Group_1321317003.svg) 

## Контакт для связи с командой разработки:
`nekrasov-nekras-nekrasov@mail.ru`


