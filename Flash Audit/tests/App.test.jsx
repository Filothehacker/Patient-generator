import { render, screen, fireEvent } from '@testing-library/react'
import App from '../src/App'

test('renders home screen by default', () => {
  render(<App />)
  expect(screen.getByTestId('home-screen')).toBeInTheDocument()
})

test('navigates to study screen when deck is selected', () => {
  render(<App />)
  const studyButtons = screen.getAllByText(/studia/i)
  fireEvent.click(studyButtons[0])
  expect(screen.getByTestId('study-screen')).toBeInTheDocument()
})

test('navigates back to home from study screen', () => {
  render(<App />)
  const studyButtons = screen.getAllByText(/studia/i)
  fireEvent.click(studyButtons[0])
  fireEvent.click(screen.getByTestId('back-to-home'))
  expect(screen.getByTestId('home-screen')).toBeInTheDocument()
})
