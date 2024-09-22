import numpy as np
from matplotlib import pyplot as plt
table=np.recfromtxt('./table2021-2024.csv',skip_header=1)
dateb2022=[]
tempe2022=[]
prec2022=[]
depth2022=[]
dateb2023=[]
tempe2023=[]
prec2023=[]
depth2023=[]
dateb2021=[]
tempe2021=[]
prec2021=[]
depth2021=[]
for k in range(0,len(table)):
    s=table[k]
    print(s)
    jour=s[0]
    mois=s[1]
    an=s[2]
    if an==2021:
      prec2021.append(float(s[5]))
      if (float(s[4])==0):
          depth2021.append(np.nan)
      else:
          depth2021.append(float(s[4]))
      if (float(s[3])==0):
          tempe2021.append(np.nan)
      else:
          tempe2021.append(float(s[3]))
      dateb2021.append( np.datetime64('{}-{:02d}-{:02d}'.format(2022, mois, jour)) )
    if an==2022:
      prec2022.append(float(s[5]))
      depth2022.append(float(s[4]))
      tempe2022.append(float(s[3]))
      dateb2022.append( np.datetime64('{}-{:02d}-{:02d}'.format(2022, mois, jour)) )
    if an==2023:
      prec2023.append(float(s[5]))
      depth2023.append(float(s[4]))
      tempe2023.append(float(s[3]))
      dateb2023.append( np.datetime64('{}-{:02d}-{:02d}'.format(2022, mois, jour)) )
    print(f"{an} {mois} {jour}")
ax=plt.subplot(311)
#ax.bar(dateb2023, depth2023, width=1,label='2023')
ax.bar(dateb2022, depth2022, width=1,label='2022')
ax.bar(dateb2021, depth2021, width=1,label='2021')
ax.xaxis_date()
# plt.plot(dateb,depth,'.')
plt.xlim((np.datetime64('{}-{:02d}-{:02d}'.format(2022, 2, 1)),np.datetime64('{}-{:02d}-{:02d}'.format(2022, 6, 15))))
plt.ylabel("snow depth (cm)")
plt.legend()
ax=plt.subplot(312)
#ax.bar(dateb2023, prec2023, width=1,label='2023')
ax.bar(dateb2022, prec2022, width=1,label='2022')
ax.bar(dateb2021, prec2021, width=1,label='2021')
ax.legend()
ax.xaxis_date()
plt.xlim((np.datetime64('{}-{:02d}-{:02d}'.format(2022, 2, 1)),np.datetime64('{}-{:02d}-{:02d}'.format(2022, 6, 15))))
plt.ylabel("precipitations (mm)")
plt.subplot(313)
#plt.plot(dateb2023,tempe2023,'-',label='2023')
plt.plot(dateb2022,tempe2022,'-',label='2022')
plt.plot(dateb2021,tempe2021,'-',label='2021')
plt.ylabel("temperature (degC)")
plt.xlim((np.datetime64('{}-{:02d}-{:02d}'.format(2022, 2, 1)),np.datetime64('{}-{:02d}-{:02d}'.format(2022, 6, 15))))
plt.ylim((-25,15))
plt.grid(True)
plt.xlabel("date")
plt.legend()
#plt.figure()
#[y,x]=np.histogram(tempe,bins=42)
#plt.plot((x[0:-1]+x[1:])/2,y)
plt.show()

