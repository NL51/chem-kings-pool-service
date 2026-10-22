import fs from 'node:fs';
const data=fs.readFileSync('assets-data.json','utf8');
const source=fs.readFileSync('worker/site.js','utf8').replace(/export \{page,origin,services,areas,slug,google\};/,'');
fs.writeFileSync('worker/index.js','const assetData='+data+';\n'+source+'\n'+fs.readFileSync('worker/handler.js','utf8'));
