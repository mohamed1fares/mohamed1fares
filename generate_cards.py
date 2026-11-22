import os
import xml.etree.ElementTree as ET
import textwrap
import html

os.makedirs('assets', exist_ok=True)

def safe_wrap(text, width):
    lines = textwrap.wrap(text, width=width)
    return [html.escape(l) for l in lines]

# -----------------------------------------------------------------
# 1. ACHIEVEMENT CARD: Huawei ICT 3rd in Africa & VulnCraft
# -----------------------------------------------------------------
def generate_achievement():
    for mode, bg, surface, border, text_pri, text_sec, trophy_col in [
        ('dark', '#0D1117', '#161B22', '#30363D', '#E6EDF3', '#8B949E', '#F59E0B'),
        ('light', '#FFFFFF', '#F8FAFC', '#E2E8F0', '#0F172A', '#64748B', '#D97706')
    ]:
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 140" width="100%" height="100%">
  <defs>
    <linearGradient id="achieveGrad_{mode}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{surface}" />
      <stop offset="50%" stop-color="{bg}" />
      <stop offset="100%" stop-color="{surface}" />
    </linearGradient>

    <linearGradient id="achieveLaser_{mode}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{trophy_col}" stop-opacity="0" />
      <stop offset="50%" stop-color="{trophy_col}" stop-opacity="1" />
      <stop offset="100%" stop-color="#DD0031" stop-opacity="0" />
    </linearGradient>

    <filter id="achieveShadow_{mode}" x="-3%" y="-4%" width="106%" height="114%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="{'0.35' if mode=='dark' else '0.07'}" />
    </filter>
  </defs>

  <rect x="2" y="2" width="896" height="136" rx="14" fill="url(#achieveGrad_{mode})" stroke="{border}" stroke-width="1.5" filter="url(#achieveShadow_{mode})" />

  <!-- Animated Laser Perimeter Highlight -->
  <rect x="2" y="2" width="896" height="136" rx="14" fill="none" stroke="url(#achieveLaser_{mode})" stroke-width="2" stroke-dasharray="100 500" stroke-dashoffset="0">
    <animate attributeName="stroke-dashoffset" values="0;-1200" dur="6s" repeatCount="indefinite" />
  </rect>

  <!-- Accent bar left with animated glow -->
  <path d="M 4 16 Q 4 4 16 4 L 18 4 L 18 136 L 16 136 Q 4 136 4 124 Z" fill="#DD0031">
    <animate attributeName="opacity" values="0.8;1;0.8" dur="2s" repeatCount="indefinite" />
  </path>

  <!-- Trophy Icon with Glowing Ring -->
  <g transform="translate(34, 30)">
    <circle cx="36" cy="36" r="32" fill="{trophy_col}" fill-opacity="0.12" stroke="{trophy_col}" stroke-width="1.2">
      <animate attributeName="r" values="30;36;30" dur="2.5s" repeatCount="indefinite" />
      <animate attributeName="stroke-opacity" values="0.4;1;0.4" dur="2.5s" repeatCount="indefinite" />
    </circle>
    
    <path d="M 26 22 L 46 22 L 46 32 C 46 38 42 44 36 44 C 30 44 26 38 26 32 Z" fill="{trophy_col}" />
    <path d="M 22 24 C 18 24 17 28 19 32 C 21 36 26 38 26 38" stroke="{trophy_col}" stroke-width="2.5" fill="none" stroke-linecap="round" />
    <path d="M 50 24 C 54 24 55 28 53 32 C 51 36 46 38 46 38" stroke="{trophy_col}" stroke-width="2.5" fill="none" stroke-linecap="round" />
    <line x1="36" y1="44" x2="36" y2="52" stroke="{trophy_col}" stroke-width="3" stroke-linecap="round" />
    <line x1="28" y1="52" x2="44" y2="52" stroke="{trophy_col}" stroke-width="3" stroke-linecap="round" />
    
    <polygon points="36,12 38,18 44,18 39,21 41,27 36,23 31,27 33,21 28,18 34,18" fill="#FFFFFF">
      <animate attributeName="opacity" values="0.3;1;0.3" dur="1.8s" repeatCount="indefinite" />
    </polygon>
  </g>

  <!-- Content Center -->
  <g transform="translate(120, 26)">
    <rect x="0" y="0" width="180" height="20" rx="10" fill="{trophy_col}" fill-opacity="0.15" stroke="{trophy_col}" stroke-width="0.8" />
    <text x="90" y="14" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="10.5" fill="{trophy_col}">CONTINENTAL RECOGNITION</text>

    <text x="0" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="800" font-size="19" fill="{text_pri}">Huawei ICT Competition 2025 • 3rd Place in Africa</text>
    <text x="0" y="66" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="13" fill="#22D3EE">Co-Founder &amp; Platform Architect at VulnCraft (vulncraft.software)</text>
    <text x="0" y="86" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="400" font-size="12" fill="{text_sec}">Awarded for excellence in enterprise distributed architecture, automated threat scanning, and cloud scalability.</text>
  </g>

  <!-- Right Emblem Badge -->
  <g transform="translate(768, 28)">
    <rect x="0" y="0" width="102" height="84" rx="10" fill="{surface}" stroke="{border}" stroke-width="1.2" />
    <circle cx="51" cy="24" r="14" fill="{trophy_col}" fill-opacity="0.15" />
    <text x="51" y="29" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="800" font-size="14" fill="{trophy_col}">#3</text>
    <text x="51" y="52" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="800" font-size="11.5" fill="{text_pri}">AFRICA</text>
    <text x="51" y="68" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="600" font-size="9.5" fill="{text_sec}">HUAWEI 2025</text>
  </g>
