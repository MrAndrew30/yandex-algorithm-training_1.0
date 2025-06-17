import sys

sales = {}
for sale in sys.stdin:
    customer, item, count = sale.split()
    count = int(count.strip())
    if customer not in sales:
        sales[customer] = dict()
        sales[customer][item] = 0
    if item not in sales[customer]:
        sales[customer][item] = 0
    sales[customer][item] += count

for customer in sorted(sales):
    print(f"{customer}:")
    for item in sorted(sales[customer]):
        print(f"{item} {sales[customer][item]}")
