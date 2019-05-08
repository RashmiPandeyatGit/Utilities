import matplotlib.pyplot as plt
from  matplotlib.ticker  import  * 

text = r'$\displaystyle \int\int\int_V\left(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}\right)dx dy dz=\int\int_S(P dy dz+Q dz dx+R dx dy)$'

fig = plt.figure()
ax = plt.subplot(111)
plt.axis('off')
ax.set_axis_off()

ax.text(1, 2, text,
        horizontalalignment='right',
        verticalalignment='center',
        fontsize=15, color='black',
        transform=ax.transAxes)

plt.show()
