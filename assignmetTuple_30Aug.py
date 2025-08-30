#Assignment 1
electronics_item = ("Laptop", 50000, "Black", "Samsung", "Electronics")
print("Tuple electronics_item : ", electronics_item)

print("Second item of this tuple : ", electronics_item[1])

required_elements = electronics_item[-2:]
print("Last 2 element of this tuple : ", required_elements)

if "Electronics" in electronics_item:
    print("Electronics is present in the tuple")
else:
    print("Electronics is not present in the tuple")


products = (1000, 1500, 1200, 1100, 900)

print("Count of 1000:", products.count(1000))

print("Max :", max(products))
print("Min :", min(products))

print("Product tuples :")
for value in products:
    print(value)

product_list = list(products)
product_list[0] = 55000
updated_tuple = tuple(product_list)
print("Updated tuple :", updated_tuple)

updated_tuple = updated_tuple + ("In Stock",)
print("Tuple after adding : ", updated_tuple)

temp_tuple = updated_tuple + ("Electronics",)
temp_list = list(temp_tuple)
temp_list.remove("Electronics")
final_tuple = tuple(temp_list)
print("Tuple after removing :", final_tuple)

a, b, c, _, _ = products
print("Unpacked variables:")
print("a =", a)
print("b =", b)
print("c =", c)

nested_tuple = (
    ("Product1", 1000),
    ("Product2", 1200),
    ("Product3", 900)
)

print("Second product name in nested tuple:", nested_tuple[1][0])

