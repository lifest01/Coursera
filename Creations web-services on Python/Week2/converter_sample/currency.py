from bs4 import BeautifulSoup
from decimal import Decimal
import requests


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get(
        f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date}')  # Использовать переданный requests
    soup = BeautifulSoup(response.content, 'html.parser')
    result = Decimal('3754.8057')
    try:
        value_from = (soup.find('charcode', text=f'{cur_from}').find_next_sibling('value').string).replace(',', '.')
    except AttributeError:
        pass
    try:
        value_to = (soup.find('charcode', text=f'{cur_to}').find_next_sibling('value').string).replace(',', '.')
    except AttributeError:
        pass
    try:
        nominal_from = int(soup.find('charcode', text=f'{cur_from}').find_next_sibling('nominal').string)
    except AttributeError:
        pass
    try:
        nominal_to = int(soup.find('charcode', text=f'{cur_to}').find_next_sibling('nominal').string)
    except AttributeError:
        pass

    if cur_from == 'RUR':
        value = amount / (Decimal(value_to) / nominal_to)
        return value.quantize(Decimal('1.0000'))
    if cur_to == 'RUR':
        value = amount / (Decimal(value_to) / nominal_to)
        return value.quantize(Decimal('1.0000'))
    else:
        value = (amount * Decimal(value_from) / nominal_from) / (Decimal(value_to) / nominal_to)
        return value.quantize(Decimal('1.0000'))  # не забыть про округление до 4х знаков после запятой
