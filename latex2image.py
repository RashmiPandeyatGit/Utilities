import matplotlib.pyplot as plt
import io
from PIL import Image, ImageChops
from Equation import Expression
white = (255, 255, 255, 255)
def latex_to_img(tex):
    buf = io.BytesIO()
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.axis('off')
    plt.text(0, 0.6, tex, size=12)
    plt.savefig(buf, format='png')
    plt.close()
    #plt.plot()

    im = Image.open(buf)
    bg = Image.new(im.mode, im.size, white)
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    
    return im.crop(bbox)

fn = Expression("sqrt(a^2+b^2)",["a","b"])
# latex_to_img(r'$\displaystyle \int\int\int_V\left(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}\right)dx dy dz=\int\int_S(P dy dz+Q dz dx+R dx dy)$')
latex_to_img(fn)
