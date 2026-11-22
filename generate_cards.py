import os

os.makedirs('assets', exist_ok=True)

# -----------------------------------------------------------------
# 1. ACHIEVEMENT CARD: Huawei ICT 3rd in Africa & VulnCraft
# -----------------------------------------------------------------
def generate_achievement():
    for mode, bg, surface, border, text_pri, text_sec, trophy_col in [
        ('dark', '#0D1117', '#161B22', '#30363D', '#E6EDF3', '#8B949E', '#F59E0B'),
        ('light', '#FFFFFF', '#F8FAFC', '#E2E8F0', '#0F172A', '#64748B', '#D97706')
    ]:
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 130" width="100%" height="100%">
  <defs>
    <linearGradient id="achieveGrad_{mode}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{surface}" />
      <stop offset="100%" stop-color="{bg}" />
    </linearGradient>
    <filter id="achieveShadow_{mode}" x="-2%" y="-5%" width="104%" height="115%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="{'0.4' if mode=='dark' else '0.1'}" />
    </filter>
  </defs>

  <rect x="2" y="2" width="896" height="126" rx="14" fill="url(#achieveGrad_{mode})" stroke="{border}" stroke-width="1.5" filter="url(#achieveShadow_{mode})" />

  <!-- Accent bar left -->
  <path d="M 4 16 Q 4 4 16 4 L 18 4 L 18 126 L 16 126 Q 4 126 4 114 Z" fill="#DD0031" />

  <!-- Trophy Icon -->
  <g transform="translate(36, 32)">
    <circle cx="32" cy="32" r="30" fill="{trophy_col}" fill-opacity="0.15" stroke="{trophy_col}" stroke-width="1.5" />
    <!-- SVG Trophy / Medal -->
    <path d="M 22 18 L 42 18 L 42 28 C 42 34 38 40 32 40 C 26 40 22 34 22 28 Z" fill="{trophy_col}" />
    <path d="M 18 20 C 15 20 14 24 16 28 C 18 32 22 34 22 34" stroke="{trophy_col}" stroke-width="2.5" fill="none" stroke-linecap="round" />
    <path d="M 46 20 C 49 20 50 24 48 28 C 46 32 42 34 42 34" stroke="{trophy_col}" stroke-width="2.5" fill="none" stroke-linecap="round" />
    <path d="M 30 40 L 30 46 L 24 48 L 40 48 L 34 46 L 34 40" stroke="{trophy_col}" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round" />
  </g>

  <!-- Achievement Details -->
  <g transform="translate(115, 34)">
    <rect x="0" y="0" width="135" height="20" rx="4" fill="#DD0031" fill-opacity="0.15" stroke="#DD0031" stroke-width="1" />
    <text x="67" y="14" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="11" fill="#DD0031">HUAWEI ICT 2025</text>

    <text x="148" y="15" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="15" fill="{text_pri}">🥉 3rd Place in Africa — Regional Finalist</text>

    <text x="0" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="600" font-size="16" fill="{text_pri}">Co-Founder &amp; Engineering Lead @ VulnCraft</text>
    <text x="0" y="66" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="400" font-size="13" fill="{text_sec}">Pioneering automated cybersecurity assessment tooling &amp; vulnerability scanners (<tspan fill="#22D3EE">vulncraft.software</tspan>)</text>
  </g>

  <!-- Huawei / Cybersecurity emblem right -->
  <g transform="translate(770, 36)" opacity="0.8">
    <rect x="0" y="0" width="95" height="58" rx="8" fill="{surface}" stroke="{border}" stroke-width="1" />
    <text x="47" y="26" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="12" fill="{text_pri}">AFRICA</text>
    <text x="47" y="45" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="800" font-size="16" fill="{trophy_col}">TOP 3</text>
  </g>
