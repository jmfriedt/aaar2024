#!/usr/bin/python3

import numpy as np
from matplotlib import pyplot as plt
table=np.recfromtxt('./table2021-2024.csv',skip_header=1)
n2021=0
n2022=0
n2023=0
s2021=0
s2022=0
s2023=0
total2021=0
total2022=0
total2023=0
erreur2021=0
erreur2022=0
erreur2023=0
t2021=[]
t2022=[]
t2023=[]
date2021=[]
date2022=[]
date2023=[]
temp2021=[]
temp2022=[]
temp2023=[]
for k in range(0,len(table)):
    s=table[k]
    jour=int(s[0])
    mois=int(s[1])
    an=int(s[2])
    temp=float(s[3])
    if an==2021:
        date2021.append( np.datetime64('{}-{:02d}-{:02d}'.format(2022, mois, jour)) )
        total2021+=1
        temp2021.append(temp)
        if temp>0:
            n2021+=1
            s2021+=temp
            t2021.append(temp)
        else:
            t2021.append(0)
        if temp==0:
            erreur2021+=1
    if an==2022:
        date2022.append( np.datetime64('{}-{:02d}-{:02d}'.format(2022, mois, jour)) )
        total2022+=1
        temp2022.append(temp)
        if temp>0:
            n2022+=1
            s2022+=temp
            t2022.append(temp)
        else:
            t2022.append(0)
        if temp==0:
            erreur2022+=1
    if an==2023:
        date2023.append( np.datetime64('{}-{:02d}-{:02d}'.format(2022, mois, jour)) )
        total2023+=1
        temp2023.append(temp)
        if temp>0:
            n2023+=1
            s2023+=temp
            t2023.append(temp)
        else:
            t2023.append(0)
        if temp==0:
            erreur2023+=1
print(f"2021: {int(s2021)}/{n2021} days (total: {total2021}, erreur: {erreur2021})")
print(f"2022: {int(s2022)}/{n2022} days (total: {total2022}, erreur: {erreur2022})")
print(f"2023: {int(s2023)}/{n2023} days (total: {total2023}, erreur: {erreur2023})")
plt.subplot(312)
plt.plot(date2022,np.cumsum(t2022),'b',label='2022')
plt.plot(date2023,np.cumsum(t2023),'r',label='2023')
plt.xlim((np.datetime64('{}-{:02d}-{:02d}'.format(2022, 5, 1)), np.datetime64('{}-{:02d}-{:02d}'.format(2022, 9, 20))))
plt.legend()
plt.ylabel('PDD ($^o$C)')
plt.subplot(313)
plt.plot(date2022,(temp2021),'g',label='2021')
plt.plot(date2022,(temp2022),'b',label='2022')
plt.plot(date2023,(temp2023),'r',label='2023')
# plt.xlim((np.datetime64('{}-{:02d}-{:02d}'.format(2022, 5, 1)), np.datetime64('{}-{:02d}-{:02d}'.format(2022, 9, 20))))
plt.xlim((np.datetime64('{}-{:02d}-{:02d}'.format(2022, 5, 1)), np.datetime64('{}-{:02d}-{:02d}'.format(2022, 12, 31))))
plt.ylabel('Temperature ($^o$C)')
plt.legend()
plt.xlabel('Date (month-day)')
plt.show()
