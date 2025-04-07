def total_revenue(purchases: list) -> float:
    '''Подсчет общей выручки'''
    total = 0
    for i in purchases:
        total += i['price'] * i['quantity']
    return total

def items_by_category(purchases) -> dict:
    '''Формирование списка товаров по категориям'''
    category = dict()
    for i in purchases:
        for _ in i:
            pass

def expensive_purchases(purchases, min_price):
    '''Вывод списка товаров, где цена превышает заданное значение'''
    pass

def average_price_by_category(purchases):
    '''Вывод средней цены товаров по категориям'''
    pass

def most_frequent_category(purchases):
    '''Вывод категории с наибольшим числом проданных товаров'''
    pass
