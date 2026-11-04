#!/usr/bin/env python3
"""Builds README.md (catalog by niche) from the data below.
Data collected 2026-11-04 from the repos' SKILL.md files and GitHub stats."""

GH = "https://github.com/"

REPOS = {
    # repo: (stars, license, default_branch)
    "anthropics/skills": (187236, "see repo (some source-available)", "main"),
    "obra/superpowers": (312086, "MIT", "main"),
    "mattpocock/skills": (312011, "MIT", "main"),
    "vercel-labs/agent-skills": (33509, "none stated", "main"),
    "coreyhaines31/marketingskills": (58394, "MIT", "main"),
    "agricidaniel/claude-seo": (26465, "MIT", "main"),
    "nextlevelbuilder/ui-ux-pro-max-skill": (144967, "MIT", "main"),
    "remotion-dev/skills": (6303, "none stated", "main"),
    "trailofbits/skills": (7992, "CC-BY-SA-4.0", "main"),
    "hamelsmu/evals-skills": (1675, "MIT", "main"),
    "muratcankoylan/agent-skills-for-context-engineering": (18296, "none stated", "main"),
    "kepano/obsidian-skills": (50724, "none stated", "main"),
    "alirezarezvani/claude-skills": (29262, "none stated", "main"),
    "alchaincyf/huashu-motion": (2306, "none stated", "main"),
    "supabase/agent-skills": (2999, "none stated", "main"),
    "cloudflare/skills": (3275, "none stated", "main"),
    "getsentry/sentry-for-ai": (274, "none stated", "main"),
    "forrestchang/andrej-karpathy-skills": (229264, "none stated", "main"),
    "jeffallan/claude-skills": (12208, "none stated", "main"),
    "199-biotechnologies/claude-deep-research-skill": (1206, "none stated", "main"),
    "pleaseprompto/notebooklm-skill": (7786, "MIT", "master"),
    "neolabhq/context-engineering-kit": (1799, "GPL-3.0", "master"),
}

def L(repo, path):
    b = REPOS.get(repo, (0, "", "main"))[2]
    return f"{GH}{repo}/tree/{b}/{path}" if path else f"{GH}{repo}"

A = "anthropics/skills"; SP = "obra/superpowers"; MP = "mattpocock/skills"
VL = "vercel-labs/agent-skills"; MK = "coreyhaines31/marketingskills"
SEO = "agricidaniel/claude-seo"; UX = "nextlevelbuilder/ui-ux-pro-max-skill"
RM = "remotion-dev/skills"; AR = "alirezarezvani/claude-skills"
JA = "jeffallan/claude-skills"; CE = "muratcankoylan/agent-skills-for-context-engineering"

