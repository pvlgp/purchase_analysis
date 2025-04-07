from datetime import datetime as dt

import data
import purchase_analysis as pa


def main():
    price = int(input("Введите значение для отчета: 'Список покупок, где цена превышает заданное значение.': "))
    current_datetime = dt.now()
    try:
        reports = {
        "Отчет создан": current_datetime.strftime("%d.%m.%Y %H:%M:%S"),
        "Общая выручка": pa.total_revenue(data.purchases),
        "Товары по категориям": pa.items_by_category(data.purchases),
        f"Покупки дороже {price:.1f}": pa.expensive_purchases(data.purchases, price),
        "Средняя цена по категориям": pa.average_price_by_category(data.purchases),
        "Категория с наибольшим количеством проданных товаров": pa.most_frequent_category(data.purchases)
        }
    except Exception as err:
        print(f"Ошибка формирования отчета: {err}")
    print()
    try:
        for key, value in reports.items():
            print(f"{key}: {value}")
    except Exception as err:
        print(f"Ошибка вывода отчета: {err}")
    try:
        with open("report.txt", "a", encoding="UTF-8") as file:
            file.write("\n")
            for key, value in reports.items():
                file.writelines(f"{key}: {value}\n")
            print("***Отчет сохранен в файл report.txt***")
    except Exception as err:
        print(f"Ошибка создания файла: {err}")
    end_time = dt.now()
    lead_time = end_time - current_datetime
    print(f"Затрачено времени {lead_time}")


if __name__ == "__main__":
    main()
