#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number<0:
        number *= -1
    return number


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    list = []
    for char in prefixes :
        list.append(char+suffixe)
    return list


def prime_integer_summation() -> int:
    somme = 2
    for number in range(2, 101) :
        for i in range(2, number):
            for i in range(2,number):
                if (number % i) != 0:
                    if(number==i+1):
                        somme += number
                        continue
                else :
                    break
    return somme


def factorial(number: int) -> int:
    factoriel = 1
    for i in range(1, number + 1) :
        factoriel *= i
    return factoriel


def use_continue() -> None:
    for number in range(1, 11):
        if number == 5:
            continue
        print(number)
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    listBool=[]
    indexInt=0
    for i in groups:
        if len(i)>10 or len(i)<=3:
            listBool.append(False)
            continue

        if len(listBool)==indexInt:
            for j in i:
                if j==25:
                    listBool.append(True)
                    break
        
        if len(listBool)==indexInt:
            for j in i:
                if j<18:
                    listBool.append(False)
                    break

        if len(listBool)==indexInt:
            plus70 = False
            exact50 = False
            for j in i:
                if j==50:
                    exact50 = True
                if j>70:
                    plus70 = True
            if (plus70 and exact50):
                listBool.append(False)
        
        else:
            listBool.append(True)
        i=+1
            
    return listBool


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
