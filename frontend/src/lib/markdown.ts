import { Marked } from "marked";
import hljs from "highlight.js/lib/core";
import python from "highlight.js/lib/languages/python";

hljs.registerLanguage("python", python);

export function highlightPython(code: string): string {
  return hljs.highlight(code, { language: "python" }).value;
}

const marked = new Marked({
  renderer: {
    code({ text, lang }) {
      const html = lang === "python" ? highlightPython(text) : escapeHtml(text);
      return `<pre class="code"><code class="hljs">${html}</code></pre>`;
    },
  },
});

function escapeHtml(s: string): string {
  return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

// Content is authored in this repo, so rendering it as HTML is safe.
export function renderMarkdown(md: string): string {
  return marked.parse(md, { async: false });
}
