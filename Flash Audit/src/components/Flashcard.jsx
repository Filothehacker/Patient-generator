export default function Flashcard({ front, back, isFlipped, onFlip }) {
  return (
    <div className="flashcard-scene" onClick={onFlip}>
      <div className={`flashcard${isFlipped ? ' is-flipped' : ''}`} data-testid="flashcard">
        <div className="flashcard-face flashcard-front">
          <span className="card-hint">Domanda · Question</span>
          <p className="card-text">{front}</p>
          <span className="card-tap">tocca per risposta · tap to reveal</span>
        </div>
        <div className="flashcard-face flashcard-back">
          <span className="card-hint">Risposta · Answer</span>
          <p className="card-text">{back}</p>
          <span className="card-tap">continua → continue</span>
        </div>
      </div>
    </div>
  )
}
