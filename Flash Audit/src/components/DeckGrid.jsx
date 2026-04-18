export default function DeckGrid({ decks, onStart }) {
  return (
    <div data-testid="home-screen">
      {decks.map(deck => (
        <div key={deck.id}>
          <span>{deck.title}</span>
          <button onClick={() => onStart(deck.id)}>Studia</button>
        </div>
      ))}
    </div>
  )
}
