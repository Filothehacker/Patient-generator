import { useState, useMemo, useEffect } from 'react'

export default function useStudySession(cards, shuffle = false) {
  const deck = useMemo(() => {
    if (!shuffle) return cards
    return [...cards].sort(() => Math.random() - 0.5)
  }, [cards, shuffle])

  const [currentIndex, setCurrentIndex] = useState(0)
  const [isFlipped, setIsFlipped] = useState(false)

  useEffect(() => {
    setCurrentIndex(0)
    setIsFlipped(false)
  }, [shuffle])

  const isEnd = currentIndex >= deck.length

  function flip() {
    setIsFlipped(f => !f)
  }

  function next() {
    setIsFlipped(false)
    setCurrentIndex(i => i + 1)
  }

  function prev() {
    if (currentIndex === 0) return
    setIsFlipped(false)
    setCurrentIndex(i => i - 1)
  }

  return {
    currentIndex,
    currentCard: deck[currentIndex] ?? null,
    isFlipped,
    isEnd,
    total: deck.length,
    flip,
    next,
    prev,
  }
}
