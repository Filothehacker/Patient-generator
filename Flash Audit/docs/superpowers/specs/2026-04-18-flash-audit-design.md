# Flash Audit — Flashcard App Design Spec

**Date:** 2026-04-18  
**Status:** Approved

---

## Overview

A static React + Vite flashcard web app to help students (Italian and international) learn the concepts from the Bocconi University *Bilancio (Modulo 1)* financial accounting course. Flashcards are bilingual (Italian / English), organized by chapter, and auto-extracted from the PDF `BILANCIO 1 - DISPENSA.pdf`.

---

## Architecture

**Type:** Static site — no backend, no database, no authentication.

**Stack:**
- React + Vite
- Custom CSS via the `frontend-design` skill (no UI library)
- No routing library — screen transitions handled via React state

**Data source:** `src/data/cards.json` — a single JSON file containing all chapter decks and cards, extracted from the PDF once and committed to the repo.

**Deployment:** Build output (`dist/`) deployable to GitHub Pages, Netlify, or Vercel.

---

## Data Structure

`src/data/cards.json`:

```json
[
  {
    "id": "ch1",
    "title": "Introduzione al Sistema di Contabilità Generale",
    "cards": [
      {
        "id": "ch1-1",
        "front_it": "Cos'è il bilancio d'esercizio?",
        "front_en": "What is the annual financial statement?",
        "back_it": "Un atto analitico di conoscenza critica circa il divenire della produzione economica d'impresa in un determinato periodo amministrativo.",
        "back_en": "An analytical act of critical knowledge about the evolution of a company's economic production in a given administrative period."
      }
    ]
  }
]
```

Cards are extracted from all chapters of the PDF. Each card has bilingual front (question) and back (answer). The JSON is the single source of truth and can be manually edited to fix individual cards.

---

## Screens & User Flow

### 1. Home Screen
- Header with app title and **IT / EN language toggle** (global, persists across screens)
- Grid of chapter deck cards, each showing:
  - Chapter title (in selected language)
  - Card count (e.g. "12 cards")
  - "Study" button
- Clicking "Study" navigates to the Study Session screen for that chapter

### 2. Study Session Screen
- Header with:
  - Chapter title
  - "Back to decks" button
  - "Shuffle" toggle
- Centered flashcard:
  - Front shows the question in the selected language
  - Click/tap to flip and reveal the answer
  - Smooth flip animation
- Progress bar: "Card 3 of 12"
- Previous / Next navigation arrows
- Language toggle remains accessible in header

### 3. End of Deck Screen
- "You finished this deck!" message
- "Restart" button (re-starts from card 1, reshuffles if shuffle is on)
- "Back to home" button

---

## Language

- A single React context holds the active language: `"it" | "en"`
- All card text (front and back) and UI labels switch based on this context
- The toggle is always visible in the header across all screens

---

## UI

- Built using the `frontend-design` skill for a polished, distinctive look
- No external UI library — custom CSS only
- Card flip uses CSS 3D transform animation
- Responsive: works on desktop and mobile

---

## Out of Scope (v1)

- Spaced repetition / scoring
- User accounts or progress persistence
- Adding new PDFs at runtime
- Multiple language pairs beyond IT / EN