# (niche, intro, [(skill, repo, path, what it does)])
SECTIONS = [
("Start here: the 10 most installed", "If you install nothing else, install these.", [
 ("frontend-design", A, "skills/frontend-design", "Picks a visual direction before coding UI, so pages stop looking like AI defaults"),
 ("superpowers", SP, "", "Full dev workflow: brainstorm, plan, TDD, review, subagents"),
 ("skill-creator", A, "skills/skill-creator", "Builds and tests your own skills"),
 ("karpathy-guidelines", "forrestchang/andrej-karpathy-skills", "", "Rules that cut the typical LLM coding mistakes"),
 ("ui-ux-pro-max", UX, ".claude/skills/ui-ux-pro-max", "UI/UX design intelligence for web, mobile and desktop"),
 ("web-design-guidelines", VL, "skills/web-design-guidelines", "Audits UI code for accessibility and interface best practice"),
 ("copywriting", MK, "skills/copywriting", "Writes and rewrites copy for landing, pricing and product pages"),
 ("seo", SEO, "skills/seo", "Full SEO analysis: site audit, page, technical, Core Web Vitals"),
 ("grill-me", MP, "skills/productivity/grill-me", "Interrogates your plan until the holes show"),
 ("obsidian-markdown", "kepano/obsidian-skills", "", "Lets the agent read and write your Obsidian vault properly"),
]),
("Developers: workflow", "How the agent plans, codes, reviews and ships.", [
 ("brainstorming", SP, "skills/brainstorming", "Forces a design conversation before any new feature"),
 ("writing-plans", SP, "skills/writing-plans", "Turns a spec into a step-by-step implementation plan"),
 ("executing-plans", SP, "skills/executing-plans", "Works through a plan inline, step by step"),
 ("subagent-driven-development", SP, "skills/subagent-driven-development", "Runs plan tasks through separate subagents"),
 ("dispatching-parallel-agents", SP, "skills/dispatching-parallel-agents", "Splits independent tasks across agents in parallel"),
 ("test-driven-development", SP, "skills/test-driven-development", "Red-green-refactor before writing implementation"),
 ("systematic-debugging", SP, "skills/systematic-debugging", "Root-cause debugging instead of guess-and-check"),
 ("verification-before-completion", SP, "skills/verification-before-completion", "Makes the agent prove tests pass before saying done"),
 ("requesting-code-review", SP, "skills/requesting-code-review", "Self-review against requirements before merge"),
 ("receiving-code-review", SP, "skills/receiving-code-review", "Handles review feedback with rigor, not blind agreement"),
 ("using-git-worktrees", SP, "skills/using-git-worktrees", "Isolated workspace per feature"),
 ("finishing-a-development-branch", SP, "skills/finishing-a-development-branch", "Decides how to merge finished work"),
 ("code-review", MP, "skills/engineering/code-review", "Reviews a diff against repo standards and spec"),
 ("diagnosing-bugs", MP, "skills/engineering/diagnosing-bugs", "Diagnosis loop for hard bugs and slowdowns"),
 ("tdd", MP, "skills/engineering/tdd", "Test-first features and fixes"),
 ("to-spec", MP, "skills/engineering/to-spec", "Turns the chat into a spec in your issue tracker"),
 ("to-tickets", MP, "skills/engineering/to-tickets", "Breaks a spec into tracer-bullet tickets"),
 ("implement", MP, "skills/engineering/implement", "Implements work from a spec or tickets"),
 ("improve-codebase-architecture", MP, "skills/engineering/improve-codebase-architecture", "Finds refactor opportunities, shows an HTML report"),
 ("prototype", MP, "skills/engineering/prototype", "Throwaway prototype to answer a design question"),
 ("pr", MP, "skills/engineering/pr", "Writes the PR description"),
 ("git-guardrails-claude-code", MP, "skills/misc/git-guardrails-claude-code", "Blocks dangerous git commands via hooks"),
 ("setup-pre-commit", MP, "skills/misc/setup-pre-commit", "Husky + lint-staged + type check + tests"),
 ("handoff", MP, "skills/productivity/handoff", "Compacts a session into a handoff doc for another agent"),
 ("simplify", A, "", "Cleans up changed code (built into Claude Code)"),
 ("webapp-testing", A, "skills/webapp-testing", "Tests local web apps with Playwright"),
 ("mcp-builder", A, "skills/mcp-builder", "Builds MCP servers the right way"),
]),
("Developers: languages, frameworks, infra", "Specialist skills per stack.", [
 ("react-best-practices", VL, "skills/react-best-practices", "Vercel's React and Next.js performance rules"),
 ("composition-patterns", VL, "skills/composition-patterns", "React composition patterns that scale"),
 ("react-native-skills", VL, "skills/react-native-skills", "React Native and Expo best practices"),
 ("react-view-transitions", VL, "skills/react-view-transitions", "Native-feeling animations with the View Transition API"),
 ("deploy-to-vercel", VL, "skills/deploy-to-vercel", "Deploys and returns the link"),
 ("typescript-pro", JA, "skills/typescript-pro", "Advanced TypeScript types and guards"),
 ("python-pro", JA, "skills/python-pro", "Typed, async Python 3.11+"),
 ("fastapi-expert", JA, "skills/fastapi-expert", "Async APIs with FastAPI and Pydantic"),
 ("nextjs-developer", JA, "skills/nextjs-developer", "Next.js App Router and server components"),
 ("golang-pro", JA, "skills/golang-pro", "Concurrent Go patterns"),
 ("rust-engineer", JA, "skills/rust-engineer", "Idiomatic, safe Rust"),
 ("swift-expert", JA, "skills/swift-expert", "iOS/macOS apps with SwiftUI"),
 ("flutter-expert", JA, "skills/flutter-expert", "Cross-platform apps with Flutter"),
 ("shopify-expert", JA, "skills/shopify-expert", "Shopify themes and apps"),
 ("wordpress-pro", JA, "skills/wordpress-pro", "WordPress themes, plugins, Gutenberg blocks"),
 ("postgres-pro", JA, "skills/postgres-pro", "PostgreSQL tuning and replication"),
 ("kubernetes-specialist", JA, "skills/kubernetes-specialist", "Kubernetes deployments and workloads"),
 ("terraform-engineer", JA, "skills/terraform-engineer", "Infrastructure as code on AWS/Azure/GCP"),
 ("devops-engineer", JA, "skills/devops-engineer", "Dockerfiles, CI/CD, K8s manifests"),
 ("playwright-expert", JA, "skills/playwright-expert", "End-to-end tests with Playwright"),
 ("supabase", "supabase/agent-skills", "", "Official: anything Supabase, plus Postgres best practices"),
 ("cloudflare", "cloudflare/skills", "", "Official: Workers, Durable Objects, Wrangler, web perf (19 skills)"),
 ("sentry-sdk-setup", "getsentry/sentry-for-ai", "", "Official: add Sentry to any stack, fix issues via MCP (34 skills)"),
]),
("Developers: security", "From Trail of Bits, one of the best-known security firms (97 skills).", [
 ("semgrep / codeql", "trailofbits/skills", "", "Static analysis with Semgrep and CodeQL"),
 ("supply-chain-risk-auditor", "trailofbits/skills", "", "Checks dependencies for supply-chain risk"),
 ("differential-review", "trailofbits/skills", "", "Security review of a diff"),
 ("property-based-testing", "trailofbits/skills", "", "Finds bugs with generated inputs"),
 ("libfuzzer / aflpp / cargo-fuzz", "trailofbits/skills", "", "Fuzzing harnesses for C/C++/Rust"),
 ("solana / cosmos / ton vulnerability scanners", "trailofbits/skills", "", "Smart-contract vulnerability checks"),
 ("security-reviewer", JA, "skills/security-reviewer", "Structured audit report with severity"),
]),
("Designers", "UI, brand and visuals.", [
 ("ui-ux-pro-max", UX, ".claude/skills/ui-ux-pro-max", "Design intelligence for pages, components, apps"),
 ("design", UX, ".claude/skills/design", "Brand identity, tokens, logos (55 styles), CI kits"),
 ("design-system", UX, ".claude/skills/design-system", "Token architecture and component specs"),
 ("ui-styling", UX, ".claude/skills/ui-styling", "shadcn/ui + Tailwind interfaces"),
 ("banner-design", UX, ".claude/skills/banner-design", "Banners for social, ads, heroes and print"),
 ("brand", UX, ".claude/skills/brand", "Brand voice, identity, messaging frameworks"),
 ("slides", UX, ".claude/skills/slides", "Strategic HTML presentations with charts"),
 ("frontend-design", A, "skills/frontend-design", "Distinctive UI instead of AI-default look"),
 ("canvas-design", A, "skills/canvas-design", "Posters and covers as PNG/PDF from a design philosophy"),
 ("theme-factory", A, "skills/theme-factory", "10 ready themes for any artifact"),
 ("algorithmic-art", A, "skills/algorithmic-art", "Generative art with p5.js and live sliders"),
 ("web-artifacts-builder", A, "skills/web-artifacts-builder", "React + Tailwind + shadcn artifacts in one HTML file"),
 ("brand-guidelines", A, "skills/brand-guidelines", "Example of applying brand colors and type"),
 ("web-design-guidelines", VL, "skills/web-design-guidelines", "Audits accessibility and UX of your UI"),
 ("apple-hig-expert", AR, "", "Apple Human Interface Guidelines"),
 ("ux-researcher-designer", AR, "", "UX research and design"),
]),
("SEO and AI search", "Classic SEO plus getting cited by ChatGPT, Perplexity, AI Overviews.", [
 ("seo", SEO, "skills/seo", "Orchestrator for all SEO checks"),
 ("seo-audit", SEO, "skills/seo-audit", "Full-site scored, prioritized audit"),
 ("seo-page", SEO, "skills/seo-page", "Single-URL analysis"),
 ("seo-technical", SEO, "skills/seo-technical", "Crawlability, indexability, Core Web Vitals"),
 ("seo-content / seo-content-brief", SEO, "skills/seo-content", "Content and briefs for ranking"),
 ("seo-cluster", SEO, "skills/seo-cluster", "Topic clusters"),
 ("seo-backlinks", SEO, "skills/seo-backlinks", "Backlink profile, toxic links, gaps"),
 ("seo-geo", SEO, "skills/seo-geo", "Generative engine optimization"),
 ("seo-local / seo-maps", SEO, "skills/seo-local", "Local SEO and Maps"),
 ("seo-ecommerce", SEO, "skills/seo-ecommerce", "Store SEO"),
 ("seo-schema", SEO, "skills/seo-schema", "Structured data"),
 ("seo-programmatic", SEO, "skills/seo-programmatic", "Pages at scale from templates"),
 ("seo-image-gen", SEO, "skills/seo-image-gen", "OG images, heroes, infographics via Gemini"),
 ("seo-audit", MK, "skills/seo-audit", "Diagnoses why you are not ranking"),
 ("ai-seo", MK, "skills/ai-seo", "Get cited by LLMs (AEO/GEO)"),
 ("programmatic-seo", MK, "skills/programmatic-seo", "Template pages at scale"),
 ("schema", MK, "skills/schema", "JSON-LD and rich results"),
 ("site-architecture", MK, "skills/site-architecture", "Page hierarchy, URLs, internal links"),
 ("link-building", MK, "skills/link-building", "Earn backlinks and mentions"),
 ("competitors", MK, "skills/competitors", "Alternative and vs pages"),
 ("directory-submissions", MK, "skills/directory-submissions", "Submits to startup/AI/SaaS directories for links"),
 ("web-perf", "cloudflare/skills", "", "Core Web Vitals audit and fixes"),
]),
("Marketing and growth", "53 skills in one repo; this is the best single marketing pack.", [
 ("marketing-plan", MK, "skills/marketing-plan", "Full marketing plan for a product"),
 ("marketing-ideas", MK, "skills/marketing-ideas", "Growth ideas for SaaS"),
 ("launch", MK, "skills/launch", "Launches, Product Hunt, announcements"),
 ("cro", MK, "skills/cro", "Raises conversion on any page or form"),
 ("ab-testing", MK, "skills/ab-testing", "Designs experiments"),
 ("pricing", MK, "skills/pricing", "Pricing, tiers, packaging"),
 ("offers", MK, "skills/offers", "Builds the offer: value, bonuses, guarantee"),
 ("emails", MK, "skills/emails", "Email sequences and lifecycle flows"),
 ("cold-email", MK, "skills/cold-email", "B2B outbound that gets replies"),
 ("lead-magnets", MK, "skills/lead-magnets", "Gated content for email capture"),
 ("referrals", MK, "skills/referrals", "Referral and affiliate programs"),
 ("churn-prevention", MK, "skills/churn-prevention", "Cancel flows, save offers, dunning"),
 ("analytics", MK, "skills/analytics", "GA4 and event tracking"),
 ("attribution", MK, "skills/attribution", "Which marketing actually drives revenue"),
 ("customer-research", MK, "skills/customer-research", "ICP research from transcripts"),
 ("competitor-profiling", MK, "skills/competitor-profiling", "Competitor research from URLs"),
 ("reverse-engineer-marketing", MK, "skills/reverse-engineer-marketing", "How another company grew, and what to copy"),
 ("marketing-council", MK, "skills/marketing-council", "Simulated board of legendary marketers"),
 ("marketing-psychology", MK, "skills/marketing-psychology", "Behavioral science for marketing"),
 ("marketing-loops", MK, "skills/marketing-loops", "Recurring marketing workflows an agent runs"),
 ("public-relations", MK, "skills/public-relations", "Press and journalist outreach"),
 ("aso", MK, "skills/aso", "App Store / Google Play listing optimization"),
 ("community-marketing", MK, "skills/community-marketing", "Discord/Slack community growth"),
 ("growth-marketer / cmo-advisor", AR, "", "Growth and CMO-level advice"),
]),
("Copywriting and content", "Writing that sells and reads like a person.", [
 ("copywriting", MK, "skills/copywriting", "Homepage, landing, pricing, product copy"),
 ("copy-editing", MK, "skills/copy-editing", "Edits and refreshes existing copy"),
 ("content-strategy", MK, "skills/content-strategy", "What to write and why"),
 ("sales-enablement", MK, "skills/sales-enablement", "Decks, one-pagers, objection docs"),
 ("content-humanizer", AR, "", "Removes AI tone from text"),
 ("content-creator / content-production", AR, "", "Content pipeline end to end"),
 ("email-sequence", AR, "", "Email sequences"),
 ("writing-guidelines", VL, "skills/writing-guidelines", "Audits docs voice and tone"),
 ("doc-coauthoring", A, "skills/doc-coauthoring", "Structured co-writing of specs and proposals"),
 ("internal-comms", A, "skills/internal-comms", "Company updates in house formats"),
 ("writing-fragments / writing-beats / writing-shape", MP, "skills/in-progress", "Matt Pocock's 3-step article writing loop"),
]),
("SMM, X and LinkedIn", "Social content, scheduling, analytics.", [
 ("social", MK, "skills/social", "Content for LinkedIn, X, Instagram, TikTok, plus listening"),
 ("influencer-marketing", MK, "skills/influencer-marketing", "Finds, vets and briefs creators"),
 ("co-marketing", MK, "skills/co-marketing", "Partner campaigns"),
 ("social-media-manager", AR, "", "Runs social channels"),
 ("social-media-analyzer", AR, "", "Analyzes social performance"),
 ("social-content", AR, "", "Social post creation"),
 ("x-twitter-growth", AR, "", "X growth"),
 ("linkedin-content / -strategy / -engagement / -profile / -analytics", AR, "", "Five LinkedIn skills"),
 ("youtube-full / video-content-strategist", AR, "", "YouTube channel and video strategy"),
 ("youtube", "agricidaniel/claude-youtube", "", "YouTube SEO and channel work"),
 ("x-reach (ours)", "", "skills/x-reach", "How to write X posts that get reach, from data on 2,194 posts"),
]),
("UGC, ads and creatives", "Ads that convert, scripts for UGC videos.", [
 ("ad-creative", MK, "skills/ad-creative", "Headlines, primary text, full ad variations at scale"),
 ("ads", MK, "skills/ads", "Google, Meta, LinkedIn, X ad campaigns"),
 ("video", MK, "skills/video", "AI and programmatic video production"),
 ("image", MK, "skills/image", "Marketing images: heroes, social, mockups"),
 ("paid-ads / ad-creative", AR, "", "Paid ads and creatives"),
 ("landing-page-generator", AR, "", "Landing pages for campaigns"),
 ("banner-design", UX, ".claude/skills/banner-design", "Ad and social banners"),
]),
("Video and motion", "Videos and animation written as code.", [
 ("remotion-best-practices", RM, "skills/remotion-best-practices", "Official Remotion router skill"),
 ("remotion-create", RM, "skills/remotion-create", "New Remotion video"),
 ("remotion-captions", RM, "skills/remotion-captions", "Transcribe and animate captions"),
 ("remotion-render", RM, "skills/remotion-render", "Export the video"),
 ("remotion-maps", RM, "skills/remotion-maps", "Map animations"),
 ("huashu-motion", "alchaincyf/huashu-motion", "", "Launch videos and explainers; click a frame to fix that part"),
 ("mg-styles-15", "Vincentwei1021/mg-styles-15", "", "15 motion-graphics styles with demos and prompts"),
 ("pixelfx", "patch-gg/pixelfx", "", "244 pixel effects plus a pixel-artist skill"),
 ("slack-gif-creator", A, "skills/slack-gif-creator", "Animated GIFs that fit Slack limits"),
 ("demo-video", AR, "", "Product demo videos"),
]),
("Docs, slides, spreadsheets", "Office files from plain language.", [
 ("pdf", A, "skills/pdf", "Read, merge, split, fill PDFs"),
 ("docx", A, "skills/docx", "Word documents with real formatting"),
 ("pptx", A, "skills/pptx", "Slide decks"),
 ("xlsx", A, "skills/xlsx", "Spreadsheets with formulas and charts"),
 ("md-slides / md-document", AR, "", "Markdown to slides and documents"),
]),
("Product, founders, business", "PRDs, strategy, C-level thinking.", [
 ("write-a-prd / to-spec", MP, "skills/engineering/to-spec", "Specs from conversation"),
 ("grill-with-docs", MP, "skills/engineering/grill-with-docs", "Stress-tests a plan and writes ADRs"),
 ("prd / product-manager / roadmap-communicator", AR, "", "Product management pack"),
 ("ceo-advisor / cto-advisor / cfo-advisor", AR, "", "Board of C-level advisors"),
 ("solo-founder / founder-coach", AR, "", "For one-person companies"),
 ("saas-metrics-coach / financial-analyst", AR, "", "SaaS metrics and finance"),
 ("okr / rice / sprint-plan", AR, "", "Planning frameworks"),
 ("soc2 / gdpr / iso27001 audit prep", AR, "", "Compliance readiness"),
 ("feature-forge", JA, "skills/feature-forge", "Requirements workshops into specs"),
 ("the-fool", JA, "skills/the-fool", "Structured critique of any plan"),
]),
("Research and knowledge", "Second brain, notes, deep research.", [
 ("obsidian-cli / obsidian-bases / json-canvas", "kepano/obsidian-skills", "", "By Obsidian's CEO: vault, Bases, Canvas"),
 ("defuddle", "kepano/obsidian-skills", "", "Any web page to clean Markdown"),
 ("notebooklm", "pleaseprompto/notebooklm-skill", "", "Query your NotebookLM notebooks from Claude Code"),
 ("deep-research", "199-biotechnologies/claude-deep-research-skill", "", "Multi-source research with citations"),
 ("research", MP, "skills/engineering/research", "Research from primary sources into a Markdown file"),
 ("digital-brain", CE, "", "Personal operating-system workflows"),
 ("llm-wiki / wiki-ingest / wiki-query", AR, "", "Build a wiki the agent maintains"),
 ("market-research / litreview / patent", AR, "", "Research pack"),
]),
("AI agents, context and evals", "For people building agents.", [
 ("context-optimization", CE, "", "Context budgeting so the agent doesn't degrade"),
 ("context-compression", CE, "", "Compaction for long sessions"),
 ("multi-agent-patterns", CE, "", "Multi-agent design"),
 ("memory-systems", CE, "", "Persistent agent memory"),
 ("harness-engineering", CE, "", "Designing autonomous agent harnesses"),
 ("tool-design", CE, "", "Tool interfaces agents use well"),
 ("evaluation / advanced-evaluation", CE, "", "LLM-as-judge and agent evals"),
 ("error-analysis", "hamelsmu/evals-skills", "", "Hamel Husain's eval workflow"),
 ("write-judge-prompt", "hamelsmu/evals-skills", "", "Judge prompts that agree with humans"),
 ("evaluate-rag", "hamelsmu/evals-skills", "", "RAG evaluation"),
 ("rag-architect / prompt-engineer / fine-tuning-expert", JA, "", "Agent and model building"),
 ("context-engineering-kit", "neolabhq/context-engineering-kit", "", "70 commands: judge, critique, tree-of-thoughts, kaizen"),
]),
]