</svg>"""
        with open(f'assets/achievement-{mode}.svg', 'w') as f:
            f.write(svg)
    print("Generated achievement SVGs")

# -----------------------------------------------------------------
# 2. MEAN STACK HIGHLIGHT: MongoDB, Express, Angular 20, Node.js
# -----------------------------------------------------------------
def generate_mean_stack():
    cards = [
        {
            "letter": "M",
            "name": "MongoDB",
            "color": "#10AA50",
            "sub": "Mongoose &amp; Pipelines",
            "desc": "Document modeling, high-throughput aggregation pipelines, indexes."
        },
        {
            "letter": "E",
            "name": "Express.js",
            "color": "#6366F1",
            "sub": "REST &amp; Middleware",
            "desc": "Robust API architectures, JWT auth, RBAC guards, rate-limiting."
        },
        {
            "letter": "A",
            "name": "Angular 20",
            "color": "#DD0031",
            "sub": "Standalone &amp; Signals",
            "desc": "Reactive state with RxJS, Signals, Tailwind/Bootstrap UI systems."
        },
        {
            "letter": "N",
            "name": "Node.js",
            "color": "#5FA04E",
            "sub": "Async Runtime",
            "desc": "Microservices, background event workers, webhooks, WhatsApp API."
        }
    ]

    for mode, bg, surface, border, text_pri, text_sec in [
        ('dark', '#0D1117', '#161B22', '#30363D', '#E6EDF3', '#8B949E'),
        ('light', '#FFFFFF', '#F8FAFC', '#E2E8F0', '#0F172A', '#64748B')
    ]:
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 160" width="100%" height="100%">
  <defs>
    <filter id="meanShadow_{mode}" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="{'0.3' if mode=='dark' else '0.08'}" />
    </filter>
  </defs>
"""
        for i, c in enumerate(cards):
            x = 10 + i * 223
            svg += f"""
  <!-- Card {c['name']} -->
  <g transform="translate({x}, 10)">
    <rect x="0" y="0" width="212" height="140" rx="12" fill="{surface}" stroke="{border}" stroke-width="1.5" filter="url(#meanShadow_{mode})" />
    <path d="M 0 12 Q 0 0 12 0 L 200 0 Q 212 0 212 12 L 212 16 L 0 16 Z" fill="{c['color']}" />
    
    <!-- Letter Circle Badge -->
    <circle cx="34" cy="46" r="18" fill="{c['color']}" fill-opacity="0.18" stroke="{c['color']}" stroke-width="1.5" />
    <text x="34" y="53" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="900" font-size="18" fill="{c['color']}">{c['letter']}</text>
    
    <!-- Name &amp; Sub -->
    <text x="62" y="44" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="15" fill="{text_pri}">{c['name']}</text>
    <text x="62" y="58" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="600" font-size="11" fill="{c['color']}">{c['sub']}</text>
    
    <!-- Description -->
    <text x="14" y="88" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="400" font-size="11.5" fill="{text_sec}">{c['desc'][:36]}</text>
    <text x="14" y="106" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="400" font-size="11.5" fill="{text_sec}">{c['desc'][36:]}</text>
  </g>"""
        svg += "\n</svg>"
        with open(f'assets/mean-stack-{mode}.svg', 'w') as f:
            f.write(svg)
    print("Generated MEAN stack SVGs")

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
            "title": "Backend &amp; Cloud APIs",
            "color": "#6366F1",
            "skills": [("Node.js", "#5FA04E"), ("Express.js", "#6366F1"), ("FastAPI", "#059669"), ("Python", "#3776AB"), ("JWT / RBAC", "#F59E0B"), ("RESTful APIs", "#22D3EE")]
        },
        {
            "title": "Databases &amp; Storage",
            "color": "#10B981",
            "skills": [("PostgreSQL", "#4169E1"), ("Supabase", "#3ECF8E"), ("MongoDB", "#10AA50"), ("Mongoose", "#880000"), ("Data Modeling", "#64748B"), ("Aggregation", "#F59E0B")]
        },
        {
            "title": "DevOps, Automation &amp; Tools",
            "color": "#22D3EE",
            "skills": [("Git &amp; GitHub", "#F05032"), ("n8n Automation", "#FF6584"), ("WhatsApp API", "#25D366"), ("Vercel", "#000000" if True else ""), ("Postman", "#FF6C37"), ("Linux", "#FCC624")]
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
            svg += f"""
  <!-- {grp['title']} -->
  <g transform="translate({gx}, {gy})">
    <rect x="0" y="0" width="430" height="126" rx="12" fill="{surface}" stroke="{border}" stroke-width="1.5" filter="url(#techShadow_{mode})" />
    
    <!-- Header -->
    <circle cx="20" cy="22" r="5" fill="{grp['color']}" />
    <text x="32" y="26" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="14" fill="{text_pri}">{grp['title']}</text>
    
    <!-- Skills Pills -->
    <g transform="translate(14, 42)">
"""
            # 6 skills: 3 per row
            for s_idx, (name, col) in enumerate(grp['skills']):
                row = s_idx // 3
                col_idx = s_idx % 3
                bx = col_idx * 134
                by = row * 38
                pill_bg = "#0D1117" if mode == 'dark' else "#FFFFFF"
                svg += f"""
      <rect x="{bx}" y="{by}" width="126" height="30" rx="7" fill="{pill_bg}" stroke="{border}" stroke-width="1" />
      <circle cx="{bx + 12}" cy="{by + 15}" r="3.5" fill="{col or text_pri}" />
      <text x="{bx + 22}" y="{by + 19}" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="600" font-size="11" fill="{text_pri}">{name}</text>
"""
            svg += """    </g>
  </g>"""
        svg += "\n</svg>"
        with open(f'assets/tech-stack-{mode}.svg', 'w') as f:
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
            "type": "Full Stack Healthcare Platform",
            "impact": "Multi-platform clinic management with automated patient WhatsApp scheduling &amp; n8n workflows.",
            "stack": ["Angular 20", "Express.js", "PostgreSQL", "Supabase", "WhatsApp API", "n8n"],
            "status": "Private, available on request",
            "color": "#10B981"
        },
        {
            "num": "02",
            "name": "VulnCraft Platform",
            "type": "Cybersecurity Scanner Suite",
            "impact": "Automated vulnerability assessment orchestrating FastAPI bridges across 5+ specialized Python scanners.",
            "stack": ["Angular 20", "FastAPI", "Python", "MongoDB", "Cybersecurity", "Docker"],
            "status": "Private, available on request (vulncraft.software)",
            "color": "#DD0031"
        },
        {
            "num": "03",
            "name": "Wasel Management",
            "type": "Hypermarket Enterprise ERP",
            "impact": "High-volume inventory platform handling 5,000+ SKU units, 15+ nested categories &amp; aggregation pipelines.",
            "stack": ["Angular", "Node.js", "MongoDB Aggregations", "Express.js", "Tailwind"],
            "status": "Private, available on request",
            "color": "#6366F1"
        },
        {
            "num": "04",
            "name": "DELMA Medical",
            "type": "B2B Medical E-Commerce",
            "impact": "Comprehensive B2B medical supply procurement engine with JWT auth, granular RBAC &amp; live order tracking.",
            "stack": ["Angular", "Node.js", "JWT / RBAC", "Express.js", "MongoDB"],
            "status": "Private, available on request",
            "color": "#22D3EE"
        }
    ]

    for mode, bg, surface, border, text_pri, text_sec in [
        ('dark', '#0D1117', '#161B22', '#30363D', '#E6EDF3', '#8B949E'),
        ('light', '#FFFFFF', '#F8FAFC', '#E2E8F0', '#0F172A', '#64748B')
    ]:
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 480" width="100%" height="100%">
  <defs>
    <filter id="projShadow_{mode}" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="3" stdDeviation="5" flood-color="#000000" flood-opacity="{'0.3' if mode=='dark' else '0.08'}" />
    </filter>
  </defs>
