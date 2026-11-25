#!/usr/bin/env python3
"""Rebuild consistent schema and answer-first content from data/business.json.
Runs locally; generated HTML files are committed and deploy as static files on Vercel.
Requires: pip install beautifulsoup4
"""
from pathlib import Path
import json, re, html
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/'data/business.json').read_text(encoding='utf-8'))
BASE=DATA['website'].rstrip('/')
STORES=DATA['locations']
PAGES=[('index.html','/','Home'),('locations.html','/locations','Locations'),('about.html','/about','About'),('contact.html','/contact','Contact'),('faq.html','/faq','FAQs')]+[(f"locations/{s['slug']}.html",f"/locations/{s['slug']}",s['city']) for s in STORES]
DAYS=['Monday','Tuesday','Wednesday','Thursday','Friday']

def make(tag, name, **attrs):
    t=tag.new_tag(name)
    for k,v in attrs.items(): t.attrs[k.replace('_','-')]=v
    return t

def store_schema(s):
    url=BASE+'/locations/'+s['slug']
    return {'@type':'AutoPartsStore','@id':url+'#store','name':DATA['name']+' - '+s['city'],'url':url,'telephone':s['phoneE164'],
        'address':{'@type':'PostalAddress','streetAddress':s['street'],'addressLocality':s['city'],'addressRegion':s['state'],'postalCode':s['zip'],'addressCountry':'US'},
        'openingHoursSpecification':{'@type':'OpeningHoursSpecification','dayOfWeek':['https://schema.org/'+d for d in DAYS],'opens':'08:00','closes':'17:00'},
        'branchOf':{'@id':BASE+'/#organization'},
        'hasMap':'https://www.google.com/maps/search/?api=1&query='+__import__('urllib.parse',fromlist=['quote']).quote(s['street']+', '+s['city']+', '+s['state']+' '+s['zip']),
        'description':f"Independent auto parts store in {s['city']}, Pennsylvania, serving retail customers and repair shops. Open Monday through Friday, 8 AM to 5 PM. An Auto Value partner."}

def breadcrumb_schema(path,title):
    if path=='/': return None
    items=[{'@type':'ListItem','position':1,'name':'Home','item':BASE+'/'}]
    if path.startswith('/locations/'):
        items.append({'@type':'ListItem','position':2,'name':'Locations','item':BASE+'/locations'})
    items.append({'@type':'ListItem','position':len(items)+1,'name':title,'item':BASE+path})
    return {'@type':'BreadcrumbList','@id':BASE+path+'#breadcrumb','itemListElement':items}

def graph_for(path,title):
    org={'@type':'Organization','@id':BASE+'/#organization','name':DATA['name'],
         'alternateName':['Olson and Tenglund','Olson Tenglund','Olson & Tenglund Auto Parts'],
         'url':BASE+'/','logo':BASE+'/assets/olson-horizontal.webp',
         'description':DATA['description'],
         'sameAs':list(DATA.get('socialProfiles',{}).values()),
         'subOrganization':[{'@id':BASE+'/locations/'+s['slug']+'#store'} for s in STORES]}
    website={'@type':'WebSite','@id':BASE+'/#website','name':DATA['name']+' Auto Parts','url':BASE+'/','publisher':{'@id':BASE+'/#organization'},'inLanguage':'en-US'}
    page={'@type':'WebPage','@id':BASE+path+'#webpage','url':BASE+path if path!='/' else BASE+'/','name':title,'isPartOf':{'@id':BASE+'/#website'},'inLanguage':'en-US'}
    g=[org,website,page]
    bc=breadcrumb_schema(path,title)
    if bc: g.append(bc);page['breadcrumb']={'@id':bc['@id']}
    if path=='/' or path=='/locations': g += [store_schema(s) for s in STORES]
    elif path.startswith('/locations/'):
        s=next(s for s in STORES if s['slug']==path.split('/')[-1]);g.append(store_schema(s));page['mainEntity']={'@id':BASE+path+'#store'}
    return {'@context':'https://schema.org','@graph':g}

