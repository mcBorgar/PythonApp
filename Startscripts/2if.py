#!/bin/python
print("Hva er temperaturen?")
temperatur = int(input())  

if temperatur > 40:
    print("Det er varmt")
elif 20 <= temperatur <= 40:
    print("Det er middels")
elif temperatur < 20:
    print("Det er kaldt")
