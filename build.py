#!/usr/bin/env python3
"""Builds README.md (catalog by niche) from the data below.
Data collected 2026-11-04 from the repos' SKILL.md files and GitHub stats."""

GH = "https://github.com/"

REPOS = {
    # repo: (stars, license, default_branch)
    "anthropics/skills": (187236, "see repo (some source-available)", "main"),
    "obra/superpowers": (312086, "MIT", "main"),
    "massgen/massgen": (1100, "Apache-2.0", "main"),
    "blader/humanizer": (64600, "MIT", "main"),
    "heygen-com/hyperframes": (78600, "Apache-2.0", "main"),
    "retieedra-profound/skills-marketing-library": (3, "MIT", "main"),
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
    "ComposioHQ/awesome-claude-skills": (0, "none stated", "master"),
    "VoltAgent/awesome-design-md": (0, "MIT", "main"),
    "wshobson/agents": (0, "MIT", "main"),
    "phuryn/pm-skills": (0, "MIT", "main"),
    "deanpeters/Product-Manager-Skills": (0, "CC-BY-NC-SA-4.0", "main"),
    "aaron-he-zhu/aaron-marketing-skills": (0, "Apache-2.0", "main"),
    "Eronred/aso-skills": (0, "MIT", "main"),
    "ognjengt/founder-skills": (0, "MIT", "main"),
    "BrianRWagner/ai-marketing-skills": (0, "none stated", "main"),
    "realkimbarrett/advertising-skills": (0, "none stated", "main"),
    "CosmoBlk/email-marketing-bible": (0, "MIT", "main"),
    "Xquik-dev/tweetclaw": (0, "MIT", "master"),
    "greensock/gsap-skills": (0, "MIT", "main"),
    "czlonkowski/n8n-skills": (0, "MIT", "main"),
    "addyosmani/agent-skills": (0, "MIT", "main"),
    "safishamsi/graphify": (0, "Apache-2.0", "v8"),
    "browser-use/video-use": (0, "MIT", "main"),
    "digitalsamba/claude-code-video-toolkit": (0, "MIT", "main"),
    "typefully/agent-skills": (0, "MIT", "main"),
    "firecrawl/firecrawl-claude-plugin": (0, "MIT", "main"),
    "hashicorp/agent-skills": (0, "MPL-2.0", "main"),
    "MicrosoftDocs/Agent-Skills": (0, "CC-BY-4.0", "main"),
    "awslabs/agent-plugins": (0, "Apache-2.0", "main"),
    "K-Dense-AI/claude-scientific-skills": (0, "MIT", "main"),
    "BehiSecc/VibeSec-Skill": (0, "Apache-2.0", "main"),
    "feedtailor/ccskill-nanobanana": (0, "MIT", "main"),
    "kingbootoshi/nano-banana-2-skill": (0, "MIT", "main"),
    "hungv47/meta-skills": (0, "MIT", "main"),
    "gokapso/agent-skills": (198, "none stated", "master"),
    "olelehmann100kMRR/autoresearch-skill": (0, "none stated", "main"),
    "elvarofficial/teardown": (1975, "MIT", "main"),
    "cursor/plugins": (0, "MIT", "main"),
    "whaleyxbt/claude-motion": (0, "MIT", "main"),
    "lemomo-ai/lemo-opuscar": (13200, "MIT", "main"),
    "Mort1d/motion-graphics-skills": (78, "MIT", "main"),
    "howseen-ai/claude-motion-design": (0, "MIT", "main"),
    "charlie947/motion-graphics-skills": (0, "MIT", "main"),
    "haidrrrry/claude-remotion-skill": (0, "MIT", "main"),
    "t3knobox/klik-anim-skill-creation": (0, "none stated", "main"),
    "Sunwood-ai-labs/hyperframes-motion-reel-skill": (0, "MIT", "main"),
    "AbubakrChan/product-launch-motion": (0, "MIT", "main"),
    "cth9191/animate": (0, "MIT", "main"),
    "iart-ai/motion-design-skills": (0, "MIT", "main"),
    "nateherkai/hyperframes-student-kit": (0, "MIT", "main"),
    "LottieFiles/motion-design-skill": (0, "MIT", "main"),
    "frankxai/awesome-motion-design-agent-skills": (0, "CC0-1.0", "main"),
    "Barty-Bart/motion-graphics": (0, "MIT", "main"),
    "199-biotechnologies/motion-dev-animations-skill": (0, "MIT", "main"),
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
 ("file-search", "massgen/massgen", "massgen/skills/file-search", "Fast code search with ripgrep for text and ast-grep for syntax"),
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
 ("spec-driven-development", "addyosmani/agent-skills", "skills/spec-driven-development", "Writes the spec before any code (Addy Osmani)"),
 ("incremental-implementation", "addyosmani/agent-skills", "skills/incremental-implementation", "Ships changes in thin, verifiable slices"),
 ("doubt-driven-development", "addyosmani/agent-skills", "skills/doubt-driven-development", "Fresh-context adversarial review of each non-trivial decision"),
 ("interview-me", "addyosmani/agent-skills", "skills/interview-me", "Pulls out what you actually want before building"),
 ("multi-reviewer-patterns", "wshobson/agents", "plugins/agent-teams/skills/multi-reviewer-patterns", "Parallel code review across several quality dimensions"),
 ("parallel-debugging", "wshobson/agents", "plugins/agent-teams/skills/parallel-debugging", "Debugs with competing hypotheses investigated in parallel"),
 ("changelog-generator", "ComposioHQ/awesome-claude-skills", "changelog-generator", "User-facing changelogs from git history"),
 ("graphify", "safishamsi/graphify", "", "Turns a codebase or any folder into a queryable knowledge graph"),
 ("statechart / create-formal-verification-skill", "cursor/plugins", "pstack/skills/statechart", "Lauren Tan's pstack: models state machines in TLA+ and finds logic bugs"),
 ("pstack (58 skills)", "cursor/plugins", "pstack", "Lauren Tan's skills for careful agent coding: arena, blast-radius, swarm, unslop"),
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
 ("agents (185 skills)", "wshobson/agents", "", "Big pack of plugins: languages, infra, data, testing, accessibility"),
 ("gsap-core / gsap-scrolltrigger / gsap-react", "greensock/gsap-skills", "", "Official GSAP animation skills"),
 ("terraform-style-guide / terraform-test", "hashicorp/agent-skills", "", "Official HashiCorp: Terraform and Packer"),
 ("deploy / aws-lambda", "awslabs/agent-plugins", "", "Official AWS: deploy, serverless, SageMaker"),
 ("azure-* (201 skills)", "MicrosoftDocs/Agent-Skills", "", "Official Microsoft Docs: one skill per Azure service"),
]),
("Developers: security", "From Trail of Bits, one of the best-known security firms (97 skills).", [
 ("semgrep / codeql", "trailofbits/skills", "", "Static analysis with Semgrep and CodeQL"),
 ("supply-chain-risk-auditor", "trailofbits/skills", "", "Checks dependencies for supply-chain risk"),
 ("differential-review", "trailofbits/skills", "", "Security review of a diff"),
 ("property-based-testing", "trailofbits/skills", "", "Finds bugs with generated inputs"),
 ("libfuzzer / aflpp / cargo-fuzz", "trailofbits/skills", "", "Fuzzing harnesses for C/C++/Rust"),
 ("solana / cosmos / ton vulnerability scanners", "trailofbits/skills", "", "Smart-contract vulnerability checks"),
 ("security-reviewer", JA, "skills/security-reviewer", "Structured audit report with severity"),
 ("VibeSec-Skill", "BehiSecc/VibeSec-Skill", "", "Makes Claude write secure web apps by default"),
 ("security-and-hardening", "addyosmani/agent-skills", "skills/security-and-hardening", "Hardens input handlers and auth against common vulnerabilities"),
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
 ("awesome-design-md", "VoltAgent/awesome-design-md", "", "84 DESIGN.md files from real sites to drop into a project"),
 ("design", "firecrawl/firecrawl-claude-plugin", "skills/design", "Extracts a site's visual system into an implementation-ready DESIGN.md"),
 ("brand-identity", "firecrawl/firecrawl-claude-plugin", "skills/brand-identity", "Collects a company's logo, palette and fonts"),
 ("nano-banana", "kingbootoshi/nano-banana-2-skill", "", "Image generation with Gemini via the nano-banana CLI"),
 ("ccskill-nanobanana", "feedtailor/ccskill-nanobanana", "", "Generate and edit images with Nano Banana (Gemini Image API)"),
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
 ("keyword-research", "aaron-he-zhu/aaron-marketing-skills", "seo-geo/survey/keyword-research", "Keyword research, part of a full SEO/GEO pack"),
 ("geo-content-optimizer", "aaron-he-zhu/aaron-marketing-skills", "seo-geo/implement/geo-content-optimizer", "Optimizes content to get cited by AI answers"),
 ("technical-seo-checker", "aaron-he-zhu/aaron-marketing-skills", "seo-geo/tune/technical-seo-checker", "Technical SEO checks"),
 ("content-gap-analysis", "aaron-he-zhu/aaron-marketing-skills", "seo-geo/survey/content-gap-analysis", "Finds topics competitors cover and you don't"),
 ("ai-discoverability-audit", "BrianRWagner/ai-marketing-skills", "ai-discoverability-audit", "How your brand shows up in ChatGPT, Perplexity, Claude"),
 ("seo-audit", "firecrawl/firecrawl-claude-plugin", "skills/seo-audit", "Inspects titles, meta, headings, canonicals, structured data"),
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
 ("aso-audit / metadata-optimization", "Eronred/aso-skills", "skills/aso-audit", "40 App Store / Google Play skills: ASO, paywalls, Apple Search Ads"),
 ("email-marketing-bible", "CosmoBlk/email-marketing-bible", "skills/email-marketing-bible", "Email marketing manual with send-safety gates, any ESP"),
 ("go-to-market-plan", "ognjengt/founder-skills", "skills/go-to-market-plan", "3 best GTM strategies from your business context"),
 ("product-hunt-launch-plan", "ognjengt/founder-skills", "skills/product-hunt-launch-plan", "Personalized Product Hunt launch plan"),
 ("pricing-strategist", "ognjengt/founder-skills", "skills/pricing-strategist", "Pricing strategy from your business context"),
 ("conquistador", "hungv47/meta-skills", "skills/conquistador", "Default product-marketing and growth teammate"),
 ("launch-day-conductor", "aaron-he-zhu/aaron-marketing-skills", "launch/mobilize/launch-day-conductor", "Runs launch day; one of 120 skills for launch, email, ads, influencers"),
 ("find-leads / enrich-lead", "firecrawl/firecrawl-claude-plugin", "skills/find-leads", "Ranked lead lists with sourced contact data"),
]),
("Copywriting and content", "Writing that sells and reads like a person.", [
 ("humanizer", "blader/humanizer", "", "Strips the signs of AI writing so text reads like a person wrote it"),
 ("copywriting", MK, "skills/copywriting", "Homepage, landing, pricing, product copy"),
 ("copy-editing", MK, "skills/copy-editing", "Edits and refreshes existing copy"),
 ("content-strategy", MK, "skills/content-strategy", "What to write and why"),
 ("writing", "retieedra-profound/skills-marketing-library", "wisprflow/writing", "Edits AI text to sound human: cuts banned words and filler, adds voice"),
 ("improved-copywriting", "retieedra-profound/skills-marketing-library", "profound/improved-copywriting", "Diagnoses page copy first, then writes only claims the facts support"),
 ("brand-voice", "retieedra-profound/skills-marketing-library", "wisprflow/brand-voice", "Keeps one brand voice across everything you write"),
 ("sales-enablement", MK, "skills/sales-enablement", "Decks, one-pagers, objection docs"),
 ("content-humanizer", AR, "", "Removes AI tone from text"),
 ("content-creator / content-production", AR, "", "Content pipeline end to end"),
 ("email-sequence", AR, "", "Email sequences"),
 ("writing-guidelines", VL, "skills/writing-guidelines", "Audits docs voice and tone"),
 ("doc-coauthoring", A, "skills/doc-coauthoring", "Structured co-writing of specs and proposals"),
 ("internal-comms", A, "skills/internal-comms", "Company updates in house formats"),
 ("writing-fragments / writing-beats / writing-shape", MP, "skills/in-progress", "Matt Pocock's 3-step article writing loop"),
 ("de-ai-ify", "BrianRWagner/ai-marketing-skills", "de-ai-ify", "Removes AI jargon and restores a human voice"),
 ("generic-language-killer", "realkimbarrett/advertising-skills", "skills/qa/generic-language-killer", "Replaces vague, corporate, AI-sounding language"),
 ("voice-extractor", "BrianRWagner/ai-marketing-skills", "voice-extractor", "Documents your writing voice from samples"),
 ("brand-copywriter", "ognjengt/founder-skills", "skills/brand-copywriter", "Marketing copy on proven frameworks"),
 ("headline-matrix", "realkimbarrett/advertising-skills", "skills/copy-chief/headline-matrix", "Headline variations across angles"),
 ("write-copy / write-longform", "hungv47/meta-skills", "skills/write-copy", "Finished product-marketing copy and long-form pieces"),
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
 ("typefully", "typefully/agent-skills", "skills/typefully", "Official: draft and schedule posts for X, LinkedIn, Threads, Bluesky"),
 ("x-writer", "ognjengt/founder-skills", "skills/x-writer", "X posts from proven formats and templates"),
 ("viral-hook-creator", "ognjengt/founder-skills", "skills/viral-hook-creator", "Hooks built on psychological patterns"),
 ("linkedin-writer", "ognjengt/founder-skills", "skills/linkedin-writer", "LinkedIn posts with voice matching"),
 ("tweet-draft-reviewer", "BrianRWagner/ai-marketing-skills", "tweet-draft-reviewer", "Scores tweet drafts 1-10 against voice rules"),
 ("tweetclaw", "Xquik-dev/tweetclaw", "skills/tweetclaw", "Post, reply, search tweets, export followers"),
]),
("UGC, ads and creatives", "Ads that convert, scripts for UGC videos.", [
 ("ad-creative", MK, "skills/ad-creative", "Headlines, primary text, full ad variations at scale"),
 ("ads", MK, "skills/ads", "Google, Meta, LinkedIn, X ad campaigns"),
 ("video", MK, "skills/video", "AI and programmatic video production"),
 ("image", MK, "skills/image", "Marketing images: heroes, social, mockups"),
 ("paid-ads / ad-creative", AR, "", "Paid ads and creatives"),
 ("landing-page-generator", AR, "", "Landing pages for campaigns"),
 ("banner-design", UX, ".claude/skills/banner-design", "Ad and social banners"),
 ("ad-angle-multiplier", "realkimbarrett/advertising-skills", "skills/operator-os/ad-angle-multiplier", "One idea into many distinct ad angles"),
 ("scroll-stopping-creative", "realkimbarrett/advertising-skills", "skills/operator-os/scroll-stopping-creative", "Ad concepts that hold the first 3 seconds"),
 ("offer-extraction", "realkimbarrett/advertising-skills", "skills/foundations/offer-extraction", "Turns a product into a high-converting offer"),
 ("performance-diagnosis", "realkimbarrett/advertising-skills", "skills/operator-os/performance-diagnosis", "Why a campaign underperforms"),
 ("competitive-ads-extractor", "ComposioHQ/awesome-claude-skills", "competitive-ads-extractor", "Pulls and analyzes competitors' ads from ad libraries"),
 ("create-paid-campaign", "hungv47/meta-skills", "skills/create-paid-campaign", "Focused paid-media tests on Meta, Google, LinkedIn, TikTok"),
 ("creator-ugc-marketing", "Eronred/aso-skills", "skills/creator-ugc-marketing", "Plans and briefs creator and UGC campaigns"),
]),
("Video and motion", "Videos and animation written as code.", [
 ("hyperframes", "heygen-com/hyperframes", "skills/hyperframes", "Write HTML, render video: explainers, captions, charts, vertical clips"),
 ("frame-critic (ours)", "", "skills/frame-critic", "Watches your AI video before you ship: scores every frame out of 10 and boxes the bugs"),
 ("teardown", "elvarofficial/teardown", "", "A 3D simulator of any machine you can take apart part by part, then recorded to a 60 fps video"),
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
 ("video-use", "browser-use/video-use", "", "Edit any video by conversation: transcribe, cut, grade, overlays"),
 ("manim-video", "browser-use/video-use", "skills/manim-video", "Math and technical animations with Manim"),
 ("claude-code-video-toolkit", "digitalsamba/claude-code-video-toolkit", "", "Explainer videos: Remotion, FFmpeg, ElevenLabs voice, AI clips"),
 ("synthetic-ui-demo", "digitalsamba/claude-code-video-toolkit", ".claude/skills/synthetic-ui-demo", "Product demo videos without screen recording"),
 ("claude-motion (4 skills)", "whaleyxbt/claude-motion", ".claude/skills", "Motion with taste: checks its own frames, writes the sound in code, review loop"),
 ("motion-design", "howseen-ai/claude-motion-design", "skill/motion-design", "HTML, Playwright and ffmpeg pipeline, no Remotion"),
 ("motion-graphics-skills (15 skills)", "charlie947/motion-graphics-skills", "skills", "Launch videos: brand intake, title sequences, animated charts, explainers, reel export"),
 ("remotion-motion-graphics", "haidrrrry/claude-remotion-skill", "remotion-motion-graphics", "A Remotion editor from one prompt: captions, B-roll, sound"),
 ("klik-anim / klik-cam / klik-remotion-method", "t3knobox/klik-anim-skill-creation", "", "The laws of animation and camera for agents"),
 ("hyperframes-motion-reel", "Sunwood-ai-labs/hyperframes-motion-reel-skill", "", "A showreel cut to the beat with HyperFrames"),
 ("product-launch-motion", "AbubakrChan/product-launch-motion", "", "A full launch film with voice-over, camera and color grade"),
 ("animate", "cth9191/animate", "plugins/animate/skills/animate", "A short clip in one canvas file, storyboarded as it goes"),
 ("motion-design-skills (9 skills)", "iart-ai/motion-design-skills", "skills", "Timing, color, shot composition, logo animation, beat-sync editing"),
 ("hyperframes-student-kit (15 skills)", "nateherkai/hyperframes-student-kit", ".claude/skills", "HyperFrames kit: cut silences, short-form edits, storytelling, motion cards"),
 ("motion-design", "LottieFiles/motion-design-skill", "skills/motion-design", "LottieFiles' motion principles for any engine"),
 ("awesome-motion-design-agent-skills (5 skills)", "frankxai/awesome-motion-design-agent-skills", "skills", "Map of GSAP, Remotion, Lottie and Rive skills plus motion director agents"),
 ("motion-graphics (6 skills)", "Barty-Bart/motion-graphics", "skills", "B-roll and explainers built from your transcript, plus sound effects"),
 ("motion-dev-animations", "199-biotechnologies/motion-dev-animations-skill", "", "Web animation with Motion.dev (formerly Framer Motion)"),
 ("lemo-opuscar", "lemomo-ai/lemo-opuscar", "plugin/skills/lemo-opuscar", "66 film styles in code (oil paint, ukiyo-e, teardown), each with a demo film"),
 ("motion-graphics", "Mort1d/motion-graphics-skills", "skills/motion-graphics", "Promo from a link or clips: picks a style, reads the brand, writes the score, self-reviews"),
 ("create-shortform", "hungv47/meta-skills", "skills/create-shortform", "Researches and scripts TikTok, Reels, Shorts"),
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
 ("create-prd", "phuryn/pm-skills", "pm-execution/skills/create-prd", "Lean, decision-ready PRD (Pawe\u0142 Huryn, 65+ PM skills)"),
 ("pre-mortem", "phuryn/pm-skills", "pm-execution/skills/pre-mortem", "Risk analysis on a PRD or launch plan"),
 ("strategy-red-team", "phuryn/pm-skills", "pm-execution/skills/strategy-red-team", "Attacks the load-bearing assumptions of a strategy"),
 ("market-sizing", "phuryn/pm-skills", "pm-market-research/skills/market-sizing", "TAM, SAM, SOM top-down and bottom-up"),
 ("jobs-to-be-done", "deanpeters/Product-Manager-Skills", "skills/jobs-to-be-done", "Customer jobs, pains and gains"),
 ("opportunity-solution-tree", "deanpeters/Product-Manager-Skills", "skills/opportunity-solution-tree", "Outcomes to opportunities to experiments"),
 ("prd-generator", "ognjengt/founder-skills", "skills/prd-generator", "PRD files built for AI coding agents"),
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
 ("firecrawl-deep-research", "firecrawl/firecrawl-claude-plugin", "skills/firecrawl-deep-research", "Multi-source research on live web data"),
 ("read-docs / read-literature", "firecrawl/firecrawl-claude-plugin", "skills/read-docs", "Reads current official docs and papers instead of memory"),
 ("last30days", "BrianRWagner/ai-marketing-skills", "last30days", "What Reddit, X and the web said on a topic in 30 days"),
 ("youtube-summarizer", "BrianRWagner/ai-marketing-skills", "youtube-summarizer", "YouTube transcript to structured summary"),
 ("claude-scientific-skills", "K-Dense-AI/claude-scientific-skills", "", "177 science skills: biology, chemistry, data, lab tools"),
 ("academy-guide", A, "skills/academy-guide", "Points you to the matching Claude Academy course when you ask how to use Claude"),
 ("discernment-nudge", A, "skills/discernment-nudge", "After advice or a draft, adds 2-3 questions on what to check before you act on it"),
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
 ("autoresearch", "olelehmann100kMRR/autoresearch-skill", "", "Improves any skill by itself: runs it, scores with yes/no evals, keeps what works (Karpathy's autoresearch method)"),
 ("rag-architect / prompt-engineer / fine-tuning-expert", JA, "", "Agent and model building"),
 ("context-engineering-kit", "neolabhq/context-engineering-kit", "", "70 commands: judge, critique, tree-of-thoughts, kaizen"),
 ("n8n-workflow-patterns / n8n-agents", "czlonkowski/n8n-skills", "", "Build n8n workflows and AI agents with n8n-mcp"),
 ("context-engineering", "addyosmani/agent-skills", "skills/context-engineering", "Sets up agent context so output stays sharp"),
 ("task-coordination-strategies", "wshobson/agents", "plugins/agent-teams/skills/task-coordination-strategies", "Splits work and coordinates agent teams"),
 ("debate-agents", "hungv47/meta-skills", "skills/debate-agents", "Independent positions argue out a big decision"),
 ("composio automations", "ComposioHQ/awesome-claude-skills", "composio-skills", "833 app automations (Gmail, Slack, Notion...) via Composio Rube MCP"),
 ("integrate-whatsapp", "gokapso/agent-skills", "skills/integrate-whatsapp", "Connect WhatsApp to your product: webhooks, messages, templates (Kapso)"),
 ("automate-whatsapp", "gokapso/agent-skills", "skills/automate-whatsapp", "Build and debug WhatsApp workflows and triggers"),
 ("integrate-whatsapp-calling", "gokapso/agent-skills", "skills/integrate-whatsapp-calling", "Connect a voice agent to WhatsApp calls"),
]),
]

