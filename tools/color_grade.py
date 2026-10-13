import sys,io,json,hashlib,os
from pathlib import Path
import numpy as np
from PIL import Image,ImageOps,ImageCms,ImageFilter
try:
 import pillow_heif;pillow_heif.register_heif_opener()
except ImportError:pass
SRGB=ImageCms.ImageCmsProfile(ImageCms.createProfile('sRGB')).tobytes()
def load_photo(path):
 im=Image.open(path);im=ImageOps.exif_transpose(im)
 icc=im.info.get('icc_profile')
 if icc:
  try:im=ImageCms.profileToProfile(im,ImageCms.ImageCmsProfile(io.BytesIO(icc)),ImageCms.createProfile('sRGB'),outputMode='RGB')
  except Exception:im=im.convert('RGB')
 else:im=im.convert('RGB')
 return im

def grade(im,profile='core',exposure=0.,wb=(1,1,1)):
 # Scene-referred exposure first, display-referred editorial curve afterwards.
 a=np.asarray(im,dtype=np.float32)/255
 linear=np.where(a<=0.04045,a/12.92,((a+0.055)/1.055)**2.4)
 linear*=2**exposure;linear*=np.array(wb,dtype=np.float32)
 a=np.where(linear<=0.0031308,12.92*linear,1.055*np.maximum(linear,0)**(1/2.4)-0.055)
 a=np.clip(a,0,1)
 curve=np.interp(a,[0,.035,.12,.25,.5,.75,.9,1],[.014,.038,.116,.246,.515,.764,.893,.975]).astype(np.float32)
 l=(curve*np.array([.2126,.7152,.0722])).sum(axis=2,keepdims=True)
 sat={'core':.94,'daylight':.97,'interior':.92,'night':.96}[profile]
 curve=l+(curve-l)*sat
 # Restrained warmth in middle values; keep bright whites nearly neutral.
 mid=4*l*(1-l);curve+=mid*np.array([.006,.002,-.005],dtype=np.float32)
 arr=np.clip(curve*255+.5,0,255).astype('uint8')
 return Image.fromarray(arr)

