import xml.etree.ElementTree as ET
import os

os.makedirs('assets', exist_ok=True)

def generate_snake():
    for mode, bg, cell_empty, c1, c2, c3, c4, s_head, s_body, food_col in [
        ('dark', '#0D1117', '#161B22', '#0e4429', '#006d32', '#26a641', '#39d353', '#22D3EE', '#10B981', '#F59E0B'),
        ('light', '#FFFFFF', '#EBEDF0', '#9BE9A8', '#40C463', '#30A14E', '#216E39', '#4F46E5', '#0284C7', '#D97706')
    ]:
        suffix = f"-{mode}" if mode == 'dark' else ""
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 150" width="100%" height="100%">
  <defs>
    <filter id="snakeGlow_{mode}" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur" />
      <feMerge>
        <feMergeNode in="blur" />
        <feMergeNode in="SourceGraphic" />
      </feMerge>
    </filter>
  </defs>

  <rect width="100%" height="100%" rx="12" fill="{bg}" stroke="{'#30363D' if mode=='dark' else '#E2E8F0'}" stroke-width="1.5" />
  
  <!-- Contribution Grid Header -->
  <g transform="translate(24, 20)">
    <circle cx="6" cy="6" r="4.5" fill="{s_head}" />
    <text x="18" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="13" fill="{'#E6EDF3' if mode=='dark' else '#0F172A'}">2026 Contribution Activity Matrix</text>
    <text x="850" y="10" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="500" font-size="11" fill="{'#8B949E' if mode=='dark' else '#64748B'}">Less ■ ■ ■ ■ ■ More</text>
  </g>
  <line x1="24" y1="34" x2="876" y2="34" stroke="{'#30363D' if mode=='dark' else '#E2E8F0'}" stroke-width="0.8" />

  <!-- Grid of 52 weeks x 7 days -->
  <g transform="translate(26, 46)">
"""
        import random
        random.seed(1337)
        for col in range(53):
            x = col * 16
            for row in range(7):
                y = row * 13
                r = random.random()
                if r > 0.88:
                    colr = c4
                elif r > 0.72:
                    colr = c3
                elif r > 0.52:
                    colr = c2
                elif r > 0.32:
                    colr = c1
                else:
                    colr = cell_empty
                svg += f'    <rect x="{x}" y="{y}" width="11" height="10" rx="2.5" fill="{colr}" />\n'

        svg += f"""
    <!-- Food Dots -->
    <circle cx="325" cy="45" r="4" fill="{food_col}">
      <animate attributeName="opacity" values="1;0.2;1" dur="1.5s" repeatCount="indefinite" />
    </circle>
    <circle cx="580" cy="71" r="4" fill="{food_col}">
      <animate attributeName="opacity" values="0.3;1;0.3" dur="1.8s" repeatCount="indefinite" />
    </circle>

    <!-- Animated Snake -->
    <g filter="url(#snakeGlow_{mode})">
      <rect x="0" y="40" width="12" height="11" rx="3" fill="{s_head}">
        <animate attributeName="x" values="0;280;280;520;520;830;830;400;0" dur="16s" repeatCount="indefinite" />
        <animate attributeName="y" values="40;40;66;66;14;14;52;52;40" dur="16s" repeatCount="indefinite" />
      </rect>
      <rect x="-14" y="40" width="11" height="10" rx="2.5" fill="{s_body}">
        <animate attributeName="x" values="-14;266;266;506;506;816;816;386;-14" dur="16s" repeatCount="indefinite" />
        <animate attributeName="y" values="40;40;66;66;14;14;52;52;40" dur="16s" repeatCount="indefinite" />
      </rect>
      <rect x="-28" y="40" width="11" height="10" rx="2.5" fill="{s_body}" opacity="0.8">
        <animate attributeName="x" values="-28;252;252;492;492;802;802;372;-28" dur="16s" repeatCount="indefinite" />
        <animate attributeName="y" values="40;40;66;66;14;14;52;52;40" dur="16s" repeatCount="indefinite" />
      </rect>
      <rect x="-42" y="40" width="10" height="9" rx="2" fill="{s_body}" opacity="0.5">
        <animate attributeName="x" values="-42;238;238;478;478;788;788;358;-42" dur="16s" repeatCount="indefinite" />
        <animate attributeName="y" values="40;40;66;66;14;14;52;52;40" dur="16s" repeatCount="indefinite" />
      </rect>
    </g>
  </g>
</svg>"""
        ET.fromstring(svg)
        with open(f"assets/github-contribution-grid-snake{suffix}.svg", "w") as f:
            f.write(svg)

    print("Generated Contribution Snake SVGs successfully")

if __name__ == '__main__':
    generate_snake()
