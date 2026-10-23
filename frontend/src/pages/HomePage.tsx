import { useEffect, useRef, useState } from "react";
import { Link } from "react-router-dom";
import { matchesQuery, patterns, patternsByCategory, shortComplexity } from "../lib/content";

export default function HomePage() {
  const [query, setQuery] = useState("");
  const inputRef = useRef<HTMLInputElement>(null);
  const groups = patternsByCategory(patterns.filter((p) => matchesQuery(p, query)));

  // Press "/" anywhere to jump to search.
  useEffect(() => {
    function onKey(e: KeyboardEvent) {
      if (e.key === "/" && document.activeElement !== inputRef.current) {
        e.preventDefault();
        inputRef.current?.focus();
      }
    }
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, []);

  return (
    <>
      <section className="hero">
        <h1>Recognize the pattern, then write the code yourself.</h1>
        <p className="lede">
          {patterns.length} core patterns, each with the signals that give it away, a tested Python
          template, and practice problems ordered easy to hard.
        </p>
        <input
          ref={inputRef}
          className="search"
          type="search"
          placeholder='Search by keyword, signal, or problem — e.g. "substring", "k largest"   ( / )'
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
      </section>

      {groups.length === 0 && (
        <p className="muted">
          No pattern matches "{query}". Try <Link to="/signals">Spot the pattern</Link> or the{" "}
          <Link to="/guides/how-to-choose">pattern guide</Link>.
        </p>
      )}

      {groups.map(([category, list]) => (
        <section key={category} className="category">
          <h2 className="category-title">{category}</h2>
          <div className="grid">
            {list.map((p) => (
              <Link key={p.slug} to={`/patterns/${p.slug}`} className="card">
                <h3>{p.title}</h3>
                <p>{p.summary}</p>
                <div className="card-meta">
                  <span className="mono">{shortComplexity(p.complexity.time)}</span>
                  <span>{p.problems.length} problems</span>
                </div>
              </Link>
            ))}
          </div>
        </section>
      ))}
    </>
  );
}