def answer_panel(s):
    city=s['city'];phone=s['phone'];url='/locations/'+s['slug'];
    return f'''<section class="answer-panel" aria-labelledby="answers-{s['slug']}"><div class="shell answer-panel-inner"><span class="eyebrow">STORE INFORMATION &amp; ANSWERS</span><h2 id="answers-{s['slug']}">Questions about our {city} store</h2><div class="answer-grid">
      <article><h3>Is Olson &amp; Tenglund open in {city}?</h3><p>Yes. Our {city} auto parts store remains open and serves retail customers and professional repair shops.</p></article>
      <article><h3>What time does the {city} store close?</h3><p>Our {city} parts counter is open Monday through Friday from 8:00 AM until 5:00 PM. For weekend or holiday availability, please call ahead.</p></article>
      <article><h3>Is this still a NAPA store?</h3><p>No. Olson &amp; Tenglund is now an Auto Value partner. Older online directories may still show our previous supplier affiliation.</p></article>
      <article><h3>How can I check on an auto part?</h3><p>Call <a href="tel:{s['phoneE164']}">{phone}</a> and tell our team what vehicle you're working on and which part you need. Availability and ordering options should be confirmed with the store.</p></article>
      </div><p class="answer-panel-links">Find <a href="/locations">all three locations</a> or <a href="/faq">read additional FAQs</a>.</p></div></section>'''

def home_panel():
    return '''<section class="answer-panel" aria-labelledby="quick-business-answers"><div class="shell answer-panel-inner"><span class="eyebrow">QUICK ANSWERS</span><h2 id="quick-business-answers">Still open. Still local. Now with Auto Value.</h2><div class="answer-grid"><article><h3>Is Olson &amp; Tenglund still in business?</h3><p>Yes. Our three Pennsylvania stores in Port Allegany, Coudersport, and Smethport are open and serving customers.</p></article><article><h3>Did Olson &amp; Tenglund close when it left NAPA?</h3><p>No. The business continues operating and is now partnered with Auto Value. Some older directory listings have not yet been updated.</p></article><article><h3>When can I visit?</h3><p>Each store is open Monday through Friday, 8:00 AM to 5:00 PM. Call your local store for weekend or holiday availability.</p></article><article><h3>Can professional repair shops call for parts?</h3><p>Yes. We serve professional shops as well as retail customers. Contact the nearest parts counter to discuss your needs.</p></article></div><p class="answer-panel-links"><a href="/faq">Read more answers</a> · <a href="/locations">See all locations</a></p></div></section>'''

def breadcrumb_html(path,title):
    if path=='/': return ''
    parts=['<a href="/">Home</a>']
    if path.startswith('/locations/'):
        parts.append('<a href="/locations">Locations</a>')
    parts.append(f'<span aria-current="page">{html.escape(title)}</span>')
    return '<nav class="breadcrumb-trail shell" aria-label="Breadcrumb">'+'<span class="breadcrumb-separator"> / </span>'.join(parts)+'</nav>'

for filename,path,title in PAGES:
    target=ROOT/filename
    doc=BeautifulSoup(target.read_text(encoding='utf-8'),'html.parser')
    for old in doc.select('script[type="application/ld+json"]'): old.decompose()
    head=doc.head
    ld=doc.new_tag('script',type='application/ld+json')
    ld.string=json.dumps(graph_for(path,title),ensure_ascii=False,separators=(',',':'))
    head.append(ld)
    for old in doc.select('.answer-panel, .breadcrumb-trail'): old.decompose()
    main=doc.select_one('main')
    if path!='/':
        main.insert(0,BeautifulSoup(breadcrumb_html(path,title),'html.parser'))
    if path=='/':
        # Before main bottom CTA, preserving existing hero and visual design.
        node=doc.select_one('.ref-cta')
        if node: node.insert_before(BeautifulSoup(home_panel(),'html.parser'))
    if path.startswith('/locations/'):
        s=next(s for s in STORES if s['slug']==path.split('/')[-1])
        node=doc.select_one('main .seo-status')
        if node: node.insert_before(BeautifulSoup(answer_panel(s),'html.parser'))
        else: main.append(BeautifulSoup(answer_panel(s),'html.parser'))
    # Correct unsupported weekend assumptions throughout HTML.
    for p in doc.find_all(string=True):
        if p.parent and p.parent.name=='script': continue
        text=str(p)
        revised=text.replace('Saturday & Sunday: Closed','Weekend hours: Please call to confirm')
        revised=revised.replace('Saturday &amp; Sunday: Closed','Weekend hours: Please call to confirm')
        revised=revised.replace('They are closed Saturday and Sunday.','Weekend hours are not yet confirmed; please call your local store.')
        if revised!=text: p.replace_with(revised)
    # Preserve original layout, except remove duplicate HTML doctype and malformed closing br tags normalized by parser.
    rendered=str(doc)
    rendered=re.sub(r'^(?:\s*<!doctype html>\s*)+', '<!doctype html>\n',rendered,flags=re.I)
    target.write_text(rendered,encoding='utf-8')

