from pathlib import Path
import base64,json
r=Path(__file__).resolve().parent.parent
a=json.loads((r/'assets-data.json').read_text())
a['logo']=base64.b64encode((r/'logo.png').read_bytes()).decode()
a['og']=base64.b64encode((r/'homepage-preview.jpg').read_bytes()).decode()
(r/'assets-data.json').write_text(json.dumps(a))
