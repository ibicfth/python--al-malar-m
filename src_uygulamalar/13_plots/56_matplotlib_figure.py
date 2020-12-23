import matplotlib.pyplot as plt  
import numpy as np  

# x=np.linspace(-10,9,20)
# y=x**3

# figure=plt.figure() 

# axes=figure.add_axes([0.1,0.1,0.8,0.8]) ##add axes figure alanı üzerine eklenecek olan axes in konumunu belirtir.
# axes.plot(x,y,'b')

# axes.set_xlabel("x label")
# axes.set_ylabel("y label")

# axes.set_title("grafik adı")
# plt.show()

########################################################
##bir figure birden fazla grafik(axes) ekleyebilriz
# x=np.linspace(-10,9,20)
# y=x**3
# z=x**2
# figure=plt.figure() 

# ## 1. axes küp olan y=x**3 için
# axes_cube=figure.add_axes([0.1,0.1,0.8,0.8]) ##add axes figure alanı üzerine eklenecek olan axes in konumunu belirtir.
# axes_cube.plot(x,y,'b')

# axes_cube.set_xlabel("x label")
# axes_cube.set_ylabel("y label")

# axes_cube.set_title("1. axes grafiği")

# ## 2. axes kare olan z=x**2 için
# axes_square=figure.add_axes([0.15,0.6,0.25,0.25]) ##add axes figure alanı üzerine eklenecek olan axes in konumunu belirtir.
# axes_square.plot(x,z,'r')

# axes_square.set_xlabel("x label")
# axes_square.set_ylabel("y label")

# axes_square.set_title("2. axes grafiği")

# plt.legend()
# plt.show()

## ##bunları tek bir axes üzerinden de 2grafik yazdırılavilir.
# x=np.linspace(-10,9,20)
# y=x**3
# z=x**2

# figure=plt.figure()

# axes=figure.add_axes([0,0,1,1])

# axes.plot(x,y,label='küp')
# axes.plot(x,z,label='kare')
# axes.legend()

# plt.show()

###################################
# x=np.linspace(-10,9,20)
# y=x**3
# z=x**2

# fig, axes=plt.subplots(2,1) ##matris gibi düşünülebiri 2 satır(2grafik) x 1 kolon(1sayfa)
##ayrıca subplots a figsize parametresi ile boyut verilebilir.fig, axes=plt.subplots(2,1,figsize=4,4)
# axes[0].plot(x,y)
# axes[0].set_title("1. grafik")

# axes[1].plot(x,z)
# axes[1].set_title("2. grafik")

# plt.tight_layout() ##grafiklerin çakışmaması için
# plt.show()

#####################################
## çizdirdiğimiz grafiği kaydetmek için fig.savefig("Dosya_Adı") verilir.


x=np.linspace(-10,9,20)
y=x**3
z=x**2

fig, axes=plt.subplots(2,1) ##matris gibi düşünülebiri 2 satır(2grafik) x 1 kolon(1sayfa)
#ayrıca subplots a figsize parametresi ile boyut verilebilir.fig, axes=plt.subplots(2,1,figsize=4,4)
axes[0].plot(x,y)
axes[0].set_title("1. grafik")

axes[1].plot(x,z)
axes[1].set_title("2. grafik")

plt.tight_layout() ##grafiklerin çakışmaması için
fig.savefig("13_plots/grafikcizim.png")
plt.show()
