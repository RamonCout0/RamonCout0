import urllib.request
import base64

# 1. COLOQUE AQUI OS LINKS DOS SEUS 4 DESENHOS NOVOS
# Lembre-se de usar o link com ?raw=true no final!
assets = {
    "sprite_esq_1": "https://github.com/RamonCout0/RamonCout0/blob/main/img/bailarinaa.gif?raw=true",
    "sprite_esq_2": "https://github.com/RamonCout0/RamonCout0/blob/main/img/nutubus.gif?raw=true",
    "sprite_dir_1": "https://github.com/RamonCout0/RamonCout0/blob/main/img/Sofia.gif?raw=true",
    "sprite_dir_2": "https://github.com/RamonCout0/RamonCout0/blob/main/img/repete.gif?raw=true",
    
    # O link do dev_gif estava cortado no seu, aqui está o link inteiro e consertado:
    "dev_gif": "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGNmc3oyYXN3N2JtbzJ6NnloY3lodm90cTF3eTZsZXE0NmxvcGpiNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/873uvl8mzbfpWofOvF/giphy.gif",
    "linkedin": "https://img.shields.io/badge/LinkedIn-3b82f6?style=for-the-badge&logo=linkedin&logoColor=white",
    "gmail": "https://img.shields.io/badge/Gmail-8b5cf6?style=for-the-badge&logo=gmail&logoColor=white",
    "itchio": "https://img.shields.io/badge/Itch.io-FA5B5B?style=for-the-badge&logo=itch.io&logoColor=white",
    "instagram": "https://img.shields.io/badge/Instagram-d946ef?style=for-the-badge&logo=instagram&logoColor=white",
    "godot": "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Godot-Dark.svg",
    "csharp": "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/CS.svg",
    "cpp": "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/CPP.svg",
    "c": "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/C.svg",
    "aseprite": "https://github.com/RamonCout0/RamonCout0/blob/main/img/ase128.png?raw=true",
    "python": "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Python-Dark.svg",
    "discordbots": "https://raw.githubusercontent.com/BlueNyang/custom-skill-icons/master/icons/DiscordBots.svg",
    "django": "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Django.svg",
    "figma": "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Figma-Dark.svg",
    "git": "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Git.svg",
    "java": "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Java-Dark.svg",
    "pytorch": "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/PyTorch-Dark.svg",
    "lua": "https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Lua-Dark.svg"
}

b64_assets = {}

print("⏳ Baixando e convertendo as imagens para Base64...")
for name, url in assets.items():
    if url.startswith("SUA_IMAGEM"):
        print(f"⚠️ Atenção: Você esqueceu de colocar o link real para {name}")
        b64_assets[name] = ""
        continue
        
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            content_type = response.headers.get('Content-Type', '')
            data = response.read()
            b64_str = base64.b64encode(data).decode('utf-8')
            
            if "svg" in url or "svg" in content_type:
                mime = "image/svg+xml"
            elif "gif" in url or "gif" in content_type:
                mime = "image/gif"
            else:
                mime = "image/png"
                
            b64_assets[name] = f"data:{mime};base64,{b64_str}"
            print(f"✅ {name} convertido!")
    except Exception as e:
        print(f"❌ Erro ao baixar {name}: {e}")
        b64_assets[name] = ""