"""
        for idx, p in enumerate(projects):
            gx = 10 if idx % 2 == 0 else 460
            gy = 10 if idx < 2 else 244
            svg += f"""
  <!-- Project {p['name']} -->
  <g transform="translate({gx}, {gy})">
    <rect x="0" y="0" width="430" height="222" rx="14" fill="{surface}" stroke="{border}" stroke-width="1.5" filter="url(#projShadow_{mode})" />
    
    <!-- Top accent border line -->
    <path d="M 0 14 Q 0 0 14 0 L 416 0 Q 430 0 430 14 L 430 18 L 0 18 Z" fill="{p['color']}" />
    
    <!-- Number &amp; Type -->
    <text x="20" y="42" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="800" font-size="12" fill="{p['color']}">{p['num']}</text>
    <text x="44" y="42" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="600" font-size="11.5" fill="{text_sec}">{p['type'].upper()}</text>
    
    <!-- Name -->
    <text x="20" y="68" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="19" fill="{text_pri}">{p['name']}</text>
    
    <!-- Impact Description (wrapped) -->
    <text x="20" y="94" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="400" font-size="12.5" fill="{text_sec}">{p['impact'][:52]}</text>
    <text x="20" y="112" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="400" font-size="12.5" fill="{text_sec}">{p['impact'][52:108]}</text>
    <text x="20" y="130" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="400" font-size="12.5" fill="{text_sec}">{p['impact'][108:]}</text>

    <!-- Stack Tags -->
    <g transform="translate(20, 148)">
