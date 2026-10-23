import { Link, useParams } from "react-router-dom";
import CodeBlock from "../components/CodeBlock";
import DifficultyBadge from "../components/DifficultyBadge";
import Markdown from "../components/Markdown";
import { leetcodeUrl, patterns } from "../lib/content";
import NotFound from "./NotFound";

export default function PatternPage() {
  const { slug } = useParams();
  const index = patterns.findIndex((p) => p.slug === slug);
  if (index === -1) return <NotFound />;
  const p = patterns[index];
  const prev = patterns[index - 1];
  const next = patterns[index + 1];

  return (
    <article className="pattern">
      <Link to="/" className="back">← All patterns</Link>
      <p className="eyebrow">{p.category}</p>
      <h1>{p.title}</h1>
      <p className="lede">{p.summary}</p>

      <div className="layout">
        <div className="col-main">
          <section className="panel signals">
            <h2>Spot it when…</h2>
            <ul>
              {p.signals.map((s) => <li key={s}>{s}</li>)}
            </ul>
          </section>

          <Markdown source={p.body} />

          <section>
            <h2>Template</h2>
            <CodeBlock code={p.template} filename={`${p.slug}/template.py`} />
          </section>
        </div>

        <aside className="col-side">
          <section className="panel">
            <h2>Complexity</h2>
            <dl className="complexity">
              <dt>Time</dt><dd>{p.complexity.time}</dd>
              <dt>Space</dt><dd>{p.complexity.space}</dd>
            </dl>
          </section>

          <section className="panel">
            <h2>Practice</h2>
            <ol className="problems">
              {p.problems.map((prob) => (
                <li key={prob.id}>
                  <a href={leetcodeUrl(prob)} target="_blank" rel="noreferrer">
                    <span className="mono muted">{prob.id}.</span> {prob.name}
                  </a>
                  <span className="problem-tags">
                    <DifficultyBadge level={prob.difficulty} />
                    {prob.premium && <span className="badge badge-premium" title="LeetCode Premium">Premium</span>}
                  </span>
                </li>
              ))}
            </ol>
          </section>
        </aside>
      </div>

      <nav className="pager">
        {prev ? <Link to={`/patterns/${prev.slug}`}>← {prev.title}</Link> : <span />}
        {next ? <Link to={`/patterns/${next.slug}`}>{next.title} →</Link> : <span />}
      </nav>
    </article>
  );
}
