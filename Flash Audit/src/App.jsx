import './index.css'
import { useState } from 'react'
import { LanguageProvider } from './contexts/LanguageContext'
import DeckGrid from './components/DeckGrid'
import StudySession from './components/StudySession'
import EndScreen from './components/EndScreen'
import cardsData from './data/cards.json'

export default function App() {
  const [screen, setScreen] = useState('home')
  const [activeDeckId, setActiveDeckId] = useState(null)

  function startDeck(deckId) {
    setActiveDeckId(deckId)
    setScreen('study')
  }

  function goHome() {
    setScreen('home')
    setActiveDeckId(null)
  }

  function goEnd() {
    setScreen('end')
  }

  const activeDeck = cardsData.find(d => d.id === activeDeckId) ?? null

  return (
    <LanguageProvider>
      {screen === 'home' && (
        <DeckGrid decks={cardsData} onStart={startDeck} />
      )}
      {screen === 'study' && activeDeck && (
        <StudySession deck={activeDeck} onEnd={goEnd} onBack={goHome} />
      )}
      {screen === 'end' && (
        <EndScreen onRestart={() => setScreen('study')} onHome={goHome} />
      )}
    </LanguageProvider>
  )
}