"""
            tag_x = 0
            tag_y = 0
            for t in p['stack']:
                width = len(t) * 7 + 16
                if tag_x + width > 390:
                    tag_x = 0
                    tag_y += 24
                pill_bg = "#0D1117" if mode == 'dark' else "#FFFFFF"
                svg += f"""      <rect x="{tag_x}" y="{tag_y}" width="{width}" height="20" rx="5" fill="{pill_bg}" stroke="{border}" stroke-width="1" />
      <text x="{tag_x + width//2}" y="{tag_y + 14}" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="600" font-size="10.5" fill="{p['color']}">{t}</text>
"""
                tag_x += width + 6

            svg += f"""    </g>

    <!-- Status Footer -->
    <g transform="translate(20, 204)">
      <circle cx="5" cy="-4" r="3.5" fill="#8B949E" />
      <text x="14" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="500" font-size="11" fill="{text_sec}">🔒 {p['status']}</text>
    </g>
  </g>"""
        svg += "\n</svg>"
        with open(f'assets/projects-{mode}.svg', 'w') as f:
            f.write(svg)
    print("Generated Projects SVGs")

# -----------------------------------------------------------------
# 5. GITHUB STATS & LANGUAGES (Static SVGs for instantaneous loading)
# -----------------------------------------------------------------
def generate_stats_and_languages():
    for mode, bg, surface, border, text_pri, text_sec in [
        ('dark', '#0D1117', '#161B22', '#30363D', '#E6EDF3', '#8B949E'),
        ('light', '#FFFFFF', '#F8FAFC', '#E2E8F0', '#0F172A', '#64748B')
    ]:
        # Stats SVG
        stats_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 220" width="100%" height="100%">
  <defs>
    <filter id="statShadow_{mode}" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="{'0.25' if mode=='dark' else '0.06'}" />
    </filter>
  </defs>

  <rect x="2" y="2" width="436" height="216" rx="14" fill="{surface}" stroke="{border}" stroke-width="1.5" filter="url(#statShadow_{mode})" />
  
  <text x="24" y="36" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="16" fill="{text_pri}">⚡ GitHub Performance &amp; Activity</text>
  <line x1="24" y1="48" x2="416" y2="48" stroke="{border}" stroke-width="1" />

  <!-- Metric Rows -->
  <g transform="translate(24, 76)">
    <circle cx="10" cy="-4" r="5" fill="#6366F1" />
    <text x="26" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="500" font-size="13" fill="{text_sec}">Total Repositories</text>
    <text x="390" y="0" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="14" fill="{text_pri}">34</text>
  </g>

  <g transform="translate(24, 110)">
    <circle cx="10" cy="-4" r="5" fill="#22D3EE" />
    <text x="26" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="500" font-size="13" fill="{text_sec}">Primary Specialization</text>
    <text x="390" y="0" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="13" fill="#22D3EE">MEAN Stack Architect</text>
  </g>

  <g transform="translate(24, 144)">
    <circle cx="10" cy="-4" r="5" fill="#10B981" />
    <text x="26" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="500" font-size="13" fill="{text_sec}">Competition Rank</text>
    <text x="390" y="0" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="13" fill="#10B981">Top 3 in Africa (Huawei 2025)</text>
  </g>

  <g transform="translate(24, 178)">
    <circle cx="10" cy="-4" r="5" fill="#DD0031" />
    <text x="26" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="500" font-size="13" fill="{text_sec}">Cybersecurity Organization</text>
    <text x="390" y="0" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="13" fill="#DD0031">Co-Founder @ VulnCraft</text>
  </g>
</svg>"""

        # Languages SVG
        lang_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 220" width="100%" height="100%">
  <defs>
    <filter id="langShadow_{mode}" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="{'0.25' if mode=='dark' else '0.06'}" />
    </filter>
  </defs>

  <rect x="2" y="2" width="436" height="216" rx="14" fill="{surface}" stroke="{border}" stroke-width="1.5" filter="url(#langShadow_{mode})" />
  
  <text x="24" y="36" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="16" fill="{text_pri}">💻 Most Used Languages &amp; Core Stack</text>
  <line x1="24" y1="48" x2="416" y2="48" stroke="{border}" stroke-width="1" />

  <!-- Multi-color progress bar -->
  <g transform="translate(24, 62)">
    <rect x="0" y="0" width="392" height="12" rx="6" fill="#30363D" />
    <!-- TypeScript 42% -->
    <rect x="0" y="0" width="164" height="12" rx="6" fill="#3178C6" />
    <!-- JavaScript 25% -->
    <rect x="164" y="0" width="98" height="12" fill="#F7DF1E" />
    <!-- HTML/CSS 15% -->
    <rect x="262" y="0" width="58" height="12" fill="#E34F26" />
    <!-- Python 12% -->
    <rect x="320" y="0" width="47" height="12" fill="#3776AB" />
    <!-- Shell/Other 6% -->
    <rect x="367" y="0" width="25" height="12" rx="6" fill="#89E051" />
  </g>

  <!-- Legend 2 columns -->
  <g transform="translate(24, 100)">
    <!-- TypeScript -->
    <circle cx="8" cy="8" r="6" fill="#3178C6" />
    <text x="22" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="600" font-size="12.5" fill="{text_pri}">TypeScript</text>
    <text x="160" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="500" font-size="12" fill="{text_sec}">42%</text>

    <!-- JavaScript -->
    <circle cx="8" cy="36" r="6" fill="#F7DF1E" />
    <text x="22" y="40" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="600" font-size="12.5" fill="{text_pri}">JavaScript</text>
    <text x="160" y="40" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="500" font-size="12" fill="{text_sec}">25%</text>

    <!-- HTML/SCSS -->
    <circle cx="8" cy="64" r="6" fill="#E34F26" />
    <text x="22" y="68" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="600" font-size="12.5" fill="{text_pri}">HTML / SCSS</text>
    <text x="160" y="68" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="500" font-size="12" fill="{text_sec}">15%</text>

    <!-- Col 2: Python -->
    <circle cx="218" cy="8" r="6" fill="#3776AB" />
    <text x="232" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="600" font-size="12.5" fill="{text_pri}">Python</text>
    <text x="360" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="500" font-size="12" fill="{text_sec}">12%</text>

    <!-- Shell / SQL -->
    <circle cx="218" cy="36" r="6" fill="#89E051" />
    <text x="232" y="40" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="600" font-size="12.5" fill="{text_pri}">SQL / Others</text>
    <text x="360" y="40" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="500" font-size="12" fill="{text_sec}">6%</text>
  </g>
