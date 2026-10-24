import { useEffect } from "react";
import { NavLink, Route, Routes, useLocation } from "react-router-dom";
import ThemeToggle from "./components/ThemeToggle";
import { guides } from "./lib/content";
import HomePage from "./pages/HomePage";
import PatternPage from "./pages/PatternPage";
import GuidePage from "./pages/GuidePage";
import SignalsPage from "./pages/SignalsPage";
import NotFound from "./pages/NotFound";

export default function App() {
  const { pathname } = useLocation();
  useEffect(() => {
    window.scrollTo(0, 0);
  }, [pathname]);

  return (
    <div className="shell">
      <header className="topbar">
        <NavLink to="/" className="brand">
          <span className="brand-mark" aria-hidden>{"{ }"}</span> DSA Trainer
        </NavLink>
        <nav className="nav">
          <NavLink to="/" end>Patterns</NavLink>
          <NavLink to="/signals">Spot the pattern</NavLink>
          {guides.map((g) => (
            <NavLink key={g.slug} to={`/guides/${g.slug}`}>{g.title.replace(/^Python /, "")}</NavLink>
          ))}
        </nav>
        <ThemeToggle />
      </header>
      <main className="main">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/patterns/:slug" element={<PatternPage />} />
          <Route path="/guides/:slug" element={<GuidePage />} />
          <Route path="/signals" element={<SignalsPage />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </main>
      <footer className="footer">Templates are tested with pytest · Python 3</footer>
    </div>
  );
}
