import json,time,threading
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from pathlib import Path
slides=json.loads(Path('dist/slides.js').read_text().removeprefix('const slides = ').rstrip(';'))
lock=threading.Lock()
state=dict(index=0,total=0,elapsed=0,running=False,auto=False,stamp=time.time()*1000)
def update():
 now=time.time()*1000
 delta=now-state['stamp'];state['stamp']=now
 if state['running']:
  state['total']+=delta;state['elapsed']+=delta
  while state['auto'] and state['elapsed']>=slides[state['index']]['seconds']*1000:
   if state['index']==len(slides)-1:state['running']=False;break
   state['elapsed']-=slides[state['index']]['seconds']*1000;state['index']+=1
class Handler(SimpleHTTPRequestHandler):
 def __init__(self,*a,**kw):super().__init__(*a,directory='dist',**kw)
 def response(self,status,data):
  body=json.dumps(data).encode();self.send_response(status);self.send_header('Content-Type','application/json');self.send_header('Cache-Control','no-store');self.send_header('Content-Length',str(len(body)));self.end_headers();self.wfile.write(body)
 def do_GET(self):
  if self.path=='/api/state':
   with lock:update();self.response(200,state.copy())
  else:super().do_GET()
 def do_POST(self):
  if self.path!='/api/command':self.response(404,{});return
  try:
   size=int(self.headers.get('Content-Length','0'))
   if size>1024:raise ValueError()
   data=json.loads(self.rfile.read(size));cmd=data['type']
   if cmd not in ['next','prev','go','play','auto','reset']:raise ValueError()
   if cmd=='go' and (type(data.get('index')) is not int or not 0<=data['index']<len(slides)):raise ValueError()
  except (ValueError,KeyError):self.response(400,{'error':'Comando inválido'});return
  with lock:
   update()
   if cmd in ['next','prev','go']:
    state['index']=max(0,min(len(slides)-1,data['index'] if cmd=='go' else state['index']+(1 if cmd=='next' else -1)));state['elapsed']=0
   elif cmd=='play':state['running']=not state['running']
   elif cmd=='auto':state['auto']=not state['auto']
   elif cmd=='reset':state.update(index=0,total=0,elapsed=0,running=False,auto=False)
   self.response(200,state.copy())
ThreadingHTTPServer(('0.0.0.0',4318),Handler).serve_forever()
