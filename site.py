"""Builds docs/index.html (the GitHub Pages site) from the data in build.py."""
import json, html, os

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "build.py")).read().replace("\nmain()", "\n# main()")
B = {"__file__": os.path.join(HERE, "build.py")}
exec(compile(src, "build.py", "exec"), B)

SECTIONS, REPOS, INDEX, L, stars = B["SECTIONS"], B["REPOS"], B["INDEX"], B["L"], B["stars"]
SHORT, EMO = B["SHORT"], B["EMO"]

def count(v):
    return len([x for x in v.replace("; extensions:", ",").split(",") if x.strip()])

total = sum(count(v) for v in INDEX.values())
nrepos = len(open(os.path.join(HERE, "data/repos.txt")).read().split())

def install(sk, repo, path):
    if not repo:
        return "git clone https://github.com/f0rgent/claude-skills-catalog"
    return f"npx skills@latest add {repo}/{sk}" if path else f"npx skills@latest add {repo}"

skills = []
for i, (name, intro, rows) in enumerate(SECTIONS):
    for sk, repo, path, desc in rows:
        skills.append({
            "n": sk, "d": desc, "r": repo or "f0rgent/claude-skills-catalog",
            "u": L(repo, path) if repo else "https://github.com/f0rgent/claude-skills-catalog/tree/main/" + path,
            "s": stars(repo) if repo else "", "c": i, "i": install(sk, repo, path),
        })

niches = [{"t": SHORT[i], "e": EMO[i], "h": SECTIONS[i][0], "x": SECTIONS[i][1], "k": len(SECTIONS[i][2])} for i in range(len(SECTIONS))]
index = [{"r": r, "s": stars(r), "l": REPOS[r][1], "k": count(INDEX[r]), "v": INDEX[r]} for r in REPOS if r in INDEX]

DATA = json.dumps({"skills": skills, "niches": niches, "index": index}, ensure_ascii=False)

page = open(os.path.join(HERE, "site_template.html")).read()
page = (page.replace("{{DATA}}", DATA)
            .replace("{{TOTAL}}", f"{total:,}")
            .replace("{{REPOS}}", str(nrepos))
            .replace("{{NICHES}}", str(len(SECTIONS) - 1))
            .replace("{{PICKS}}", str(len(skills))))
os.makedirs(os.path.join(HERE, "docs"), exist_ok=True)
open(os.path.join(HERE, "docs/index.html"), "w").write(page)
open(os.path.join(HERE, "docs/.nojekyll"), "w").write("")
print("site:", len(skills), "picks,", total, "indexed,", nrepos, "repos")