INDEX = {
 "blader/humanizer": "humanizer",
 "heygen-com/hyperframes": "captions-overlay, changelog-video, cut-the-curve, figma, hyperframes, hyperframes-cli, hyperframes-registry, media-use, motion-doctrine, oversized-cursor, remotion-to-hyperframes, reverse-any-video, seam-craft, slideshow, style-sampling",
 "retieedra-profound/skills-marketing-library": "aeo-operator-2026, ai-answer-accuracy-auditor, ai-citation-mix-strategist, ai-commerce-readiness-auditor, ai-prompt-portfolio-builder, ai-retrieval-fanout-mapper, ai-search-attribution-planner, brand-voice, claude-code-discoverability-auditor, commercial-ai-journey-mapper, copy-editing, humanizer, improved-copywriting, international-aeo-strategist, link-creator, newsletter-copy, session-end, session-start, writing",
 "massgen/massgen": "audio-generation, backend-integrator, evolving-skill-creator, file-search, image-generation, massgen, massgen-config-creator, massgen-develops-massgen, massgen-log-analyzer, massgen-release-documenter, model-registry-maintainer, multimedia-backend-integrator, pr-checks, release-prep, semtools, serena, skill-organizer, textual-ui-developer, video-generation",
 "anthropics/skills": "academy-guide, algorithmic-art, brand-guidelines, canvas-design, claude-api, discernment-nudge, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing, xlsx",
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
 "ComposioHQ/awesome-claude-skills": "artifacts-builder, brand-guidelines, canvas-design, changelog-generator, competitive-ads-extractor, connect-apps, connect, content-research-writer, developer-growth-analysis, docx, pdf, pptx, xlsx, domain-name-brainstormer, file-organizer, image-enhancer, internal-comms, invoice-organizer, langsmith-fetch, lead-research-assistant, mcp-builder, meeting-insights-analyzer, raffle-winner-picker, skill-creator, skill-share, slack-gif-creator, tailored-resume-generator, template-skill, theme-factory, twitter-algorithm-optimizer, video-downloader, webapp-testing",
 "VoltAgent/awesome-design-md": "awesome-design-md",
 "wshobson/agents": "screen-reader-testing, wcag-audit-patterns, multi-reviewer-patterns, parallel-debugging, parallel-feature-development, task-coordination-strategies, team-communication-protocols, team-composition-patterns, fastapi-templates, avoid-ai-writing, api-design-principles, architecture-patterns, cqrs-implementation, event-store-design, microservices-patterns, projection-patterns, saga-orchestration, temporal-python-testing, workflow-orchestration-patterns, before-you-build, block-no-verify-hook, defi-protocol-templates, nft-standards, solidity-security, web3-testing, brand-landingpage, data-storytelling, kpi-dashboard-design, deployment-pipeline-design, github-actions-templates, gitlab-ci-patterns, secrets-management, cost-optimization, hybrid-cloud-networking, istio-traffic-management, linkerd-patterns, mtls-configuration, multi-cloud-architecture, service-mesh-observability, terraform-module-library, context-driven-development, track-management, workflow-patterns, social-evidence-research, airflow-dag-patterns, data-quality-frameworks, dbt-transformation-patterns, spark-optimization, postgresql-table-design, auth-implementation-patterns, bazel-build-optimization, code-review-excellence, debugging-strategies, e2e-testing-patterns, error-handling-patterns, git-advanced-workflows, monorepo-management, nx-workspace-patterns, sql-optimization-patterns, turborepo-caching, spark-environment-setup, spark-memory-thermal-ops, spark-training-gotchas, architecture-decision-records, changelog-automation, openapi-spec-generation, grounded-vault, hads, dotnet-backend-patterns, file-conversion, angular-migration, database-migration, dependency-upgrade, react-modernization, nextjs-app-router-patterns, react-native-architecture, react-state-management, tailwind-design-system, godot-gdscript-patterns, unity-ecs-patterns, hermes-tweet, employment-contract-templates, gdpr-data-handling, connectivity-triage, incident-runbook-templates, on-call-handoff-patterns, postmortem-writing, javascript-testing-patterns, modern-javascript-patterns, nodejs-backend-patterns, typescript-advanced-types, gitops-workflow, helm-chart-scaffolding, k8s-manifest-generator, k8s-security-policies, embedding-strategies, hybrid-search-implementation, langchain-architecture, llm-evaluation, prompt-engineering-patterns, rag-implementation, similarity-search-patterns, vector-index-tuning, checkpoint-promotion, dataset-curation, eval-harness-first, finetuning-method-selection, grpo-rlvr-training, lora-qlora-recipes, preference-optimization, quantized-export, trace-to-training-data, vision-sft, ml-pipeline-workflow, recsys-pipeline-architect, distributed-tracing, grafana-dashboards, prometheus-configuration, slo-implementation, billing-automation, paypal-integration, pci-compliance, stripe-integration, evaluation-methodology, pptx-deck-context, pptx-quality-gates, pptx-reference-deck-analysis, pptx-slide-specification, pptx-visual-assets, protect-mcp-setup, async-python-patterns, python-anti-patterns, python-background-jobs, python-code-style, python-configuration, python-design-patterns, python-error-handling, python-observability, python-packaging, python-performance-optimization, python-project-structure, python-resilience, python-resource-management, python-testing-patterns, python-type-safety, uv-package-manager, backtesting-frameworks, risk-metrics-calculation, anti-reversing-techniques, binary-analysis-patterns, memory-forensics, protocol-reverse-engineering, review-agent-setup, attack-tree-construction, sast-configuration, security-requirement-extraction, stride-analysis-patterns, threat-mitigation-mapping, bash-defensive-patterns, bats-testing-patterns, shellcheck-configuration, scan, signed-audit-trails-recipe, ai-debt-detector, session-guard, visual-edit-precision, social-publishing, competitive-landscape, market-sizing-analysis, startup-financial-modeling, startup-metrics-framework, team-composition-analysis, superself, go-concurrency-patterns, memory-safety-patterns, rust-async-patterns, accessibility-compliance, design-system-patterns, interaction-design, mobile-android-design, mobile-ios-design, react-native-design, responsive-design, visual-design-foundations, web-component-design",
 "phuryn/pm-skills": "code-review, intended-vs-implemented, shipping-artifacts, ab-test-analysis, cohort-analysis, sql-queries, brainstorm-okrs, create-prd, dummy-dataset, job-stories, outcome-roadmap, pre-mortem, prioritization-frameworks, release-notes, retro, sprint-plan, stakeholder-map, strategy-red-team, summarize-meeting, test-scenarios, user-stories, wwas, beachhead-segment, competitive-battlecard, growth-loops, gtm-motions, gtm-strategy, ideal-customer-profile, competitor-analysis, customer-journey-map, market-segments, market-sizing, sentiment-analysis, user-personas, user-segmentation, marketing-ideas, north-star-metric, positioning-ideas, product-name, value-prop-statements, analyze-feature-requests, brainstorm-experiments-existing, brainstorm-experiments-new, brainstorm-ideas-existing, brainstorm-ideas-new, identify-assumptions-existing, identify-assumptions-new, interview-script, metrics-dashboard, opportunity-solution-tree, prioritize-assumptions, prioritize-features, summarize-interview, ansoff-matrix, business-model, lean-canvas, monetization-strategy, pestle-analysis, porters-five-forces, pricing-strategy, product-strategy, product-vision, startup-canvas, swot-analysis, value-proposition, draft-nda, grammar-check, privacy-policy, review-resume",
 "deanpeters/Product-Manager-Skills": "acquisition-channel-advisor, agent-orchestration-advisor, ai-shaped-readiness-advisor, altitude-horizon-framework, ansoff-matrix, autonomous-investigation, battle-card-builder, business-health-diagnostic, company-intel, company-research, competitive-analysis-process, competitive-intel-watch, competitive-research-snapshot, context-engineering-advisor, customer-journey-map, customer-journey-mapping-workshop, derisk-measurement-advisor, director-readiness-advisor, discovery-interview-prep, discovery-process, eol-checklist, eol-internal-enablement, eol-message, eol-process, eol-readiness-advisor, eol-stakeholder-sequence, epic-breakdown-advisor, epic-hypothesis, executive-onboarding-playbook, feature-investment-advisor, finance-based-pricing-advisor, finance-metrics-quickref, incoming-request-advisor, intel-discipline-advisor, intelligence-collection-disciplines, jobs-to-be-done, lean-ux-canvas, lifecycle-play-advisor, market-landscape-scan, opportunity-solution-tree, organic-growth-advisor, pestel-analysis, pestel-delta-monitor, pm-skill-creator, pol-probe-advisor, pol-probe, porters-five-forces, positioning-statement, positioning-workshop, prd-development, press-release, pricing-packaging-tracker, prioritization-advisor, problem-framing-canvas, problem-statement, product-lifecycle-plays, product-sense-interview-answer, product-strategy-session, proto-persona, recommendation-canvas, roadmap-planning, saas-economics-efficiency-metrics, saas-revenue-growth-metrics, skill-authoring-workflow, stakeholder-engagement-advisor, stakeholder-identification, stakeholder-mapping, storyboard, swot-analysis, tam-sam-som-calculator, user-story-mapping-workshop, user-story-mapping, user-story-splitting, user-story, voice-of-customer-miner, vp-cpo-readiness-advisor, workshop-facilitation",
 "aaron-he-zhu/aaron-marketing-skills": "ad-account-auditor, conversion-signal-qa, conversion-value-mapper, placement-exclusion-manager, ad-creative-builder, ad-test-designer, bid-strategy-planner, landing-experience-checker, audience-segment-builder, campaign-architect, product-feed-optimizer, search-term-miner, attribution-reconciler, budget-pacing-monitor, fatigue-frequency-manager, paid-measurement-loop, cold-outbound-sequencer, email-quality-auditor, inbox-placement-monitor, send-experiment-designer, dynamic-content-personalizer, email-creative-builder, email-render-builder, subject-line-lab, email-sequence-designer, newsletter-monetization-planner, preference-frequency-manager, reactivation-specialist, deliverability-qa, list-growth-designer, list-hygiene-monitor, list-segment-builder, content-amplifier, contract-helper, creator-content-auditor, outreach-manager, landing-optimizer, performance-analyzer, report-generator, roi-calculator, audience-mapper, fit-scorer, influencer-discovery, trend-spotter, brief-generator, budget-optimizer, campaign-planner, competitor-tracker, launch-asset-packager, message-house-builder, pricing-packaging-planner, sales-enablement-kit, community-launch-runner, launch-day-conductor, launch-readiness-auditor, press-media-relations, launch-feedback-synthesizer, launch-monitor, launch-retro-analyzer, momentum-planner, early-access-designer, launch-tier-planner, launch-window-planner, positioning-mapper, brand-language-codifier, message-system-architect, story-bank-builder, strategic-narrative-designer, message-test-designer, narrative-drift-monitor, narrative-quality-auditor, narrative-resonance-monitor, narrative-cascade-planner, narrative-enablement-kit, pitch-narrative-builder, proof-point-packager, audience-belief-mapper, category-narrative-mapper, narrative-baseline-mapper, positioning-truth-tracer, channel-registry, consent-registry, creator-registry, entity-registry, launch-registry, memory-management, narrative-registry, offer-claims-registry, domain-authority-auditor, offsite-signal-analyzer, performance-monitor, rank-tracker, content-writer, geo-content-optimizer, page-play-builder, serp-markup-builder, competitor-analysis, content-gap-analysis, keyword-research, serp-analysis, content-quality-auditor, on-page-seo-checker, site-structure-optimizer, technical-seo-checker, advocacy-program-designer, short-video-scripter, social-calendar-builder, social-creative-builder, channel-portfolio-planner, participation-warmup-planner, platform-norm-profiler, voice-dossier-builder, crisis-response-planner, engagement-inbox-manager, social-quality-auditor, social-selling-planner, dark-social-attributor, share-of-voice-tracker, social-measurement-loop, social-pulse-monitor",
 "Eronred/aso-skills": "ab-test-store-listing, android-aso, app-analytics, app-clips, app-icon-optimization, app-launch, app-marketing-context, app-preview-video, app-rejection-recovery, app-store-featured, apple-search-ads, asc-metrics, aso-audit, aso-router, attribution-setup, category-positioning, competitor-analysis, competitor-tracking, crash-analytics, creator-ugc-marketing, custom-product-pages, in-app-events, keyword-research, localization, market-movers, market-pulse, metadata-optimization, monetization-strategy, onboarding-optimization, paywall-optimization, press-and-pr, rating-prompt-strategy, referral-program, retention-optimization, review-management, screenshot-optimization, seasonal-aso, subscription-lifecycle, ua-campaign, web-to-app-funnel",
 "ognjengt/founder-skills": "brand-copywriter, competitor-intel, cro-optimization, go-to-market-plan, lead-magnet-generator, linkedin-writer, marketing-ideas, outreach-specialist, prd-generator, pricing-strategist, product-hunt-launch-plan, sop-creator, strategic-planning, viral-hook-creator, x-writer",
 "BrianRWagner/ai-marketing-skills": "ai-discoverability-audit, case-study-builder, cold-outreach-sequence, content-idea-generator, daily-briefing-builder, de-ai-ify, go-mode, homepage-audit, last30days, linkedin-authority-builder, linkedin-profile-optimizer, marketing-principles, meeting-prep, newsletter-creation-curation, plan-my-day, positioning-basics, reddit-insights, social-card-gen, testimonial-collector, tweet-draft-reviewer, vault-cleanup-auditor, voice-extractor, youtube-summarizer",
 "realkimbarrett/advertising-skills": "headline-matrix, mechanism-builder, objection-crusher, schwartz-awareness-mapper, avatar-extraction, offer-extraction, ad-angle-multiplier, conversion-path-builder, performance-diagnosis, scroll-stopping-creative, full-funnel-campaign-orchestrator, generic-language-killer",
 "CosmoBlk/email-marketing-bible": "email-marketing-bible",
 "Xquik-dev/tweetclaw": "tweetclaw",
 "greensock/gsap-skills": "gsap-core, gsap-frameworks, gsap-performance, gsap-plugins, gsap-react, gsap-scrolltrigger, gsap-timeline, gsap-utils",
 "czlonkowski/n8n-skills": "n8n-agents, n8n-binary-and-data, n8n-code-javascript, n8n-code-python, n8n-code-tool, n8n-error-handling, n8n-expression-syntax, n8n-mcp-tools-expert, n8n-multi-instance, n8n-node-configuration, n8n-self-hosting, n8n-subworkflows, n8n-validation-expert, n8n-workflow-patterns, using-n8n-mcp-skills",
 "addyosmani/agent-skills": "api-and-interface-design, browser-testing-with-devtools, ci-cd-and-automation, code-review-and-quality, code-simplification, constraint-driven-development, context-engineering, debugging-and-error-recovery, deprecation-and-migration, documentation-and-adrs, doubt-driven-development, frontend-ui-engineering, git-workflow-and-versioning, idea-refine, incremental-implementation, interview-me, observability-and-instrumentation, performance-optimization, planning-and-task-breakdown, security-and-hardening, shipping-and-launch, source-driven-development, spec-driven-development, test-driven-development, using-agent-skills",
 "safishamsi/graphify": "graphify",
 "browser-use/video-use": "video-use, manim-video",
 "digitalsamba/claude-code-video-toolkit": "acestep, elevenlabs, ffmpeg, frontend-design, ideogram4, ltx2, moviepy, playwright-recording, qwen-edit, remotion-official, remotion, runpod, synthetic-ui-demo, video-toolkit",
 "typefully/agent-skills": "typefully",
 "firecrawl/firecrawl-claude-plugin": "brand-identity, business-contact-research, design, enrich-lead, fantasy-sports, find-leads, firecrawl-deep-research, firecrawl, job-postings, read-docs, read-literature, seo-audit",
 "hashicorp/agent-skills": "aws-ami-builder, azure-image-builder, push-to-registry, windows-builder, azure-verified-modules, new-terraform-provider, provider-actions, provider-configuration, provider-docs, provider-ephemeral-resources, provider-framework-migration, provider-resources, provider-test-patterns, refactor-module, run-acceptance-tests, terraform-policy, terraform-search-import, terraform-stacks, terraform-style-guide, terraform-test",
 "MicrosoftDocs/Agent-Skills": "azure-active-directory-b2c, azure-advisor, azure-ai-vision, azure-aks-edge-essentials, azure-analysis-services, azure-anyscale-on-azure, azure-api-center, azure-api-management, azure-app-configuration, azure-app-service, azure-app-testing, azure-application-gateway, azure-application-network, azure-arc, azure-architecture, azure-artifact-signing, azure-artifacts, azure-attestation, azure-automation, azure-backup, azure-bastion, azure-batch, azure-blob-storage, azure-blueprints, azure-boards, azure-bot-service, azure-business-process-tracking, azure-cache-redis, azure-carbon-optimization, azure-chaos-studio, azure-cloud-adoption-framework, azure-cloud-hsm, azure-cloud-services, azure-cloud-shell, azure-cognitive-search, azure-communication-services, azure-confidential-computing, azure-confidential-ledger, azure-connector-namespace, azure-container-apps, azure-container-instances, azure-container-registry, azure-container-storage, azure-content-safety, azure-content-understanding, azure-copilot, azure-cosmos-db, azure-cost-management, azure-custom-vision, azure-cyclecloud, azure-data-api-builder, azure-data-box-family, azure-data-explorer, azure-data-factory, azure-data-manager-for-agri, azure-data-science-vm, azure-data-share, azure-database-migration, azure-database-mysql, azure-database-postgresql, azure-databricks, azure-ddos-protection, azure-dedicated-hsm, azure-defender-for-cloud, azure-defender-for-iot, azure-deployment-environments, azure-dev-box, azure-devops, azure-devtest-labs, azure-digital-twins, azure-dns, azure-document-intelligence, azure-documentdb, azure-durable-task, azure-education-hub, azure-elastic-san, azure-enclave, azure-energy-data-services, azure-event-grid, azure-event-hubs, azure-expressroute, azure-extended-zones, azure-external-attack-surface-management, azure-face, azure-files, azure-firewall-manager, azure-firewall, azure-firmware-analysis, azure-fluid-relay, azure-front-door, azure-functions, azure-hdinsight, azure-health-bot, azure-health-data-services, azure-horizondb, azure-hpc-cache, azure-immersive-reader, azure-impact-reporting, azure-import-export, azure-information-protection, azure-internet-peering, azure-iot-central, azure-iot-edge, azure-iot-hub, azure-iot-operations, azure-iot, azure-key-vault, azure-kubernetes-service, azure-lab-services, azure-language-service, azure-large-instances, azure-lighthouse, azure-load-balancer, azure-local, azure-logic-apps, azure-machine-learning, azure-managed-applications, azure-managed-grafana, azure-managed-lustre, azure-managed-redis, azure-maps, azure-metrics-advisor, azure-microsoft-discovery, azure-microsoft-opentelemetry, azure-migrate, azure-monitor, azure-nat-gateway, azure-netapp-files, azure-network-function-manager, azure-network-watcher, azure-networking, azure-notification-hubs, azure-nutanix, azure-open-datasets, azure-operator-nexus, azure-operator-service-manager, azure-oracle, azure-osconfig, azure-partner-solutions, azure-payment-hsm, azure-peering-service, azure-personalizer, azure-pipelines, azure-planetary-computer-pro, azure-playwright-workspaces, azure-policy, azure-portal, azure-private-link, azure-quantum, azure-queue-storage, azure-quotas, azure-rbac, azure-redhat-openshift, azure-relay, azure-reliability, azure-repos, azure-resiliency, azure-resource-graph, azure-resource-manager, azure-route-server, azure-sap, azure-security, azure-sentinel, azure-service-bus, azure-service-connector, azure-service-fabric, azure-service-health, azure-signalr-service, azure-site-recovery, azure-sovereign-us, azure-speech, azure-spring-apps, azure-sql-database, azure-sql-managed-instance, azure-sql-virtual-machines, azure-sre-agent, azure-stack-edge, azure-static-web-apps, azure-stream-analytics, azure-synapse-analytics, azure-table-storage, azure-test-plans, azure-traffic-manager, azure-translator, azure-update-manager, azure-video-indexer, azure-virtual-desktop, azure-virtual-machines, azure-virtual-network-manager, azure-virtual-network, azure-virtual-wan, azure-vm-scalesets, azure-vmware-solution, azure-vpn-gateway, azure-web-application-firewall, azure-web-pubsub, azure-well-architected, microsoft-foundry-classic, microsoft-foundry-local, microsoft-foundry-tools, microsoft-foundry",
 "awslabs/agent-plugins": "amazon-location-service, amplify-workflow, api-gateway, aws-lambda-durable-functions, aws-lambda-managed-instances, aws-lambda-microvms, aws-lambda, aws-serverless-deployment, aws-step-functions, aws-transform, document-service, dsql, aws-architecture-diagram, deploy, elastic-beanstalk, dataset-evaluation, dataset-transformation, directory-management, finetuning-technique, finetuning, hyperpod-cluster-debugger, hyperpod-issue-report, hyperpod-nccl, hyperpod-node-debugger, hyperpod-performance-debugger, hyperpod-slurm-debugger, hyperpod-ssm, hyperpod-version-checker, model-deployment, model-evaluation, model-selection, planning, sdk-getting-started, use-case-specification",
 "K-Dense-AI/claude-scientific-skills": "13c-metabolic-flux, adaptyv, aeon, alphagenome, analytical-method-validation, anndata, arbor, arboreto, astropy, autoskill, benchling-integration, bgpt-paper-search, bids, biopython, bioservices, bulk-rnaseq, cantera, cellprofiler, cellxgene-census, cirq, citation-management, clinical-decision-support, clinical-reports, cobrapy, consciousness-council, dask, database-lookup, datalad, datamol, deepchem, deepspot-m, deeptools, depmap, dhdna-profiler, diffdock, dnanexus-integration, esm, etetoolkit, exa-search, experimental-design, exploratory-data-analysis, fictiv, flowio, flowkit, fluidsim, folklore-variant-evidence, generate-image, geniml, genomic-coordinates, genomic-intelligence, geomaster, geopandas, get-available-resources, gget, ginkgo-cloud-lab, glycoengineering, gtars, histolab, hugging-science, hypogenic, hypothesis-generation, imaging-data-commons, infographics, iso-standards-readiness, lab-hardware-cad, labarchive-integration, lamindb, latchbio-integration, latex-posters, liteparse, literature-review, mageck, marine-carbonate-chemistry, markdown-mermaid-writing, market-research-reports, markitdown, matchms, matlab, matplotlib, medchem, modal, molecular-dynamics, molfeat, ncats-arax, networkx, neurokit2, neuropixels-analysis, nextflow, nmrglue, nwb-conversion, omero-integration, onekgpd, ontology-term-resolution, open-notebook, openpiv, opentrons-integration, optimize-for-gpu, pacsomatic, paper-lookup, paperclip, paperzilla, parallel-web, pathml, pathogen-variant-surveillance, pathway-enrichment, peer-review, pennylane, phylogenetics, pi-agent, pkpd-modeling, polars-bio, polars, pptx-posters, primekg, primer-design, protocolsio-integration, pufferlib, pybamm, pycalphad, pydeseq2, pydicom, pyhealth, pylabrobot, pymatgen, pymc, pymoo, pyopenms, pysam, pytdc, pytorch-lightning, pyzotero, qiime2-amplicon, qiskit, qutip, rdkit, relion, relsa-severity-assessment, research-grants, research-lookup, rowan, scanpy, scholar-evaluation, scientific-brainstorming, scientific-critical-thinking, scientific-schematics, scientific-slides, scientific-visualization, scientific-writing, scikit-bio, scikit-learn, scikit-survival, scvelo, scvi-tools, seaborn, shap, simpy, stable-baselines3, statistical-analysis, statistical-power, statsmodels, sympy, tamarind, tellurium, tiledbvcf, timesfm-forecasting, torch-geometric, torchdrug, transformers, treatment-plans, umap-learn, uncertainty-and-units, usfiscaldata, vaex, venue-templates, waypoint-bio, what-if-oracle, zarr-python",
 "BehiSecc/VibeSec-Skill": "VibeSec-Skill",
 "feedtailor/ccskill-nanobanana": "ccskill-nanobanana",
 "kingbootoshi/nano-banana-2-skill": "nano-banana",
 "hungv47/meta-skills": "brief-creative, brief-product-ui, conquistador, create-brand, create-paid-campaign, create-shortform, debate-agents, improve-conversion, knowledge-review, map-user-flow, measure-growth, model-growth-funnel, optimize-search, plan-campaign, polish-vietnamese, research-channel, research-positioning, write-copy, write-longform, write-outreach, write-social",
 "elvarofficial/teardown": "teardown",
 "cursor/plugins": "architect, arena, automate-me, benchmark-checklist, blast-radius, bro, correct, create-formal-verification-skill, create-verification-skill, figure-it-out, how, in-your-own-words, interrogate, ketchup, ketchup-video, maintain-formal-verification-skill, maintain-verification-skill, make-bot-ui, no-comments, poteto-help, poteto-mode, principle-attack-the-premise, principle-boundary-discipline, principle-build-the-lever, principle-encode-lessons-in-structure, principle-exhaust-the-design-space, principle-experience-first, principle-explain-the-number, principle-fix-root-causes, principle-foundational-thinking, principle-guard-the-context-window, principle-laziness-protocol, principle-make-operations-idempotent, principle-migrate-callers-then-delete-legacy-apis, principle-minimize-reader-load, principle-model-the-domain, principle-never-block-on-the-human, principle-outcome-oriented-execution, principle-prove-it-works, principle-redesign-from-first-principles, principle-separate-before-serializing-shared-state, principle-sequence-verifiable-units, principle-subtract-before-you-add, principle-test-behavior-not-implementation, principle-type-system-discipline, recall, reflect, setup-pstack, sharpen, show-me-your-work, statechart, swarm, tdd, teach, technical-writing, typescript-best-practices, unslop, why",
 "gokapso/agent-skills": "automate-whatsapp, integrate-whatsapp, integrate-whatsapp-calling, observe-whatsapp",
 "whaleyxbt/claude-motion": "motion-design, review-loop, sound-design, web-sims",
 "lemomo-ai/lemo-opuscar": "lemo-opuscar",
 "Mort1d/motion-graphics-skills": "motion-graphics",
 "howseen-ai/claude-motion-design": "motion-design",
 "charlie947/motion-graphics-skills": "animated-chart, apple-launch-film, brand-intake, launch-video, loop-cover, milestone-reveal, model-showdown, motion-brief-writer, motion-effects, motion-prompt-writer, newsletter-promo, reel-export, reference-to-motion, title-sequence-3d, vox-explainer",
 "haidrrrry/claude-remotion-skill": "remotion-motion-graphics",
 "t3knobox/klik-anim-skill-creation": "klik-anim, klik-cam, klik-remotion-method",
 "Sunwood-ai-labs/hyperframes-motion-reel-skill": "hyperframes-motion-reel",
 "AbubakrChan/product-launch-motion": "product-launch-motion",
 "cth9191/animate": "animate",
 "iart-ai/motion-design-skills": "after-effects, animation-principles, beat-sync-editing, color-motion, logo-animation, motion-art-direction, motion-background, remotion-video, shot-composition",
 "nateherkai/hyperframes-student-kit": "cut-mistakes, cut-silences, edit-video, gsap, hyperframes, hyperframes-cli, hyperframes-registry, hyperframes-video-beats, make-a-video, motion-showreel, short-form-edit, short-form-video, style-library, video-storytelling, website-to-hyperframes",
 "LottieFiles/motion-design-skill": "motion-design",
 "frankxai/awesome-motion-design-agent-skills": "generative-media-director, motion-director, remotion-video-agent, site-motion-excellence-director, web-motion-auditor",
 "Barty-Bart/motion-graphics": "explainer-default, explainer-engaging, explainer-high-energy, motion-broll, object-separation, sound-effects",
 "199-biotechnologies/motion-dev-animations-skill": "motion-dev-animations",
 "olelehmann100kMRR/autoresearch-skill": "autoresearch",
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
    w('<p align="center"><b>The best open-source skills for Claude Code, sorted by what you do.</b><br>Every skill links to its original author, so you always get the latest version.<br>The list keeps growing. ⭐ Star the repo to get updates.<br><br><a href="https://f0rgent.github.io/claude-skills-catalog/"><b>🌐 Open the catalog as a website, with search</b></a></p>\n')
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
    w("> **Bonus: [x-reach](skills/x-reach/SKILL.md)** and **[frame-critic](skills/frame-critic/SKILL.md)**. Our own skills: x-reach shows how to write X posts that get reach, built from a study of 2,194 video posts across 300 accounts plus our own tests. frame-critic watches your AI video before you ship it: a contact sheet, a score out of 10 for every frame, red boxes on the bugs. Install them like any other skill.\n")
    w(f"> **Want the full version?** The [X Creator Pack](https://f0rgent.gumroad.com/l/x-creator-pack) ($9) adds 2 more post templates, the first-reply recipe, series, a video checklist, tracking, plus agent-episodes, X Article playbooks, an X monetization playbook and the full frame-critic that fixes and re-renders until every frame is 8/10 or higher. The free skills stay free.\n")
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
    w("- Our own files (this README, build.py, install.sh, skills/x-reach, skills/frame-critic) are MIT. Everything under vendor/ belongs to its authors and keeps its own license. Repos with no license stated are linked, not copied.")
    w("- Lists that pointed us to these repos: @Bober_smart, @Mr_Buzzoni, @zodchiii, @eng_khairallah1, @Mnilax, @e1genqq, @DDJCXX, @fayzonnn on X.\n")
    w('<p align="center"><sub>Made by <a href="https://x.com/f0rgent">@f0rgent</a> · Showing how AI agents actually do practical things + giving away the prompts</sub></p>')
    open(__file__.replace("build.py", "README.md"), "w").write("\n".join(out))
    print("skills in index:", total)
    import subprocess, sys
    subprocess.run([sys.executable, __file__.replace("build.py", "site.py")], check=True)

main()
