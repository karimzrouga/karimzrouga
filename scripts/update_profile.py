"""Refresh public profile statistics. The dedicated 3D action renders the activity city."""
import datetime, html, json, math, os, re, urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def fetch(url,payload=None):
    headers={'Authorization':'Bearer '+os.environ['GH_TOKEN'],'User-Agent':'karimzrouga-profile','Accept':'application/vnd.github+json'}
    data=None if payload is None else json.dumps(payload).encode()
    if data: headers['Content-Type']='application/json'
    with urllib.request.urlopen(urllib.request.Request(url,data=data,headers=headers),timeout=45) as response:return json.load(response)
def render(title,body,height):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="{height}" viewBox="0 0 1000 {height}" role="img"><title>{html.escape(title)}</title><rect width="1000" height="{height}" rx="16" fill="#120f16"/><style>text{{font-family:Arial,sans-serif;fill:#e6edf3}} .reveal{{animation:reveal 1.4s ease both;transform-box:fill-box;transform-origin:bottom}} @keyframes reveal{{from{{opacity:0;transform:scaleY(.05)}}to{{opacity:1;transform:scaleY(1)}}}} @media(prefers-reduced-motion:reduce){{.reveal{{animation:none}}}}</style>{body}</svg>'
def label(x,y,value,size=16,color='#e6edf3'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}">{html.escape(str(value))}</text>'
def build(user,calendar):
    now=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M UTC')
    items=[('PUBLIC REPOS',user['public_repos']),('FOLLOWERS',user['followers']),('FOLLOWING',user['following']),('YEAR CONTRIBUTIONS',calendar['totalContributions'])]
    body=label(32,38,'05 / GITHUB ACTIVITY',13,'#60a5fa')
    for i,(name,value) in enumerate(items):
        x=32+i*245;body+=label(x,101,value,38)+label(x,133,name,11,'#94a3b8')
    body+=label(32,180,'Updated '+now,12,'#94a3b8')
    body+='<rect x="32" y="155" width="936" height="2" fill="#312e81"/><rect x="32" y="155" width="50" height="2" fill="#60a5fa"><animate attributeName="x" values="32;918;32" dur="8s" repeatCount="indefinite"/></rect>'
    (ROOT/'assets/stats.svg').write_text(render('Live public GitHub statistics',body,210))

def main():
    username=os.environ.get('PROFILE_USERNAME','karimzrouga')
    user=fetch('https://api.github.com/users/'+username)
    response=fetch('https://api.github.com/graphql',{'query':'query($login:String!){ user(login:$login){ contributionsCollection{ contributionCalendar{totalContributions weeks{contributionDays{date weekday contributionCount}}} } } }','variables':{'login':username}})
    if response.get('errors'):raise RuntimeError(json.dumps(response['errors']))
    calendar=response['data']['user']['contributionsCollection']['contributionCalendar']
    build(user,calendar)
    readme=ROOT/'README.md';version=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%d%H%M%S')
    readme.write_text(re.sub(r'(assets/(?:stats|city)\.svg)\?v=\d+',lambda m:m[1]+'?v='+version,readme.read_text()))
if __name__=='__main__':main()
