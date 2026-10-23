import { useMemo, useState } from "react";
import { highlightPython } from "../lib/markdown";

export default function CodeBlock({ code, filename }: { code: string; filename?: string }) {
  const html = useMemo(() => highlightPython(code), [code]);
  const [copied, setCopied] = useState(false);

  async function copy() {
    await navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 1500);
  }

  return (
    <div className="codeblock">
      <div className="codeblock-bar">
        <span>{filename ?? "python"}</span>
        <button className="copy-btn" onClick={copy}>{copied ? "Copied" : "Copy"}</button>
      </div>
      <pre className="code"><code className="hljs" dangerouslySetInnerHTML={{ __html: html }} /></pre>
    </div>
  );
}