INDEX = {
 "anthropics/skills": "algorithmic-art, brand-guidelines, canvas-design, claude-api, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing, xlsx",
 "obra/superpowers": "brainstorming, diagnosing-superpowers, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans, writing-skills",
 "mattpocock/skills": "ask-matt, code-review, codebase-design, diagnosing-bugs, domain-modeling, grill-with-docs, implement-spec, implement, improve-codebase-architecture, pr, prototype, research, retro, setup-matt-pocock-skills, tdd, to-spec, to-tickets, triage, wayfinder, wizard, chief-of-staff, claude-handoff, loop-me, setup-ts-deep-modules, software-factory, writing-beats, writing-fragments, writing-shape, git-guardrails-claude-code, migrate-to-shoehorn, scaffold-exercises, setup-pre-commit, grill-me, grilling, handoff, teach, to-questionnaire, wait-what, writing-for-agents",
 "vercel-labs/agent-skills": "composition-patterns, deploy-to-vercel, react-best-practices, react-native-skills, react-view-transitions, vercel-cli-with-tokens, vercel-optimize, web-design-guidelines, writing-guidelines",
 "coreyhaines31/marketingskills": "ab-testing, ad-creative, ads, ai-seo, analytics, aso, attribution, churn-prevention, co-marketing, cold-email, community-marketing, competitor-profiling, competitors, content-strategy, conversion-tracking, copy-editing, copywriting, cro, customer-research, directory-submissions, emails, events, free-tools, image, influencer-marketing, launch, lead-magnets, link-building, marketing-council, marketing-ideas, marketing-loops, marketing-plan, marketing-psychology, offers, onboarding, paywalls, popups, pricing, product-marketing, programmatic-seo, prospecting, public-relations, referrals, reverse-engineer-marketing, revops, sales-enablement, schema, seo-audit, signup, site-architecture, sms, social, video",
 "agricidaniel/claude-seo": "seo, seo-agentic, seo-audit, seo-backlinks, seo-cluster, seo-competitor-pages, seo-content-brief, seo-content, seo-dataforseo, seo-drift, seo-ecommerce, seo-flow, seo-geo, seo-google, seo-hreflang, seo-image-gen, seo-images, seo-local, seo-maps, seo-page, seo-plan, seo-programmatic, seo-schema, seo-sitemap, seo-sxo, seo-technical; extensions: seo-ahrefs, seo-bing, seo-dataforseo, seo-firecrawl, seo-matomo, seo-profound, seo-seranking, seo-unlighthouse",
 "nextlevelbuilder/ui-ux-pro-max-skill": "ui-ux-pro-max, design, design-system, ui-styling, banner-design, brand, slides",
 "remotion-dev/skills": "remotion-best-practices, remotion-captions, remotion-create, remotion-docs, remotion-interactivity, remotion-license, remotion-maps, remotion-markup, remotion-multimedia, remotion-render, remotion-saas, remotion-studio, remotion-upgrade",
 "hamelsmu/evals-skills": "build-review-interface, error-analysis, eval-audit, evaluate-rag, generate-synthetic-data, validate-evaluator, write-judge-prompt",
 "muratcankoylan/agent-skills-for-context-engineering": "context-engineering-collection, book-sft-pipeline, digital-brain, reasoning-trace-optimizer, comprehensive-research-agent, advanced-evaluation, bdi-mental-states, context-compression, context-degradation, context-fundamentals, context-optimization, evaluation, filesystem-context, harness-engineering, hosted-agents, latent-briefing, long-horizon-prompting, memory-systems, multi-agent-patterns, project-development, self-improvement-loops, self-managed-context, tool-design",
 "kepano/obsidian-skills": "defuddle, json-canvas, knap, obsidian-bases, obsidian-cli, obsidian-markdown",
 "supabase/agent-skills": "supabase, supabase-postgres-best-practices",
 "cloudflare/skills": "agents-sdk, basin, cf-cli, cloudflare-email-service, cloudflare-one-migrations, cloudflare-one, cloudflare, durable-objects, gateway-workers, k2, nextjs-on-cloudflare, sandbox-migrate-to-next, sandbox-next, sandbox-stable, turnstile-spin, web-perf, workers-best-practices, workers-profiling, wrangler",
 "getsentry/sentry-for-ai": "sentry-sdk-setup, sentry-android-sdk, sentry-browser-sdk, sentry-cloudflare-sdk, sentry-cocoa-sdk, sentry-dotnet-sdk, sentry-elixir-sdk, sentry-flutter-sdk, sentry-go-sdk, sentry-nestjs-sdk, sentry-nextjs-sdk, sentry-node-sdk, sentry-php-sdk, sentry-python-sdk, sentry-react-native-sdk, sentry-react-router-framework-sdk, sentry-react-sdk, sentry-ruby-sdk, sentry-svelte-sdk, sentry-tanstack-start-sdk, sentry-fix-issues, sentry-instrument-logging, sentry-instrumentation-guide, sentry-sdk-skill-creator, sentry-sdk-upgrade, sentry-setup-ai-monitoring, sentry-create-alert, sentry-debug-issue, sentry-fix-stack-traces, sentry-get-started, sentry-instrument, sentry-otel-exporter-setup, sentry-setup-releases, sentry-snapshots-cocoa",
 "forrestchang/andrej-karpathy-skills": "karpathy-guidelines",
 "jeffallan/claude-skills": "angular-architect, api-designer, architecture-designer, atlassian-mcp, chaos-engineer, cli-developer, cloud-architect, code-documenter, code-reviewer, cpp-pro, csharp-developer, database-optimizer, debugging-wizard, devops-engineer, django-expert, django-storages-s3, dotnet-core-expert, embedded-systems, fastapi-expert, feature-forge, fine-tuning-expert, flutter-expert, fullstack-guardian, game-developer, golang-pro, graphql-architect, java-architect, javascript-pro, kotlin-specialist, kubernetes-specialist, laravel-specialist, legacy-modernizer, mcp-developer, microservices-architect, ml-pipeline, monitoring-expert, nestjs-expert, nextjs-developer, pandas-pro, php-pro, playwright-expert, postgres-pro, prompt-engineer, python-pro, rag-architect, rails-expert, react-expert, react-native-expert, rust-engineer, salesforce-developer, secure-code-guardian, security-reviewer, shopify-expert, spark-engineer, spec-miner, spring-boot-engineer, sql-pro, sre-engineer, swift-expert, terraform-engineer, test-master, the-fool, typescript-pro, vue-expert-js, vue-expert, websocket-engineer, wordpress-pro",
 "199-biotechnologies/claude-deep-research-skill": "deep-research",
 "pleaseprompto/notebooklm-skill": "notebooklm",
 "alchaincyf/huashu-motion": "huashu-motion",
 "neolabhq/context-engineering-kit": "actualize, add-task, agent-evaluation, analyse-problem, analyse, analyze-issue, apply-anthropic-skill-best-practices, attach-review-to-pr, brainstorm, build-mcp, cause-and-effect, commit, context-engineering, create-agent, create-command, create-hook, create-ideas, create-pr, create-rule, create-skill, create-workflow-command, critique, decay, design-testing-strategy, do-and-judge, do-competitively, do-in-parallel, do-in-steps, fix-tests, git-notes, git-worktrees, implement-task, judge-with-debate, judge, kaizen, launch-sub-agent, load-issues, load-pr-comments, memorize, multi-agent-patterns, plan-do-check-act, plan-task, prompt-engineering, propose-hypotheses, query, reflect, reset, resolve-fixed-pr-comments, review-local-changes, review-pr, root-cause-tracing, setup-arxiv-mcp, setup-codemap-cli, setup-context7-mcp, setup-serena-mcp, status, subagent-driven-development, test-coverage, test-driven-development, test-prompt, test-skill, thought-based-reasoning, traiage-review, tree-of-thoughts, update-docs, why, write-concisely, write-tests",
 "trailofbits/skills": "agentic-actions-auditor, audit-context-building, algorand-vulnerability-scanner, audit-prep-assistant, cairo-vulnerability-scanner, code-maturity-assessor, cosmos-vulnerability-scanner, guidelines-advisor, secure-workflow-guide, solana-vulnerability-scanner, substrate-vulnerability-scanner, token-integration-analyzer, ton-vulnerability-scanner, burpsuite-project-parser, c-review, chrome-mcp-troubleshooting, code-improver, pr-improver, skill-improver, review-pr, panel-review, constant-time-analysis, interpreting-culture-index, devcontainer-setup, differential-review, dimensional-analysis, dwarf-expert, entry-point-analyzer, firebase-apk-scanner, fp-check, gh-cli, github-triage, goal-prompt, let-fate-decide, modern-cpp, modern-python, mutation-testing, open-sourcing, implement-patch, patching-bugs, prove-patch, reproduce-bug, validate-bug, post-patch-validation, property-based-testing, adjudicate-regression, hunt-regressions, prepare-regression, regression-hunt, replay-regression, report-regressions, reproduce-regression, review-walkthrough, rust-review, second-opinion, semgrep-rule-creator, semgrep-rule-variant-creator, sharp-edges, spec-to-code-compliance, codeql, sarif-parsing, semgrep, supply-chain-risk-auditor, address-sanitizer, aflpp, atheris, cargo-fuzz, constant-time-testing, coverage-analysis, fuzzing-dictionary, fuzzing-obstacles, harness-writing, libafl, libfuzzer, ossfuzz, ruzzy, testing-handbook-generator, wycheproof, audit-augmentation, crypto-protocol-diagram, diagramming-code, genotoxic, graph-evolution, mermaid-to-proverif, slicing-code-context, trailmark-finding-triage, trailmark-review-gate, trailmark-structural, trailmark-summary, trailmark-variant-neighborhood, trailmark, vector-forge, variant-analysis, vulnerability-triage-brocards, writing-lean-proofs, yara-rule-authoring, zeroize-audit",
}
INDEX["alirezarezvani/claude-skills"] = open(__file__.replace("build.py", "data/alirezarezvani.txt")).read().strip()