</svg>"""
        ET.fromstring(svg)
        with open(f"assets/achievement-{mode}.svg", "w") as f:
            f.write(svg)
    print("Generated Achievement SVGs")

# -----------------------------------------------------------------
# 2. MEAN STACK HIGHLIGHT: MongoDB, Express, Angular 20, Node.js
# -----------------------------------------------------------------
def generate_mean_stack():
    cards = [
        {
            "letter": "M",
            "name": "MongoDB",
            "color": "#10AA50",
            "sub": "Mongoose & Pipelines",
            "desc": "Document modeling, high-throughput aggregation pipelines, indexing & performance tuning."
        },
        {
            "letter": "E",
            "name": "Express.js",
            "color": "#6366F1",
            "sub": "REST & Middleware",
            "desc": "Robust API design, JWT auth, granular RBAC guards, rate-limiting & secure routing."
        },
        {
            "letter": "A",
            "name": "Angular 20",
            "color": "#DD0031",
            "sub": "Standalone & Signals",
            "desc": "Reactive state architecture with RxJS, Signals, Tailwind/Bootstrap UI & lazy modules."
        },
        {
            "letter": "N",
            "name": "Node.js",
            "color": "#5FA04E",
            "sub": "Async Runtime",
            "desc": "Event-driven microservices, background job workers, webhooks & WhatsApp Business API."
        }
    ]

    for mode, bg, surface, border, text_pri, text_sec in [
        ('dark', '#0D1117', '#161B22', '#30363D', '#E6EDF3', '#8B949E'),
        ('light', '#FFFFFF', '#F8FAFC', '#E2E8F0', '#0F172A', '#64748B')
    ]:
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 165" width="100%" height="100%">
  <defs>
    <filter id="meanShadow_{mode}" x="-6%" y="-6%" width="112%" height="116%">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#000000" flood-opacity="{'0.3' if mode=='dark' else '0.08'}" />
    </filter>
  </defs>
"""
        for i, c in enumerate(cards):
            x = 10 + i * 223
            delay = i * 0.9
            sub_esc = html.escape(c['sub'])
            desc_lines = safe_wrap(c['desc'], 34)

            desc_svg = ""
            for l_idx, line_text in enumerate(desc_lines[:3]):
                ly = 88 + l_idx * 18
                desc_svg += f'<text x="14" y="{ly}" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, sans-serif" font-weight="400" font-size="11.5" fill="{text_sec}">{line_text}</text>\n    '

            svg += f"""
  <!-- Card {c['name']} -->
  <g transform="translate({x}, 10)">
    <animateTransform attributeName="transform" type="translate" values="{x},10; {x},6; {x},10" dur="4.5s" begin="{delay}s" repeatCount="indefinite" />
    <rect x="0" y="0" width="212" height="145" rx="12" fill="{surface}" stroke="{border}" stroke-width="1.5" filter="url(#meanShadow_{mode})" />
    
    <path d="M 0 12 Q 0 0 12 0 L 200 0 Q 212 0 212 12 L 212 16 L 0 16 Z" fill="{c['color']}">
      <animate attributeName="opacity" values="0.7;1;0.7" dur="2.5s" repeatCount="indefinite" />
    </path>
    
    <circle cx="34" cy="46" r="18" fill="{c['color']}" fill-opacity="0.18" stroke="{c['color']}" stroke-width="1.5">
      <animate attributeName="stroke-opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite" />
    </circle>
    <text x="34" y="53" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="900" font-size="18" fill="{c['color']}">{c['letter']}</text>
    
    <text x="62" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="15" fill="{text_pri}">{c['name']}</text>
    <text x="62" y="58" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="600" font-size="11" fill="{c['color']}">{sub_esc}</text>
    
    {desc_svg}
  </g>"""
        svg += "\n</svg>"
        ET.fromstring(svg)
        with open(f"assets/mean-stack-{mode}.svg", "w") as f:
            f.write(svg)
    print("Generated MEAN Stack SVGs")

