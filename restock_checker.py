#Stock Restock Checker v1

name = input("Product name: ")
cur_stock = int(input("Current stock qty: "))
re_stock = int(input("Reorder level: "))

if cur_stock <= 0:
    print("OUT OF STOCK")

if cur_stock <= re_stock:
    print(f"Reorder {(re_stock - cur_stock)} packs of {name} soon. Current stock is below threshold.")
elif cur_stock > re_stock:
    print("Stock OK")
