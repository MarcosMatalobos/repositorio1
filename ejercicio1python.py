#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Administrator
#
# Created:     06/09/2022
# Copyright:   (c) Administrator 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    a = int(input("Ingrese un nro impar: "))
    while a % 2 == 0:
        a = int(input("ingrese un nro impar"))

    print("Ingreso nro par")

#ejercicio1

if __name__ == '__main__':
    main()
