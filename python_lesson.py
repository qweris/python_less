    ##________________________Кол-во строк в списке
purchases = [
{"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
{"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
{"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
{"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]
def count_lines (purchases):
    lines = 0
    for line in purchases:
        lines += 1
    return(lines)
##________________________Первая задача
def total_revenue(purchases):
    sum=0
    for line_sum in range(0,count_lines(purchases)):
        sum+=(purchases[line_sum].get('price')*purchases[line_sum].get('quantity'))
    print(f"Общая выручка: {sum}")
total_revenue(purchases)
##_________________________Вторая задача
def items_by_category(purchases):
    dst={}
    for id in range(0,count_lines(purchases)):
        if purchases[id].get('category') in dst:
            dst[purchases[id].get('category')]+=[purchases[id].get('item')]
        else:
            dst[purchases[id].get('category')] = [purchases[id].get('item')]
    print(f'Товары по категориям: {dst}')
items_by_category(purchases)
##_________________________Третья задача

min_price=purchases[0].get('price')
for id in range(0,count_lines(purchases)):
    if purchases[id].get('price') < min_price:
        min_price = purchases[id].get('price')
def expensive_purchases(purchases, min_price):
    dst = []
    for id in range(0,count_lines(purchases)):
        if purchases[id].get('price')>=min_price:
            dst+=[purchases[id]]
    print(f'Покупки дороже {min_price}: {dst}')
expensive_purchases(purchases, min_price)

##______________________Четвертая задача
def average_price_by_category(purchases):
    summ={}
    cnt=0
    for id in range(0,count_lines(purchases)):
        if purchases[id].get('category') in summ:
            summ[purchases[id].get('category')]+=[purchases[id].get('price')]
        else:
            summ[purchases[id].get('category')] = [purchases[id].get('price')]

    for i in summ.keys():
        summ[i]=sum(summ[i])/(len(summ[i]))
    print(f'Средняя цена по категориям: {summ}')
average_price_by_category(purchases)

##______________________Пятая задача
quan={}
max_cat=''
max_q=purchases[0].get('quantity')
for id in range(0, count_lines(purchases)):
    if purchases[id].get('category') in quan:
        quan[purchases[id].get('category')] += [purchases[id].get('quantity')]
    else:
        quan[purchases[id].get('category')] = [purchases[id].get('quantity')]

for i in quan.keys():
    quan[i]=sum(quan[i])
    if quan[i]>max_q:
        max_cat=''
        max_cat+=i
print(f'Категория с наибольшим количеством проданных товаров: {max_cat}')



