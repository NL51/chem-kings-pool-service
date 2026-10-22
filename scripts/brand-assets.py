from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import base64,json,io
root=Path(__file__).resolve().parent.parent
logo=Image.open(root/'logo.png').convert('RGBA')
b=io.BytesIO();logo.save(b,'PNG');data=json.loads((root/'assets-data.json').read_text());data['logo']=base64.b64encode(b.getvalue()).decode()
card=Image.new('RGB',(1200,630),'#eff8fb');d=ImageDraw.Draw(card)
d.rectangle((0,0,1200,16),fill='#e9c645');d.rectangle((0,570,1200,630),fill='#10191f')
card.paste(logo.resize((360,360)),(65,115),logo.resize((360,360)))
f='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
d.text((480,115),'CHEM KINGS',font=ImageFont.truetype(f,26),fill='#006d9a')
d.text((475,178),'Your pool.\nOur chemistry.',font=ImageFont.truetype(f,66),fill='#10191f',spacing=4)
d.text((481,385),'Pools & spas. Clear water. Less work.',font=ImageFont.truetype(f,23),fill='#294651')
d.text((481,433),'Sacramento & surrounding communities',font=ImageFont.truetype(f,22),fill='#294651')
d.text((66,588),'WEEKLY POOL CARE  /  REPAIRS  /  SPA SERVICE',font=ImageFont.truetype(f,19),fill='white')
b=io.BytesIO();card.save(b,'JPEG',quality=92);data['og']=base64.b64encode(b.getvalue()).decode();(root/'assets-data.json').write_text(json.dumps(data))
