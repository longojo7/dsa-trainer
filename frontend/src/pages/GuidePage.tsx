import { useParams } from "react-router-dom";
import Markdown from "../components/Markdown";
import { guides } from "../lib/content";
import NotFound from "./NotFound";

export default function GuidePage() {
  const { slug } = useParams();
  const guide = guides.find((g) => g.slug === slug);
  if (!guide) return <NotFound />;

  return (
    <article className="guide">
      <h1>{guide.title}</h1>
      <p className="lede">{guide.summary}</p>
      <Markdown source={guide.body} />
    </article>
  );
}
