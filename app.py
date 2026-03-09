# ==============================================================================
# DỰ ÁN TRANG WEB QUỐC TẾ PHỤ NỮ 8/3 - TỐI ƯU TRẢI NGHIỆM VÀ ÂM THANH
# ==============================================================================

from flask import Flask, render_template_string, send_file
import os

app = Flask(__name__)

HTML_CONTENT = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Chúc Mừng Ngày 8/3</title>
    
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Great+Vibes&family=Pacifico&display=swap" rel="stylesheet">
    
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }
        body, html { width: 100%; height: 100%; overflow: hidden; background: linear-gradient(-45deg, #ff9a9e, #fecfef, #fbc2eb, #a18cd1, #fad0c4); background-size: 400% 400%; animation: gradientBG 15s ease infinite; font-family: 'Pacifico', cursive; }
        @keyframes gradientBG { 0% { background-position: 0% 50%; } 50% { background-position: 100% 50%; } 100% { background-position: 0% 50%; } }
        #fireworks-canvas { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: 10; pointer-events: none; background: transparent; }
        #music-btn { position: fixed; top: 20px; right: 20px; z-index: 1000; background: rgba(255, 255, 255, 0.4); border: 2px solid #fff; border-radius: 30px; padding: 8px 16px; font-family: 'Pacifico', cursive; font-size: 16px; color: #d81b60; cursor: pointer; box-shadow: 0 4px 15px rgba(0,0,0,0.1); transition: 0.3s; }
        #music-btn:hover { background: rgba(255, 255, 255, 0.8); transform: scale(1.05); }
        .particle { position: fixed; pointer-events: none; z-index: 5; will-change: transform, opacity; }
        .sakura { background-color: #ffb7b2; border-radius: 10px 0 10px 0; box-shadow: 0 0 5px rgba(255, 183, 178, 0.8); }
        #step1-container { position: fixed; top: 0; left: 0; width: 100%; height: 100%; display: flex; flex-direction: column; justify-content: center; align-items: center; z-index: 100; transition: opacity 1s ease, visibility 1s; }
        .envelope-wrapper { position: relative; width: 320px; height: 200px; cursor: pointer; animation: floatEnvelope 3s ease-in-out infinite; transform-style: preserve-3d; }
        @keyframes floatEnvelope { 0%, 100% { transform: translateY(0); filter: drop-shadow(0 10px 15px rgba(0,0,0,0.2)); } 50% { transform: translateY(-15px); filter: drop-shadow(0 20px 20px rgba(0,0,0,0.15)); } }
        .env-back { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: #c62828; border-radius: 10px; z-index: 1; }
        .letter { position: absolute; bottom: 5px; left: 5%; width: 90%; height: 190px; background: #fff; border-radius: 10px; z-index: 2; box-shadow: 0 0 10px rgba(0,0,0,0.1); display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 15px; text-align: center; transition: transform 1s cubic-bezier(0.25, 1, 0.5, 1) 0.5s, z-index 0s linear 1s; }
        .env-front { position: absolute; bottom: 0; left: 0; width: 100%; height: 100%; z-index: 3; pointer-events: none; }
        .env-front::before { content: ''; position: absolute; bottom: 0; left: 0; border-left: 160px solid #e53935; border-top: 100px solid transparent; border-bottom: 100px solid #e53935; border-radius: 0 0 0 10px; }
        .env-front::after { content: ''; position: absolute; bottom: 0; right: 0; border-right: 160px solid #e53935; border-top: 100px solid transparent; border-bottom: 100px solid #e53935; border-radius: 0 0 10px 0; }
        .env-flap { position: absolute; top: 0; left: 0; width: 100%; height: 110px; background: #ef5350; clip-path: polygon(0 0, 100% 0, 50% 100%); z-index: 4; transform-origin: top; transition: transform 0.6s ease; pointer-events: none; }
        .envelope-wrapper.open { animation: none; transform: translateY(50px); cursor: default; }
        .envelope-wrapper.open .env-flap { transform: rotateX(180deg); z-index: 1; }
        .envelope-wrapper.open .letter { transform: translateY(-160px); z-index: 5; }
        .click-text { margin-top: 40px; color: #fff; font-size: 24px; text-shadow: 0 2px 4px rgba(0,0,0,0.4); animation: pulseText 1.5s infinite; }
        @keyframes pulseText { 0%, 100% {opacity: 0.6; transform: scale(1);} 50% {opacity: 1; transform: scale(1.1);} }
        .letter h2 { font-family: 'Dancing Script', cursive; font-size: 24px; color: #d81b60; margin-bottom: 5px; }
        .letter p { font-family: 'Pacifico', cursive; font-size: 14px; color: #555; margin-bottom: 15px; }
        .letter input { font-family: 'Pacifico', cursive; font-size: 16px; text-align: center; width: 90%; padding: 8px; border: 2px solid #f8bbd0; border-radius: 20px; outline: none; margin-bottom: 15px; }
        .letter input:focus { border-color: #ff4081; box-shadow: 0 0 8px rgba(255, 64, 129, 0.5); }
        .letter button { background: linear-gradient(45deg, #d81b60, #ff4081); color: white; border: none; padding: 8px 30px; border-radius: 20px; font-size: 18px; font-family: 'Dancing Script', cursive; cursor: pointer; box-shadow: 0 4px 10px rgba(216, 27, 96, 0.4); transition: 0.3s; }
        .letter button:hover { transform: scale(1.1); }
        #step2-container { position: fixed; top: 0; left: 0; width: 100%; height: 100%; display: none; flex-direction: column; justify-content: center; align-items: center; z-index: 90; opacity: 0; transition: opacity 2s ease; }
        .heart-wrapper { position: relative; width: 350px; height: 350px; display: flex; justify-content: center; align-items: center; }
        .svg-heart { position: absolute; width: 100%; height: 100%; overflow: visible; filter: drop-shadow(0 0 15px rgba(255, 64, 129, 0.8)); }
        .heart-path { fill: none; stroke-width: 2; stroke: url(#gradientHeart); }
        .heartbeat-active { animation: realHeartbeat 1.2s infinite; }
        @keyframes realHeartbeat { 0% { transform: scale(1); filter: drop-shadow(0 0 15px rgba(255, 64, 129, 0.8)); } 15% { transform: scale(1.1); filter: drop-shadow(0 0 25px rgba(255, 64, 129, 1)); } 30% { transform: scale(1); filter: drop-shadow(0 0 15px rgba(255, 64, 129, 0.8)); } 45% { transform: scale(1.1); filter: drop-shadow(0 0 25px rgba(255, 64, 129, 1)); } 60% { transform: scale(1); filter: drop-shadow(0 0 15px rgba(255, 64, 129, 0.8)); } 100% { transform: scale(1); filter: drop-shadow(0 0 15px rgba(255, 64, 129, 0.8)); } }
        .final-name { font-family: 'Great Vibes', cursive; font-size: 65px; color: #fff; text-shadow: 0 0 10px #ff4081, 0 0 20px #d81b60; z-index: 2; opacity: 0; transition: opacity 1s ease; text-align: center; line-height: 1; margin-top: -20px; }
        .final-message { font-family: 'Dancing Script', cursive; font-size: 32px; color: #fff; text-shadow: 2px 2px 5px rgba(216, 27, 96, 0.8); margin-top: 30px; text-align: center; padding: 0 20px; opacity: 0; transition: opacity 1s ease; }
    </style>
</head>
<body>

    <audio id="bg-music" loop>
        <source src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Satie_-_Gymnop%C3%A9die_No._1.ogg" type="audio/ogg">
    </audio>
    
    <audio id="custom-heartbeat-music" loop>
        <source src="/audio" type="audio/mpeg">
    </audio>

    <button id="music-btn">Bật nhạc 🎵</button>

    <canvas id="fireworks-canvas"></canvas>

    <div id="step1-container">
        <div class="envelope-wrapper" id="envelope">
            <div class="env-back"></div>
            
            <div class="letter" id="letter-card">
                <h2>Chúc mừng Ngày 8/3!</h2>
                <p>Hãy nhập tên của bạn</p>
                <input type="text" id="user-name-input" placeholder="Nhập tên của bạn..." autocomplete="off">
                <button id="btn-ok">Xác nhận</button>
            </div>
            
            <div class="env-front"></div>
            <div class="env-flap"></div>
        </div>
        <div class="click-text" id="click-hint">Nhấn vào để mở thư</div>
    </div>

    <div id="step2-container">
        <div class="heart-wrapper" id="heart-wrapper">
            <svg class="svg-heart" viewBox="0 0 100 100" preserveAspectRatio="xMidYMid meet">
                <defs>
                    <linearGradient id="gradientHeart" x1="0%" y1="0%" x2="100%" y2="100%">
                        <stop offset="0%" stop-color="#ff4081">
                            <animate attributeName="stop-color" values="#ff4081;#ea80fc;#ff5252;#ff4081" dur="4s" repeatCount="indefinite" />
                        </stop>
                        <stop offset="100%" stop-color="#ea80fc">
                            <animate attributeName="stop-color" values="#ea80fc;#ff5252;#ff4081;#ea80fc" dur="4s" repeatCount="indefinite" />
                        </stop>
                    </linearGradient>
                </defs>
                <path id="heart-path" class="heart-path" d="M50,85 C20,55 10,40 10,25 C10,12 22,5 35,5 C43,5 47,10 50,15 C53,10 57,5 65,5 C78,5 90,12 90,25 C90,40 80,55 50,85 Z" />
            </svg>
            <div class="final-name" id="final-name">Tên</div>
        </div>
        <div class="final-message" id="final-message">Chúc bạn luôn xinh đẹp, hạnh phúc và tràn đầy yêu thương. ❤️</div>
    </div>

    <script>
        const AudioSys = (() => {
            let ctx = null;
            const init = () => { if (!ctx) ctx = new (window.AudioContext || window.webkitAudioContext)(); };
            
            return {
                init,
                playPop: () => {
                    if (!ctx) return;
                    const osc = ctx.createOscillator(); const gain = ctx.createGain();
                    osc.type = 'sine'; osc.frequency.setValueAtTime(300, ctx.currentTime);
                    osc.frequency.exponentialRampToValueAtTime(800, ctx.currentTime + 0.5);
                    gain.gain.setValueAtTime(0, ctx.currentTime);
                    gain.gain.linearRampToValueAtTime(0.5, ctx.currentTime + 0.1);
                    gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.5);
                    osc.connect(gain); gain.connect(ctx.destination);
                    osc.start(); osc.stop(ctx.currentTime + 0.5);
                },
                playSparkle: () => {
                    if (!ctx) return;
                    for(let i=0; i<8; i++) {
                        setTimeout(() => {
                            const osc = ctx.createOscillator(); const gain = ctx.createGain();
                            osc.type = 'triangle'; osc.frequency.value = 1000 + Math.random() * 2000;
                            gain.gain.setValueAtTime(0.2, ctx.currentTime);
                            gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.2);
                            osc.connect(gain); gain.connect(ctx.destination);
                            osc.start(); osc.stop(ctx.currentTime + 0.2);
                        }, i * 50);
                    }
                },
                playFirework: () => {
                    if (!ctx) return;
                    const osc = ctx.createOscillator(); const gain = ctx.createGain();
                    osc.type = 'square'; osc.frequency.setValueAtTime(150, ctx.currentTime);
                    osc.frequency.exponentialRampToValueAtTime(40, ctx.currentTime + 0.6);
                    gain.gain.setValueAtTime(0.3, ctx.currentTime);
                    gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.6);
                    osc.connect(gain); gain.connect(ctx.destination);
                    osc.start(); osc.stop(ctx.currentTime + 0.6);
                }
            };
        })();

        // ==========================================
        // HÀM XỬ LÝ NHẠC MỜ DẦN / RÕ DẦN
        // ==========================================
        function fadeOutAudio(audio, duration) {
            if (!audio || audio.paused) return;
            let vol = audio.volume;
            const step = vol / (duration / 50);
            const fadeOut = setInterval(() => {
                if (vol - step > 0) {
                    vol -= step;
                    audio.volume = vol;
                } else {
                    clearInterval(fadeOut);
                    audio.volume = 0;
                    audio.pause();
                }
            }, 50);
        }

        function fadeInAudio(audio, duration) {
            audio.volume = 0;
            audio.play().catch(e => console.log("Lỗi phát nhạc:", e));
            let vol = 0;
            const step = 1 / (duration / 50);
            const fadeIn = setInterval(() => {
                if (vol + step < 1) {
                    vol += step;
                    audio.volume = vol;
                } else {
                    clearInterval(fadeIn);
                    audio.volume = 1;
                }
            }, 50);
        }

        let musicPlaying = false;
        const bgMusic = document.getElementById('bg-music');
        const customHeartbeatMusic = document.getElementById('custom-heartbeat-music'); 
        const musicBtn = document.getElementById('music-btn');
        
        musicBtn.addEventListener('click', () => {
            AudioSys.init();
            if(musicPlaying) { 
                fadeOutAudio(bgMusic, 500);
                fadeOutAudio(customHeartbeatMusic, 500);
                musicBtn.innerText = "Bật nhạc 🎵"; 
            }
            else { 
                bgMusic.volume = 1;
                bgMusic.play(); 
                musicBtn.innerText = "Tắt nhạc 🔇"; 
            }
            musicPlaying = !musicPlaying;
        });

        function spawnParticle(type) {
            const el = document.createElement('div');
            el.className = `particle ${type}`;
            el.style.left = Math.random() * 100 + 'vw';
            
            if (type === 'sakura') {
                const size = Math.random() * 10 + 8 + 'px';
                el.style.width = size; el.style.height = size;
                el.style.top = '-20px';
                const duration = Math.random() * 5 + 5;
                el.style.transition = `transform ${duration}s linear, opacity ${duration}s`;
                document.body.appendChild(el);
                
                el.getBoundingClientRect();
                el.style.transform = `translate(${Math.random()*200-100}px, 110vh) rotate(${Math.random()*720}deg)`;
                el.style.opacity = '0';
                setTimeout(() => el.remove(), duration * 1000);
            } else if (type === 'heart') {
                el.innerHTML = '❤️';
                el.style.fontSize = Math.random() * 15 + 15 + 'px';
                el.style.bottom = '-30px';
                const duration = Math.random() * 4 + 4;
                el.style.transition = `transform ${duration}s ease-in, opacity ${duration}s`;
                document.body.appendChild(el);
                
                el.getBoundingClientRect();
                el.style.transform = `translate(${Math.random()*100-50}px, -110vh) scale(1.5)`;
                el.style.opacity = '0';
                setTimeout(() => el.remove(), duration * 1000);
            }
        }
        setInterval(() => spawnParticle('sakura'), 400);
        setInterval(() => spawnParticle('heart'), 800);

        const canvas = document.getElementById('fireworks-canvas');
        const ctxCanvas = canvas.getContext('2d');
        let particles = [];
        const colors = ['#ff4081', '#ea80fc', '#fff', '#ffff8d', '#ffb7b2'];

        function resizeCanvas() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
        window.addEventListener('resize', resizeCanvas); resizeCanvas();

        class Firework {
            constructor(x, y) {
                this.x = x; this.y = y;
                this.color = colors[Math.floor(Math.random() * colors.length)];
                this.radius = Math.random() * 2 + 1;
                const angle = Math.random() * Math.PI * 2;
                const speed = Math.random() * 8 + 2;
                this.vx = Math.cos(angle) * speed; this.vy = Math.sin(angle) * speed;
                this.alpha = 1; this.decay = Math.random() * 0.02 + 0.01;
            }
            update() {
                this.vx *= 0.96; this.vy *= 0.96; this.vy += 0.1; 
                this.x += this.vx; this.y += this.vy; this.alpha -= this.decay;
            }
            draw() {
                ctxCanvas.globalAlpha = this.alpha; ctxCanvas.beginPath();
                ctxCanvas.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                ctxCanvas.fillStyle = this.color; ctxCanvas.fill();
            }
        }

        function explode(x, y) {
            for(let i=0; i<80; i++) particles.push(new Firework(x, y));
            AudioSys.playFirework();
        }

        function animateCanvas() {
            ctxCanvas.clearRect(0, 0, canvas.width, canvas.height);
            particles = particles.filter(p => p.alpha > 0);
            particles.forEach(p => { p.update(); p.draw(); });
            requestAnimationFrame(animateCanvas);
        }
        animateCanvas();

        document.addEventListener('DOMContentLoaded', () => {
            const envelope = document.getElementById('envelope');
            const btnOk = document.getElementById('btn-ok');
            const inputName = document.getElementById('user-name-input');
            const step1 = document.getElementById('step1-container');
            const step2 = document.getElementById('step2-container');
            const heartPath = document.getElementById('heart-path');
            
            let envelopeOpened = false;

            envelope.addEventListener('click', (e) => {
                if(e.target.tagName === 'INPUT' || e.target.tagName === 'BUTTON') return;
                if(!envelopeOpened) {
                    AudioSys.init(); AudioSys.playPop();
                    envelope.classList.add('open');
                    document.getElementById('click-hint').style.display = 'none';
                    envelopeOpened = true;
                    if(!musicPlaying) { bgMusic.play().catch(e=>{}); musicBtn.innerText = "Tắt nhạc 🔇"; musicPlaying = true; }
                    
                    // CẬP NHẬT MỚI: Tự động trỏ chuột vào ô nhập tên sau khi thư kéo lên (1 giây)
                    setTimeout(() => {
                        inputName.focus();
                    }, 1000); 
                }
            });

            btnOk.addEventListener('click', (e) => {
                e.stopPropagation();
                const name = inputName.value.trim() || "Người Phụ Nữ Xinh Đẹp";
                document.getElementById('final-name').innerText = name;
                
                AudioSys.playSparkle();
                explode(window.innerWidth/2, window.innerHeight/2);
                
                // CẬP NHẬT MỚI: Tắt từ từ nhạc nền piano (trong 2 giây) 
                // và từ từ bật nhạc mp3 ở ổ D lên (trong 4 giây)
                fadeOutAudio(bgMusic, 2000);
                fadeInAudio(customHeartbeatMusic, 4000);

                step1.style.opacity = '0';
                setTimeout(() => {
                    step1.style.display = 'none';
                    step2.style.display = 'flex';
                    
                    setTimeout(() => {
                        step2.style.opacity = '1';
                        
                        const length = heartPath.getTotalLength();
                        heartPath.style.strokeDasharray = length;
                        heartPath.style.strokeDashoffset = length;
                        
                        let start = null;
                        const duration = 3000;
                        function drawHeartAnim(timestamp) {
                            if (!start) start = timestamp;
                            const progress = timestamp - start;
                            const percentage = Math.min(progress / duration, 1);
                            heartPath.style.strokeDashoffset = length * (1 - percentage);
                            if (progress < duration) {
                                requestAnimationFrame(drawHeartAnim);
                            } else {
                                document.getElementById('final-name').style.opacity = '1';
                                document.getElementById('final-message').style.opacity = '1';
                                
                                const heartWrapper = document.getElementById('heart-wrapper');
                                heartWrapper.classList.add('heartbeat-active');
                            }
                        }
                        requestAnimationFrame(drawHeartAnim);
                        
                        setInterval(() => {
                            if(Math.random() > 0.6) {
                                explode(Math.random() * window.innerWidth, Math.random() * window.innerHeight * 0.6);
                            }
                        }, 1200);

                    }, 100);
                }, 1000);
            });
            
            // Cho phép ấn Enter để submit thay vì phải ấn nút OK
            inputName.addEventListener("keypress", function(event) {
                if (event.key === "Enter") {
                    event.preventDefault();
                    btnOk.click();
                }
            });
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_CONTENT)

@app.route('/audio')
def play_audio():
    audio_path = r"D:\1.mp3" 
    if os.path.exists(audio_path):
        return send_file(audio_path, mimetype="audio/mpeg")
    else:
        return "Không tìm thấy file mp3 tại ổ D", 404

if __name__ == '__main__':
    print("🚀 Server đang khởi chạy...")
    print("👉 Mở trình duyệt và truy cập: http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000)