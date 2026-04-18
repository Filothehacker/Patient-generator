export default function Flashcard({ front, back, isFlipped, onFlip }) {
  return (
    <div data-testid="flashcard" onClick={onFlip}>
      <div>{isFlipped ? back : front}</div>
    </div>
  )
}
