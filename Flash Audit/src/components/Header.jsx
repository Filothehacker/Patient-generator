export default function Header({ title, onBack, showBack }) {
  return (
    <header>
      {showBack && <button data-testid="back-to-home" onClick={onBack}>←</button>}
      <h1>{title}</h1>
    </header>
  )
}
