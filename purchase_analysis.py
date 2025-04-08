def total_revenue(purchases: list) -> float:
    '''Подсчет общей выручки'''
    try:
        total = 0
        for i in purchases:
            total += i['price'] * i['quantity']
        return total
    except Exception as err:
        return f"Ошибка выполнения отчета: {err}"

def items_by_category(purchases: list) -> dict:
    '''Формирование списка товаров по категориям'''
    try:
        category = dict()
        for i in purchases:
            for key, value in i.items():
                if value not in category and key == 'category':
                    category[value] = []
            if i['category'] in category:
                category[i['category']].append(i['item'])
        return category
    except Exception as err:
        return f"Ошибка выполнения отчета: {err}"

def expensive_purchases(purchases: list, min_price: float) -> list:
    '''Вывод списка товаров, где цена превышает заданное значение'''
    try:
        list_purchases = []
        for i in purchases:
            if i['price'] > min_price:
                list_purchases.append(i)
        return list_purchases
    except Exception as err:
        return f"Ошибка выполнения отчета: {err}"

def average_price_by_category(purchases: list) -> dict:
    '''Вывод средней цены товаров по категориям'''
    try:
        avg_price = dict()
        count_category = dict()
        for i in purchases:
            for key, value in i.items():
                if value not in avg_price and key == 'category':
                    avg_price[value] = 0
            if i['category'] in avg_price:
                avg_price[i['category']] += i['price']
        for i in purchases:
            if i['category'] in count_category:
                count_category[i['category']] += 1
            else:
                count_category[i['category']] = 1
        for key in avg_price.keys():
            if key in count_category:
                avg_price[key] /= count_category[key]
        return avg_price
    except Exception as err:
        return f"Ошибка формирования отчета: {err}"

def most_frequent_category(purchases: list) -> str:
    '''Вывод категории с наибольшим числом проданных товаров'''
    try:
        dict_counts = dict()
        counter = 0
        max_quantity_category = None
        for i in purchases:
            if i['category'] in dict_counts:
                dict_counts[i['category']] += i['quantity']
            else:
                dict_counts[i['category']] = i['quantity']
        for key, value in dict_counts.items():
            if value > counter:
                counter = value
                max_quantity_category = key
        return max_quantity_category
    except Exception as err:
        return f"Ошибка выполнения отчета: {err}"
