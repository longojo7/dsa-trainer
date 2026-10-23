import { Link } from "react-router-dom";

export default function NotFound() {
  return (
    <article>
      <h1>Page not found</h1>
      <p><Link to="/">Back to all patterns</Link></p>
    </article>
  );
}
