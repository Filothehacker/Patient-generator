export default function EndScreen({ onRestart, onHome }) {
  return (
    <div data-testid="end-screen">
      <button onClick={onRestart}>Restart</button>
      <button onClick={onHome}>Home</button>
    </div>
  )
}
