import { useLanguage } from '../contexts/LanguageContext'
import Header from './Header'
import DeckCard from './DeckCard'

const labels = {
  it: {
    subtitle: 'Bilancio — Modulo 1 · Università Bocconi',
    instruction: 'Scegli un capitolo per iniziare',
  },
  en: {
    subtitle: 'Financial Accounting — Module 1 · Bocconi University',
    instruction: 'Select a chapter to begin',
  },
}

export default function DeckGrid({ decks, onStart }) {
  const { lang } = useLanguage()
  const l = labels[lang]

  return (
    <div className="page">
      <Header />
      <main className="home-main">
        <div className="home-hero">
          <h1 className="home-title">Flash<em>Audit</em></h1>
          <p className="home-subtitle">{l.subtitle}</p>
          <p className="home-instruction">{l.instruction}</p>
        </div>
        <div className="deck-grid" data-testid="home-screen">
          {decks.map((deck, i) => (
            <DeckCard key={deck.id} deck={deck} onStart={onStart} index={i} />
          ))}
        </div>
      </main>
    </div>
  )
}
