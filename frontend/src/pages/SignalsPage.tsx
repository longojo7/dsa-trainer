import { useState } from "react";
import { Link } from "react-router-dom";
import { patterns } from "../lib/content";

// Every recognition signal in one searchable table: "I see X in the problem → try pattern Y".
const rows = patterns.flatMap((p) => p.signals.map((signal) => ({ signal, pattern: p })));

export default function SignalsPage() {
  const [query, setQuery] = useState("");
  const q = query.trim().toLowerCase();
  const visible = q
    ? rows.filter((r) => q.split(/\s+/).every((w) => `${r.signal} ${r.pattern.title}`.toLowerCase().includes(w)))
    : rows;

  return (
    <article>
      <h1>Spot the pattern</h1>
      <p className="lede">
        Type what you notice in the problem statement. Every clue from every pattern is listed here.
      </p>
      <input
        className="search"
        type="search"
        placeholder='e.g. "sorted", "contiguous", "prerequisites", "k"'
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        autoFocus
      />
      <table className="signal-table">
        <thead>
          <tr><th>If the problem has…</th><th>Try</th></tr>
        </thead>
        <tbody>
          {visible.map((r) => (
            <tr key={`${r.pattern.slug}-${r.signal}`}>
              <td>{r.signal}</td>
              <td><Link to={`/patterns/${r.pattern.slug}`}>{r.pattern.title}</Link></td>
            </tr>
          ))}
        </tbody>
      </table>
      {visible.length === 0 && <p className="muted">No signals match. Try fewer words.</p>}
    </article>
  );
}
