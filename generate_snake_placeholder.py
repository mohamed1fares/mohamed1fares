# Generate an initial contribution grid snake animation SVG placeholder
for mode, bg, cell_empty, cell_active in [
    ('dark', '#0D1117', '#161B22', '#10B981'),
    ('', '#FFFFFF', '#EBEDF0', '#059669')
]:
    suffix = f"-{mode}" if mode else ""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 110" width="100%" height="100%">
  <rect width="100%" height="100%" fill="{bg}" rx="10" />
  <g transform="translate(25, 20)">
"""
    # 52 weeks x 7 days
    import random
    random.seed(42)
    for col in range(52):
        for row in range(7):
            val = random.random()
            if val > 0.8:
                colr = cell_active
                op = 0.9
            elif val > 0.6:
                colr = cell_active
                op = 0.5
            elif val > 0.4:
                colr = cell_active
                op = 0.25
            else:
                colr = cell_empty
                op = 1.0
            svg += f'    <rect x="{col * 15}" y="{row * 12}" width="10" height="9" rx="2" fill="{colr}" opacity="{op}" />\n'

    # Animated Snake
    snake_color = "#22D3EE" if mode == 'dark' else "#0284C7"
    svg += f"""
    <!-- Contribution Snake -->
    <rect x="0" y="36" width="10" height="9" rx="2" fill="{snake_color}">
      <animate attributeName="x" values="0;765;0" dur="15s" repeatCount="indefinite" />
      <animate attributeName="y" values="36;12;60;24;36" dur="15s" repeatCount="indefinite" />
    </rect>
  </g>
</svg>"""
    filename = f"assets/github-contribution-grid-snake{suffix}.svg"
    with open(filename, 'w') as f:
        f.write(svg)

print("Generated contribution snake placeholder SVGs")
