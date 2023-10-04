from typing import List

from openpyxl import Workbook

from models import Product

'''
Пример ввода:
lst_products = [
    Product('name1', 100, 'd1', 'l1', ['l1', 'l2']),
    Product('name2', 101, 'd2', 'l2', ['l1', 'l2']),
]

lst_to_exel(lst_products)
'''

def lst_to_exel(products: List[Product]):
    for i in products:
        i.about = ''.join(i.about)
        i.images = ','.join(i.images)

    wb = Workbook()

    # grab the active worksheet
    ws = wb.active

    # Data can be assigned directly to cell

    # Rows can also be appended
    fields = ['title', 'price', 'about', 'link', 'images']
    ws.append(fields)

    for p in products:
        ws.append(p.get_field_lst())

    # Save the file
    wb.save("./my_book.xlsx")
    print(f'Result parsing: {len(products)} objects')
