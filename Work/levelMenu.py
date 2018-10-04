#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###
# Created Date: 2018-10-04,Thursday 10:07:51
# Author: YangXu
# Last Modified: 2018-10-04,Thursday 11:08:51
# Modified By: YangXu
###

province = ['SiChuan','ChongQing','YunNan']
citys = [['ChengDu','LiangShan','MianYang'],['ChongQingShi','DianJiang','WanZhou'],['KunMing','DaLi','LanCang']]
county = [[['JinNiu','ChengHua','WuHou','JinJiang'],['XiChang','XiDe','HuiLi'],['SanTai','JiangYou']],[['YuZhong','JiangBei'],['DianJiang1','DianJiang2'],['WanZhou1','WanZhou2']],[['KunMing1','KunMing2'],['DaLi1','DaLi2'],['LanCang1','LanCang2']]]
finalList = [province,citys,county]

def chooseList(indexList):
    if indexList[2] > 0:
        thisList = finalList[indexList[0]-1][indexList[1]-1][indexList[2]-1]
    elif indexList[1] > 0:
        thisList = finalList[indexList[0]-1][indexList[1]-1]
    else:
        thisList = finalList[indexList[0]-1]
    for i,x in enumerate(thisList,1):
        print(i,">>>",x)
    return len(thisList)

#Start !
print("There is the Provices meun : ")
indexList = [1,0,0]
nowLevel = 0
lenList = chooseList(indexList)
while True:
    print("Input 'up' to get parent meun, Input 'q' to exit.")
    chooseInput = input('Please input a sort number:')
    if chooseInput == 'q':
        break
    elif chooseInput == 'up':
        if nowLevel == 0:
            print("You are already in the first level!")
            continue
        else:
            indexList[nowLevel] = 0
            indexList[0] -= 1
            nowLevel -= 1
    else:
        try:
            chooseNum = int(chooseInput)
        except:
            print("Wrong input ! Please try again !")
            continue
        else:
            if chooseNum<1 or chooseNum>lenList:
                print("Wrong input ! Please try again !")
                continue
            else:
                if nowLevel == 2:
                    print("Con't get in. You are in the last level.")
                    continue
                else:
                    indexList[0] += 1
                    nowLevel += 1
                    indexList[nowLevel] = chooseNum
    lenList = chooseList(indexList)


print("Thanks for using this program!")