from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
import json,base64,io
root=Path(__file__).resolve().parent.parent
im=Image.new('RGBA',(480,480),'#083f55');d=ImageDraw.Draw(im);f='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
d.text((95,58),'P',font=ImageFont.truetype(f,300),fill='#83e7ed');d.arc((65,330,420,440),0,180,fill='white',width=12)
im.save(root/'logo.png');data=json.loads((root/'assets-data.json').read_text());data['logo']=base64.b64encode((root/'logo.png').read_bytes()).decode();(root/'assets-data.json').write_text(json.dumps(data))

if (root/'homepage-preview.jpg').exists():
 data['og']=base64.b64encode((root/'homepage-preview.jpg').read_bytes()).decode()
 (root/'assets-data.json').write_text(json.dumps(data))
