import { useLanguage } from '../contexts/LanguageContext'

const labels = {
  it: { toggle: 'EN', back: '← Mazzi' },
  en: { toggle: 'IT', back: '← Decks' },
}

export default function Header({ showBack = false, onBack }) {
  const { lang, setLang } = useLanguage()
  const l = labels[lang]

  return (
    <header className="header">
      <div className="header-left">
        {showBack ? (
          <button className="back-btn" data-testid="back-to-home" onClick={onBack}>
            {l.back}
          </button>
        ) : (
          <span className="header-logo">Flash<em style={{ fontStyle: 'italic', color: 'var(--gold)' }}>Audit</em></span>
        )}
      </div>
      <button
        className="lang-toggle"
        onClick={() => setLang(lang === 'it' ? 'en' : 'it')}
        aria-label="Toggle language"
      >
        {l.toggle}
      </button>
    </header>
  )
}