</svg>"""

        with open(f'assets/stats-{mode}.svg', 'w') as f:
            f.write(stats_svg)
        with open(f'assets/languages-{mode}.svg', 'w') as f:
            f.write(lang_svg)

    print("Generated Stats and Languages SVGs")

# -----------------------------------------------------------------
# 6. FOOTER & CONTACT CARDS
# -----------------------------------------------------------------
def generate_footer():
    for mode, bg, surface, border, text_pri, text_sec in [
        ('dark', '#0D1117', '#161B22', '#30363D', '#E6EDF3', '#8B949E'),
        ('light', '#FFFFFF', '#F8FAFC', '#E2E8F0', '#0F172A', '#64748B')
    ]:
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 110" width="100%" height="100%">
  <defs>
    <filter id="footShadow_{mode}" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="{'0.25' if mode=='dark' else '0.06'}" />
    </filter>
  </defs>

  <rect x="2" y="2" width="896" height="106" rx="14" fill="{surface}" stroke="{border}" stroke-width="1.5" filter="url(#footShadow_{mode})" />

  <text x="30" y="42" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="17" fill="{text_pri}">🤝 Let's Collaborate &amp; Build Something Great</text>
  <text x="30" y="66" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="400" font-size="13" fill="{text_sec}">Open to full-stack engineering roles, high-scale MEAN architectures &amp; security collaborations.</text>
  <text x="30" y="86" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="500" font-size="12" fill="#6366F1">📍 Giza, Egypt <tspan fill="{text_sec}">• BSc Computer Science (6 October University, June 2026)</tspan></text>

  <!-- Status indicator right -->
  <g transform="translate(680, 36)">
    <rect x="0" y="0" width="180" height="38" rx="19" fill="#10B981" fill-opacity="0.12" stroke="#10B981" stroke-width="1.2" />
    <circle cx="20" cy="19" r="4.5" fill="#10B981">
      <animate attributeName="r" values="3.5;5.5;3.5" dur="2s" repeatCount="indefinite" />
      <animate attributeName="opacity" values="0.7;1;0.7" dur="2s" repeatCount="indefinite" />
    </circle>
    <text x="34" y="24" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="12" fill="#10B981">Open for Opportunities</text>
  </g>
</svg>"""
        with open(f'assets/footer-{mode}.svg', 'w') as f:
            f.write(svg)
    print("Generated Footer SVGs")

generate_achievement()
generate_mean_stack()
generate_tech_stack()
generate_projects()
generate_stats_and_languages()
generate_footer()