# -----------------------------------------------------------------
# 3. TECH STACK: Grouped (Frontend, Backend, Databases, Tools)
# -----------------------------------------------------------------
def generate_tech_stack():
    groups = [
        {
            "title": "Frontend Engineering",
            "color": "#DD0031",
            "skills": [("Angular 20", "#DD0031"), ("TypeScript", "#3178C6"), ("RxJS", "#B7178C"), ("Tailwind CSS", "#06B6D4"), ("Bootstrap", "#7952B3"), ("HTML5 / CSS3", "#E34F26")]
        },
        {
            "title": "Backend & Cloud APIs",
            "color": "#6366F1",
            "skills": [("Node.js", "#5FA04E"), ("Express.js", "#6366F1"), ("FastAPI", "#059669"), ("Python", "#3776AB"), ("JWT / RBAC", "#F59E0B"), ("RESTful APIs", "#22D3EE")]
        },
        {
            "title": "Databases & Storage",
            "color": "#10B981",
            "skills": [("PostgreSQL", "#4169E1"), ("Supabase", "#3ECF8E"), ("MongoDB", "#10AA50"), ("Mongoose", "#880000"), ("Data Modeling", "#64748B"), ("Aggregation", "#F59E0B")]
        },
        {
            "title": "DevOps, Automation & Tools",
            "color": "#22D3EE",
            "skills": [("Git & GitHub", "#F05032"), ("n8n Automation", "#FF6584"), ("WhatsApp API", "#25D366"), ("Vercel", "#000000"), ("Postman", "#FF6C37"), ("Linux", "#FCC624")]
        }
    ]

    for mode, bg, surface, border, text_pri, text_sec in [
        ('dark', '#0D1117', '#161B22', '#30363D', '#E6EDF3', '#8B949E'),
        ('light', '#FFFFFF', '#F8FAFC', '#E2E8F0', '#0F172A', '#64748B')
    ]:
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 290" width="100%" height="100%">
  <defs>
    <filter id="techShadow_{mode}" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="{'0.25' if mode=='dark' else '0.06'}" />
    </filter>
  </defs>
"""
        for idx, grp in enumerate(groups):
            gx = 10 if idx % 2 == 0 else 460
            gy = 10 if idx < 2 else 150
            delay = idx * 0.7
            title_esc = html.escape(grp['title'])

            svg += f"""
  <!-- {title_esc} -->
  <g transform="translate({gx}, {gy})">
    <animateTransform attributeName="transform" type="translate" values="{gx},{gy}; {gx},{gy-2}; {gx},{gy}" dur="4s" begin="{delay}s" repeatCount="indefinite" />
    <rect x="0" y="0" width="430" height="128" rx="12" fill="{surface}" stroke="{border}" stroke-width="1.5" filter="url(#techShadow_{mode})" />
    
    <path d="M 0 12 Q 0 0 12 0 L 418 0 Q 430 0 430 12 L 430 15 L 0 15 Z" fill="{grp['color']}">
      <animate attributeName="opacity" values="0.7;1;0.7" dur="2.5s" repeatCount="indefinite" />
    </path>

    <circle cx="20" cy="28" r="5" fill="{grp['color']}" />
    <text x="32" y="32" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="14.5" fill="{text_pri}">{title_esc}</text>
    
    <g transform="translate(14, 46)">
"""
            for s_idx, (name, col) in enumerate(grp['skills']):
                row = s_idx // 3
                col_idx = s_idx % 3
                bx = col_idx * 134
                by = row * 36
                name_esc = html.escape(name)
                pill_bg = "#0D1117" if mode == 'dark' else "#FFFFFF"
                svg += f"""      <rect x="{bx}" y="{by}" width="126" height="28" rx="6" fill="{pill_bg}" stroke="{border}" stroke-width="1" />
      <circle cx="{bx + 12}" cy="{by + 14}" r="3.5" fill="{col or text_pri}" />
      <text x="{bx + 22}" y="{by + 18}" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="600" font-size="11" fill="{text_pri}">{name_esc}</text>