def stars(r):
    s = REPOS.get(r, (0,))[0]
    return f"{s/1000:.0f}k" if s >= 1000 else (str(s) if s else "")

EMO = ["🏆","💻","🧩","🛡️","🎨","🔎","📈","✍️","📱","🎯","🎬","📄","🚀","🧠","🤖"]
SHORT = ["Start here","Dev workflow","Dev stacks","Security","Design","SEO","Marketing","Copywriting","SMM","UGC & Ads","Video","Docs","Product","Research","AI agents"]
SHOW = 3

def row(sk, repo, path, desc):
    if not repo:
        return f"| [**{sk}**]({path}) | {desc} | this repo |"
    return f"| [**{sk}**]({L(repo, path)}) | {desc} | [{repo}]({GH}{repo}) |"

def main():
    total = sum(len([x for x in v.replace("; extensions:", ",").split(",") if x.strip()]) for v in INDEX.values())
    nrepos = len(open(__file__.replace('build.py','data/repos.txt')).read().split())
    out = []
    w = out.append
    w('<p align="center"><img src="assets/cover.png" alt="Every Claude skill you actually need" width="100%"></p>\n')
    w('<p align="center">')
    for lab, val, col in [("skills", str(total), "1d7f86"), ("repos", str(nrepos), "1d7f86"), ("niches", str(len(SECTIONS)-1), "1d7f86"), ("updated", "nov 2026", "e8b04a"), ("license", "MIT", "3c7d3c")]:
        w(f'  <img src="https://img.shields.io/badge/{lab}-{val.replace(" ", "%20")}-{col}?style=flat-square" alt="{lab}">')
    w('  <a href="https://x.com/f0rgent"><img src="https://img.shields.io/badge/follow-@f0rgent-000000?style=flat-square&logo=x" alt="follow @f0rgent"></a>')
    w('</p>\n')
    w('<p align="center">' + " · ".join(f'<a href="#s{i}">{SHORT[i]}</a>' for i in range(1, len(SECTIONS))) + '</p>\n')
    w('<p align="center"><b>The best open-source skills for Claude Code, sorted by what you do.</b><br>Every skill links to its original author, so you always get the latest version.<br>The list keeps growing. ⭐ Star the repo to get updates.</p>\n')
    w("## ⚡ Install in 10 seconds\n")
    w("```bash\n# one skill\nnpx skills@latest add coreyhaines31/marketingskills/copywriting\n\n# everything in this catalog (pulls each repo from its author)\ngit clone --recursive https://github.com/f0rgent/claude-skills-catalog\n```\n")
    name, intro, rows = SECTIONS[0]
    w(f'<a id="s0"></a>\n## {EMO[0]} Start here: top 10\n\n{intro}\n')
    w("| # | Skill | What it does | Repo | ⭐ |\n|---|---|---|---|---|")
    for k, (sk, repo, path, desc) in enumerate(rows, 1):
        w(f"| {k} | [**{sk}**]({L(repo, path)}) | {desc} | [{repo}]({GH}{repo}) | {stars(repo)} |")
    w("\n## 🗂 Browse by niche\n")
    w("<table>")
    cells = list(range(1, len(SECTIONS)))
    for r0 in range(0, len(cells), 4):
        w("<tr>")
        for i in cells[r0:r0+4]:
            w(f'<td align="center" width="25%"><a href="#s{i}"><h1>{EMO[i]}</h1><b>{SHORT[i]}</b></a><br><sub>{len(SECTIONS[i][2])} picks</sub></td>')
        w("</tr>")
    w("</table>\n")
    for i in range(1, len(SECTIONS)):
        name, intro, rows = SECTIONS[i]
        w(f'<a id="s{i}"></a>\n## {EMO[i]} {name}\n\n{intro}\n')
        w("| Skill | What it does | Repo |\n|---|---|---|")
        for r in rows[:SHOW]:
            w(row(*r))
        if len(rows) > SHOW:
            w(f"\n<details><summary><b>Show all {len(rows)} {SHORT[i].lower()} skills</b></summary>\n")
            w("| Skill | What it does | Repo |\n|---|---|---|")
            for r in rows[SHOW:]:
                w(row(*r))
            w("\n</details>")
        w('\n<p align="right"><a href="#s0">↑ top</a></p>\n')
    w("> [!TIP]")
    w("> **Bonus: [x-reach](skills/x-reach/SKILL.md)**. Our own skill: how to write X posts that get reach, built from a study of 2,194 video posts across 300 accounts plus our own tests. Install it like any other skill.\n")
    w("## 📚 Full index\n")
    w(f"<details><summary><b>All {total} skills, grouped by repo</b></summary>\n")
    w("| Repo | ⭐ | License | Skills |\n|---|---|---|---|")
    for r in REPOS:
        if r in INDEX:
            n = len([x for x in INDEX[r].replace("; extensions:", ",").split(",") if x.strip()])
            w(f"| [{r}]({GH}{r}) ({n}) | {stars(r)} | {REPOS[r][1]} | {INDEX[r]} |")
    w("\n</details>\n")
    w("## 📝 Notes\n")
    w("- Names and descriptions were read from each skill's SKILL.md; stars from GitHub on 2026-11-04.")
    w("- Our own files (this README, build.py, install.sh, skills/x-reach) are MIT. Everything under vendor/ belongs to its authors and keeps its own license. Repos with no license stated are linked, not copied.")
    w("- Lists that pointed us to these repos: @Bober_smart, @Mr_Buzzoni, @zodchiii, @eng_khairallah1, @Mnilax, @e1genqq, @DDJCXX, @fayzonnn on X.\n")
    w('<p align="center"><sub>Made by <a href="https://x.com/f0rgent">@f0rgent</a> · Showing how AI agents actually do practical things + giving away the prompts</sub></p>')
    open(__file__.replace("build.py", "README.md"), "w").write("\n".join(out))
    print("skills in index:", total)

main()
