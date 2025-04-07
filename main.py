from datetime import datetime as dt

import data
import purchase_analysis as pa


def main():
    # TODO Реализовать создание файла с отчетом. Отчет необходимо вывести и терминал и сохранить в файле report.txt
    price = int(input("Введите значение для отчета: 'Список покупок, где цена превышает заданное значение.': "))
    current_datetime = dt.now()
    reports = [
    "\n***",
    f"Отчет создан: {current_datetime.strftime("%d.%m.%Y %H:%M:%S")}",
    "***",
    f"Общая выручка: {pa.total_revenue(data.purchases)}",
    f"Товары по категориям: {pa.items_by_category(data.purchases)}",
    f"Покупки дороже {price:.1f}: {pa.expensive_purchases(data.purchases, price)}",
    f"Средняя цена по категориям: {pa.average_price_by_category(data.purchases)}",
    f"Категория с наибольшим количеством проданных товаров: {pa.most_frequent_category(data.purchases)}"
    ]
    for report in reports:
        print(report)
    try:
        with open("report.txt", "a", encoding="UTF-8") as file:
            for report in reports:
                file.writelines(f"{report}\n")
    except Exception as err:
        print(f"Ошибка создания файла: {err}")
    print("Отчет сохранен в файл report.txt")


if __name__ == "__main__":
    main()
