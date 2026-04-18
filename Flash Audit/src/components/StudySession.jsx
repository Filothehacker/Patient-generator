export default function StudySession({ deck, onEnd, onBack }) {
  return (
    <div data-testid="study-screen">
      <button data-testid="back-to-home" onClick={onBack}>Back</button>
      <button onClick={onEnd}>End</button>
    </div>
  )
}
