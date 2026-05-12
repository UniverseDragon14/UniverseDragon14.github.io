#!/usr/bin/env python3
"""Universal Dragon Microsoft Job Hunter Bot
Safe mode: finds relevant jobs and creates apply-ready materials.
It does not auto-apply. The user must review and submit manually.
"""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode, quote_plus
from urllib.request import Request, urlopen
import html
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OUT_HTML = ROOT / "microsoft-jobs.html"
OUT_JSON = ROOT / "microsoft-jobs.json"
OUT_COVER = ROOT / "microsoft-cover-letter.txt"

PROFILE_URL = "https://universaldragon.com/career.html"
GITHUB_URL = "https://github.com/UniverseDragon14"
UDOS_URL = "https://udos.universaldragon.com/#modules"
LINKEDIN_URL = "https://www.linkedin.com/in/aam-aslam-51777017b"

TARGETS = [
    ("Data Center Technician", "United Arab Emirates"),
    ("Data Center Technician", "Abu Dhabi"),
    ("Data Center Technician", "Dubai"),
    ("Datacenter Technician", "United Arab Emirates"),
    ("IT Support Technician", "United Arab Emirates"),
    ("Technical Support Specialist", "United Arab Emirates"),
    ("Hardware Support Technician", "United Arab Emirates"),
    ("Field Support Technician", "United Arab Emirates"),
    ("Support Engineer", "United Arab Emirates"),
    ("Cloud Support", "United Arab Emirates"),
    ("Infrastructure Technician", "United Arab Emirates"),
]

GOOD = [
    "data center", "datacenter", "technician", "it support", "technical support",
    "support engineer", "hardware", "troubleshooting", "linux", "network",
    "server", "operations", "field", "cloud", "infrastructure", "rack", "cabling"
]
BAD = [
    "senior software engineer", "principal", "director", "manager", "architect",
    "10+ years", "8+ years", "7+ years", "machine learning scientist", "researcher"
]

STATIC_FALLBACKS = [
    {
        "title": "Microsoft Careers Search: Data Center Technician - UAE",
        "company": "Microsoft",
        "location": "United Arab Emirates / Abu Dhabi / Dubai",
        "score": 5,
        "why": ["target search", "data center", "hardware support"],
        "url": "https://jobs.careers.microsoft.com/global/en/search?" + urlencode({"q": "Data Center Technician", "lc": "United Arab Emirates"}),
        "source": "Microsoft Careers Search",
    },
    {
        "title": "Microsoft Careers Search: IT Support Technician - UAE",
        "company": "Microsoft",
        "location": "United Arab Emirates",
        "score": 5,
        "why": ["target search", "IT support", "technical support"],
        "url": "https://jobs.careers.microsoft.com/global/en/search?" + urlencode({"q": "IT Support Technician", "lc": "United Arab Emirates"}),
        "source": "Microsoft Careers Search",
    },
    {
        "title": "Microsoft Careers Search: Technical Support Specialist - UAE",
        "company": "Microsoft",
        "location": "United Arab Emirates",
        "score": 4,
        "why": ["target search", "support role"],
        "url": "https://jobs.careers.microsoft.com/global/en/search?" + urlencode({"q": "Technical Support Specialist", "lc": "United Arab Emirates"}),
        "source": "Microsoft Careers Search",
    },
]


def clean(value: object) -> str:
    text = str(value or "")
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def find_jobs(obj: object) -> list[dict]:
    found: list[dict] = []
    if isinstance(obj, dict):
        for key, value in obj.items():
            lowered = key.lower()
            if lowered in {"jobs", "jobresults", "results", "operationresult", "value"} and isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        title = clean(item.get("title") or item.get("jobTitle") or item.get("name"))
                        if title:
                            found.append(item)
            found.extend(find_jobs(value))
    elif isinstance(obj, list):
        for value in obj:
            found.extend(find_jobs(value))
    return found


def score_job(title: str, desc: str, loc: str) -> tuple[int, list[str]]:
    text = f"{title} {desc} {loc}".lower()
    score = 0
    reasons: list[str] = []

    for word in GOOD:
        if word in text:
            score += 2
            reasons.append(word)

    for word in BAD:
        if word in text:
            score -= 4
            reasons.append("skip-risk:" + word)

    title_l = title.lower()
    if "technician" in title_l:
        score += 4
        reasons.append("technician title")
    if "support" in title_l:
        score += 3
        reasons.append("support title")
    if "data center" in text or "datacenter" in text:
        score += 4
        reasons.append("data center match")
    if "united arab emirates" in text or "abu dhabi" in text or "dubai" in text:
        score += 3
        reasons.append("UAE location")

    return score, reasons[:8]


