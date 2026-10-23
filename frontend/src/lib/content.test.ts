// Catches content mistakes (a missing field, a typo in difficulty) before they reach the site.
import { describe, expect, it } from "vitest";
import { CATEGORY_ORDER, guides, matchesQuery, patterns, shortComplexity, splitFrontmatter } from "./content";

describe("content", () => {
  it("loads every pattern", () => {
    expect(patterns.length).toBeGreaterThanOrEqual(20);
  });

  it.each(patterns.map((p) => [p.slug, p] as const))("%s is complete", (_slug, p) => {
    expect(p.title).toBeTruthy();
    expect(CATEGORY_ORDER).toContain(p.category);
    expect(p.summary).toBeTruthy();
    expect(p.signals.length).toBeGreaterThan(0);
    expect(p.complexity.time).toBeTruthy();
    expect(p.complexity.space).toBeTruthy();
    expect(p.template).toContain("def ");
    expect(p.body).toContain("## Key idea");
    expect(p.problems.length).toBeGreaterThan(0);
    for (const prob of p.problems) {
      expect(["Easy", "Medium", "Hard"]).toContain(prob.difficulty);
      expect(prob.slug).toMatch(/^[a-z0-9-]+$/);
    }
  });

  it("has unique slugs", () => {
    expect(new Set(patterns.map((p) => p.slug)).size).toBe(patterns.length);
  });

  it("loads guides", () => {
    expect(guides.map((g) => g.slug)).toContain("how-to-choose");
  });

  it("search matches signals and problem names", () => {
    const sw = patterns.find((p) => p.slug === "sliding-window")!;
    expect(matchesQuery(sw, "substring")).toBe(true);
    expect(matchesQuery(sw, "minimum window")).toBe(true);
    expect(matchesQuery(sw, "dijkstra")).toBe(false);
  });

  it("shortens complexity strings", () => {
    expect(shortComplexity("O((V + E) log V)")).toBe("O((V + E) log V)");
    expect(shortComplexity("O(n log n) for the sort")).toBe("O(n log n)");
    expect(shortComplexity("Exponential — O(2ⁿ)")).toBe("Exponential");
  });

  it("parses frontmatter", () => {
    const { data, body } = splitFrontmatter("---\ntitle: X\n---\nhello");
    expect(data.title).toBe("X");
    expect(body).toBe("hello");
  });
});
