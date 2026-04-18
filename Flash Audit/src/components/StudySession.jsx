import { useState } from 'react'
import { useLanguage } from '../contexts/LanguageContext'
import Header from './Header'
import Flashcard from './Flashcard'
import useStudySession from '../hooks/useStudySession'

const labels = {
  it: { card: 'Carta', of: 'di', shuffle: 'Mescola', shuffled: '⇌ Misto' },
  en: { card: 'Card', of: 'of', shuffle: 'Shuffle', shuffled: '⇌ On' },
}

export default function StudySession({ deck, onEnd, onBack }) {
  const { lang } = useLanguage()
  const l = labels[lang]
  const [shuffle, setShuffle] = useState(false)
  const session = useStudySession(deck.cards, shuffle)

  const front = session.currentCard?.[`front_${lang}`] ?? ''
  const back = session.currentCard?.[`back_${lang}`] ?? ''
  const progress = session.total > 0
    ? (session.currentIndex / session.total) * 100
    : 0

  function handleNext() {
    if (session.currentIndex >= session.total - 1) {
      onEnd()
    } else {
      session.next()
    }
  }

  if (!session.currentCard) return null

  return (
    <div className="page" data-testid="study-screen">
      <Header showBack onBack={onBack} />
      <div className="progress-bar">
        <div className="progress-fill" style={{ width: `${progress}%` }} />
      </div>
      <main className="study-main">
        <div className="study-meta">
          <span className="study-chapter">{deck.title}</span>
          <span className="study-counter">
            {l.card} {session.currentIndex + 1} {l.of} {session.total}
          </span>
        </div>
        <Flashcard
          front={front}
          back={back}
          isFlipped={session.isFlipped}
          onFlip={session.flip}
        />
        <div className="study-controls">
          <button
            className="nav-btn"
            onClick={session.prev}
            disabled={session.currentIndex === 0}
            aria-label="Previous card"
          >
            ←
          </button>
          <button
            className={`shuffle-btn${shuffle ? ' active' : ''}`}
            onClick={() => setShuffle(s => !s)}
          >
            {shuffle ? l.shuffled : l.shuffle}
          </button>
          <button
            className="nav-btn"
            onClick={handleNext}
            aria-label="Next card"
          >
            →
          </button>
        </div>
      </main>
    </div>
  )
}
