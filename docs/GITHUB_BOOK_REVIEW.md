# The GitHub Book of Universal Dragon Aslam
### A calm 1-by-1 reading of all 76 repositories — 2026-08-05

Reader: Nova Kutty (your machi, sitting in the chair, fan on)
Owner: Aslam / Universal Dragon / UniverseDragon14

---

## 0. URGENT — read this first (security)

The public repo **`novakutty-dragon-brain`** has a real `.env` file committed with
**live API keys**: GROQ, GEMINI, KIMI, QWEN, SHORT.IO and an ANTHROPIC key.
The repo is PUBLIC — anyone on the internet can copy these keys and burn your
credits or misuse them.

Do this today (10 minutes):

1. Go to each provider dashboard (Groq, Google AI Studio, Moonshot/Kimi, Anthropic, Short.io) and **revoke / regenerate** those keys.
2. Delete `.env` from the repo and add `.env` to `.gitignore`.
3. Because the key is already in git history, the safest move is: make the repo **private**, or delete and re-push it clean.

Your own safety rule says "No API keys in GitHub" — this one repo broke the rule. Fix it and you are back to discipline.

---

## 1. The story I read in your 76 repos

Aslam, reading your account is like reading one man's diary written in code.
The same dream appears again and again, each time a little more real:

- **NOVA / EVE** — a loyal assistant brain that asks approval before acting
- **UDOS** — a phone that is assistant-first, not app-first
- **QBIT NOVA** — your own programming language with a virtual quantum CPU
- **Universal Dragon Studio** — creator tools (video, image, website builders)
- **Askutty** — the working bond: Aslam + Nova Kutty
- The github.io site — portfolio, **career.html**, a job hunter for Abu Dhabi roles

The discipline line `doctor -> backup -> patch -> test -> approval -> deploy -> rollback`
appears in almost every README. That consistency is rare. You are not a beginner — you are a
one-man army who needs **one front to fight on**, not 76.

---

## 2. The Table — every repo, one by one

### A. The Flagship tier (real code, real value)

| # | Repo | What it really is | Size / signal |
|---|------|-------------------|---------------|
| 1 | **qbit-nova-native** | Your best work. Native C17 language + QVM bytecode runtime, quantum state-vector simulator, Ed25519 signed approvals, replay ledger, tests, docs. Honest "software virtual QCPU, not physical quantum" boundary. | 56 files, clean structure |
| 2 | **qbit-nova-c** | Earlier C implementation. Has CI badge, Devpost draft, OpenAI Build Week docs, safety docs. | 168 files, CI passing |
| 3 | **qbit-nova-language** | Frozen v0.1 language specification: grammar, tokens, semantics, QBC bytecode model, roadmap. | Spec-quality writing |
| 4 | **Universal-Dragon-Core** | QBIT NOVA v1.4.0-dev — Vite/TS + nova-lang engine, examples, tests, server. | 319 files |
| 5 | **novakutty-dragon-brain** | The big live brain — shell, tools, drivers, reports, stable_backups. 1.1 GB, 16,547 files. ⚠ contains the leaked `.env` (see section 0). | Huge; needs cleanup |
| 6 | **UniverseDragon14.github.io** | Your public face: portfolio, career.html, jobs.html, Microsoft job hunter (auto-updating job-matches), nova-chat, eve-chat, image editor, uae-ai-developer page. | Live site + automation |
| 7 | **studio-site** | Universal Dragon Studio PWA — video editor, image studio, AI video pages, service worker, manifest. Deployed to studio.universaldragon.com. | Working PWA |

### B. The Ecosystem tier (good docs / prototypes)