# Rewrite FAQ answer body to reflect uncertainty on weekends and add customer-focused Q&A.
fp=ROOT/'faq.html';doc=BeautifulSoup(fp.read_text(encoding='utf-8'),'html.parser')
faq=doc.select_one('.seo-faq-list')
extra=[('Do you help customers find parts for their vehicles?', 'Yes. Call your nearest Olson & Tenglund store with your vehicle year, make, model, and the part you need. Our team can discuss available options.'),
       ('Do you serve independent repair shops?', 'Yes. Olson & Tenglund serves professional repair shops as well as retail customers at its three Pennsylvania locations. Call your local store to discuss your parts needs.'),
       ('Are parts availability and online ordering listed on this website?', 'This is the official store information website, not an online checkout. For current stock, ordering, or special requests, call the appropriate store.'),
       ('Where can I find the official Olson & Tenglund website?', 'The official website is olsontenglund.com. It includes current store locations, phone numbers, and information about the Auto Value partnership.')]
status=faq.select_one('.seo-status')
existing_questions={h.get_text(' ',strip=True) for h in faq.select('h2')}
for q,a in extra:
    if q in existing_questions: continue
    article=BeautifulSoup('<article class="seo-faq-item"><h2></h2><p></p></article>','html.parser').article
    article.h2.string=q;article.p.string=a
    if status: status.insert_before(article)
    else: faq.append(article)
fp.write_text(str(doc),encoding='utf-8')

css='''
/* Location-aware AEO content; intentionally subordinate to the existing site design. */
.breadcrumb-trail{padding-top:14px;padding-bottom:14px;font-size:.83rem;color:#55657a}
.breadcrumb-trail a{color:#385b7d;text-decoration:underline;text-underline-offset:2px}
.breadcrumb-separator{padding:0 7px;color:#8290a0}
.answer-panel{background:#f5f7fa;border-top:1px solid #e0e5eb;border-bottom:1px solid #e0e5eb;padding:clamp(38px,5vw,70px) 0}
.answer-panel-inner>h2{margin:.5rem 0 1.5rem;color:#091c34;font-size:clamp(1.65rem,3vw,2.4rem);line-height:1.18}
.answer-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}
.answer-grid article{background:white;border:1px solid #dee5ec;border-radius:12px;padding:23px 24px;box-shadow:0 4px 16px rgba(8,31,55,.035)}
.answer-grid h3{font-size:1.07rem;line-height:1.4;margin:0 0 .6rem;color:#071a33}
.answer-grid p{font-size:1rem;line-height:1.7;color:#465469;margin:0}
.answer-grid a,.answer-panel-links a{color:#9e1e25;text-decoration:underline;text-underline-offset:3px}
.answer-panel-links{margin:1.4rem 0 0;font-size:.96rem;color:#45566a}
@media(max-width:700px){.answer-grid{grid-template-columns:1fr}.answer-grid article{padding:20px}.breadcrumb-trail{font-size:.78rem}}
'''
css_path=ROOT/'site.css'
if '/* Location-aware AEO content;' not in css_path.read_text(encoding='utf-8'):
    with css_path.open('a',encoding='utf-8') as f:f.write('\n'+css)

# Sitemap from published HTML paths (no speculative URLs or invented modification dates).
sitemap=['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for _,p,_ in PAGES:sitemap.append(f'  <url><loc>{BASE+p if p!="/" else BASE+"/"}</loc></url>')
sitemap.append('</urlset>')
(ROOT/'sitemap.xml').write_text('\n'.join(sitemap)+'\n',encoding='utf-8')
print('Updated',len(PAGES),'pages, sitemap and structured data.')
