import urllib.request
import urllib.error
import json
import os
import ssl

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
    lang_counts = {"TypeScript": 7, "HTML/SCSS": 6, "JavaScript": 3, "Python": 2, "Other": 1}

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
                            key = "HTML/SCSS"
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
        "HTML/SCSS": "#E34F26",
        "Python": "#3776AB",
        "CSS": "#563D7C",
        "Shell": "#89E051",
        "Other": "#8B949E"
    }

    lang_pcts = []
    for idx, (lang, count) in enumerate(sorted_langs):
        pct = round((count / total_l) * 100)
        col = color_map.get(lang, "#22D3EE")
        lang_pcts.append((lang, pct, col))

    for mode, bg, surface, border, text_pri, text_sec in [
        ('dark', '#0D1117', '#161B22', '#30363D', '#E6EDF3', '#8B949E'),
        ('light', '#FFFFFF', '#F8FAFC', '#E2E8F0', '#0F172A', '#64748B')
    ]:
        # 1. Stats SVG
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
    <text x="390" y="0" text-anchor="end" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="700" font-size="14" fill="{text_pri}">{total_repos}</text>
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

        # 2. Languages SVG
        total_bar_w = 392
        cur_x = 0
        rects = []
        for idx, (lang, pct, col) in enumerate(lang_pcts):
            seg_w = max(4, round((pct / 100.0) * total_bar_w))
            if idx == len(lang_pcts) - 1:
                seg_w = max(0, total_bar_w - cur_x)
            rx_attr = 'rx="6"' if (cur_x == 0 or idx == len(lang_pcts) - 1) else ''
            rects.append(f'<rect x="{cur_x}" y="0" width="{seg_w}" height="12" {rx_attr} fill="{col}" />')
            cur_x += seg_w

        bar_svg_str = "\n    ".join(rects)

        legend_items = []
        for idx, (lang, pct, col) in enumerate(lang_pcts):
            col_idx = idx % 2
            row_idx = idx // 2
            lx = 24 + col_idx * 194
            ly = 100 + row_idx * 28
            legend_items.append(f"""    <g transform="translate({lx}, {ly})">
      <circle cx="8" cy="8" r="6" fill="{col}" />
      <text x="22" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="600" font-size="12.5" fill="{text_pri}">{lang}</text>
      <text x="160" y="12" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-weight="500" font-size="12" fill="{text_sec}">{pct}%</text>
    </g>""")

        legend_svg_str = "\n".join(legend_items)

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
    {bar_svg_str}
  </g>

  <!-- Legend -->
  <g>
{legend_svg_str}
  </g>
</svg>"""

        with open(f"assets/stats-{mode}.svg", "w") as f:
            f.write(stats_svg)
        with open(f"assets/languages-{mode}.svg", "w") as f:
            f.write(lang_svg)

    print(f"Successfully generated dynamic Stats & Languages SVGs (Repos: {total_repos}, Stars: {total_stars}, Langs: {len(sorted_langs)})")

def main():
    repos, stars, langs = fetch_data()
    generate_svgs(repos, stars, langs)

if __name__ == "__main__":
    main()
