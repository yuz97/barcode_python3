import barcode
from barcode.writer import ImageWriter

'''
barcode.PROVIDED_BARCODES 
['code128','code39','ean','ean13','ean14','ean8','gs1',
'gs_128','gtin','isbn','isbn10','isbn13','issn','itf','jan','pzn',
'upc','upca']
'''
ISBN = barcode.get_barcode_class('isbn10')
x = ISBN('9989786765',writer = ImageWriter())

x.save('barcode_ISBNKU')