"""
            svg += """    </g>
  </g>"""
        svg += "\n</svg>"
        ET.fromstring(svg)
        with open(f"assets/tech-stack-{mode}.svg", "w") as f:
            f.write(svg)
    print("Generated Tech Stack SVGs")

# -----------------------------------------------------------------
# 4. PROJECTS SECTION: 4 Key Projects
# -----------------------------------------------------------------
def generate_projects():
    projects = [
        {
            "num": "01",
            "name": "Clinic Hub",
            "type": "Healthcare Enterprise ERP",
            "impact": "Multi-platform clinic management with automated WhatsApp scheduling & n8n workflows.",
            "stack": ["Angular 20", "Express.js", "PostgreSQL", "Supabase", "WhatsApp API", "n8n"],
            "status": "Private, available on request",
            "color": "#10B981"
        },
        {
            "num": "02",
            "name": "VulnCraft Platform",
            "type": "Automated Scanner Suite",
            "impact": "Automated vulnerability scanner orchestrating FastAPI bridges across 5+ specialized Python tools.",
            "stack": ["Angular 20", "FastAPI", "Python", "MongoDB", "Cybersecurity", "Docker"],
            "status": "Private, available on request (vulncraft.software)",
            "color": "#DD0031"
        },
        {
            "num": "03",
            "name": "Wasel Management",
            "type": "Hypermarket Enterprise ERP",
            "impact": "High-volume platform handling 5,000+ SKU units, 15+ nested categories & aggregation pipelines.",
            "stack": ["Angular", "Node.js", "MongoDB Aggregations", "Express.js", "Tailwind"],
            "status": "Private, available on request",
            "color": "#6366F1"
        },
        {
            "num": "04",
            "name": "DELMA Medical",
            "type": "B2B Medical Procurement",
            "impact": "Comprehensive B2B medical supply procurement engine with JWT auth, granular RBAC & order tracking.",
            "stack": ["Angular", "Node.js", "JWT / RBAC", "Express.js", "MongoDB"],
            "status": "Private, available on request",
            "color": "#22D3EE"
        }
    ]

    for mode, bg, surface, border, text_pri, text_sec in [
        ('dark', '#0D1117', '#161B22', '#30363D', '#E6EDF3', '#8B949E'),
        ('light', '#FFFFFF', '#F8FAFC', '#E2E8F0', '#0F172A', '#64748B')
    ]:
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 500" width="100%" height="100%">
  <defs>
    <filter id="projShadow_{mode}" x="-4%" y="-5%" width="108%" height="114%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="{'0.3' if mode=='dark' else '0.07'}" />
    </filter>
  </defs>
"""
        for idx, p in enumerate(projects):
            gx = 10 if idx % 2 == 0 else 460
            gy = 10 if idx < 2 else 254
            delay = idx * 0.8
            status_esc = html.escape(p['status'])
            pill_bg = "#0D1117" if mode == 'dark' else "#FFFFFF"
            wrapped_impact = safe_wrap(p['impact'], 52)

            impact_svg = ""
            for l_idx, line_text in enumerate(wrapped_impact[:3]):
                ly = 102 + l_idx * 18
                impact_svg += f'<text x="20" y="{ly}" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, sans-serif" font-weight="400" font-size="12.5" fill="{text_sec}">{line_text}</text>\n    '

            svg += f"""
  <!-- Project {p['name']} -->
  <g transform="translate({gx}, {gy})">
    <animateTransform attributeName="transform" type="translate" values="{gx},{gy}; {gx},{gy-3}; {gx},{gy}" dur="5s" begin="{delay}s" repeatCount="indefinite" />
    <rect x="0" y="0" width="430" height="232" rx="14" fill="{surface}" stroke="{border}" stroke-width="1.5" filter="url(#projShadow_{mode})" />
    
    <path d="M 0 14 Q 0 0 14 0 L 416 0 Q 430 0 430 14 L 430 18 L 0 18 Z" fill="{p['color']}">
      <animate attributeName="opacity" values="0.8;1;0.8" dur="3s" repeatCount="indefinite" />
    </path>
    
    <text x="20" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="900" font-size="13" fill="{p['color']}">{p['num']}</text>
    <rect x="42" y="32" width="200" height="18" rx="9" fill="{p['color']}" fill-opacity="0.12" />
    <text x="142" y="45" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="10" fill="{p['color']}">{p['type'].upper()}</text>
    
    <text x="20" y="74" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="800" font-size="20" fill="{text_pri}">{p['name']}</text>
    
    {impact_svg}

    <!-- Stack Tags -->
    <g transform="translate(20, 154)">
"""
            tag_x = 0
            tag_y = 0
            for t in p['stack']:
                width = len(t) * 7 + 16
                if tag_x + width > 390:
                    tag_x = 0
                    tag_y += 24
                t_esc = html.escape(t)
                svg += f"""      <rect x="{tag_x}" y="{tag_y}" width="{width}" height="20" rx="5" fill="{pill_bg}" stroke="{border}" stroke-width="1" />
      <text x="{tag_x + width//2}" y="{tag_y + 14}" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="600" font-size="10.5" fill="{p['color']}">{t_esc}</text>
"""
                tag_x += width + 6

            svg += f"""    </g>

    <g transform="translate(20, 214)">
      <circle cx="5" cy="-4" r="4" fill="{p['color']}">
        <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite" />
      </circle>
      <text x="16" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="500" font-size="11" fill="{text_sec}">🔒 {status_esc}</text>
    </g>
  </g>"""
        svg += "\n</svg>"
        ET.fromstring(svg)
        with open(f"assets/projects-{mode}.svg", "w") as f:
            f.write(svg)
    print("Generated Projects SVGs")

