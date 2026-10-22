import assert from 'node:assert/strict';import worker from '../worker/index.js';
const base='https://chem-kings-pool-service.roundprawn256.chatgpt.site';const get=p=>worker.fetch(new Request(base+p),{});
const home=await get('/');assert.equal(home.status,200);let html=await home.text();assert(html.includes('og:image'));assert(html.includes('chem.kings'));
const links=[...html.matchAll(/href="(\/[^"#]*)"/g)].map(m=>m[1]);for(const p of new Set(links)){const r=await get(p);assert.equal(r.status,200,p)}
const map=await(await get('/sitemap.xml')).text();const routes=[...map.matchAll(/<loc>(.*?)<\/loc>/g)].map(m=>m[1]);for(const url of routes){let r=await worker.fetch(new Request(url),{});assert.equal(r.status,200,url);let h=await r.text();assert.equal((h.match(/<h1[ >]/g)||[]).length,1,url)}
assert.equal((await get('/unknown/')).status,404);assert.equal((await get('/api/inquiries')).status,401);
const memory=new Map();const env={BUCKET:{async get(k){return memory.has(k)?{text:async()=>memory.get(k)}:null},async put(k,v){memory.set(k,v)},async list(){return {objects:[...memory.keys()].filter(x=>x.startsWith('inquiries/')).map(key=>({key})),truncated:false}}} ,INBOX_KEY:'test-key'};
const form=()=>{let f=new FormData();Object.entries({name:'QA Test',phone:'9165550100',email:'test@example.com',zip:'95838',service:'Weekly pool service',message:'Test only',consent:'on'}).forEach(([k,v])=>f.set(k,v));return f};
let bad=form();bad.set('email','invalid');assert.equal((await worker.fetch(new Request(base+'/api/quote',{method:'POST',body:bad}),env)).status,400);
let ok=await worker.fetch(new Request(base+'/api/quote',{method:'POST',body:form()}),env);assert.equal(ok.status,201);assert((await ok.json()).reference.startsWith('CK-'));
let inbox=await worker.fetch(new Request(base+'/api/inquiries',{headers:{Authorization:'Bearer test-key'}}),env);assert.equal((await inbox.json()).inquiries.length,1);
assert.equal((await worker.fetch(new Request(base+'/api/quote',{method:'POST',body:form(),headers:{Origin:'https://other.example'}}),env)).status,403);
console.log('Passed: '+routes.length+' pages, internal links, metadata, assets, form validation, durable-store flow, private inbox, origin checks.');
