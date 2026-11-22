import urllib.request
import urllib.error
import json
import os
import ssl
import xml.etree.ElementTree as ET
import html

USERNAME = "mohamed1fares"
REPOS_URL = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&type=owner"
USER_URL = f"https://api.github.com/users/{USERNAME}"
TOKEN = os.environ.get("GITHUB_TOKEN")

def open_url(url, headers):
    try:
        ctx = ssl.create_default_context()
        req = urllib.request.Request(url, headers=headers)
        return urllib.request.urlopen(req, context=ctx, timeout=10)
    except (ssl.SSLCertVerificationError, urllib.error.URLError) as e:
        if "CERTIFICATE_VERIFY_FAILED" in str(e):
            ctx = ssl._create_unverified_context()
            req = urllib.request.Request(url, headers=headers)
            return urllib.request.urlopen(req, context=ctx, timeout=10)
        raise

def fetch_data():
    headers = {"User-Agent": "GitHub-Profile-Stats-Bot"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"

    total_repos = 17
    total_stars = 0
    lang_counts = {"TypeScript": 7, "HTML / SCSS": 6, "JavaScript": 3, "Python": 2, "SQL & Others": 1}

    try:
        with open_url(USER_URL, headers=headers) as resp:
            u_data = json.loads(resp.read().decode())
            total_repos = u_data.get("public_repos", total_repos)
    except Exception as e:
        print(f"Notice: using fallback for user profile: {e}")

    try:
        with open_url(REPOS_URL, headers=headers) as resp:
            repos = json.loads(resp.read().decode())
            if isinstance(repos, list) and repos:
                fetched_langs = {}
                stars = 0
                for r in repos:
                    stars += r.get("stargazers_count", 0)
                    lang = r.get("language")
                    if lang:
                        if lang in ["HTML", "CSS", "SCSS"]:
                            key = "HTML / SCSS"
                        elif lang in ["SQL", "Shell"]:
                            key = "SQL & Others"
                        else:
                            key = lang
                        fetched_langs[key] = fetched_langs.get(key, 0) + 1
                if fetched_langs:
                    lang_counts = fetched_langs
                total_stars = stars
    except Exception as e:
        print(f"Notice: using fallback for repos: {e}")

    return total_repos, total_stars, lang_counts

def generate_svgs(total_repos, total_stars, lang_counts):
    os.makedirs("assets", exist_ok=True)
    
    total_l = sum(lang_counts.values()) or 1
    sorted_langs = sorted(lang_counts.items(), key=lambda x: x[1], reverse=True)[:5]
    
    color_map = {
        "TypeScript": "#3178C6",
        "JavaScript": "#F7DF1E",
        "HTML / SCSS": "#E34F26",
        "Python": "#3776AB",
        "SQL & Others": "#10B981",
        "CSS": "#563D7C",
        "Other": "#8B949E"
    }

    lang_pcts = []
    for idx, (lang, count) in enumerate(sorted_langs):
        pct = max(3, round((count / total_l) * 100))
        col = color_map.get(lang, "#22D3EE")
        lang_pcts.append((lang, pct, col))

    for mode, bg, surface, border, text_pri, text_sec in [
        ('dark', '#0D1117', '#161B22', '#30363D', '#E6EDF3', '#8B949E'),
        ('light', '#FFFFFF', '#F8FAFC', '#E2E8F0', '#0F172A', '#64748B')
    ]:
        laser_color = "#6366F1" if mode == 'dark' else "#4F46E5"
        laser_stop2 = "#22D3EE" if mode == 'dark' else "#0284C7"

        # Multi-color Progress Bar segments
        bar_w = 380
        cur_x = 0
        rects = []
        for idx, (lang, pct, col) in enumerate(lang_pcts):
            seg_w = max(6, round((pct / 100.0) * bar_w))
            if idx == len(lang_pcts) - 1:
                seg_w = max(0, bar_w - cur_x)
            rx_attr = 'rx="5"' if (cur_x == 0 or idx == len(lang_pcts) - 1) else ''
            rects.append(f"""      <rect x="{cur_x}" y="0" width="{seg_w}" height="11" {rx_attr} fill="{col}">
        <animate attributeName="opacity" values="0.75;1;0.75" dur="3s" repeatCount="indefinite" />
      </rect>""")
            cur_x += seg_w
        bar_str = "\n".join(rects)

        # Legend Grid
        legend_items = []
        for idx, (lang, pct, col) in enumerate(lang_pcts):
            col_idx = idx % 2
            row_idx = idx // 2
            lx = col_idx * 190
            ly = row_idx * 26
            lang_esc = html.escape(lang)
            legend_items.append(f"""      <g transform="translate({lx}, {ly})">
        <circle cx="6" cy="6" r="4.5" fill="{col}" />
        <text x="16" y="10" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="600" font-size="12" fill="{text_pri}">{lang_esc}</text>
        <text x="165" y="10" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="11.5" fill="{text_sec}">{pct}%</text>
      </g>""")
        legend_str = "\n".join(legend_items)

        # Unified 900x230 Dashboard
        dashboard_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 230" width="100%" height="100%">
  <defs>
    <linearGradient id="dashLaser_{mode}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{laser_color}" stop-opacity="0" />
      <stop offset="50%" stop-color="{laser_stop2}" stop-opacity="1" />
      <stop offset="100%" stop-color="#DD0031" stop-opacity="0" />
    </linearGradient>
    <filter id="dashShadow_{mode}" x="-3%" y="-4%" width="106%" height="112%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000000" flood-opacity="{'0.3' if mode=='dark' else '0.07'}" />
    </filter>
  </defs>

  <rect x="2" y="2" width="896" height="226" rx="14" fill="{surface}" stroke="{border}" stroke-width="1.5" filter="url(#dashShadow_{mode})" />
  
  <rect x="2" y="2" width="896" height="226" rx="14" fill="none" stroke="url(#dashLaser_{mode})" stroke-width="2" stroke-dasharray="120 600" stroke-dashoffset="0">
    <animate attributeName="stroke-dashoffset" values="0;-1440" dur="8s" repeatCount="indefinite" />
  </rect>

  <!-- LEFT: Profile Performance -->
  <g transform="translate(30, 26)">
    <circle cx="8" cy="8" r="4.5" fill="#6366F1" />
    <text x="22" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="15" fill="{text_pri}">⚡ GitHub Performance &amp; Activity</text>
    <line x1="0" y1="26" x2="390" y2="26" stroke="{border}" stroke-width="1" />

    <g transform="translate(0, 52)">
      <circle cx="8" cy="-4" r="4.5" fill="{laser_color}" />
      <text x="22" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="500" font-size="13" fill="{text_sec}">Public Repositories</text>
      <text x="385" y="0" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="800" font-size="14" fill="{text_pri}">{total_repos}</text>
    </g>

    <g transform="translate(0, 84)">
      <circle cx="8" cy="-4" r="4.5" fill="{laser_stop2}" />
      <text x="22" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="500" font-size="13" fill="{text_sec}">Architecture Specialization</text>
      <text x="385" y="0" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="12.5" fill="{laser_stop2}">MEAN Stack Architect</text>
    </g>

    <g transform="translate(0, 116)">
      <circle cx="8" cy="-4" r="4.5" fill="#10B981" />
      <text x="22" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="500" font-size="13" fill="{text_sec}">Continental Competition</text>
      <text x="385" y="0" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="12.5" fill="#10B981">Top 3 in Africa (Huawei 2025)</text>
    </g>

    <g transform="translate(0, 148)">
      <circle cx="8" cy="-4" r="4.5" fill="#DD0031" />
      <text x="22" y="0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="500" font-size="13" fill="{text_sec}">Cybersecurity Organization</text>
      <text x="385" y="0" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="12.5" fill="#DD0031">Co-Founder @ VulnCraft</text>
    </g>
  </g>

  <!-- Center Divider with Pulsing Point -->
  <line x1="450" y1="26" x2="450" y2="204" stroke="{border}" stroke-width="1.2" />
  <circle cx="450" cy="115" r="4" fill="{laser_color}">
    <animate attributeName="r" values="3;5;3" dur="2s" repeatCount="indefinite" />
    <animate attributeName="opacity" values="0.6;1;0.6" dur="2s" repeatCount="indefinite" />
  </circle>

  <!-- RIGHT: Most Used Languages & Stack -->
  <g transform="translate(480, 26)">
    <circle cx="8" cy="8" r="4.5" fill="{laser_stop2}" />
    <text x="22" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="15" fill="{text_pri}">💻 Most Used Languages &amp; Core Stack</text>
    <line x1="0" y1="26" x2="390" y2="26" stroke="{border}" stroke-width="1" />

    <g transform="translate(0, 46)">
      <rect x="0" y="0" width="{bar_w}" height="11" rx="5" fill="{border}" />
{bar_str}
    </g>

    <g transform="translate(0, 78)">
{legend_str}
    </g>
  </g>
</svg>"""

        ET.fromstring(dashboard_svg)
        with open(f"assets/stats-{mode}.svg", "w") as f:
            f.write(dashboard_svg)

        # Standalone Languages SVG (440x220) for standalone reference
        lang_alone_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 220" width="100%" height="100%">
  <rect x="2" y="2" width="436" height="216" rx="14" fill="{surface}" stroke="{border}" stroke-width="1.5" />
  <text x="24" y="36" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="15" fill="{text_pri}">💻 Most Used Languages</text>
  <line x1="24" y1="48" x2="416" y2="48" stroke="{border}" stroke-width="1" />
  <g transform="translate(24, 62)">
    <rect x="0" y="0" width="392" height="12" rx="6" fill="{border}" />
    {bar_str}
  </g>
  <g transform="translate(24, 100)">
    {legend_str}
  </g>
</svg>"""
        ET.fromstring(lang_alone_svg)
        with open(f"assets/languages-{mode}.svg", "w") as f:
            f.write(lang_alone_svg)

    print(f"Updated Dashboard Stats SVGs successfully (Repos: {total_repos})")

def main():
    repos, stars, langs = fetch_data()
    generate_svgs(repos, stars, langs)

if __name__ == "__main__":
    main()
