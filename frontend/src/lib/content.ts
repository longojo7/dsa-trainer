// Loads the cheat-sheet content from /content at build time.
// To add a pattern, create content/patterns/<slug>/{pattern.md,template.py} — no code changes needed.
import { parse as parseYaml } from "yaml";

export type Difficulty = "Easy" | "Medium" | "Hard";

export interface Problem {
  name: string;
  id: number;
  slug: string;
  difficulty: Difficulty;
  premium?: boolean;
}

export interface Pattern {
  slug: string;
  title: string;
  category: string;
  order: number;
  summary: string;
  signals: string[];
  complexity: { time: string; space: string };
  problems: Problem[];
  body: string; // markdown
  template: string; // python source
}

export interface Guide {
  slug: string;
  title: string;
  order: number;
  summary: string;
  body: string;
}

// Categories appear on the home page in this order; unknown ones go last.
export const CATEGORY_ORDER = [
  "Arrays & Strings",
  "Searching",
  "Stacks & Queues",
  "Linked Lists",
  "Trees",
  "Graphs",
  "Heaps",
  "Recursion",
  "Dynamic Programming",
  "Strings",
];

export function splitFrontmatter(raw: string): { data: Record<string, unknown>; body: string } {
  const match = /^---\r?\n([\s\S]*?)\r?\n---\r?\n?([\s\S]*)$/.exec(raw);
  if (!match) return { data: {}, body: raw };
  return { data: (parseYaml(match[1]) ?? {}) as Record<string, unknown>, body: match[2].trim() };
}

function slugFromPath(path: string, depthFromEnd: number): string {
  const parts = path.split("/");
  return parts[parts.length - depthFromEnd].replace(/\.md$/, "");
}

const patternFiles = import.meta.glob("../../../content/patterns/*/pattern.md", {
  query: "?raw",
  import: "default",
  eager: true,
}) as Record<string, string>;

const templateFiles = import.meta.glob("../../../content/patterns/*/template.py", {
  query: "?raw",
  import: "default",
  eager: true,
}) as Record<string, string>;

const guideFiles = import.meta.glob("../../../content/guides/*.md", {
  query: "?raw",
  import: "default",
  eager: true,
}) as Record<string, string>;

function categoryRank(category: string): number {
  const i = CATEGORY_ORDER.indexOf(category);
  return i === -1 ? CATEGORY_ORDER.length : i;
}

export const patterns: Pattern[] = Object.entries(patternFiles)
  .map(([path, raw]) => {
    const slug = slugFromPath(path, 2);
    const { data, body } = splitFrontmatter(raw);
    const templatePath = path.replace(/pattern\.md$/, "template.py");
    return {
      slug,
      body,
      template: (templateFiles[templatePath] ?? "").trim(),
      ...(data as Omit<Pattern, "slug" | "body" | "template">),
    };
  })
  .sort((a, b) => categoryRank(a.category) - categoryRank(b.category) || a.order - b.order);

export const guides: Guide[] = Object.entries(guideFiles)
  .map(([path, raw]) => {
    const { data, body } = splitFrontmatter(raw);
    return { slug: slugFromPath(path, 1), body, ...(data as Omit<Guide, "slug" | "body">) };
  })
  .sort((a, b) => a.order - b.order);

export function patternsByCategory(list: Pattern[] = patterns): [string, Pattern[]][] {
  const groups = new Map<string, Pattern[]>();
  for (const p of list) {
    if (!groups.has(p.category)) groups.set(p.category, []);
    groups.get(p.category)!.push(p);
  }
  return [...groups.entries()];
}

export function matchesQuery(p: Pattern, query: string): boolean {
  const q = query.trim().toLowerCase();
  if (!q) return true;
  const haystack = [p.title, p.summary, p.category, ...p.signals, ...p.problems.map((x) => x.name)]
    .join(" ")
    .toLowerCase();
  return q.split(/\s+/).every((word) => haystack.includes(word));
}

// "O((V + E) log V) — note" → "O((V + E) log V)". Falls back to the first word.
export function shortComplexity(time: string): string {
  if (!time.startsWith("O(")) return time.split(" ")[0];
  let depth = 0;
  for (let i = 1; i < time.length; i++) {
    if (time[i] === "(") depth++;
    if (time[i] === ")" && --depth === 0) return time.slice(0, i + 1);
  }
  return time;
}

export function leetcodeUrl(problem: Problem): string {
  return `https://leetcode.com/problems/${problem.slug}/`;
}
