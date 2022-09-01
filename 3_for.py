"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
smartphones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
def main(price):
    sold_sum = 0
    for score in price:
        sold_sum += score
    return sold_sum / len(price)
    
prices_avg_sum = 0    
for one_item in smartphones:
    phone_avg = main(one_item['items_sold'])
    print(f'Среднее количество продаж телефона {one_item["product"]}:  {phone_avg}')
    prices_avg_sum += phone_avg
print(f'Среднее количество продаж {prices_avg_sum / len(smartphones)}')

def sales_sum(items_sold):
  items_sold_sum = 0
  for items in items_sold:
    items_sold_sum += items
  return items_sold_sum

items_sold_sum = 0
for phone_items_sum in smartphones: 
  phone_sold_sum = sales_sum(phone_items_sum['items_sold'])
  print(f'Суммарное количество продаж для товара {phone_items_sum["product"]}: {phone_sold_sum}')
  items_sold_sum += phone_sold_sum
print(f'Суммарное количество продаж всех товаров: {items_sold_sum}')


