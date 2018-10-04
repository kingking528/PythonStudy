#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###
# Created Date: 2018-09-26,Wednesday 09:58:37
# Author: YangXu
# Last Modified: 2018-09-26,Wednesday 11:08:05
# Modified By: YangXu
###

#简单的购物车小程序

#定义货架，包含品名与价格
products = {}
products['iPhone XS 64G'] = 8699
products['iPhone XS 256G'] = 10099
products['iPhone XS 256G'] = 11899
products['Coffee'] = 32
products['Tea'] = 18
products['Juice'] = 26
products['Cigarettes'] = 56
productsList = list(products.keys())

# Go !

salary = int(input("Please input your salary :"))
sumPrice = 0
print("There is our goods:")
for i in range(len(productsList)):
    print("%d : %-30s%d" % (i+1,productsList[i],products.get(productsList[i])))
chooseList = []

def checkgood(goodName):
    global sumPrice
    sumPrice += products.get(goodName)
    if sumPrice > salary:
        print("Not enough Money !")
    else:
        chooseList.append(goodName)
    

def printout():
    if len(chooseList) > 1:
        print("Here is the items you have:")
        for i in range(len(chooseList)):
            print("%d : %-30s%d" % (i+1,chooseList[i],products.get(chooseList[i])))
        print("You have used %d for shopping." % sumPrice)
        print("You have %d left." % (salary-sumPrice))
    else:
        print("You have buy nothing !")

while True:
    chooseInput = input('Please choose a item(input "checkout" to end shopping):')
    if chooseInput == 'checkout':
        printout()
        break
    else:
        try:
            chooseNum = int(chooseInput) - 1
        except:
            print("Wrong input ! Please try again !")
            continue
        else:
            if chooseNum<0 or chooseNum+1>len(productsList):
                print("Wrong input ! Please try again !")
                continue
            else:
                checkgood(productsList[chooseNum])