def microsoft_api_search(keyword: str, location: str) -> dict:
    base = "https://gcsservices.careers.microsoft.com/search/api/v1/search"
    params = {
        "q": keyword,
        "lc": location,
        "l": "en_us",
        "pg": "1",
        "pgSz": "20",
        "o": "Relevance",
        "flt": "true",
    }
    req = Request(base + "?" + urlencode(params), headers={
        "User-Agent": "UniversalDragon-MicrosoftJobHunter/1.0",
        "Accept": "application/json",
    })
    with urlopen(req, timeout=30) as response:
        return json.loads(response.read().decode("utf-8", errors="replace"))


def job_url(job: dict, keyword: str, location: str) -> str:
    job_id = clean(job.get("jobId") or job.get("job_id") or job.get("id") or job.get("JobId"))
    if job_id:
        return "https://jobs.careers.microsoft.com/global/en/job/" + quote_plus(job_id)
    return "https://jobs.careers.microsoft.com/global/en/search?" + urlencode({"q": keyword, "lc": location})


def collect_jobs() -> tuple[list[dict], list[str]]:
    matches: list[dict] = []
    seen: set[tuple[str, str, str]] = set()
    notes: list[str] = []

    for keyword, location in TARGETS:
        try:
            data = microsoft_api_search(keyword, location)
            jobs = find_jobs(data)
            notes.append(f"{keyword} / {location}: API OK, {len(jobs)} result objects")
        except Exception as exc:  # noqa: BLE001
            notes.append(f"{keyword} / {location}: API failed: {exc}")
            continue

        for job in jobs:
            title = clean(job.get("title") or job.get("jobTitle") or job.get("name"))
            desc = clean(job.get("description") or job.get("summary") or job.get("jobDescription"))
            loc_text = clean(job.get("location") or job.get("primaryLocation") or job.get("jobLocation") or location)
            company = clean(job.get("company") or "Microsoft")
            url = job_url(job, keyword, location)

            key = (title.lower(), loc_text.lower(), url)
            if not title or key in seen:
                continue
            seen.add(key)

            score, reasons = score_job(title, desc, loc_text)
            if score >= 3:
                matches.append({
                    "title": title,
                    "company": company,
                    "location": loc_text,
                    "score": score,
                    "why": reasons,
                    "url": url,
                    "source": "Microsoft Careers",
                })

    if not matches:
        notes.append("No direct API matches. Using safe Microsoft Careers search links.")
        matches = STATIC_FALLBACKS.copy()

    matches.sort(key=lambda item: item["score"], reverse=True)
    return matches, notes


def write_cover_letter() -> None:
    cover = f"""Dear Hiring Team,

My name is Aslam and I am based in Abu Dhabi, UAE. I am interested in Microsoft opportunities related to Data Center Technician, IT Support, Technical Support, Hardware Support, Field Support, and Cloud/Infrastructure Operations.

I have hands-on experience through real personal projects using Raspberry Pi, Linux command line, GitHub, 3D printing, electronics components, camera modules, motor drivers, and robotics prototype building. I also have practical office support and installation experience, which helped me build strong troubleshooting, coordination, and problem-solving skills.

My project work includes Universal Dragon / EVE / NOVA / UDOS, where I am building practical AI assistant systems, robotics concepts, 3D world experiments, safe automation, and real hardware/software workflows.

Portfolio: {PROFILE_URL}
GitHub: {GITHUB_URL}
UDOS Modules: {UDOS_URL}
LinkedIn: {LINKEDIN_URL}

I am a fast learner, practical worker, and ready to grow in a technical support or data center environment.

Kind regards,
Aslam
"""
    OUT_COVER.write_text(cover, encoding="utf-8")


