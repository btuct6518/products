products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入價格:')
	p = []
	p.append(name)
	p.append(price)   # p = [name, price]
	products.append(p) # or products.append([name, prcie]) 就不用p了
print(products)

products[0][0]
