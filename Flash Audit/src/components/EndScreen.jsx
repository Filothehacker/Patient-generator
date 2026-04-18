import { useLanguage } from '../contexts/LanguageContext'
import Header from './Header'

const labels = {
  it: {
    title: 'Capitolo completato',
    subtitle: 'Hai completato tutte le carte di questo mazzo.',
    restart: 'Ricomincia',
    home: 'Torna ai mazzi',
  },
  en: {
    title: 'Chapter complete',
    subtitle: "You've gone through all the cards in this deck.",
    restart: 'Restart',
    home: 'Back to decks',
  },
}

export default function EndScreen({ onRestart, onHome }) {
  const { lang } = useLanguage()
  const l = labels[lang]

  return (
    <div className="page" data-testid="end-screen">
      <Header showBack onBack={onHome} />
      <main className="end-main">
        <div className="end-card">
          <div className="end-icon">✓</div>
          <h2 className="end-title">{l.title}</h2>
          <p className="end-subtitle">{l.subtitle}</p>
          <div className="end-actions">
            <button className="btn-primary" onClick={onRestart}>{l.restart}</button>
            <button className="btn-secondary" onClick={onHome}>{l.home}</button>
          </div>
        </div>
      </main>
    </div>
  )
}
