export default function DeckCard({ deck, onStart }) {
  return (
    <div>
      <span>{deck.title}</span>
      <button onClick={() => onStart(deck.id)}>Studia</button>
    </div>
  )
}
