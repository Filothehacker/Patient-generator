import { render, screen, fireEvent } from '@testing-library/react'
import { LanguageProvider, useLanguage } from '../src/contexts/LanguageContext'

function TestConsumer() {
  const { lang, setLang } = useLanguage()
  return (
    <div>
      <span data-testid="lang">{lang}</span>
      <button onClick={() => setLang(lang === 'it' ? 'en' : 'it')}>toggle</button>
    </div>
  )
}

test('default language is Italian', () => {
  render(<LanguageProvider><TestConsumer /></LanguageProvider>)
  expect(screen.getByTestId('lang')).toHaveTextContent('it')
})

test('toggles language between it and en', () => {
  render(<LanguageProvider><TestConsumer /></LanguageProvider>)
  fireEvent.click(screen.getByText('toggle'))
  expect(screen.getByTestId('lang')).toHaveTextContent('en')
  fireEvent.click(screen.getByText('toggle'))
  expect(screen.getByTestId('lang')).toHaveTextContent('it')
})
