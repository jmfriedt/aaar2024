import numpy as np
from matplotlib import pyplot as plt
dateb=[]
tempe1=[]
tempe2=[]
# table=np.recfromcsv('./H187_winter2021.csv',skip_header=1)
table=np.recfromtxt('./220424_15h24_H186_winter2021.txt',encoding='ASCII',skip_header=10)
dateb=[]
tempe=[]
hauteur=[]
for k in range(0,len(table)):
    s=table[k]
    date=s[0]
    mois=int(date[0:2])
    jour=int(date[3:5])
    an=int(date[6:8])
    date=s[1]
    heur=int(date[0:2])
    tempe1.append(float(s[5]))
    tempe2.append(float(s[9]))
#    date=s[1]
#    jour=int(date[0:2])
#    mois=int(date[3:5])
#    an=int(date[6:8])
    an=an+2000
#    tempe1.append(float(s[2]))
#    tempe2.append(float(s[3]))
    dateb.append( np.datetime64('{}-{:02d}-{:02d}T{:02d}:00:00'.format(an, mois, jour,heur)) )
print(tempe1)
print(tempe2)
plt.subplot(313)
plt.plot(dateb,tempe1,'-',label='Onset Hobo')
#plt.plot(dateb,tempe2,'-')


dateb=[]
tempe1=[]
tempe2=[]
# table=np.recfromcsv('./H187_winter2021.csv',skip_header=1)
table=np.recfromtxt('./220425_19h18_H184_winter2021.txt',encoding='ASCII',skip_header=10)
dateb=[]
tempe=[]
hauteur=[]
for k in range(0,len(table)):
    s=table[k]
    date=s[0]
    mois=int(date[0:2])
    jour=int(date[3:5])
    an=int(date[6:8])
    date=s[1]
    heur=int(date[0:2])
    tempe1.append(float(s[5]))
    tempe2.append(float(s[9]))
#    date=s[1]
#    jour=int(date[0:2])
#    mois=int(date[3:5])
#    an=int(date[6:8])
    an=an+2000
#    tempe1.append(float(s[2]))
#    tempe2.append(float(s[3]))
    dateb.append( np.datetime64('{}-{:02d}-{:02d}T{:02d}:00:00'.format(an, mois, jour,heur)) )
print(tempe1)
print(tempe2)
plt.subplot(313)
plt.plot(dateb,tempe1,'-',label='Onset Hobo')
#plt.plot(dateb,tempe2,'-')

table=np.recfromcsv('./table.csv',skip_header=1)
dateb=[]
tempe=[]
prec=[]
depth=[]
for k in range(0,len(table)):
    s=table[k]
    print(s)
    date=s[2]
    jour=int(date[0:2])
    mois=int(date[3:5])
    an=int(date[6:10])
    if an>2000:
      prec.append(float(s[3]))
      depth.append(float(s[4]))
      tempe.append(float(s[6]))
      dateb.append( np.datetime64('{}-{:02d}-{:02d}'.format(an, mois, jour)) )
    print(f"{date} {an} {mois} {jour}")
plt.plot(dateb,tempe,'-',label='seklima')
plt.ylabel("temperature (degC)")
plt.xlim((np.datetime64('{}-{:02d}-{:02d}'.format(2022, 3, 1)),np.datetime64('{}-{:02d}-{:02d}'.format(2022, 4, 1))))
plt.xlabel("date")
plt.grid(True)
plt.legend()
#plt.figure()
#[y,x]=np.histogram(tempe,bins=42)
#plt.plot((x[0:-1]+x[1:])/2,y)
plt.show()
