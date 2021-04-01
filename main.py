a = [1, 2, 3]
b = True
c = None
d = "sfnjask"
e = {
    "a": ["x", 3, 4.756],
}
f = 3

if a[0] == 1:
    print("sim")
    if b:
        print("True")
    if c is None:
        print("None")
    if d is not None:
        print("not None")
    if b is not False:
        print("True2")
    if d == "sfnjask":
        print("str confirma")
    if d != "akd":
        print(a)
        print(e)
    string_a = str(e)
    string_b = str(b)
    if f < 3.5:
        print("menor")
elif a[0] == 2:
    print(2)
else:
    print("não")
    print("else")

print("fim")

print("branch: main")

while b:
    print("while")
    b = False

lista_a = [4, 5, 6, 7, 8, 4, 2, 6]

# for x in lista_a:
#     print(x)

# for x in range(1, 12, 2):
#     print(x)

# for i, item in enumerate(lista_a):
#     print(f"{i}: {item}")

# for i, item in enumerate(lista_a[1:-2]):
#     print(f"{i}: {item}")
#
# lista_b = lista_a[1:-2]
#
# item_a = lista_a[-3]

lista_c = []
for x in range(1, 12, 2):
    lista_c.append(x**2)

lista_c.extend(lista_a)

e = {
    "a": ["x", 3, 4.756],
    "x": (1, 3),
}

# for chave, valor in e.items():
#     print(f"chave: {chave}, val: {valor}")

# for chave in e.keys():
#     print(f"chave: {chave}")

# for valor in e.values():
#     print(f"val: {valor}")

for chave in e.keys():
    valor = e[chave]
    print(f"chave: {chave}, val: {valor}")
