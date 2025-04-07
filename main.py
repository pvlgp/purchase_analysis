import purchase_analysis as pa
import data


def main():
    # TODO Реализовать создание файла с отчетом. Отчет необходимо вывести и терминал и сохранить в файле report.txt
    price = int(input("Введите значение для отчета: 'Список покупок, где цена превышает заданное значение.': "))
    print()
    print(f"Общая выручка: {pa.total_revenue(data.purchases)}")
    print(f"Товары по категориям: {pa.items_by_category(data.purchases)}")
    print(f"Покупки дороже {price:.1f}: {pa.expensive_purchases(data.purchases, price)}")
    print(f"Средняя цена по категориям: {pa.average_price_by_category(data.purchases)}")
    print(f"Категория с наибольшим количеством проданных товаров: {pa.most_frequent_category(data.purchases)}")


if __name__ == "__main__":
    main()
