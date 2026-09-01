
products = []

n = int(input("Enter number of products: "))

for i in range(n):
    name = input("Enter product name: ")
    products.append(name)

search = input("Enter product to search: ")

if search in products:
    print("Product found!")
    print("Index:", products.index(search))
else:
    print("Product not found!")