# -----------------------------------------------------------------
# 5. FOOTER & CONTACT CARDS
# -----------------------------------------------------------------
def generate_footer():
    for mode, bg, surface, border, text_pri, text_sec in [
        ('dark', '#0D1117', '#161B22', '#30363D', '#E6EDF3', '#8B949E'),
        ('light', '#FFFFFF', '#F8FAFC', '#E2E8F0', '#0F172A', '#64748B')
    ]:
        laser_color = "#6366F1" if mode == 'dark' else "#4F46E5"
        laser_stop2 = "#22D3EE" if mode == 'dark' else "#0284C7"
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 115" width="100%" height="100%">
  <defs>
    <linearGradient id="footLaser_{mode}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{laser_color}" stop-opacity="0" />
      <stop offset="50%" stop-color="{laser_stop2}" stop-opacity="1" />
      <stop offset="100%" stop-color="#10B981" stop-opacity="0" />
    </linearGradient>
    <filter id="footShadow_{mode}" x="-3%" y="-4%" width="106%" height="114%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="{'0.3' if mode=='dark' else '0.07'}" />
    </filter>
  </defs>

  <rect x="2" y="2" width="896" height="111" rx="14" fill="{surface}" stroke="{border}" stroke-width="1.5" filter="url(#footShadow_{mode})" />

  <!-- Animated Laser Perimeter Highlight -->
  <rect x="2" y="2" width="896" height="111" rx="14" fill="none" stroke="url(#footLaser_{mode})" stroke-width="2" stroke-dasharray="100 500" stroke-dashoffset="0">
    <animate attributeName="stroke-dashoffset" values="0;-1200" dur="6s" repeatCount="indefinite" />
  </rect>

  <text x="32" y="40" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="17" fill="{text_pri}">🤝 Let's Collaborate &amp; Build Something Great</text>
  <text x="32" y="66" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="400" font-size="13" fill="{text_sec}">Open to full-stack engineering roles, high-scale MEAN architectures &amp; security collaborations.</text>
  <text x="32" y="88" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="600" font-size="12" fill="{laser_color}">📍 Giza, Egypt <tspan fill="{text_sec}">• BSc Computer Science (6 October University, June 2026)</tspan></text>

  <!-- Status indicator right -->
  <g transform="translate(670, 38)">
    <rect x="0" y="0" width="195" height="40" rx="20" fill="#10B981" fill-opacity="0.12" stroke="#10B981" stroke-width="1.2" />
    <circle cx="22" cy="20" r="5" fill="#10B981" />
    <circle cx="22" cy="20" r="5" stroke="#10B981" fill="none" stroke-width="1.5">
      <animate attributeName="r" values="5;14" dur="2s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0.8;0" dur="2s" repeatCount="indefinite" />
    </circle>
    <text x="38" y="25" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="12" fill="#10B981">Open for Opportunities</text>
  </g>
</svg>"""
        ET.fromstring(svg)
        with open(f"assets/footer-{mode}.svg", "w") as f:
            f.write(svg)
    print("Generated Footer SVGs")

if __name__ == '__main__':
    generate_achievement()
    generate_mean_stack()
    generate_tech_stack()
    generate_projects()
    generate_footer()
