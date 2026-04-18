import { useLanguage } from '../contexts/LanguageContext'

const labels = {
  it: { study: 'Studia', cards: 'carte' },
  en: { study: 'Study', cards: 'cards' },
}

export default function DeckCard({ deck, onStart, index }) {
  const { lang } = useLanguage()
  const l = labels[lang]

  return (
    <article className="deck-card" style={{ '--i': index }}>
      <div className="deck-card-inner">
        <span className="deck-num">{String(index + 1).padStart(2, '0')}</span>
        <h2 className="deck-title">{deck.title}</h2>
        <div className="deck-footer">
          <span className="deck-count">{deck.cards.length} {l.cards}</span>
          <button className="study-btn" onClick={() => onStart(deck.id)}>
            {l.study} →
          </button>
        </div>
      </div>
    </article>
  )
}
