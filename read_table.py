import numpy as np
from matplotlib import pyplot as plt
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
ax=plt.subplot(311)
ax.bar(dateb, depth, width=1)
ax.xaxis_date()
# plt.plot(dateb,depth,'.')
plt.xlim((np.datetime64('{}-{:02d}-{:02d}'.format(2022, 2, 1)),np.datetime64('{}-{:02d}-{:02d}'.format(2022, 11, 1))))
plt.ylabel("snow depth (cm)")
ax=plt.subplot(312)
# plt.plot(dateb,prec,'.')
ax.bar(dateb, prec, width=1)
ax.xaxis_date()
plt.xlim((np.datetime64('{}-{:02d}-{:02d}'.format(2022, 2, 1)),np.datetime64('{}-{:02d}-{:02d}'.format(2022, 11, 1))))
plt.ylabel("precipitations (mm)")
plt.subplot(313)
plt.plot(dateb,tempe,'-')
plt.ylabel("temperature (degC)")
plt.xlim((np.datetime64('{}-{:02d}-{:02d}'.format(2022, 2, 1)),np.datetime64('{}-{:02d}-{:02d}'.format(2022, 11, 1))))
plt.xlabel("date")
#plt.figure()
#[y,x]=np.histogram(tempe,bins=42)
#plt.plot((x[0:-1]+x[1:])/2,y)
plt.show()
