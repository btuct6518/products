import os # oprerating system
products = []
if os.path.isfile('products.csv'): # 檢查檔案在不再
	print('yeah! 找到檔案了')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續
			name, price = line.strip().split(',') # 等於 name = [0] price = [1]
			products.append([name, price])
	print(products)
else:
	print('找不到檔案')

#讓使用者輸入
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

 #印出商品價格
for w in products:
	print(w[0], '的價格是:', w[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')





