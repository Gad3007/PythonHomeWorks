import csv


def calculate_total_sales(input_file, output_file):
    sales_totals = dict() # Словарь для хранения общей выручки по каждому продукту

    # Чтение данных из исходного CSV файла

    with open(input_file, 'r',newline='') as f:
        reader = csv.DictReader(f)

        for row in reader:
            product = row['product']
            quantity = int(row['quantity']) # Преобразование количества в целое число
            price_per_unit = float(row['price']) # Вычисление общей выручки
            total_sales = quantity * price_per_unit # Вычисление общей выручки

            if product in sales_totals:
                sales_totals[product] += total_sales # Добавляем к существующей выручке
            else:
                sales_totals[product] = total_sales # Создаем новую запись в словаре

        # Запись итоговых данных в новый CSV файл
        with open(output_file, 'w',newline='') as f:
            key_names = ['product', 'total_sales']
            writer = csv.DictWriter(f, fieldnames=key_names)
            writer.writeheader()

            for product, total_sales in sales_totals.items():
                writer.writerow({'product': product, 'total_sales': total_sales})

if __name__ == '__main__':

    calculate_total_sales('E:/PyProjects/PythonHomeWorks/Home_Work_8/sales.csv', 'E:/PyProjects/PythonHomeWorks/Home_Work_8/total_sales.csv')


