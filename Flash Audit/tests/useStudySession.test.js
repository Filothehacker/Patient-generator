import { renderHook, act } from '@testing-library/react'
import useStudySession from '../src/hooks/useStudySession'

const cards = [
  { id: 'c1', front_it: 'Q1', front_en: 'Q1en', back_it: 'A1', back_en: 'A1en' },
  { id: 'c2', front_it: 'Q2', front_en: 'Q2en', back_it: 'A2', back_en: 'A2en' },
  { id: 'c3', front_it: 'Q3', front_en: 'Q3en', back_it: 'A3', back_en: 'A3en' },
]

test('starts at index 0, not flipped', () => {
  const { result } = renderHook(() => useStudySession(cards))
  expect(result.current.currentIndex).toBe(0)
  expect(result.current.isFlipped).toBe(false)
})

test('flip toggles isFlipped', () => {
  const { result } = renderHook(() => useStudySession(cards))
  act(() => result.current.flip())
  expect(result.current.isFlipped).toBe(true)
  act(() => result.current.flip())
  expect(result.current.isFlipped).toBe(false)
})

test('next advances index and resets flip', () => {
  const { result } = renderHook(() => useStudySession(cards))
  act(() => result.current.flip())
  act(() => result.current.next())
  expect(result.current.currentIndex).toBe(1)
  expect(result.current.isFlipped).toBe(false)
})

test('prev does not go below 0', () => {
  const { result } = renderHook(() => useStudySession(cards))
  act(() => result.current.prev())
  expect(result.current.currentIndex).toBe(0)
})

test('isEnd is true when past last card', () => {
  const { result } = renderHook(() => useStudySession(cards))
  act(() => result.current.next())
  act(() => result.current.next())
  expect(result.current.isEnd).toBe(false)
  act(() => result.current.next())
  expect(result.current.isEnd).toBe(true)
})

test('restart resets to beginning', () => {
  const { result } = renderHook(() => useStudySession(cards))
  act(() => result.current.next())
  act(() => result.current.next())
  act(() => result.current.next())
  act(() => result.current.restart())
  expect(result.current.currentIndex).toBe(0)
  expect(result.current.isEnd).toBe(false)
})

test('currentCard returns correct card', () => {
  const { result } = renderHook(() => useStudySession(cards))
  expect(result.current.currentCard.id).toBe('c1')
  act(() => result.current.next())
  expect(result.current.currentCard.id).toBe('c2')
})
