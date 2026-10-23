import { useMemo } from "react";
import { renderMarkdown } from "../lib/markdown";

export default function Markdown({ source }: { source: string }) {
  const html = useMemo(() => renderMarkdown(source), [source]);
  return <div className="prose" dangerouslySetInnerHTML={{ __html: html }} />;
}
