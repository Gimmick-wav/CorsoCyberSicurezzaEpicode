Str_a = input("inserisci numero ")
a= int(Str_a)
opr =input("digita un'operazione tra le seguenti: +, -, *, /, **: ")
Str_b = input("inserisci un altro numero: ")
b= int(Str_b)
if opr == "+":
    print(a + b)
elif opr == "-":
    print(a - b)
elif opr == "*":
    print(a * b)
elif opr == "/":
    print(a / b)
elif opr == "**":
    print(a**b)
else:
    print("era difficile scegliere una delle opzioni date?")