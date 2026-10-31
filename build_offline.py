from pathlib import Path
import json,base64
p=Path(__file__).parent/'web'
assets={str(f.relative_to(p)):'data:image/jpeg;base64,'+base64.b64encode(f.read_bytes()).decode() for f in (p/'assets').glob('*.jpg')}
assets.update({str(f.relative_to(p)):'data:audio/mpeg;base64,'+base64.b64encode(f.read_bytes()).decode() for f in (p/'assets'/'audio').glob('*.mp3')})
s=(p/'index.html').read_text().replace('<link rel="stylesheet" href="style.css">','<style>'+(p/'style.css').read_text()+'</style>')
s=s.replace('<script src="data.js"></script>', '<script>'+ (p/'data.js').read_text()+'\nwindow.EMBEDDED_ASSETS='+json.dumps(assets)+';</script>')
s=s.replace('<script src="app.js"></script>','<script>'+(p/'app.js').read_text()+'</script>')
out=Path(__file__).parent/'Natali-Quiz.html';out.write_text(s);print(out,round(out.stat().st_size/1024/1024,2),'MB')
