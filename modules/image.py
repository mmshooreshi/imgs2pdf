from PIL import Image
from io import BytesIO
import requests


def imgdimension(imglink):
    try:
        if(str(imglink[:4:1])=="http"):
            response = requests.get(imglink)
            img = Image.open(BytesIO(response.content))
        else:
            img = Image.open(imglink)
    except:
        img=Image.open(imglink[:imglink.rfind("."):1]+'.png')
    #rgb_im = img.convert('RGBA')
    #rgb_im.mode='RGBA'
    #print(imglink[:imglink.rfind("."):1]+'.jpg')
    if(str(imglink[-3::1])=="png"):
        #print(imglink)
        png = img.convert('RGBA')
        background = Image.new('RGBA', png.size, (255,255,255))
        alpha_composite = Image.alpha_composite(background, png)
        alpha_composite= alpha_composite.convert("RGB")
        alpha_composite.save(imglink[:imglink.rfind("."):1]+'.jpg', 'JPEG', quality=90)
    #img.convert('RGB').save(imglink[:imglink.rfind("."):1]+'.jpg', 'JPEG')
    #rgb_im.save(imglink[:imglink.rfind("."):1]+'.jpg')
    widthpx, heightpx = img.size
    widthmm=185
    heightmm= heightpx*(widthmm/widthpx)

    return widthmm,heightmm,heightpx,widthpx