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
        for key, value in i.items():
            if key == 'category':
                if value in category:
                    category[value] = ''

def expensive_purchases(purchases, min_price) -> list:
    '''Вывод списка товаров, где цена превышает заданное значение'''
    list_purchases = []
    for i in purchases:
        if i['price'] > min_price:
            list_purchases.append(i)
    return list_purchases

def average_price_by_category(purchases):
    '''Вывод средней цены товаров по категориям'''
    pass

def most_frequent_category(purchases):
    '''Вывод категории с наибольшим числом проданных товаров'''
    pass