# HTML e CSS Atualizados
svg_template = f"""<svg fill="none" viewBox="0 0 850 820" width="850" height="820" xmlns="http://www.w3.org/2000/svg">
  <foreignObject width="100%" height="100%">
    <div xmlns="http://www.w3.org/1999/xhtml">
      <style>
        .container {{
          width: 846px;
          height: 816px;
          background: linear-gradient(145deg, #090d16 0%, #1e1b4b 40%, #311042 75%, #090d16 100%);
          border: 2px solid #a855f7;
          border-radius: 20px;
          box-shadow: 0 0 40px rgba(147, 51, 234, 0.4);
          font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
          color: #f1f5f9;
          padding: 30px;
          box-sizing: border-box;
          display: table;
          overflow: hidden;
        }}
        .side-panel {{
          display: table-cell;
          vertical-align: middle;
          width: 90px;
          text-align: center;
        }}
        .main-content {{
          display: table-cell;
          vertical-align: top;
          width: 606px;
          text-align: center;
          padding: 10px 20px;
        }}
        /* A MAGIA PARA SPRITES DE RESOLUÇÕES DIFERENTES */
        .side-sprite {{
          width: 70px;
          height: 70px;
          object-fit: contain; /* Encaixa sem distorcer */
          margin: 40px auto;
          display: block;
          filter: drop-shadow(0 0 8px rgba(168, 85, 247, 0.5));
        }}
        .header-title {{
          font-size: 32px;
          font-weight: 800;
          margin: 0 0 8px 0;
          background: linear-gradient(90deg, #38bdf8, #c084fc, #f472b6);
          -webkit-background-clip: text;
          -webkit-text-fill-color: transparent;
        }}
        .header-welcome {{
          font-size: 18px;
          color: #94a3b8;
          margin: 0 0 15px 0;
          font-weight: 500;
        }}
        .roles {{
          font-size: 16px;
          font-weight: 600;
          color: #cbd5e1;
          margin: 0 0 6px 0;
        }}
        .studio {{
          font-size: 14px;
          color: #f472b6;
          font-weight: 600;
          margin: 0 0 24px 0;
          letter-spacing: 1px;
          text-transform: uppercase;
        }}
        .divider {{
          height: 1px;
          background: linear-gradient(90deg, transparent, #a855f7, transparent);
          margin: 20px auto;
          width: 80%;
        }}
        .quote-container {{
          background: rgba(15, 23, 42, 0.7);
          border-left: 4px solid #38bdf8;
          border-right: 4px solid #a855f7;
          padding: 16px 20px;
          border-radius: 8px;
          margin: 0 auto 24px auto;
          max-width: 560px;
          text-align: left;
        }}
        .quote-phrase {{
          font-size: 13px;
          font-style: italic;
          color: #cbd5e1;
          line-height: 1.6;
          margin: 0;
        }}
        .quote-signature {{
          font-size: 12px;
          color: #38bdf8;
          text-align: right;
          margin: 8px 0 0 0;
          font-weight: 700;
        }}
        .illustration {{
          width: 140px;
          height: auto;
          border-radius: 10px;
          margin: 10px 0 24px 0;
          box-shadow: 0 8px 24px rgba(0,0,0,0.5);
        }}
        .socials {{ margin-bottom: 25px; }}
        .social-btn {{ margin: 0 6px; display: inline-block; }}
        .social-img {{ height: 30px; border-radius: 4px; }}
        .skills-title {{
          font-size: 20px;
          font-weight: 700;
          color: #38bdf8;
          margin: 15px 0 20px 0;
        }}
        .grid-skills {{
          max-width: 560px;
          margin: 0 auto;
          text-align: center;
        }}
        .skill-icon {{
          width: 45px;
          height: 45px;
          margin: 8px;
          display: inline-block;
          filter: drop-shadow(0 4px 6px rgba(0,0,0,0.4));
          transition: transform 0.2s;
        }}
      </style>

      <div class="container">
        <div class="side-panel">
          <img class="side-sprite" src="{b64_assets['sprite_esq_1']}" />
          <img class="side-sprite" src="{b64_assets['sprite_esq_2']}" />
        </div>

        <div class="main-content">
          <div class="header-title">Olá, sou o Ramon Couto!</div>
          <div class="header-welcome">Sejam Bem-vindos(as) ao meu GitHub!</div>
          <div class="roles">Estudante de TADS | Desenvolvedor de Jogos Indie &amp; Aprendiz de CyberSegurança</div>
          <div class="studio">Criador da comunidade Gatuno de Estrelas</div>

          <div class="divider"></div>

          <div class="quote-container">
            <p class="quote-phrase">"A única limitação da sua vida é aquela que você mesmo impõe."</p>
            <p class="quote-phrase" style="margin-top: 8px;">"A nossa ambição faz a gente ir atrás de nossos sonhos, e eu não irei desistir. Enquanto eu tiver com saúde, vamos nos divertir em todos os nossos momentos, e assim criamos histórias da nossa jornada."</p>
            <div class="quote-signature">— Toma gap do ramones</div>
          </div>

          <img class="illustration" src="{b64_assets['dev_gif']}" />

          <div class="socials">
            <a class="social-btn" href="https://www.linkedin.com/in/ramoncout0/"><img class="social-img" src="{b64_assets['linkedin']}" /></a>
            <a class="social-btn" href="mailto:ramon.couto08.s@gmail.com"><img class="social-img" src="{b64_assets['gmail']}" /></a>
            <a class="social-btn" href="https://hajikyouto.itch.io/"><img class="social-img" src="{b64_assets['itchio']}" /></a>
            <a class="social-btn" href="https://www.instagram.com/sun.ch_/"><img class="social-img" src="{b64_assets['instagram']}" /></a>
          </div>

          <div class="divider"></div>

          <div class="skills-title">🛠️ Minhas Habilidades Técnicas</div>
          <div class="grid-skills">
            <img class="skill-icon" src="{b64_assets['godot']}" />
            <img class="skill-icon" src="{b64_assets['csharp']}" />
            <img class="skill-icon" src="{b64_assets['cpp']}" />
            <img class="skill-icon" src="{b64_assets['c']}" />
            <img class="skill-icon" src="{b64_assets['aseprite']}" />
            <img class="skill-icon" src="{b64_assets['python']}" />
            <img class="skill-icon" src="{b64_assets['discordbots']}" />
            <img class="skill-icon" src="{b64_assets['django']}" />
            <img class="skill-icon" src="{b64_assets['figma']}" />
            <img class="skill-icon" src="{b64_assets['git']}" />
            <img class="skill-icon" src="{b64_assets['java']}" />
            <img class="skill-icon" src="{b64_assets['pytorch']}" />
            <img class="skill-icon" src="{b64_assets['lua']}" />
          </div>
        </div>

        <div class="side-panel">
          <img class="side-sprite" src="{b64_assets['sprite_dir_1']}" />
          <img class="side-sprite" src="{b64_assets['sprite_dir_2']}" />
        </div>
      </div>
    </div>
  </foreignObject>
</svg>"""

with open("img/profile-card.svg", "w", encoding="utf-8") as f:
    f.write(svg_template)

print("🚀 SUCESSO! O arquivo profile-card.svg atualizado foi gerado dentro da pasta 'img/'.")