def render_page(matches: list[dict], notes: list[str]) -> str:
    generated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    cards = []
    for job in matches[:80]:
        cards.append(f"""
        <article class="card">
          <div class="meta">{html.escape(job['source'])}</div>
          <h2>{html.escape(job['title'])}</h2>
          <p><b>Company:</b> {html.escape(job['company'])}</p>
          <p><b>Location:</b> {html.escape(job['location'])}</p>
          <p><b>Score:</b> {job['score']}</p>
          <p><b>Why:</b> {html.escape(', '.join(job['why']))}</p>
          <a class="button" href="{html.escape(job['url'])}" target="_blank" rel="noopener">Open job / search</a>
        </article>
        """)

    cover_preview = OUT_COVER.read_text(encoding="utf-8") if OUT_COVER.exists() else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Microsoft Job Hunter | Universal Dragon</title>
  <style>
    :root {{ --bg:#050505; --panel:#0b1110; --line:#00ffd0; --text:#eafff7; --muted:#99b8b0; --gold:#f5b642; }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; background:radial-gradient(circle at top,#13221e,#050505 55%); color:var(--text); font-family:Arial, sans-serif; line-height:1.55; }}
    .wrap {{ max-width:1100px; margin:0 auto; padding:22px; }}
    .hero,.card,.note {{ border:1px solid rgba(0,255,208,.45); border-radius:20px; padding:20px; margin:16px 0; background:rgba(0,0,0,.55); box-shadow:0 0 24px rgba(0,255,208,.08); }}
    h1,h2 {{ color:var(--line); margin-top:0; }}
    .sub {{ color:var(--muted); }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:16px; }}
    .card {{ margin:0; }}
    .meta {{ color:var(--gold); font-size:12px; letter-spacing:1px; text-transform:uppercase; }}
    a {{ color:#8fd7ff; }}
    .button,button {{ display:inline-block; border:1px solid var(--line); color:var(--line); padding:10px 14px; border-radius:12px; text-decoration:none; background:rgba(0,255,208,.08); font-weight:700; }}
    textarea {{ width:100%; min-height:260px; border:1px solid rgba(0,255,208,.35); border-radius:14px; background:#020404; color:var(--text); padding:14px; }}
    pre {{ white-space:pre-wrap; color:var(--muted); }}
    .danger {{ color:#ffb4b4; }}
  </style>
</head>
<body>
  <main class="wrap">
    <section class="hero">
      <h1>🐉 Microsoft Job Hunter Bot</h1>
      <p class="sub">Generated: {html.escape(generated)}</p>
      <p>This page searches/prepares Microsoft and big-tech style roles for Aslam: <b>Data Center Technician, IT Support, Technical Support, Hardware Support, Field Support, Cloud/Infrastructure Operations</b>.</p>
      <p><b>Portfolio:</b> <a href="{PROFILE_URL}" target="_blank" rel="noopener">{PROFILE_URL}</a></p>
      <p><b>GitHub:</b> <a href="{GITHUB_URL}" target="_blank" rel="noopener">{GITHUB_URL}</a></p>
      <p><b>UDOS:</b> <a href="{UDOS_URL}" target="_blank" rel="noopener">{UDOS_URL}</a></p>
      <p><b>LinkedIn:</b> <a href="{LINKEDIN_URL}" target="_blank" rel="noopener">{LINKEDIN_URL}</a></p>
      <p class="danger"><b>Safe mode:</b> This bot does not auto-apply. It finds roles and prepares text. Aslam must review and submit manually.</p>
    </section>

    <section class="note">
      <h2>Apply Message / Cover Letter</h2>
      <p>Copy this when a Microsoft/Data Center/IT Support application asks for cover letter or why this role.</p>
      <textarea id="cover">{html.escape(cover_preview)}</textarea><br><br>
      <button onclick="navigator.clipboard.writeText(document.getElementById('cover').value)">Copy cover letter</button>
    </section>

    <section>
      <h2>Matches / Search Links</h2>
      <div class="grid">{''.join(cards)}</div>
    </section>

    <section class="note">
      <h2>Bot Notes</h2>
      <pre>{html.escape(chr(10).join(notes))}</pre>
    </section>
  </main>
</body>
</html>"""


def main() -> None:
    write_cover_letter()
    matches, notes = collect_jobs()
    OUT_JSON.write_text(json.dumps(matches, indent=2), encoding="utf-8")
    OUT_HTML.write_text(render_page(matches, notes), encoding="utf-8")
    print(f"Wrote {OUT_HTML}")
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_COVER}")


if __name__ == "__main__":
    main()
