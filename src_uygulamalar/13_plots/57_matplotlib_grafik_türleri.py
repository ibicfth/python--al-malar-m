import matplotlib.pyplot as plt  

### >>>> stack /yığın)plot grafiği  <<<<< ####


# yil=[2011,2012,2013,2014,2015]

# oyuncu1=[4,9,35,4,7]
# oyuncu2=[6,7,12,6,21]
# oyuncu3=[8,13,17,10,18]



# plt.plot([],[],color='y',label='oyuncu1')
# plt.plot([],[],color='r',label='oyuncu2')
# plt.plot([],[],color='b',label='oyuncu3')

# plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=["y","r","b"])
# plt.legend()
# plt.show()

# ### >>> pasta grafikleri<<< ###
# goal_types=['penaltı','kaleye atılan','serbest vuruş']

# goals=[12,14,15]
# colors=['r','b','y']

# plt.pie(goals,labels=goal_types,colors=colors,shadow=True,explode=(0.05,0.05,0.05),autopct="%1.1f%%")
# plt.show()

### >>> bar grafiği <<< ###

# plt.bar([0.25,1.25,2.25,3.25,4.25],[40,57,62,49,29],label="audi",width=.5)
# plt.bar([0.75,1.75,2.75,3.75,4.75],[49,75,49,67,84],label="mercedes",width=.5)

# plt.legend()
# plt.xlabel("gün")
# plt.ylabel("mesafe")
# plt.title("araç bilgileri")

# plt.show()

### >>> histogram grafikleri <<< ###

yaslar=[10,45,18,2,36,9,87,49,76,16,49,34,57,68,90,99,91,29]
yas_grubları=[0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar,yas_grubları,histtype="bar",rwidth=0.8)
plt.xlabel("yaş grupları")
plt.ylabel("kişi sayısı")
plt.show()