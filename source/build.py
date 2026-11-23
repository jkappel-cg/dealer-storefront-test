import base64,glob,os
A=glob.glob('/root/.claude/skills/synced/*/prototype-standardizer/assets')[0]
b=lambda p:base64.b64encode(open(p,'rb').read()).decode()
s=open('template.html').read()
s=s.replace('__GRAPHIK_400__',b(A+'/fonts/Graphik-Regular-Web.woff2')).replace('__GRAPHIK_500__',b(A+'/fonts/Graphik-Medium-Web.woff2')).replace('__GRAPHIK_600__',b(A+'/fonts/Graphik-Semibold-Web.woff2')).replace('__RUND_600__',b(A+'/fonts/RundDisplay-SemiBold.woff2'))
s=s.replace('__LOGO__',b(A+'/cargurus-logo.png'))
s=s.replace('__BERNARDI__',b('bernardi.png')).replace('__TOPRATED__',b('toprated.png'))
star='<svg><use href="#i-star"/></svg>'
s=s.replace('__STAR5__',star*5)
s=s.replace('__STAR5O__','<svg><use href="#i-star-o"/></svg>'*5)
MAPS='https://www.google.com/maps/search/?api=1&amp;query=960+Worcester+Street+Natick+MA+01760'
s=s.replace('__MAPS__',MAPS)
actions=('<button class="act primary" data-action="contact"><svg class="ic" aria-hidden="true"><use href="#i-mail"/></svg>Contact</button>'
 '<button class="act act-save" data-action="save" aria-pressed="false"><svg class="ic" aria-hidden="true"><use href="#i-bookmark"/></svg>Save</button>'
 '<button class="act act-call" data-action="call"><svg class="ic" aria-hidden="true"><use href="#i-phone"/></svg>Call</button>'
 '<button class="act act-dir" data-action="toast" data-msg="Not available in prototype"><svg class="ic" aria-hidden="true"><use href="#i-dir"/></svg><span class="m">Directions</span><span class="d">Get directions</span></button>')
s=s.replace('__ACTIONS__',actions)
mapsvg='''<svg viewBox="0 0 343 220" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Map showing the dealership location"><rect width="343" height="220" fill="#e9eef0"/><path d="M0 150 Q60 120 110 150 T230 140 T343 170 L343 220 L0 220Z" fill="#c4dcec"/><rect x="214" y="18" width="92" height="58" rx="10" fill="#d3e8d0"/><rect x="18" y="26" width="70" height="44" rx="8" fill="#d3e8d0"/><g stroke="#fff" stroke-width="9" fill="none" stroke-linecap="round"><path d="M-10 96 L350 80"/><path d="M120 -10 L150 230"/><path d="M-10 40 L120 60 L260 -10"/><path d="M200 100 L350 140"/></g><g stroke="#f7d27a" stroke-width="5" fill="none" stroke-linecap="round"><path d="M70 230 L170 100 L260 20"/></g><g fill="#fff" stroke="#cfd6db" stroke-width="1"><path d="M136 78a14 14 0 1 1 28 0c0 11-14 24-14 24s-14-13-14-24z" fill="#0763d3" stroke="#05317b"/></g><circle cx="150" cy="78" r="5" fill="#fff"/></svg>'''
from PIL import Image
import io
im=Image.open('map.png').convert('RGB');im.thumbnail((900,900));bf=io.BytesIO();im.save(bf,'JPEG',quality=82)
s=s.replace('__MAP__','<img src="data:image/jpeg;base64,'+base64.b64encode(bf.getvalue()).decode()+'" alt="Map showing Bernardi Honda location">')
open('index.html','w').write(s)
print(len(s))
