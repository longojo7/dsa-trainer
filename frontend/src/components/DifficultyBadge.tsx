import type { Difficulty } from "../lib/content";

export default function DifficultyBadge({ level }: { level: Difficulty }) {
  return <span className={`badge badge-${level.toLowerCase()}`}>{level}</span>;
}
