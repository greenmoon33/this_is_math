"""This Is Math — an interactive geometric chord instrument."""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="This Is Math", page_icon="◯", layout="wide")

INSTRUMENT = r"""
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@300;400;500&family=Manrope:wght@400;500&display=swap');
:root{--ink:#f4f0e8;--muted:#92938d;--line:rgba(244,240,232,.13);--accent:#d7ff64}
*{box-sizing:border-box}html,body{margin:0;min-height:100%;background:#090a0a;color:var(--ink)}
body{font-family:Manrope,sans-serif;background:radial-gradient(circle at 50% 44%,#30362f55,transparent 35%),linear-gradient(145deg,#0d0f0e,#070808 72%);overflow-x:hidden}
.grain{position:fixed;inset:0;pointer-events:none;opacity:.045;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 180 180' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
main{min-height:100vh;padding:30px clamp(20px,4vw,64px) 24px;display:grid;grid-template-rows:auto 1fr auto}
header{display:flex;justify-content:space-between;gap:24px}.brand{font:500 12px/1 DM Mono;letter-spacing:.2em;text-transform:uppercase}.brand span{color:var(--accent)}
.hint{color:var(--muted);font:300 11px/1.5 DM Mono;letter-spacing:.06em;text-align:right}.stage{display:grid;place-items:center;min-height:560px}
.instrument{position:relative;width:min(66vh,620px);aspect-ratio:1}canvas{width:100%;height:100%;display:block;cursor:pointer;touch-action:manipulation}
.center{position:absolute;inset:0;display:grid;place-content:center;text-align:center;pointer-events:none}.eyebrow{margin-bottom:12px;color:var(--muted);font:400 10px/1 DM Mono;letter-spacing:.18em;text-transform:uppercase}
h1{margin:0;font:400 clamp(32px,5vw,58px)/.95 Manrope;letter-spacing:-.055em}#chord{margin-top:13px;color:var(--accent);font:400 11px/1 DM Mono;letter-spacing:.12em;text-transform:uppercase}
footer{display:grid;grid-template-columns:1fr auto 1fr;align-items:end;gap:28px}.controls{display:flex;justify-content:center;flex-wrap:wrap;gap:8px}
button{appearance:none;border:1px solid var(--line);border-radius:99px;padding:10px 15px;background:#ffffff06;color:var(--muted);cursor:pointer;font:400 10px/1 DM Mono;letter-spacing:.06em;text-transform:uppercase;transition:.2s}
button:hover{color:var(--ink);border-color:#f4f0e84d}button:active{transform:scale(.96)}button.active{color:#11130e;border-color:var(--accent);background:var(--accent)}button:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.status{font:300 10px/1.5 DM Mono;color:var(--muted);text-transform:uppercase;letter-spacing:.08em}.right{text-align:right}#dot{display:inline-block;width:6px;height:6px;margin-right:8px;border-radius:50%;background:#555;transition:.2s}#dot.on{background:var(--accent);box-shadow:0 0 12px var(--accent)}
@media(max-width:720px){main{padding:22px 14px 20px}.stage{min-height:440px}.instrument{width:min(94vw,520px)}footer{grid-template-columns:1fr;justify-items:center}footer .status{display:none}.hint{max-width:155px}}
</style></head><body><div class="grain"></div><main>
<header><div class="brand"><span>●</span>&nbsp; This is math</div><div class="hint">SELECT A FORM<br>TO HEAR ITS HARMONY</div></header>
<section class="stage"><div class="instrument"><canvas id="pad" aria-label="Interactive geometric music pad"></canvas><div class="center"><div class="eyebrow">Now playing</div><h1 id="shape">Hexagon</h1><div id="chord">F major 9 · 6 voices</div></div></div></section>
<footer><div class="status"><span id="dot"></span>audio reactive</div><nav class="controls" aria-label="Choose a geometric chord"><button data-n="3">Triangle</button><button data-n="4">Square</button><button data-n="5">Pentagon</button><button class="active" data-n="6">Hexagon</button><button data-n="8">Octagon</button></nav><div class="status right">geometry / harmony<br>01—05</div></footer>
</main><script>
const forms={
3:{name:'Triangle',chord:'C major · 3 voices',color:'#ffbd59',notes:[261.63,329.63,392]},
4:{name:'Square',chord:'D minor 7 · 4 voices',color:'#6ee7f2',notes:[293.66,349.23,440,523.25]},
5:{name:'Pentagon',chord:'A minor 9 · 5 voices',color:'#ff7eb6',notes:[220,261.63,329.63,392,493.88]},
6:{name:'Hexagon',chord:'F major 9 · 6 voices',color:'#d7ff64',notes:[174.61,220,261.63,329.63,392,523.25]},
8:{name:'Octagon',chord:'E suspended · 8 voices',color:'#a792ff',notes:[164.81,220,246.94,329.63,369.99,440,493.88,659.25]}};
const canvas=document.querySelector('#pad'),ctx=canvas.getContext('2d'),buttons=[...document.querySelectorAll('button')],dot=document.querySelector('#dot');let sides=6,angle=0,pulse=0,audio;
function fit(){const d=Math.min(devicePixelRatio||1,2),r=canvas.getBoundingClientRect();canvas.width=r.width*d;canvas.height=r.height*d;ctx.setTransform(d,0,0,d,0,0)}
function poly(x,y,r,n,a){ctx.beginPath();for(let i=0;i<n;i++){let q=a+i*Math.PI*2/n,X=x+Math.cos(q)*r,Y=y+Math.sin(q)*r;i?ctx.lineTo(X,Y):ctx.moveTo(X,Y)}ctx.closePath()}
function draw(){let w=canvas.clientWidth,h=canvas.clientHeight,x=w/2,y=h/2,o=Math.min(w,h)*.475;ctx.clearRect(0,0,w,h);ctx.strokeStyle='#f4f0e829';ctx.lineWidth=1;ctx.beginPath();ctx.arc(x,y,o,0,Math.PI*2);ctx.stroke();
for(let r=1;r<=3;r++){ctx.strokeStyle=`rgba(244,240,232,${.025+r*.008})`;ctx.beginPath();ctx.arc(x,y,o*r/4,0,Math.PI*2);ctx.stroke()}for(let i=0;i<24;i++){let a=i*Math.PI/12,z=o*(i%6===0?.94:.97);ctx.strokeStyle=i%6===0?'#f4f0e838':'#f4f0e814';ctx.beginPath();ctx.moveTo(x+Math.cos(a)*z,y+Math.sin(a)*z);ctx.lineTo(x+Math.cos(a)*o,y+Math.sin(a)*o);ctx.stroke()}
let f=forms[sides],r=o*(.46+pulse*.018);ctx.save();ctx.shadowColor=f.color;ctx.shadowBlur=22+pulse*25;ctx.strokeStyle=f.color;ctx.lineWidth=1.5;poly(x,y,r,sides,angle-Math.PI/2);ctx.stroke();ctx.globalAlpha=.065+pulse*.035;ctx.fillStyle=f.color;ctx.fill();ctx.restore();
for(let i=0;i<sides;i++){let a=angle-Math.PI/2+i*Math.PI*2/sides,X=x+Math.cos(a)*r,Y=y+Math.sin(a)*r;ctx.fillStyle=f.color;ctx.shadowColor=f.color;ctx.shadowBlur=12;ctx.beginPath();ctx.arc(X,Y,3.2,0,Math.PI*2);ctx.fill();ctx.shadowBlur=0}angle+=.0016+pulse*.001;pulse*=.94;requestAnimationFrame(draw)}
function play(f){audio||=new(window.AudioContext||window.webkitAudioContext)();if(audio.state==='suspended')audio.resume();let now=audio.currentTime,master=audio.createGain();master.gain.setValueAtTime(.0001,now);master.gain.exponentialRampToValueAtTime(.15,now+.05);master.gain.exponentialRampToValueAtTime(.0001,now+2.8);master.connect(audio.destination);f.notes.forEach((hz,i)=>{let osc=audio.createOscillator(),gain=audio.createGain(),filter=audio.createBiquadFilter();osc.type=i%2?'sine':'triangle';osc.frequency.value=hz;osc.detune.value=(i-f.notes.length/2)*1.5;filter.type='lowpass';filter.frequency.value=1500+i*140;gain.gain.value=1/Math.sqrt(f.notes.length);osc.connect(filter);filter.connect(gain);gain.connect(master);osc.start(now+i*.022);osc.stop(now+3)});dot.classList.add('on');setTimeout(()=>dot.classList.remove('on'),900)}
function select(n,sound=true){sides=n;let f=forms[n];document.documentElement.style.setProperty('--accent',f.color);document.querySelector('#shape').textContent=f.name;document.querySelector('#chord').textContent=f.chord;buttons.forEach(b=>b.classList.toggle('active',+b.dataset.n===n));pulse=1;if(sound)play(f)}
buttons.forEach(b=>b.addEventListener('click',()=>select(+b.dataset.n)));canvas.addEventListener('click',()=>select(sides));window.addEventListener('resize',fit);fit();draw();
</script></body></html>
"""

components.html(INSTRUMENT, height=850, scrolling=False)
st.markdown("""<style>#MainMenu,header,footer{visibility:hidden}.stApp{background:#090a0a}.block-container{padding:0;max-width:none}iframe{display:block}</style>""", unsafe_allow_html=True)
