from pathlib import Path
import json,base64,io
from PIL import Image,ImageDraw,ImageFont
root=Path(__file__).parent
im=Image.open(root/'pool.jpg'); im.thumbnail((1600,1200)); b=io.BytesIO();im.save(b,'JPEG',quality=84); hero=base64.b64encode(b.getvalue()).decode()
share=Image.open(root/'pool.jpg').resize((1200,630));d=ImageDraw.Draw(share);d.rectangle((0,0,1200,630), fill=None)
overlay=Image.new('RGBA',(1200,630),(4,34,51,110));share=Image.alpha_composite(share.convert('RGBA'),overlay);d=ImageDraw.Draw(share)
f='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
d.text((68,60),'CHEM KINGS',font=ImageFont.truetype(f,32),fill='white');d.text((65,200),'Your pool.\nOur chemistry.',font=ImageFont.truetype(f,77),fill='white');d.text((70,465),'POOL CARE • SACRAMENTO & SURROUNDING AREAS',font=ImageFont.truetype(f,25),fill='white');b=io.BytesIO();share.convert('RGB').save(b,'JPEG',quality=90);og=base64.b64encode(b.getvalue()).decode()
(root/'assets-data.json').write_text(json.dumps({'hero':hero,'og':og}))
