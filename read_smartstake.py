#!/usr/bin/python3

import numpy as np
from matplotlib import pyplot as plt
#table=np.recfromtxt('./smartstake2022.txt',encoding='ASCII',skip_header=1)
#dateb=[]
#tempe=[]
#hauteur=[]
#for k in range(0,len(table)):
#    s=table[k]
#    indice=s[0]
#    date=s[1]
#    an=int(date[0:4])
#    mois=int(date[5:7])
#    jour=int(date[8:10])
#    if an>2000:
#      tempe.append(float(s[3]))
#      hauteur.append(float(s[2]))
#      # dateb.append( np.datetime64('{}-{:02d}-{:02d}'.format(an, mois, jour)) )
#      dateb.append( np.datetime64('{}-{:02d}-{:02d}'.format(an, mois, jour)) )
#    print(f"{date} {an} {mois} {jour}")
#plt.subplot(211)
#plt.plot(dateb,hauteur,'.')
#plt.xlim(np.datetime64('{}-{:02d}-{:02d}'.format(2022, 5, 1)))
#plt.ylim((-2, 0.1))

table=np.recfromtxt('./smartstake2023.txt',encoding='ASCII',skip_header=1)
dateb1=[]
tempe1=[]
hauteur1=[]
dateb2=[]
tempe2=[]
hauteur2=[]
for k in range(0,len(table)):
    s=table[k]
    indice=s[0]
    date=s[1]
    an=int(date[0:4])
    mois=int(date[5:7])
    jour=int(date[8:10])
    if an>2000 and an<2030: 
      if an>=2023:
         an=an-1
      # dateb.append( np.datetime64('{}-{:02d}-{:02d}'.format(an, mois, jour)) )
         hauteur2.append(float(s[2])+1.517)
         tempe2.append(float(s[3]))
         dateb2.append( np.datetime64('{}-{:02d}-{:02d}'.format(an, mois, jour)) )
      else:
         hauteur1.append(float(s[2]))
         tempe1.append(float(s[3]))
         dateb1.append( np.datetime64('{}-{:02d}-{:02d}'.format(an, mois, jour)) )
    print(f"{date} {an} {mois} {jour}")
plt.subplot(311)
plt.plot(dateb1,hauteur1,'b',label='2022')
plt.plot(dateb2,hauteur2,'r',label='2023')
plt.xlim((np.datetime64('{}-{:02d}-{:02d}'.format(2022, 5, 1)), np.datetime64('{}-{:02d}-{:02d}'.format(2022, 9, 20))))
plt.ylim((-2, 0.1))
# plt.xlabel('Date (month-day)')
plt.ylabel('Height variation (m)')
plt.legend()

import degreeday
