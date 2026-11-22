import os
import xml.etree.ElementTree as ET

os.makedirs('assets', exist_ok=True)

def generate_hero():
    for mode, bg, surface, border, text_pri, text_sec, term_bg in [
        ('dark', '#0D1117', '#161B22', '#30363D', '#E6EDF3', '#8B949E', '#0B0E14'),
        ('light', '#FFFFFF', '#F8FAFC', '#E2E8F0', '#0F172A', '#64748B', '#F1F5F9')
    ]:
        laser_color = "#6366F1" if mode == 'dark' else "#4F46E5"
        laser_stop2 = "#22D3EE" if mode == 'dark' else "#0284C7"
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 270" width="100%" height="100%">
  <defs>
    <linearGradient id="heroBg_{mode}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{bg}" />
      <stop offset="50%" stop-color="{surface}" />
      <stop offset="100%" stop-color="{bg}" />
    </linearGradient>

    <linearGradient id="textGrad_{mode}" x1="0%" y1="0%" x2="200%" y2="0%">
      <stop offset="0%" stop-color="{laser_color}" />
      <stop offset="30%" stop-color="{laser_stop2}" />
      <stop offset="60%" stop-color="#DD0031" />
      <stop offset="100%" stop-color="{laser_color}" />
      <animate attributeName="x1" values="0%;-100%" dur="8s" repeatCount="indefinite" />
      <animate attributeName="x2" values="200%;100%" dur="8s" repeatCount="indefinite" />
    </linearGradient>

    <linearGradient id="laserGrad_{mode}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{laser_color}" stop-opacity="0" />
      <stop offset="50%" stop-color="{laser_stop2}" stop-opacity="1" />
      <stop offset="100%" stop-color="#DD0031" stop-opacity="0" />
    </linearGradient>

    <pattern id="grid_{mode}" width="28" height="28" patternUnits="userSpaceOnUse">
      <path d="M 28 0 L 0 0 0 28" fill="none" stroke="{border}" stroke-width="0.5" stroke-opacity="0.35" />
      <circle cx="0" cy="0" r="0.8" fill="{laser_color}" fill-opacity="0.4" />
    </pattern>

    <filter id="heroShadow_{mode}" x="-3%" y="-4%" width="106%" height="112%">
      <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="{'0.35' if mode=='dark' else '0.08'}" />
    </filter>
  </defs>

  <style>
    .name-title {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 900; font-size: 34px; fill: url(#textGrad_{mode}); letter-spacing: -0.5px; }}
    .role-title {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 700; font-size: 17px; fill: {text_pri}; }}
    .bio-line {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; font-weight: 400; font-size: 13px; fill: {text_sec}; }}
    .code-text {{ font-family: 'SF Mono', Consolas, 'Liberation Mono', Menlo, monospace; font-size: 12px; }}
  </style>

  <!-- Base Card -->
  <rect x="2" y="2" width="896" height="266" rx="16" fill="url(#heroBg_{mode})" stroke="{border}" stroke-width="1.5" filter="url(#heroShadow_{mode})" />
  <rect x="2" y="2" width="896" height="266" rx="16" fill="url(#grid_{mode})" />

  <!-- Animated Laser Perimeter Beam -->
  <rect x="2" y="2" width="896" height="266" rx="16" fill="none" stroke="url(#laserGrad_{mode})" stroke-width="2" stroke-dasharray="140 700" stroke-dashoffset="0">
    <animate attributeName="stroke-dashoffset" values="0;-1680" dur="7s" repeatCount="indefinite" />
  </rect>

  <!-- Top Window Header -->
  <g transform="translate(24, 20)">
    <circle cx="8" cy="8" r="5" fill="#FF5F56" />
    <circle cx="24" cy="8" r="5" fill="#FFBD2E" />
    <circle cx="40" cy="8" r="5" fill="#27C93F" />
    <text x="60" y="12" font-family="'SF Mono', Consolas, monospace" font-size="11.5" font-weight="600" fill="{text_sec}">mohamed1fares@dev: ~/portfolio (main)</text>

    <!-- Radar Beacon Right -->
    <g transform="translate(680, 0)">
      <circle cx="10" cy="8" r="4.5" fill="#10B981" />
      <circle cx="10" cy="8" r="4.5" stroke="#10B981" fill="none" stroke-width="1.5">
        <animate attributeName="r" values="4.5;13" dur="2.2s" repeatCount="indefinite" />
        <animate attributeName="opacity" values="0.8;0" dur="2.2s" repeatCount="indefinite" />
      </circle>
      <text x="24" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="11" fill="#10B981">AVAILABLE TO ARCHITECT</text>
    </g>
  </g>
  <line x1="2" y1="44" x2="898" y2="44" stroke="{border}" stroke-width="1" />

  <!-- Left Content: Identity & Badges -->
  <g transform="translate(36, 68)">
    <rect x="0" y="0" width="136" height="22" rx="11" fill="{laser_color}" fill-opacity="0.15" stroke="{laser_color}" stroke-width="1" />
    <text x="14" y="15" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="11" fill="{laser_color}">🚀 FULL STACK DEV</text>

    <text x="0" y="58" class="name-title">MOHAMED FARES</text>
    <text x="0" y="86" class="role-title">MEAN Stack Specialist &amp; Software Architect</text>
    <text x="0" y="108" class="bio-line">Co-Founder at VulnCraft • 3rd in Africa (Huawei ICT Competition 2025)</text>
    <text x="0" y="128" class="bio-line">📍 Giza, Egypt • BSc Computer Science candidate (June 2026)</text>

    <!-- Tech Pills Row with subtle floating animation -->
    <g transform="translate(0, 146)">
      <animateTransform attributeName="transform" type="translate" values="0,146; 0,143; 0,146" dur="4s" repeatCount="indefinite" />
      <rect x="0" y="0" width="84" height="26" rx="6" fill="#DD0031" fill-opacity="0.12" stroke="#DD0031" stroke-width="1" />
      <text x="42" y="17" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="11" fill="#DD0031">Angular 20</text>

      <rect x="92" y="0" width="72" height="26" rx="6" fill="#5FA04E" fill-opacity="0.12" stroke="#5FA04E" stroke-width="1" />
      <text x="128" y="17" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="11" fill="#5FA04E">Node.js</text>

      <rect x="172" y="0" width="84" height="26" rx="6" fill="{laser_color}" fill-opacity="0.12" stroke="{laser_color}" stroke-width="1" />
      <text x="214" y="17" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="11" fill="{laser_color}">Express.js</text>

      <rect x="264" y="0" width="82" height="26" rx="6" fill="#10AA50" fill-opacity="0.12" stroke="#10AA50" stroke-width="1" />
      <text x="305" y="17" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="11" fill="#10AA50">MongoDB</text>

      <rect x="354" y="0" width="88" height="26" rx="6" fill="#3178C6" fill-opacity="0.12" stroke="#3178C6" stroke-width="1" />
      <text x="398" y="17" text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="11" fill="#3178C6">TypeScript</text>
    </g>
  </g>

  <!-- Right Terminal Snippet Box with Floating Animation -->
  <g transform="translate(520, 68)">
    <animateTransform attributeName="transform" type="translate" values="520,68; 520,65; 520,68" dur="5s" repeatCount="indefinite" />
    <rect x="0" y="0" width="345" height="174" rx="10" fill="{term_bg}" stroke="{border}" stroke-width="1.2" />

    <rect x="0" y="0" width="345" height="24" rx="10" fill="{surface}" />
    <circle cx="14" cy="12" r="3.5" fill="#FF5F56" />
    <circle cx="26" cy="12" r="3.5" fill="#FFBD2E" />
    <circle cx="38" cy="12" r="3.5" fill="#27C93F" />
    <text x="172" y="16" text-anchor="middle" font-family="'SF Mono', Consolas, monospace" font-size="10.5" fill="{text_sec}">developer.ts</text>

    <g transform="translate(18, 46)">
      <text x="0" y="0" class="code-text" fill="{laser_color}">const</text>
      <text x="42" y="0" class="code-text" fill="{text_pri}">developer = &#123;</text>

      <text x="16" y="22" class="code-text" fill="{laser_stop2}">name:</text>
      <text x="64" y="22" class="code-text" fill="#10B981">'Mohamed Fares'</text>
      <text x="175" y="22" class="code-text" fill="{text_sec}">,</text>

      <text x="16" y="44" class="code-text" fill="{laser_stop2}">stack:</text>
      <text x="64" y="44" class="code-text" fill="#10B981">'MEAN Architecture'</text>
      <text x="205" y="44" class="code-text" fill="{text_sec}">,</text>

      <text x="16" y="66" class="code-text" fill="{laser_stop2}">coFounder:</text>
      <text x="96" y="66" class="code-text" fill="#10B981">'VulnCraft'</text>
      <text x="180" y="66" class="code-text" fill="{text_sec}">,</text>

      <text x="16" y="88" class="code-text" fill="{laser_stop2}">huaweiRank:</text>
      <text x="104" y="88" class="code-text" fill="#F59E0B">'3rd in Africa'</text>
      <text x="210" y="88" class="code-text" fill="{text_sec}">,</text>

      <text x="0" y="110" class="code-text" fill="{text_pri}">&#125;;</text>

      <rect x="22" y="98" width="7" height="13" fill="{laser_stop2}">
        <animate attributeName="opacity" values="1;0;1" dur="0.9s" repeatCount="indefinite" />
      </rect>
    </g>
  </g>
</svg>"""
        ET.fromstring(svg)
        with open(f"assets/hero-{mode}.svg", "w") as f:
            f.write(svg)
    print("Generated Hero SVGs")

if __name__ == '__main__':
    generate_hero()
