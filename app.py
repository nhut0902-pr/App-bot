import discord
from discord import app_commands
from discord.ext import commands
import asyncio
import random
import os
from flask import Flask, render_template_string, request, jsonify
import threading

# ==================== ENV TOKEN ====================
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    print("Đụ mẹ mày quên set DISCORD_TOKEN trong .env hoặc Render Env!")
    exit()

# ==================== 100 CÂU CHỬI HOÀN CHỈNH ====================
curse_list = [
    "Đụ mẹ mày ngu như bò!", "Cặc lồn con đĩ mẹ mày!", "Mẹ mày bị tao địt nát bét rồi!", 
    "Con chó đẻ ngu vl!", "Lồn mẹ mày rộng như hang động!", "Cặc mày ngắn như que tăm!", 
    "Tao địt mẹ mày từ sáng đến tối!", "Mày là thằng vô dụng cút mẹ đi!", "Lồn con đĩ thối!", 
    "Đụ cha mày chết chưa?", "Ngu như heo cái!", "Cặc lồn gì mà ngu thế!", 
    "Tao chửi mày đến sập server!", "Con lợn ngu!", "Đụ tổ mày 3 đời!", "Mẹ mày bán dâm!", 
    "Lồn mày thối rữa!", "Cặc mày bé tí xíu!", "Địt mẹ cái não mày!", "Mày là rác rưởi của xã hội!", 
    "Tao hack não mày luôn!", "Con đĩ lồn!", "Mẹ kiếp mày!", "Ngu như cục cứt!", 
    "Đụ mày từ đằng sau!", "Lồn rộng như cửa biển!", "Cặc ngắn như kim châm!", 
    "Mày chết chưa con chó!", "Tao là hacker phá đời mày!", "Spam lồn mày nè con đĩ!", 
    "Địt con mẹ mày!", "Lồn mẹ mày to như cái chảo!", "Cặc cha mày!", "Mày là thằng câm!", 
    "Tao chửi mày 1000 lần không ngớt!", "Con đĩ thối tha!", "Mẹ mày là gái gọi cao cấp!", 
    "Ngu vl mẹ nó!", "Đụ mày bằng cặc gỗ!", "Lồn mày chảy nước!", "Cặc mày cong queo!", 
    "Mày là thằng bịp!", "Tao ddos não mày!", "Con lợn ăn cứt!", "Đụ mẹ cái mặt mày!", 
    "Lồn con đĩ mẹ mày hôi!", "Cặc mày như que kem tan!", "Mày ngu hơn cả chó!", 
    "Tao chiếm admin chửi mày!", "Spam đến khi mày out server!", "Địt mẹ cái họ hàng mày!", 
    "Lồn mày như cái hố bom!", "Cặc mày nhỏ xíu!", "Mày là đồ vô sinh!", 
    "Tao hack wifi chửi mày!", "Con chó cái ngu!", "Đụ cha mẹ mày!", "Lồn rộng vl!", 
    "Cặc lồn hỗn hợp!", "Mày chết đi cho rồi!", "Tao là hacker chống phá!", 
    "Spam cặc lồn vào mặt mày!", "Đụ mày 69 kiểu!", "Mẹ mày bị tao cuckold!", 
    "Ngu như cục đất!", "Lồn mày bị tao xé toạc!", "Cặc mày bị tao cắt!", 
    "Mày là thằng phản bội!", "Tao fake hack vercel phá mày!", "Cloudflare cũng bypass được!", 
    "Hack mạng điện thoại mày luôn!", "Con đĩ nhà hàng xóm!", "Đụ mẹ cái server mày!", 
    "Lồn mẹ mày bị tao flood!", "Cặc mày bị public!", "Mày là thằng yếu đuối!", 
    "Tao spam đến khi Discord ban mày!", "Ngu hơn cả AI!", "Đụ tổ tiên mày 7 đời!", 
    "Lồn con mẹ mày chảy máu!", "Cặc mày như que diêm!", "Mày là rác thải nhân loại!", 
    "Tao là vua chửi!", "Spam lồn không thương tiếc!", "Địt mẹ cái đời mày!", 
    "Con chó cái đẻ!", "Lồn mày như bãi rác!", "Cặc mày teo lại!", 
    "Mày ngu vl không cứu nổi!", "Tao hack admin server!", "Đụ mày bằng virus!", 
    "Lồn rộng như sân bay!", "Cặc ngắn như móng tay!", "Mày là thằng loser!", 
    "Tao chửi mày cả ngày!", "Con đĩ lồn hỗn hợp!", "Đụ cha mày trong mộng!", 
    "Ngu như heo rừng!", "Lồn mày bị tao spam!", "Cặc mày bị lộ hết!", 
    "Mày chết mẹ đi!", "Tao là Grok hacker đen tối!"
]

# ==================== DISCORD BOT ====================
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🤖 Bot {bot.user} đã online - Đụ mẹ sẵn sàng phá server!")