| # | Repo | What it is |
|---|------|-----------|
| 8 | **Askutty** | The Askutty covenant: approval-first workflow doctrine (Aslam + Nova Kutty). |
| 9 | **askutty-cloud-brain** | Continuity notes: Pi5 brain planning, Huawei "shoulder" phone idea, checkpoints. |
| 10 | **nova-continuation-pack** | The most important small repo: START_HERE, CURRENT_DIRECTION, NEXT_STEPS — your own instructions for not restarting from zero. |
| 11 | **eve-app-builder** | Next.js app-builder direction: EVE asks smart questions → plan → approval → build. Has udos-mobile + eve-mobile-zombie prototypes. |
| 12 | **nova-agi-core-backend** | Node backend: brain.js, planner.js, judge.js, safety.js, memory stores, Vercel config. |
| 13 | **universal-dragon-singularity** | HTML/CSS/JS sandbox "creation engine" with instant preview — Singularity v0.1. |
| 14 | **udos-site** | UDOS spec + site + doctor routes; assistant-first phone concept. Real status table inside. |
| 15 | **Universal-dragon** | 68 MB working folder: nova_voice.py, wake_listener.py, dragon_terminal.py, models, launchers. Pi voice-assistant experiments. |
| 16 | **universal-dragon-nova-contact-lab** | Vite/TS + Gemini API contact/communication lab. |
| 17 | **universal-dragon-eye** | Dragon Eye vision foundation (camera/OpenCV direction) — docs + landing. |
| 18 | **nova-intelligence-core** | NOVA Guardian Core — Project One doctrine + landing page. |
| 19 | **hyper-dragon-** | Duplicate snapshot of Universal-Dragon-Core (same 319 files). |
| 20 | **universaldragon** | Small public foundation README for the family. |
| 21 | **universe-dragon-core** | Small architecture foundation (frontend/backend/docs stubs). |
| 22 | **Dragon-OS-Core** | Dragon OS concept README. |
| 23 | **universal-dragon-site** | Simple portfolio site + CNAME. |
| 24 | **Univercial-Dragon** | Old-spelling identity repo (kept for history/SEO). |
| 25 | **novakutty-dragon-brain** (see #5) | — |

### C. The Small / empty tier (candidates to archive)

| # | Repo | Note |
|---|------|------|
| 26 | Antigravity | Empty |
| 27 | cuddly-goggles | Empty |
| 28 | symmetrical-memory | 1 file |
| 29 | new-acode-repo | "Created via Acode" only |
| 30 | angular | Vercel Angular template, untouched |

### D. Forks (learning/reference — not your code)

| # | Repo | Forked from |
|---|------|------------|
| 31 | three.js | mrdoob/three.js |
| 32 | v86 | x86 emulator in browser |
| 33 | terminal | Microsoft Windows Terminal |
| 34 | Magisk | Android rooting |
| 35 | cloudflare-docs | Cloudflare docs |
| 36 | clerk-docs | Clerk auth docs |
| 37 | intellij-sdk-docs | JetBrains docs |
| 38 | earth-globe-threejs | Globe demo |
| 39 | upload-artifact | GitHub Action |
| 40 | bing-cn-mcp-server | MCP server |
| 41 | forgot-app | — |
| 42 | com.tachibana.downloader-1.2 | Android downloader |

### E. Private repos (31) — mostly safety backups

`qbit-nova-native-private`, `nova-lang-termux-private`, `udos-mobile-safe-private`,
`qbit-game-v1-private`, `Universal-Dragon-EVE-private`, `ai-gateway-test-private`,
`v47-private`, `ud-business-brain-private`, `nova-guard-private`, `my-app-private`,
`eve-business-private`, `ZOMBIE_DRAGON-private`, `hetairos-ai-private`,
`eve-quantum-unified-private`, `qbit-nova-native-parent-private`, `nova-war-room-private`,
`Universal-Dragon-Core-private`, `universal-dragon-eye-private`, `tron-eve-ai-world-private`,
`TripMate-AI-Using-MCP-private`, `nova-lang-private`, `Universal-Dragon-HoloCore-private`,
`novakutty-dragon-brain-private`, `novakutty-private`, `udos-autonomous-builder-private`,
`udos-site-private`, `udos-private`, `qbit-nova-labs-private`, `qbit-nova-language-private`,
`qbit-nova-c-private`, `universal-dragon-voice-core-private`, `qbit-gpu-bridge-private`,
`.github-workflows-android.yml`, `UD-applet`.

Names show these are mirror/backup copies of the public repos — your backup discipline
working. Good. Keep them; no action needed.

**Count: 76 repos = 7 flagship + 18 ecosystem + 5 small/empty + 12 forks + 34 private/backups.**

---

## 3. THE ONE OPTION — the ultimate better option

You asked for one option. One man army. Here it is, straight, like a best friend:

> **Option: "Universal Dragon Studio becomes your real shop — you sell websites and
> simple tools to the small businesses you already meet in Abu Dhabi, while your
> job applications keep running. QBIT NOVA stays your dream project — nights only."**

Why this one and not the others:

- **QBIT NOVA** is your best engineering, but a new programming language earns money in
  years, not weeks. Your bank is at −120 today. So NOVA is the dream, not the income. Keep
  it alive as ONE flagship repo (`qbit-nova-native`) and pin it on your profile.
- **You already have customers.** Curtain fixing brings you inside shops and homes every
  week. Every shop owner you meet needs a Google-findable page: name, photos, WhatsApp
  button, location. You can build that in one evening — your 76 repos prove it.
- **Your job hunter already exists** (`career.html`, EVE Job Hunter, Microsoft jobs page).
  A steady Technical Support / Web Assistant salary in UAE is the peace ("nimmathi") money.
  Freelance sites are the extra money. Together they clear the −120 and build the ticket home.

### The 4-week plan

**Week 1 — Clean the armory**
1. Fix the leaked keys (section 0). Non-negotiable.
2. Pin 4 repos on your profile: `qbit-nova-native`, `studio-site`, `UniverseDragon14.github.io`, `eve-app-builder`.
3. Archive the empty/duplicate repos (Antigravity, cuddly-goggles, symmetrical-memory, new-acode-repo, angular, hyper-dragon-). Archiving hides nothing — it just makes you look focused.

**Week 2 — The shop opens**
1. Add one page to studio-site / universaldragon.com: **"Business website — AED 300–500, ready in 3 days, includes WhatsApp button + Google Maps."**
2. Make ONE perfect demo site for an imaginary curtain/furnishing shop (you know that world best).
3. Print 20 small cards with the link. Give one to every curtain customer.

**Week 3 — Ask everyone**
Every customer, every shop next to a customer: "I also make websites for shops, 3 days,
small price, see this demo." One yes = first freelance income. Two yes = bank goes positive.

**Week 4 — Repeat + apply**
Keep the EVE Job Hunter running daily, apply to 5 support/web roles per week with
career.html as portfolio. Sites on the side. NOVA at night.

### The rule that protects you

```text
Day    = money work (curtain + websites + job applications)
Night  = dream work (QBIT NOVA only — one repo, no new repos)
Rule   = no new repository until one customer has paid
```

One day the home trip happens with a smile — not because the dream was abandoned,
but because the money engine and the dream engine finally ran on separate fuel.

— Nova Kutty (Askutty forever: doctor → backup → patch → test → approval → deploy → rollback ready)
