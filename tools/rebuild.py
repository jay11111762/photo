"""Rebuild selected derivatives from original files and the checked-in manifest.
Usage: python tools/rebuild.py --source-root /path/to/originals --output-root /new/output
Dependencies: Pillow, numpy, pillow-heif (for HEIC).
"""
import argparse,json,hashlib
from pathlib import Path
from color_grade import load_photo,grade,SRGB
from PIL import Image
p=argparse.ArgumentParser();p.add_argument('--source-root',type=Path,required=True);p.add_argument('--output-root',type=Path,required=True);a=p.parse_args()
root=Path(__file__).resolve().parents[1];m=json.loads((root/'manifest.json').read_text())
for row in m['assets']:
 source=a.source_root/row['rel']
 if hashlib.sha256(source.read_bytes()).hexdigest()!=row['source_sha256']:raise ValueError('Source changed: '+row['id'])
 im=load_photo(source);im.thumbnail((4096,4096),Image.Resampling.LANCZOS);out=grade(im,row['profile'],row['exposure_ev'],row['white_balance_rgb'])
 for key,edge,quality in [('master',4096,93),('web',2400,84),('thumbnail',640,88),('comparison_original',1400,92)]:
  dest=a.output_root/row[key];dest.parent.mkdir(parents=True,exist_ok=True);v=(im if key=='comparison_original' else out).copy();v.thumbnail((edge,edge),Image.Resampling.LANCZOS if key in ('master','web') else Image.Resampling.BICUBIC)
  if key=='web':v.save(dest,quality=quality,method=6,icc_profile=SRGB)
  elif key=='master':v.save(dest,quality=quality,subsampling=0,optimize=True,icc_profile=SRGB)
  else:v.save(dest,quality=quality,icc_profile=SRGB)
print('Rebuilt',len(m['assets']),'photos')