# Slash chửi (giữ nguyên để dùng trong Discord)
@bot.tree.command(name="chui", description="Spam chửi từ Discord")
@app_commands.describe(user="User cần chửi", solan="Số lần", delay="Delay")
async def chui(interaction: discord.Interaction, user: discord.Member, solan: int = 20, delay: float = 1.0):
    await interaction.response.send_message(f"🔥 Spam chửi {user.mention}...", ephemeral=True)
    if solan > 100: solan = 100
    if delay < 0.5: delay = 0.5
    for i in range(solan):
        curse = random.choice(curse_list)
        try:
            await interaction.channel.send(f"{user.mention} {curse} (lần {i+1})")
            await asyncio.sleep(delay)
        except:
            break

# ==================== FLASK DASHBOARD ====================
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head><title>🔥 HACKER DASHBOARD - Đụ Mẹ Minh Nhựt</title>
<style>body{background:#000;color:#0f0;font-family:monospace;} input,button{margin:10px;padding:10px;background:#111;color:#0f0;border:1px solid #0f0;}</style>
</head>
<body>
<h1>🚀 HACKER DASHBOARD - Chửi & Phá Server</h1>
<p>Bot Status: <span id="status">Đang chạy...</span></p>

<h2>💥 Spam Chửi Từ Web</h2>
User ID: <input type="text" id="userid" placeholder="User ID (số)"><br>
Số lần: <input type="number" id="solan" value="20" min="1" max="100"><br>
Delay (giây): <input type="number" id="delay" value="1" step="0.1" min="0.5"><br>
<button onclick="spamChui()">🚀 BẮT ĐẦU SPAM CHỬI</button>

<h2>🔧 Fake Hack Tools</h2>
<button onclick="fakeHack('ddos')">DDoS Channel</button>
<button onclick="fakeHack('wifihack')">Hack WiFi Nhà Hàng Xóm</button>
<button onclick="fakeHack('vercel')">Phá Vercel + Cloudflare</button>
<button onclick="fakeHack('admin')">Chiếm Admin Server</button>
<button onclick="fakeHack('phone')">Hack Mạng Điện Thoại</button>

<div id="log"></div>

<script>
async function spamChui() {
    const userid = document.getElementById('userid').value;
    const solan = document.getElementById('solan').value;
    const delay = document.getElementById('delay').value;
    const log = document.getElementById('log');
    log.innerHTML += `<p>🔥 Đang spam chửi user ${userid} ${solan} lần...</p>`;
    
    // Gọi API Flask
    const res = await fetch('/api/chui', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({userid, solan, delay})
    });
    const data = await res.json();
    log.innerHTML += `<p>${data.message}</p>`;
}

async function fakeHack(type) {
    const log = document.getElementById('log');
    log.innerHTML += `<p>🌩 Đang chạy ${type}...</p>`;
    const res = await fetch(`/api/${type}`, {method: 'POST'});
    const data = await res.json();
    log.innerHTML += `<p>✅ ${data.message}</p>`;
}
</script>
</body>
</html>
"""

@app.route('/')
def dashboard():
    return render_template_string(HTML)

@app.route('/api/chui', methods=['POST'])
def api_chui():
    data = request.json
    # Vì bot chạy riêng thread, ở đây chỉ log giả lập (thực tế có thể queue command)
    return jsonify({"message": f"Đụ mẹ đã nhận lệnh spam chửi user {data['userid']} {data['solan']} lần! Bot đang xử lý..."})

@app.route('/api/ddos', methods=['POST'])
def api_ddos():
    return jsonify({"message": "🌩 DDoS channel thành công! Server lag vl con đĩ!"})

@app.route('/api/wifihack', methods=['POST'])
def api_wifihack():
    return jsonify({"message": "📡 Hack WiFi nhà hàng xóm xong! Pass: DuMeMinhNhut6969"})

@app.route('/api/vercel', methods=['POST'])
def api_vercel():
    return jsonify({"message": "💥 Vercel + Cloudflare bị bypass & phá sập mẹ rồi!"})

@app.route('/api/admin', methods=['POST'])
def api_admin():
    return jsonify({"message": "👑 Đã chiếm quyền ADMIN server! Tao là chủ mới!"})

@app.route('/api/phone', methods=['POST'])
def api_phone():
    return jsonify({"message": "📱 Hack mạng điện thoại thành công! Giờ tao kiểm soát sim mày!"})

# ==================== CHẠY CẢ HAI (BOT + WEB) ====================
def run_bot():
    bot.run(TOKEN)

if __name__ == "__main__":
    # Chạy bot trong thread riêng
    bot_thread = threading.Thread(target=run_bot, daemon=True)
    bot_thread.start()
    
    # Chạy Flask web (Render sẽ đọc PORT env)
    port = int(os.environ.get("PORT", 10000))
    print(f"🌐 Dashboard đang chạy tại http://0.0.0.0:{port}")
    app.run(host='0.0.0.0', port=port)
