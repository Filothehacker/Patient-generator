# Flash Audit Flashcard App — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a bilingual (IT/EN) React + Vite static flashcard web app from the Bocconi *Bilancio (Modulo 1)* accounting PDF, organized by chapter, with flip animations and simple practice mode.

**Architecture:** Static React + Vite site. All card data lives in `src/data/cards.json` (committed to repo). Screen navigation is state-based (no router). A LanguageContext provides the active language globally.

**Tech Stack:** React 18, Vite 5, Vitest + @testing-library/react for tests, custom CSS via frontend-design skill (no UI library).

---

## File Map

| Path | Responsibility |
|---|---|
| `src/data/cards.json` | All flashcard content, structured by chapter |
| `src/contexts/LanguageContext.jsx` | Global IT/EN language state and toggle |
| `src/hooks/useStudySession.js` | Card navigation, shuffle, flip, progress logic |
| `src/components/Header.jsx` | App header with title, language toggle, back button |
| `src/components/DeckGrid.jsx` | Home screen: grid of chapter deck cards |
| `src/components/DeckCard.jsx` | Single deck card tile (title, count, Study button) |
| `src/components/Flashcard.jsx` | Single flashcard with 3D flip animation |
| `src/components/StudySession.jsx` | Study screen: card + navigation + progress bar |
| `src/components/EndScreen.jsx` | Completion screen with restart/home buttons |
| `src/App.jsx` | Root component: screen state machine (home/study/end) |
| `src/main.jsx` | React entry point |
| `src/index.css` | Global styles + CSS variables |
| `tests/LanguageContext.test.jsx` | Tests for language context |
| `tests/useStudySession.test.js` | Tests for study session hook |
| `tests/App.test.jsx` | Integration tests for screen transitions |

---

## Task 1: Write cards.json

**Files:**
- Create: `src/data/cards.json`

- [ ] **Step 1: Create the src/data directory and write cards.json**

Create `src/data/cards.json` with the following complete content:

```json
[
  {
    "id": "ch1",
    "title": "Introduzione al Sistema di Contabilità Generale",
    "cards": [
      {
        "id": "ch1-1",
        "front_it": "Quali sono i tre momenti dell'amministrazione economica dell'impresa?",
        "front_en": "What are the three moments of a company's economic administration?",
        "back_it": "Gestione, Organizzazione, Rilevazione",
        "back_en": "Management (Gestione), Organisation (Organizzazione), Recording (Rilevazione)"
      },
      {
        "id": "ch1-2",
        "front_it": "Cos'è il bilancio d'esercizio?",
        "front_en": "What is the annual financial statement (bilancio d'esercizio)?",
        "back_it": "Un atto analitico di conoscenza critica circa il divenire della produzione economica d'impresa in un determinato periodo amministrativo annuale.",
        "back_en": "An analytical act of critical knowledge about the evolution of a company's economic production during a specific annual administrative period."
      },
      {
        "id": "ch1-3",
        "front_it": "Quali sono le tre tavole patrimoniali che misurano l'equilibrio aziendale?",
        "front_en": "What are the three financial statements that measure company equilibrium?",
        "back_it": "Stato Patrimoniale (dimensione patrimoniale), Conto Economico (dimensione reddituale), Rendiconto Finanziario (dimensione finanziaria)",
        "back_en": "Balance Sheet / Stato Patrimoniale (assets/liabilities), Income Statement / Conto Economico (profit/loss), Cash Flow Statement / Rendiconto Finanziario (liquidity)"
      },
      {
        "id": "ch1-4",
        "front_it": "Cos'è il principio di competenza economica?",
        "front_en": "What is the accrual principle (principio di competenza economica)?",
        "back_it": "Componenti positivi e negativi di reddito devono essere imputati al periodo amministrativo cui afferiscono, e devono essere tra loro significativamente correlati.",
        "back_en": "Positive and negative income components must be attributed to the period they belong to, and must be significantly correlated with each other."
      },
      {
        "id": "ch1-5",
        "front_it": "Cosa si intende per MMC (Momento di variazione di Moneta o Credito)?",
        "front_en": "What is the MMC (Moment of Money or Credit Variation)?",
        "back_it": "Il momento della fatturazione, in cui si effettua la rilevazione contabile poiché emergono tutti i dati necessari a definire oggettivamente l'entità della variazione monetaria.",
        "back_en": "The moment of invoicing, when the accounting entry is recorded because all data needed to objectively define the monetary variation become available."
      },
      {
        "id": "ch1-6",
        "front_it": "Qual è l'equazione fondamentale del bilancio?",
        "front_en": "What is the fundamental accounting equation?",
        "back_it": "Attività = Passività + Patrimonio netto (ovvero: Investimenti = Finanziamenti)",
        "back_en": "Assets = Liabilities + Equity (i.e., Investments = Financing)"
      },
      {
        "id": "ch1-7",
        "front_it": "Quali sono le tre tipologie di valori che formano il risultato economico d'esercizio?",
        "front_en": "What are the three types of values that make up the annual result?",
        "back_it": "1. Quantità economiche (certe e incontrovertibili), 2. Valori stimati (suscettibili di verifica futura), 3. Valori congetturati (non verificabili successivamente)",
        "back_en": "1. Economic quantities (certain and incontrovertible), 2. Estimated values (subject to future verification), 3. Conjectured values (not subsequently verifiable)"
      },
      {
        "id": "ch1-8",
        "front_it": "Cosa sono i valori numerari e non numerari?",
        "front_en": "What are monetary (numerari) and non-monetary values?",
        "back_it": "Valori numerari: modificano la disponibilità monetaria dell'azienda (cassa, crediti, debiti). Valori non numerari: modificano la disponibilità di condizioni produttive non monetarie (costi, ricavi, immobilizzazioni).",
        "back_en": "Monetary values (numerari): affect the company's monetary resources (cash, receivables, payables). Non-monetary values: affect non-monetary productive resources (costs, revenues, fixed assets)."
      }
    ]
  },
  {
    "id": "ch2",
    "title": "La Costituzione d'Azienda",
    "cards": [
      {
        "id": "ch2-1",
        "front_it": "Cosa si intende per conferimento in sede di costituzione societaria?",
        "front_en": "What is a 'conferimento' (capital contribution) in company formation?",
        "back_it": "L'apporto eseguito dai soci per costituire il capitale della società; può avvenire in denaro o in natura (beni mobili, immobili, rami d'azienda, crediti).",
        "back_en": "The contribution made by shareholders to form the company's capital; can be in cash or in kind (movable/immovable assets, business units, receivables)."
      },
      {
        "id": "ch2-2",
        "front_it": "Quale percentuale del conferimento in denaro deve essere versata su conto vincolato alla sottoscrizione (S.p.A.)?",
        "front_en": "What percentage of the cash contribution must be deposited in a restricted account at subscription (S.p.A.)?",
        "back_it": "25% dei conferimenti in denaro deve essere versato immediatamente su un conto corrente vincolato intestato alla società.",
        "back_en": "25% of cash contributions must be immediately deposited in a restricted bank account in the company's name."
      },
      {
        "id": "ch2-3",
        "front_it": "Come si registra contabilmente la sottoscrizione del capitale sociale?",
        "front_en": "How is the subscription of share capital recorded in accounting?",
        "back_it": "Dare + AZIONISTI C/SOTTOSCRIZIONI (SP); Avere – CAPITALE SOCIALE (SP)",
        "back_en": "Debit (+) SHAREHOLDERS SUBSCRIPTIONS ACCOUNT (BS); Credit (–) SHARE CAPITAL (BS)"
      },
      {
        "id": "ch2-4",
        "front_it": "Quando vengono svincolate le somme del conto corrente vincolato?",
        "front_en": "When are the funds in the restricted bank account released?",
        "back_it": "Quando la società viene iscritta nel Registro delle Imprese e acquisisce personalità giuridica.",
        "back_en": "When the company is registered in the Companies Register (Registro delle Imprese) and acquires legal personality."
      },
      {
        "id": "ch2-5",
        "front_it": "Quali obblighi formali prevede il Codice civile per la costituzione di S.p.A. e S.r.l.?",
        "front_en": "What formal requirements does the Civil Code impose for S.p.A. and S.r.l. formation?",
        "back_it": "Atto costitutivo + Statuto davanti a notaio; sottoscrivere per intero il capitale sociale; versare il 25% dei conferimenti in denaro su conto vincolato prima dell'iscrizione.",
        "back_en": "Articles of incorporation + bylaws before a notary; full subscription of share capital; deposit of 25% of cash contributions in a restricted account before registration."
      }
    ]
  },
  {
    "id": "ch3",
    "title": "Le Operazioni di Acquisto dei Fattori Produttivi Correnti",
    "cards": [
      {
        "id": "ch3-1",
        "front_it": "Cosa sono i fattori produttivi correnti?",
        "front_en": "What are current production factors?",
        "back_it": "Fattori produttivi a breve ciclo di utilizzo destinati ad essere venduti o utilizzati per la produzione: beni (merci, materie prime) e servizi (trasporti, consulenze, locazioni).",
        "back_en": "Short-cycle production factors used in production or for sale: goods (merchandise, raw materials) and services (transport, consulting, rentals)."
      },
      {
        "id": "ch3-2",
        "front_it": "Come si registra contabilmente il ricevimento di una fattura di acquisto di merci?",
        "front_en": "How is the receipt of a purchase invoice for goods recorded?",
        "back_it": "Dare + MERCI C/ACQUISTI (CE) + ERARIO C/IVA (SP); Avere – DEBITI V/FORNITORI (SP)",
        "back_en": "Debit (+) GOODS PURCHASES (IS) + VAT RECEIVABLE (BS); Credit (–) TRADE PAYABLES (BS)"
      },
      {
        "id": "ch3-3",
        "front_it": "Differenza tra sconto incondizionato e sconto di cassa negli acquisti?",
        "front_en": "What is the difference between an unconditional discount and a cash discount on purchases?",
        "back_it": "Sconto incondizionato: riduce il costo d'acquisto e la base imponibile IVA. Sconto di cassa (condizionato): è un provento finanziario, non riduce il costo né l'IVA.",
        "back_en": "Unconditional discount: reduces the purchase cost and the VAT taxable base. Cash discount (conditional): is a financial income, does not reduce cost or VAT."
      },
      {
        "id": "ch3-4",
        "front_it": "Come si registrano i resi su acquisti?",
        "front_en": "How are purchase returns recorded?",
        "back_it": "Dare + DEBITI V/FORNITORI (SP); Avere – RESI SU ACQUISTI (CE) + ERARIO C/IVA (SP). Si riceve una nota di credito dal fornitore.",
        "back_en": "Debit (+) TRADE PAYABLES (BS); Credit (–) PURCHASE RETURNS (IS) + VAT RECEIVABLE (BS). A credit note is received from the supplier."
      },
      {
        "id": "ch3-5",
        "front_it": "Cosa sono le cambiali passive e come si registrano?",
        "front_en": "What are bills payable (cambiali passive) and how are they recorded?",
        "back_it": "Titoli di credito esecutivi (effetti) emessi dal debitore; si registrano sostituendo il DEBITO V/FORNITORI con CAMBIALI PASSIVE (SP). Al pagamento: Dare + CAMBIALI PASSIVE; Avere – BANCHE C/C.",
        "back_en": "Executive credit instruments (bills of exchange) issued by the debtor; recorded by replacing TRADE PAYABLES with BILLS PAYABLE (BS). On payment: Debit (+) BILLS PAYABLE; Credit (–) BANK ACCOUNT."
      },
      {
        "id": "ch3-6",
        "front_it": "Come si gestiscono gli anticipi ai fornitori (tre MMC)?",
        "front_en": "How are advances to suppliers handled (three MMC steps)?",
        "back_it": "1. Pagamento anticipo: Dare + DEBITI V/FORNITORI; Avere – BANCHE C/C. 2. Fattura anticipo: Dare + FORNITORI C/ACCONTI + ERARIO C/IVA; Avere – DEBITI V/FORNITORI. 3. Fattura saldo: Dare + MERCI C/ACQUISTI + ERARIO C/IVA; Avere – DEBITI V/FORNITORI + FORNITORI C/ACCONTI.",
        "back_en": "1. Advance payment: Debit (+) TRADE PAYABLES; Credit (–) BANK. 2. Advance invoice: Debit (+) SUPPLIER ADVANCES + VAT; Credit (–) TRADE PAYABLES. 3. Final invoice: Debit (+) GOODS PURCHASES + VAT on balance; Credit (–) TRADE PAYABLES + SUPPLIER ADVANCES."
      }
    ]
  },
  {
    "id": "ch4",
    "title": "Le Operazioni di Vendita dei Fattori Produttivi Correnti",
    "cards": [
      {
        "id": "ch4-1",
        "front_it": "Come si registra contabilmente la vendita di merci?",
        "front_en": "How is the sale of goods recorded in accounting?",
        "back_it": "Dare + CREDITI V/CLIENTI (SP); Avere – MERCI C/VENDITE (CE) + ERARIO C/IVA (SP)",
        "back_en": "Debit (+) TRADE RECEIVABLES (BS); Credit (–) GOODS SALES (IS) + VAT PAYABLE (BS)"
      },
      {
        "id": "ch4-2",
        "front_it": "Come si registrano i resi su vendite?",
        "front_en": "How are sales returns recorded?",
        "back_it": "Dare + RESI SU VENDITE (CE) + ERARIO C/IVA (SP); Avere – CREDITI V/CLIENTI (SP). Si emette una nota di credito al cliente.",
        "back_en": "Debit (+) SALES RETURNS (IS) + VAT RECEIVABLE (BS); Credit (–) TRADE RECEIVABLES (BS). A credit note is issued to the customer."
      },
      {
        "id": "ch4-3",
        "front_it": "Come funziona il regolamento tramite cambiale attiva?",
        "front_en": "How does settlement via active bill of exchange (cambiale attiva) work?",
        "back_it": "Dare + CAMBIALI ATTIVE (SP); Avere – CREDITI V/CLIENTI (SP). Alla scadenza: Dare + BANCHE C/C (netto) + SPESE BANCARIE (CE); Avere – CAMBIALI ATTIVE (SP).",
        "back_en": "Debit (+) BILLS RECEIVABLE (BS); Credit (–) TRADE RECEIVABLES (BS). At maturity: Debit (+) BANK (net) + BANK CHARGES (IS); Credit (–) BILLS RECEIVABLE."
      },
      {
        "id": "ch4-4",
        "front_it": "Differenza tra abbuono passivo e sconto incondizionato passivo?",
        "front_en": "What is the difference between a passive allowance and an unconditional passive discount?",
        "back_it": "Abbuono passivo: per merce difettosa; IVA calcolata e variata. Sconto incondizionato passivo: IVA calcolata sull'imponibile scontato (valore merce – sconto).",
        "back_en": "Passive allowance: for defective goods; VAT is calculated and adjusted. Unconditional passive discount: VAT is calculated on the discounted taxable base (goods value – discount)."
      },
      {
        "id": "ch4-5",
        "front_it": "Come si gestiscono gli anticipi ricevuti dai clienti?",
        "front_en": "How are advances received from customers handled?",
        "back_it": "1. Ricezione anticipo: Dare + BANCHE C/C; Avere – CREDITI V/CLIENTI. 2. Fattura anticipo: Dare + CREDITI V/CLIENTI; Avere – CLIENTI C/ACCONTI + ERARIO C/IVA. 3. Fattura saldo: Dare + CREDITI V/CLIENTI + CLIENTI C/ACCONTI; Avere – MERCI C/VENDITE + ERARIO C/IVA sull'imponibile.",
        "back_en": "1. Receive advance: Debit (+) BANK; Credit (–) TRADE RECEIVABLES. 2. Advance invoice: Debit (+) TRADE RECEIVABLES; Credit (–) CUSTOMER ADVANCES + VAT. 3. Final invoice: Debit (+) TRADE RECEIVABLES + CUSTOMER ADVANCES; Credit (–) GOODS SALES + VAT on balance."
      }
    ]
  },
  {
    "id": "ch5",
    "title": "La Remunerazione del Lavoro Dipendente",
    "cards": [
      {
        "id": "ch5-1",
        "front_it": "Cos'è il TFR (Trattamento di Fine Rapporto)?",
        "front_en": "What is the TFR (severance pay / end-of-employment indemnity)?",
        "back_it": "Retribuzione differita accantonata annualmente dall'impresa; viene corrisposta al dipendente alla cessazione del rapporto di lavoro. Accantonamento: Dare + ACCANTONAMENTO TFR (CE); Avere – FONDO TFR (SP).",
        "back_en": "Deferred remuneration accrued annually by the company and paid to the employee when employment ends. Accrual: Debit (+) TFR PROVISION (IS); Credit (–) TFR FUND (BS)."
      },
      {
        "id": "ch5-2",
        "front_it": "Come si liquidano le retribuzioni dei dipendenti? Quali conti si usano?",
        "front_en": "How are employee salaries settled? Which accounts are used?",
        "back_it": "Dare + RETRIBUZIONI LORDE (CE); Avere – DEBITI V/DIPENDENTI (SP netto) + DEBITI V/ERARIO PER RITENUTE (SP IRPEF) + DEBITI V/INPS A CARICO DIPENDENTE (SP contributi).",
        "back_en": "Debit (+) GROSS SALARIES (IS); Credit (–) PAYABLE TO EMPLOYEES (BS net) + INCOME TAX PAYABLE (BS IRPEF) + SOCIAL SECURITY PAYABLE-EMPLOYEE SHARE (BS)."
      },
      {
        "id": "ch5-3",
        "front_it": "Cosa sono i contributi previdenziali a carico dell'azienda?",
        "front_en": "What are employer social security contributions?",
        "back_it": "Oneri sostenuti dall'impresa verso l'INPS per la previdenza dei dipendenti, oltre alla retribuzione netta. Dare + ONERI SOCIALI (CE); Avere – DEBITI V/INPS (SP).",
        "back_en": "Costs borne by the company towards INPS for employee social security, in addition to net salary. Debit (+) SOCIAL SECURITY COSTS (IS); Credit (–) INPS PAYABLE (BS)."
      },
      {
        "id": "ch5-4",
        "front_it": "Differenza tra retribuzione immediata e retribuzione differita?",
        "front_en": "What is the difference between immediate and deferred remuneration?",
        "back_it": "Retribuzione immediata: stipendio/salario periodico erogato durante il rapporto di lavoro. Retribuzione differita: TFR, erogato al termine del rapporto di lavoro.",
        "back_en": "Immediate remuneration: periodic salary/wage paid during employment. Deferred remuneration: TFR (severance pay), paid when employment ends."
      }
    ]
  },
  {
    "id": "ch6",
    "title": "Le Operazioni di Finanziamento Corrente",
    "cards": [
      {
        "id": "ch6-1",
        "front_it": "Cos'è l'IVA e chi la sopporta effettivamente?",
        "front_en": "What is VAT (IVA) and who ultimately bears it?",
        "back_it": "Imposta sul Valore Aggiunto: imposta indiretta sui consumi applicata alle cessioni di beni e prestazioni di servizi. Incide esclusivamente sul consumatore finale, non sull'impresa.",
        "back_en": "Value Added Tax: an indirect tax on consumption applied to sales of goods and services. It falls exclusively on the final consumer, not on the business."
      },
      {
        "id": "ch6-2",
        "front_it": "Come si liquida l'IVA periodicamente?",
        "front_en": "How is VAT settled periodically?",
        "back_it": "Si compensa l'IVA a credito (acquisti) con l'IVA a debito (vendite). Se debito > credito → versamento all'Erario. Se credito > debito → credito verso l'Erario da riportare.",
        "back_en": "Input VAT (on purchases) is offset against output VAT (on sales). If output > input → payment to tax authority. If input > output → VAT credit carried forward."
      },
      {
        "id": "ch6-3",
        "front_it": "Cosa sono le operazioni esenti IVA? Fare un esempio.",
        "front_en": "What are VAT-exempt transactions? Give an example.",
        "back_it": "Operazioni su cui non si calcola l'IVA per motivi economico-sociali, ma che devono essere fatturate. Esempi: prestazioni sanitarie, operazioni finanziarie.",
        "back_en": "Transactions on which VAT is not charged for economic/social reasons, but which must still be invoiced. Examples: healthcare services, financial transactions."
      },
      {
        "id": "ch6-4",
        "front_it": "Cos'è l'IVA indetraibile e come si tratta contabilmente?",
        "front_en": "What is non-deductible VAT and how is it treated in accounting?",
        "back_it": "Quota di IVA che non può essere recuperata (es. 60% su automezzi). Si capitalizza come onere accessorio sul valore del bene strumentale, o si iscrive a CE come costo se riferita a beni di consumo.",
        "back_en": "The portion of VAT that cannot be reclaimed (e.g. 60% on company vehicles). It is capitalised as an accessory cost on the asset's value, or expensed in the IS if related to consumables."
      }
    ]
  },
  {
    "id": "ch7",
    "title": "Le Operazioni di Finanziamento Non Corrente",
    "cards": [
      {
        "id": "ch7-1",
        "front_it": "Cos'è un mutuo passivo?",
        "front_en": "What is a mortgage/long-term loan (mutuo passivo)?",
        "back_it": "Finanziamento a lungo termine in cui la banca eroga una somma che l'impresa rimborsa a rate periodiche, ciascuna composta da quota capitale e quota interessi.",
        "back_en": "A long-term loan in which the bank disburses a sum that the company repays in periodic instalments, each consisting of a principal portion and an interest portion."
      },
      {
        "id": "ch7-2",
        "front_it": "Cos'è un prestito obbligazionario?",
        "front_en": "What is a bond loan (prestito obbligazionario)?",
        "back_it": "Finanziamento raccolto emettendo obbligazioni sul mercato; i sottoscrittori ricevono cedole periodiche (interessi) e il rimborso del valore nominale a scadenza.",
        "back_en": "Financing raised by issuing bonds on the market; subscribers receive periodic coupons (interest) and repayment of the nominal value at maturity."
      },
      {
        "id": "ch7-3",
        "front_it": "Differenza tra aggio e disaggio di emissione?",
        "front_en": "What is the difference between issue premium (aggio) and issue discount (disaggio)?",
        "back_it": "Aggio: emissione sopra la pari (il sottoscrittore paga 110, la società rimborsa 100). Disaggio: emissione sotto la pari (il sottoscrittore paga 95, la società rimborsa 100).",
        "back_en": "Issue premium (aggio): above par (subscriber pays 110, company repays 100). Issue discount (disaggio): below par (subscriber pays 95, company repays 100)."
      },
      {
        "id": "ch7-4",
        "front_it": "Quando si applica il metodo del costo ammortizzato ai debiti?",
        "front_en": "When is the amortised cost method applied to liabilities?",
        "back_it": "Si applica ai debiti a medio-lungo termine (scadenza > 12 mesi) con costi di transazione rilevanti (disaggi, aggi, commissioni, spese legali). Non si applica se i costi sono irrilevanti.",
        "back_en": "Applied to medium/long-term liabilities (maturity > 12 months) with significant transaction costs (discounts, premiums, commissions, legal fees). Not applied if costs are immaterial."
      },
      {
        "id": "ch7-5",
        "front_it": "Cosa rappresenta il TIR nel metodo del costo ammortizzato?",
        "front_en": "What does the IRR (TIR) represent in the amortised cost method?",
        "back_it": "Il Tasso Interno di Rendimento è il tasso di interesse effettivo che attualizza i flussi di cassa futuri del prestito al valore iscritto inizialmente. Serve per calcolare gli interessi effettivi di ciascun periodo.",
        "back_en": "The Internal Rate of Return is the effective interest rate that discounts all future cash flows of the loan back to its initial carrying amount. Used to calculate effective interest for each period."
      }
    ]
  },
  {
    "id": "ch8",
    "title": "Le Operazioni di Investimento in Fattori Produttivi Pluriennali",
    "cards": [
      {
        "id": "ch8-1",
        "front_it": "Cosa sono le immobilizzazioni materiali?",
        "front_en": "What are tangible fixed assets (immobilizzazioni materiali)?",
        "back_it": "Fattori produttivi di uso durevole che riversano la loro utilità su più esercizi tramite quote di ammortamento. Es: terreni, fabbricati, impianti, macchinari, automezzi.",
        "back_en": "Durable productive assets whose utility extends across multiple periods through depreciation charges. Examples: land, buildings, plant, machinery, vehicles."
      },
      {
        "id": "ch8-2",
        "front_it": "Cosa sono le immobilizzazioni immateriali? Quali categorie esistono?",
        "front_en": "What are intangible fixed assets? What categories exist?",
        "back_it": "Elementi del patrimonio privi di tangibilità. Tre categorie: (1) beni immateriali (brevetti, marchi, software), (2) oneri pluriennali (costi d'impianto, sviluppo), (3) avviamento.",
        "back_en": "Intangible assets with no physical substance. Three categories: (1) intangible assets (patents, trademarks, software), (2) deferred costs (start-up, development), (3) goodwill."
      },
      {
        "id": "ch8-3",
        "front_it": "Come si registra l'acquisto di un'immobilizzazione materiale?",
        "front_en": "How is the purchase of a tangible fixed asset recorded?",
        "back_it": "Dare + [IMPIANTI / FABBRICATI / MACCHINARI...] (SP) + ERARIO C/IVA (SP); Avere – DEBITI V/FORNITORI (SP)",
        "back_en": "Debit (+) [PLANT / BUILDINGS / MACHINERY...] (BS) + VAT RECEIVABLE (BS); Credit (–) TRADE PAYABLES (BS)"
      },
      {
        "id": "ch8-4",
        "front_it": "Come si tratta l'IVA indetraibile al 60% su un automezzo?",
        "front_en": "How is the 60% non-deductible VAT on a company vehicle treated?",
        "back_it": "Il 60% dell'IVA non detraibile si capitalizza come onere accessorio sul valore del bene. Dare + AUTOMEZZI (SP) per il 60% dell'IVA; solo il 40% resta in ERARIO C/IVA (SP).",
        "back_en": "The 60% non-deductible VAT is capitalised as an accessory cost on the asset. Debit (+) VEHICLES (BS) for 60% of VAT; only 40% remains as VAT RECEIVABLE (BS)."
      },
      {
        "id": "ch8-5",
        "front_it": "Come si registra l'ammortamento di un'immobilizzazione?",
        "front_en": "How is depreciation/amortisation of a fixed asset recorded?",
        "back_it": "Dare + AMMORTAMENTO [IMPIANTI/BREVETTI...] (CE); Avere – FONDO AMMORTAMENTO [IMPIANTI/BREVETTI...] (SP). Il fondo si accumula fino ad azzerare il valore netto contabile del bene.",
        "back_en": "Debit (+) DEPRECIATION [PLANT/PATENTS...] (IS); Credit (–) ACCUMULATED DEPRECIATION [PLANT/PATENTS...] (BS). The fund accumulates until the net book value reaches zero."
      }
    ]
  },
  {
    "id": "ch9",
    "title": "Le Scritture di Assestamento",
    "cards": [
      {
        "id": "ch9-1",
        "front_it": "Cos'è un risconto attivo e quando si usa?",
        "front_en": "What is a prepaid expense (risconto attivo) and when is it used?",
        "back_it": "Quota di costo già pagato nell'esercizio corrente ma di competenza dell'esercizio futuro (es. affitto anticipato). Dare + RISCONTO ATTIVO (SP); Avere – [COSTO] (CE).",
        "back_en": "A portion of a cost paid in the current period but belonging to a future period (e.g. prepaid rent). Debit (+) PREPAID EXPENSE (BS); Credit (–) [COST] (IS)."
      },
      {
        "id": "ch9-2",
        "front_it": "Cos'è un rateo passivo e quando si usa?",
        "front_en": "What is an accrued expense (rateo passivo) and when is it used?",
        "back_it": "Quota di costo di competenza dell'esercizio corrente che si manifesterà solo nell'esercizio futuro (es. interessi passivi da pagare a gennaio). Dare + [COSTO] (CE); Avere – RATEI PASSIVI (SP).",
        "back_en": "A portion of a cost belonging to the current period but payable in a future period (e.g. interest payable in January). Debit (+) [COST] (IS); Credit (–) ACCRUED EXPENSES (BS)."
      },
      {
        "id": "ch9-3",
        "front_it": "Come si scelgono ratei vs risconti? Regola pratica.",
        "front_en": "How do you choose between accruals (ratei) and deferrals (risconti)? Practical rule.",
        "back_it": "Risconto: si toglie (il pagamento è avvenuto all'inizio del periodo). Rateo: si aggiunge (il pagamento avverrà alla fine). Attivo/passivo dipende dalla contropartita: CPR → scrittura attiva; CNR → scrittura passiva.",
        "back_en": "Deferral (risconto): subtract (payment happened at the start of the period). Accrual (rateo): add (payment happens at the end). Active/passive depends on the counterpart: revenue → active entry; cost → passive entry."
      },
      {
        "id": "ch9-4",
        "front_it": "Come si registrano le rimanenze finali di magazzino?",
        "front_en": "How are closing inventory balances (rimanenze finali) recorded?",
        "back_it": "Dare + RIMANENZE DI MERCI (SP); Avere – VARIAZIONE RIMANENZE (CE). Le rimanenze iniziali del nuovo esercizio: Dare + VARIAZIONE RIMANENZE (CE); Avere – RIMANENZE DI MERCI (SP).",
        "back_en": "Debit (+) INVENTORY (BS); Credit (–) CHANGE IN INVENTORIES (IS). Opening inventory next year: Debit (+) CHANGE IN INVENTORIES (IS); Credit (–) INVENTORY (BS)."
      },
      {
        "id": "ch9-5",
        "front_it": "Cosa sono le fatture da ricevere e come si registrano?",
        "front_en": "What are invoices to be received (fatture da ricevere) and how are they recorded?",
        "back_it": "Valori presunti per beni/servizi ricevuti ma non ancora fatturati. Al 31/12: Dare + MERCI C/ACQUISTI (CE) senza IVA; Avere – FATTURE DA RICEVERE (SP). All'arrivo fattura: si chiude FATTURE DA RICEVERE e si apre DEBITI V/FORNITORI + ERARIO C/IVA.",
        "back_en": "Estimated values for goods/services received but not yet invoiced. At 31/12: Debit (+) GOODS PURCHASES (IS) without VAT; Credit (–) INVOICES TO RECEIVE (BS). On receipt: close INVOICES TO RECEIVE and open TRADE PAYABLES + VAT RECEIVABLE."
      },
      {
        "id": "ch9-6",
        "front_it": "Cos'è un fondo rischi e perché si accantona?",
        "front_en": "What is a risk provision (fondo rischi) and why is it accrued?",
        "back_it": "Posta del passivo per passività potenziali probabili (P > 50%) e incerte nell'importo/data. Accantonamento: Dare + ACCANTONAMENTO FONDO RISCHI (CE); Avere – FONDO RISCHI (SP). Rispetta il principio di prudenza.",
        "back_en": "A liability for probable contingent obligations (P > 50%), uncertain in amount or timing. Accrual: Debit (+) RISK PROVISION EXPENSE (IS); Credit (–) RISK PROVISION (BS). Applies the prudence principle."
      }
    ]
  },
  {
    "id": "ch10",
    "title": "Il Calcolo delle Imposte e la Chiusura dei Conti",
    "cards": [
      {
        "id": "ch10-1",
        "front_it": "Cosa sono IRES e IRAP?",
        "front_en": "What are IRES and IRAP?",
        "back_it": "IRES (Imposta sul Reddito delle Società): colpisce il reddito d'esercizio delle società. IRAP (Imposta Regionale sulle Attività Produttive): colpisce il valore della produzione netta (A – B del CE civilistico).",
        "back_en": "IRES (Corporate Income Tax): levied on the company's net income. IRAP (Regional Tax on Productive Activities): levied on net production value (section A – B of the statutory income statement)."
      },
      {
        "id": "ch10-2",
        "front_it": "Come funzionano gli acconti d'imposta?",
        "front_en": "How do tax advance payments work?",
        "back_it": "1° acconto: 40% dell'imposta dell'anno precedente, entro il 30/06. 2° acconto: 60%, entro il 30/11. Il saldo si versa al 30/06 dell'anno successivo dopo la dichiarazione.",
        "back_en": "1st instalment: 40% of prior year tax, by 30/06. 2nd instalment: 60%, by 30/11. The balance is paid by 30/06 of the following year after filing the tax return."
      },
      {
        "id": "ch10-3",
        "front_it": "Quali sono le fasi di chiusura dei conti a fine esercizio?",
        "front_en": "What are the steps for closing accounts at year-end?",
        "back_it": "1. Bilancio di verifica. 2. Scritture di epilogo (chiusura CE). 3. Determinazione utile/perdita. 4. Scritture di chiusura (chiusura SP). Il risultato confluisce in UTILE/PERDITA D'ESERCIZIO (SP).",
        "back_en": "1. Trial balance. 2. Closing entries to Income Statement. 3. Determination of profit/loss. 4. Closing entries to Balance Sheet. The result flows into PROFIT/LOSS FOR THE YEAR (BS)."
      },
      {
        "id": "ch10-4",
        "front_it": "Differenza tra imposte dirette e indirette?",
        "front_en": "What is the difference between direct and indirect taxes?",
        "back_it": "Dirette: colpiscono direttamente la ricchezza (reddito, patrimonio) — IRES, IRAP, IRPEF, IMU. Indirette: colpiscono una manifestazione indiretta della ricchezza (consumo, scambi) — IVA, bollo.",
        "back_en": "Direct: levied directly on wealth (income, assets) — IRES, IRAP, IRPEF, IMU. Indirect: levied on indirect manifestations of wealth (consumption, transactions) — VAT (IVA), stamp duty."
      }
    ]
  },
  {
    "id": "ch11",
    "title": "La Riapertura dei Conti e la Destinazione del Risultato",
    "cards": [
      {
        "id": "ch11-1",
        "front_it": "Come avviene la riapertura dei conti a inizio esercizio?",
        "front_en": "How are accounts reopened at the start of a new financial year?",
        "back_it": "Tutte le attività e le perdite (SP Dare +) in Dare +; BILANCIO DI APERTURA in Avere –. Tutte le passività, il patrimonio netto e gli utili (SP Avere –) in Avere –; BILANCIO DI APERTURA in Dare +.",
        "back_en": "All assets and losses (BS Debit +) go to Debit (+); OPENING BALANCE to Credit (–). All liabilities, equity and profits (BS Credit –) go to Credit (–); OPENING BALANCE to Debit (+)."
      },
      {
        "id": "ch11-2",
        "front_it": "Come viene distribuito l'utile d'esercizio con delibera assembleare?",
        "front_en": "How is the annual profit distributed by shareholders' resolution?",
        "back_it": "Almeno 5% a Riserva Legale (fino al 20% del capitale sociale); il resto può andare a Riserve Facoltative o distribuito come dividendi. Dare + UTILE D'ESERCIZIO; Avere – RISERVA LEGALE / RISERVE / DEBITI V/SOCI PER DIVIDENDI.",
        "back_en": "At least 5% to Legal Reserve (until it reaches 20% of share capital); the remainder to Discretionary Reserves or distributed as dividends. Debit (+) PROFIT FOR THE YEAR; Credit (–) LEGAL RESERVE / RESERVES / DIVIDENDS PAYABLE."
      },
      {
        "id": "ch11-3",
        "front_it": "Cos'è la riserva legale e quali sono i suoi limiti?",
        "front_en": "What is the legal reserve and what are its limits?",
        "back_it": "Riserva obbligatoria alimentata da almeno il 5% dell'utile netto ogni anno, fino a raggiungere il 20% del capitale sociale. Serve a proteggere i creditori.",
        "back_en": "A mandatory reserve funded by at least 5% of net profit each year, until it reaches 20% of share capital. Its purpose is to protect creditors."
      }
    ]
  },
  {
    "id": "ch12",
    "title": "Introduzione alla Valutazione del Bilancio",
    "cards": [
      {
        "id": "ch12-1",
        "front_it": "Quali documenti compongono il bilancio d'esercizio nella sua forma completa?",
        "front_en": "What documents make up the complete annual financial statements?",
        "back_it": "Stato Patrimoniale, Conto Economico, Rendiconto Finanziario, Nota Integrativa.",
        "back_en": "Balance Sheet (Stato Patrimoniale), Income Statement (Conto Economico), Cash Flow Statement (Rendiconto Finanziario), Notes to the Accounts (Nota Integrativa)."
      },
      {
        "id": "ch12-2",
        "front_it": "Quali sono i 7 principi generali di redazione del bilancio (art. 2423-bis)?",
        "front_en": "What are the 7 general principles for preparing financial statements (art. 2423-bis)?",
        "back_it": "1. Continuità, 2. Costanza dei criteri, 3. Prudenza, 4. Competenza economica, 5. Prevalenza della sostanza sulla forma, 6. Significatività e rilevanza, 7. Valutazione separata e divieto di compensazioni.",
        "back_en": "1. Going concern, 2. Consistency, 3. Prudence, 4. Accruals, 5. Substance over form, 6. Materiality and relevance, 7. Separate valuation and prohibition of offsets."
      },
      {
        "id": "ch12-3",
        "front_it": "Cosa sancisce il principio di prudenza?",
        "front_en": "What does the prudence principle state?",
        "back_it": "Gli utili attesi ma non ancora definitivamente conseguiti non si iscrivono. Le perdite anche solo probabili (P > 50%) devono essere iscritte a bilancio.",
        "back_en": "Expected but not yet definitively achieved profits must not be recognised. Losses that are merely probable (P > 50%) must be recognised in the financial statements."
      },
      {
        "id": "ch12-4",
        "front_it": "Differenza tra principi OIC e principi IAS/IFRS?",
        "front_en": "What is the difference between OIC and IAS/IFRS accounting principles?",
        "back_it": "OIC (nazionali): basati sul costo storico, orientati alla prudenza, proteggono i creditori. IAS/IFRS (internazionali): orientati al fair value, interpretazione finanziaria, privilegiano l'informazione agli investitori.",
        "back_en": "OIC (national): based on historical cost, prudence-oriented, protect creditors. IAS/IFRS (international): fair value-oriented, financial interpretation, prioritise investor information."
      },
      {
        "id": "ch12-5",
        "front_it": "Cosa sancisce la clausola generale dell'art. 2423 C.C.?",
        "front_en": "What does the general clause of art. 2423 of the Civil Code state?",
        "back_it": "Il bilancio deve essere redatto con chiarezza e deve rappresentare in modo chiaro, veritiero e corretto la situazione patrimoniale, finanziaria e il risultato economico della società.",
        "back_en": "The financial statements must be drawn up clearly and must give a true and fair view of the company's assets, liabilities, financial position and results of operations."
      }
    ]
  },
  {
    "id": "ch13",
    "title": "Struttura e Contenuto del Bilancio Destinato a Pubblicazione",
    "cards": [
      {
        "id": "ch13-1",
        "front_it": "Qual è la struttura dello Stato Patrimoniale Attivo (civilistico)?",
        "front_en": "What is the structure of the statutory Balance Sheet — Assets?",
        "back_it": "A) Crediti verso soci, B) Immobilizzazioni (I. Immateriali, II. Materiali, III. Finanziarie), C) Attivo circolante (I. Rimanenze, II. Crediti, III. Attività finanziarie, IV. Disponibilità), D) Ratei e risconti.",
        "back_en": "A) Receivables from shareholders, B) Fixed assets (I. Intangible, II. Tangible, III. Financial), C) Current assets (I. Inventories, II. Receivables, III. Financial assets, IV. Cash), D) Prepayments and accrued income."
      },
      {
        "id": "ch13-2",
        "front_it": "Qual è la struttura del Conto Economico civilistico (sintesi)?",
        "front_en": "What is the structure of the statutory Income Statement (summary)?",
        "back_it": "A) Valore della produzione – B) Costi della produzione = Differenza A–B. + C) Proventi/oneri finanziari. + D) Rettifiche di valore. = Risultato ante imposte. – 20) Imposte. = Utile/perdita d'esercizio.",
        "back_en": "A) Value of production – B) Production costs = A–B difference. + C) Financial income/charges. + D) Value adjustments. = Pre-tax result. – 20) Taxes. = Net profit/loss."
      },
      {
        "id": "ch13-3",
        "front_it": "Cosa contiene la Nota Integrativa?",
        "front_en": "What does the Notes to the Accounts (Nota Integrativa) contain?",
        "back_it": "Criteri di valutazione adottati, dettaglio delle voci di SP e CE, variazioni delle immobilizzazioni, movimenti di patrimonio netto, fatti rilevanti successivi alla chiusura.",
        "back_en": "Valuation criteria adopted, detailed breakdown of BS and IS items, movements in fixed assets, changes in equity, significant post-balance-sheet events."
      },
      {
        "id": "ch13-4",
        "front_it": "Chi può redigere il bilancio in forma abbreviata?",
        "front_en": "Who may prepare abbreviated financial statements?",
        "back_it": "Piccole imprese che non superano due dei tre limiti per due esercizi consecutivi: totale attivo ≤ 4,4 M€, ricavi netti ≤ 8,8 M€, dipendenti ≤ 50.",
        "back_en": "Small companies that do not exceed two of the three thresholds for two consecutive years: total assets ≤ €4.4M, net revenues ≤ €8.8M, employees ≤ 50."
      }
    ]
  },
  {
    "id": "ch14",
    "title": "La Valutazione delle Rimanenze di Magazzino",
    "cards": [
      {
        "id": "ch14-1",
        "front_it": "Qual è la regola generale per la valutazione delle rimanenze?",
        "front_en": "What is the general rule for valuing inventories?",
        "back_it": "Le rimanenze si valutano al minore tra il costo storico e il valore di mercato (provento netto atteso). Secondo OIC il provento netto atteso coincide con il valore di mercato.",
        "back_en": "Inventories are valued at the lower of historical cost and net realisable value (market value). Under OIC, net realisable value equals market value."
      },
      {
        "id": "ch14-2",
        "front_it": "Cos'è il costo di sostituzione e per quali beni si usa?",
        "front_en": "What is replacement cost and for which goods is it used?",
        "back_it": "Il costo al quale, in normali condizioni di gestione, un bene in giacenza può essere riacquistato alla data di chiusura. Si usa per: materie prime, sussidiarie e di consumo, semilavorati di acquisto.",
        "back_en": "The cost at which, under normal operating conditions, an inventory item could be repurchased at the closing date. Used for: raw materials, consumables, purchased semi-finished goods."
      },
      {
        "id": "ch14-3",
        "front_it": "Cos'è il valore netto di realizzo e per quali beni si usa?",
        "front_en": "What is net realisable value and for which goods is it used?",
        "back_it": "Prezzo di vendita – costi di completamento – spese dirette di vendita. Si usa per: prodotti finiti, semilavorati di produzione, prodotti in corso di lavorazione, merci.",
        "back_en": "Selling price – completion costs – direct selling expenses. Used for: finished goods, internally produced semi-finished goods, work in progress, merchandise."
      },
      {
        "id": "ch14-4",
        "front_it": "Quali sono i tre metodi di determinazione del costo delle rimanenze?",
        "front_en": "What are the three methods for determining the cost of inventories?",
        "back_it": "FIFO (First In First Out): si esauriscono prima i beni più vecchi. LIFO (Last In First Out): si esauriscono prima i beni più recenti. Costo Medio Ponderato: media ponderata dei costi di acquisto.",
        "back_en": "FIFO (First In First Out): oldest items are consumed first. LIFO (Last In First Out): most recent items are consumed first. Weighted Average Cost: weighted average of purchase costs."
      }
    ]
  },
  {
    "id": "ch15",
    "title": "La Valutazione dei Crediti di Funzionamento e dei Ricavi",
    "cards": [
      {
        "id": "ch15-1",
        "front_it": "Come si valutano i crediti di funzionamento?",
        "front_en": "How are trade receivables valued?",
        "back_it": "Al valore di presumibile realizzo. Se vi è rischio di insolvenza si svalutano tramite il Fondo Svalutazione Crediti (FSC).",
        "back_en": "At their estimated realisable value. If there is a risk of non-collection, they are written down via the Allowance for Doubtful Accounts (Fondo Svalutazione Crediti)."
      },
      {
        "id": "ch15-2",
        "front_it": "Come si registra la svalutazione di un credito?",
        "front_en": "How is the write-down of a receivable recorded?",
        "back_it": "Dare + SVALUTAZIONE CREDITI (CE); Avere – FONDO SVALUTAZIONE CREDITI (SP). Non si riduce direttamente il credito ma si usa il fondo come rettifica indiretta.",
        "back_en": "Debit (+) BAD DEBT EXPENSE (IS); Credit (–) ALLOWANCE FOR DOUBTFUL ACCOUNTS (BS). The receivable is not directly reduced; the allowance is an indirect adjustment."
      },
      {
        "id": "ch15-3",
        "front_it": "Come si registra la perdita definitiva su un credito?",
        "front_en": "How is a definitive bad debt recorded?",
        "back_it": "Dare + PERDITE SU CREDITI (CE); Avere – CREDITI V/CLIENTI (SP). Contestualmente si storna il fondo: Dare + FONDO SVALUTAZIONE CREDITI (SP); Avere – PERDITE SU CREDITI (CE).",
        "back_en": "Debit (+) BAD DEBT LOSS (IS); Credit (–) TRADE RECEIVABLES (BS). Simultaneously, reverse the allowance: Debit (+) ALLOWANCE FOR DOUBTFUL ACCOUNTS (BS); Credit (–) BAD DEBT LOSS (IS)."
      }
    ]
  },
  {
    "id": "ch16",
    "title": "La Valutazione delle Operazioni in Valuta e il Rischio di Cambio",
    "cards": [
      {
        "id": "ch16-1",
        "front_it": "Come si convertono le operazioni in valuta estera al momento dell'operazione?",
        "front_en": "How are foreign currency transactions converted at the transaction date?",
        "back_it": "Al tasso di cambio corrente alla data dell'operazione (tasso spot). Il credito/debito è iscritto in euro al cambio del giorno della fattura.",
        "back_en": "At the exchange rate prevailing at the transaction date (spot rate). The receivable/payable is recorded in euros at the invoice date exchange rate."
      },
      {
        "id": "ch16-2",
        "front_it": "Come si valutano i crediti e debiti in valuta estera alla chiusura dell'esercizio?",
        "front_en": "How are foreign currency receivables and payables valued at year-end?",
        "back_it": "Al tasso di cambio di chiusura dell'esercizio. Le differenze di cambio (utili o perdite non realizzati) si iscrivono in CE rispettando il principio di prudenza.",
        "back_en": "At the closing exchange rate. Exchange differences (unrealised gains or losses) are recognised in the IS, subject to the prudence principle."
      },
      {
        "id": "ch16-3",
        "front_it": "Come si applica il principio di prudenza alle differenze di cambio non realizzate?",
        "front_en": "How does the prudence principle apply to unrealised exchange differences?",
        "back_it": "Le perdite su cambi non realizzate si iscrivono sempre a CE. Gli utili su cambi non realizzati si iscrivono a CE ma confluiscono in una riserva non distribuibile (o fondo rischi cambio).",
        "back_en": "Unrealised exchange losses are always recognised in the IS. Unrealised exchange gains are recognised in the IS but transferred to a non-distributable reserve (or foreign exchange risk provision)."
      }
    ]
  }
]
```

- [ ] **Step 2: Commit**

```bash
git add src/data/cards.json
git commit -m "feat: add bilingual flashcard content extracted from PDF"
```

---

## Task 2: Scaffold React + Vite Project

**Files:**
- Create: `package.json`, `vite.config.js`, `index.html`, `src/main.jsx`, `src/App.jsx`, `src/index.css`

- [ ] **Step 1: Initialise Vite project and install dependencies**

Run from inside the `Flash Audit` directory:

```bash
npm create vite@latest . -- --template react
npm install
npm install -D vitest @testing-library/react @testing-library/user-event @testing-library/jest-dom jsdom
```

- [ ] **Step 2: Configure Vitest in vite.config.js**

Replace the generated `vite.config.js` with:

```js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    globals: true,
    setupFiles: './tests/setup.js',
  },
})
```

- [ ] **Step 3: Create test setup file**

Create `tests/setup.js`:

```js
import '@testing-library/jest-dom'
```

- [ ] **Step 4: Add test script to package.json**

In `package.json`, ensure the `scripts` section contains:

```json
"scripts": {
  "dev": "vite",
  "build": "vite build",
  "preview": "vite preview",
  "test": "vitest run",
  "test:watch": "vitest"
}
```

- [ ] **Step 5: Verify setup runs**

```bash
npm test
```

Expected: no test files found, exits cleanly (0 tests run).

- [ ] **Step 6: Commit**

```bash
git add package.json vite.config.js index.html src/ tests/setup.js
git commit -m "feat: scaffold React + Vite project with Vitest"
```

---

## Task 3: LanguageContext

**Files:**
- Create: `src/contexts/LanguageContext.jsx`
- Test: `tests/LanguageContext.test.jsx`

- [ ] **Step 1: Write the failing test**

Create `tests/LanguageContext.test.jsx`:

```jsx
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
```

- [ ] **Step 2: Run test to verify it fails**

```bash
npm test
```

Expected: FAIL — `LanguageContext` module not found.

- [ ] **Step 3: Write minimal implementation**

Create `src/contexts/LanguageContext.jsx`:

```jsx
import { createContext, useContext, useState } from 'react'

const LanguageContext = createContext(null)

export function LanguageProvider({ children }) {
  const [lang, setLang] = useState('it')
  return (
    <LanguageContext.Provider value={{ lang, setLang }}>
      {children}
    </LanguageContext.Provider>
  )
}

export function useLanguage() {
  return useContext(LanguageContext)
}
```

- [ ] **Step 4: Run test to verify it passes**

```bash
npm test
```

Expected: PASS — 2 tests pass.

- [ ] **Step 5: Commit**

```bash
git add src/contexts/LanguageContext.jsx tests/LanguageContext.test.jsx
git commit -m "feat: add LanguageContext for global IT/EN toggle"
```

---

## Task 4: useStudySession Hook

**Files:**
- Create: `src/hooks/useStudySession.js`
- Test: `tests/useStudySession.test.js`

- [ ] **Step 1: Write the failing test**

Create `tests/useStudySession.test.js`:

```js
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
```

- [ ] **Step 2: Run test to verify it fails**

```bash
npm test
```

Expected: FAIL — `useStudySession` module not found.

- [ ] **Step 3: Write minimal implementation**

Create `src/hooks/useStudySession.js`:

```js
import { useState, useMemo } from 'react'

export default function useStudySession(cards, shuffle = false) {
  const deck = useMemo(() => {
    if (!shuffle) return cards
    return [...cards].sort(() => Math.random() - 0.5)
  }, [cards, shuffle])

  const [currentIndex, setCurrentIndex] = useState(0)
  const [isFlipped, setIsFlipped] = useState(false)
  const [key, setKey] = useState(0)

  const isEnd = currentIndex >= deck.length

  function flip() {
    setIsFlipped(f => !f)
  }

  function next() {
    setIsFlipped(false)
    setCurrentIndex(i => i + 1)
  }

  function prev() {
    if (currentIndex === 0) return
    setIsFlipped(false)
    setCurrentIndex(i => i - 1)
  }

  function restart() {
    setCurrentIndex(0)
    setIsFlipped(false)
    setKey(k => k + 1)
  }

  return {
    currentIndex,
    currentCard: deck[currentIndex] ?? null,
    isFlipped,
    isEnd,
    total: deck.length,
    flip,
    next,
    prev,
    restart,
    key,
  }
}
```

- [ ] **Step 4: Run test to verify it passes**

```bash
npm test
```

Expected: PASS — 7 tests pass.

- [ ] **Step 5: Commit**

```bash
git add src/hooks/useStudySession.js tests/useStudySession.test.js
git commit -m "feat: add useStudySession hook with navigation and flip logic"
```

---

## Task 5: App Shell (Screen State Machine)

**Files:**
- Modify: `src/App.jsx`, `src/main.jsx`
- Test: `tests/App.test.jsx`

- [ ] **Step 1: Write the failing test**

Create `tests/App.test.jsx`:

```jsx
import { render, screen, fireEvent } from '@testing-library/react'
import App from '../src/App'

test('renders home screen by default', () => {
  render(<App />)
  expect(screen.getByTestId('home-screen')).toBeInTheDocument()
})

test('navigates to study screen when deck is selected', () => {
  render(<App />)
  const studyButtons = screen.getAllByText(/studia|study/i)
  fireEvent.click(studyButtons[0])
  expect(screen.getByTestId('study-screen')).toBeInTheDocument()
})

test('navigates back to home from study screen', () => {
  render(<App />)
  const studyButtons = screen.getAllByText(/studia|study/i)
  fireEvent.click(studyButtons[0])
  fireEvent.click(screen.getByTestId('back-to-home'))
  expect(screen.getByTestId('home-screen')).toBeInTheDocument()
})
```

- [ ] **Step 2: Run test to verify it fails**

```bash
npm test
```

Expected: FAIL — App renders placeholder content with no test IDs.

- [ ] **Step 3: Implement App.jsx**

Replace `src/App.jsx`:

```jsx
import { useState } from 'react'
import { LanguageProvider } from './contexts/LanguageContext'
import DeckGrid from './components/DeckGrid'
import StudySession from './components/StudySession'
import EndScreen from './components/EndScreen'
import cardsData from './data/cards.json'
import './index.css'

export default function App() {
  const [screen, setScreen] = useState('home')
  const [activeDeckId, setActiveDeckId] = useState(null)

  function startDeck(deckId) {
    setActiveDeckId(deckId)
    setScreen('study')
  }

  function goHome() {
    setScreen('home')
    setActiveDeckId(null)
  }

  function goEnd() {
    setScreen('end')
  }

  const activeDeck = cardsData.find(d => d.id === activeDeckId) ?? null

  return (
    <LanguageProvider>
      {screen === 'home' && (
        <DeckGrid decks={cardsData} onStart={startDeck} />
      )}
      {screen === 'study' && activeDeck && (
        <StudySession deck={activeDeck} onEnd={goEnd} onBack={goHome} />
      )}
      {screen === 'end' && (
        <EndScreen onRestart={() => setScreen('study')} onHome={goHome} />
      )}
    </LanguageProvider>
  )
}
```

- [ ] **Step 4: Implement stub components so App renders without errors**

Create `src/components/DeckGrid.jsx`:

```jsx
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
```

Create `src/components/StudySession.jsx`:

```jsx
export default function StudySession({ deck, onEnd, onBack }) {
  return (
    <div data-testid="study-screen">
      <button data-testid="back-to-home" onClick={onBack}>Back</button>
      <button onClick={onEnd}>End</button>
    </div>
  )
}
```

Create `src/components/EndScreen.jsx`:

```jsx
export default function EndScreen({ onRestart, onHome }) {
  return (
    <div data-testid="end-screen">
      <button onClick={onRestart}>Restart</button>
      <button onClick={onHome}>Home</button>
    </div>
  )
}
```

Create `src/components/DeckCard.jsx`:

```jsx
export default function DeckCard({ deck, onStart }) {
  return (
    <div>
      <span>{deck.title}</span>
      <button onClick={() => onStart(deck.id)}>Studia</button>
    </div>
  )
}
```

Create `src/components/Header.jsx`:

```jsx
export default function Header({ title, onBack, showBack }) {
  return (
    <header>
      {showBack && <button onClick={onBack}>←</button>}
      <h1>{title}</h1>
    </header>
  )
}
```

Create `src/components/Flashcard.jsx`:

```jsx
export default function Flashcard({ front, back, isFlipped, onFlip }) {
  return (
    <div onClick={onFlip}>
      <div>{isFlipped ? back : front}</div>
    </div>
  )
}
```

- [ ] **Step 5: Run test to verify it passes**

```bash
npm test
```

Expected: PASS — all tests pass.

- [ ] **Step 6: Update main.jsx**

Replace `src/main.jsx`:

```jsx
import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
```

- [ ] **Step 7: Commit**

```bash
git add src/App.jsx src/main.jsx src/components/ tests/App.test.jsx
git commit -m "feat: add App shell with screen state machine and stub components"
```

---

## Task 6: Full UI Implementation (frontend-design skill)

> **IMPORTANT:** Before writing any CSS or final component code in this task, invoke the `frontend-design` skill:
> ```
> Skill({ skill: "frontend-design" })
> ```
> Follow its instructions for producing a polished, distinctive UI. Apply its output to implement the components below.

**Files:**
- Modify: `src/index.css`
- Modify: `src/components/Header.jsx`
- Modify: `src/components/DeckGrid.jsx`
- Modify: `src/components/DeckCard.jsx`
- Modify: `src/components/Flashcard.jsx`
- Modify: `src/components/StudySession.jsx`
- Modify: `src/components/EndScreen.jsx`

**Design requirements for each component:**

### Header.jsx
- Fixed top bar with app title "Flash Audit" on the left
- Language toggle button (IT / EN) on the right — reads from `useLanguage()` and calls `setLang`
- Optional back button (`←`) shown when `showBack` prop is true
- `data-testid="back-to-home"` on the back button

### DeckGrid.jsx
- Uses `data-testid="home-screen"`
- Subtitle describing the course (Bilancio, Modulo 1 — Università Bocconi)
- Responsive grid (2 columns on desktop, 1 on mobile) of `<DeckCard>` components
- Language-aware: shows deck `title` (Italian) and card count

### DeckCard.jsx
- Card tile with chapter title, card count badge, and "Studia" (IT) / "Study" (EN) button
- Hover effect

### Flashcard.jsx
- Large centered card with smooth 3D CSS flip animation on click
- Front shows question in active language (`front_it` or `front_en`)
- Back shows answer in active language (`back_it` or `back_en`)
- Visual distinction between front (question) and back (answer) — e.g. different background colour
- `data-testid="flashcard"`

### StudySession.jsx
- Uses `data-testid="study-screen"`
- `<Header>` with back button (`data-testid="back-to-home"`) and language toggle
- Progress bar: "Carta 3 di 12" / "Card 3 of 12"
- Shuffle toggle
- `<Flashcard>` in the centre
- Previous / Next arrow buttons (prev disabled at index 0)
- Uses `useStudySession` hook

### EndScreen.jsx
- Uses `data-testid="end-screen"`
- Completion message in active language
- "Ricomincia" / "Restart" button and "Torna ai mazzi" / "Back to decks" button

- [ ] **Step 1: Invoke frontend-design skill and implement all components**

Follow the skill's output to write polished implementations. Ensure every `data-testid` listed above is present.

- [ ] **Step 2: Verify dev server renders correctly**

```bash
npm run dev
```

Open `http://localhost:5173` in browser. Verify:
- Home screen shows all 16 chapter decks in a grid
- Language toggle switches all text
- Clicking "Studia" / "Study" opens the study session
- Card flips on click
- Progress bar advances
- Next/prev navigation works
- End screen appears after last card
- Back button returns to home

- [ ] **Step 3: Run all tests to verify nothing broke**

```bash
npm test
```

Expected: all existing tests pass.

- [ ] **Step 4: Commit**

```bash
git add src/
git commit -m "feat: implement full polished UI with flip animations and language toggle"
```

---

## Task 7: Build Verification

**Files:** none

- [ ] **Step 1: Run production build**

```bash
npm run build
```

Expected: `dist/` folder created with no errors.

- [ ] **Step 2: Preview production build**

```bash
npm run preview
```

Open the preview URL and verify the app works identically to dev mode.

- [ ] **Step 3: Run full test suite one final time**

```bash
npm test
```

Expected: all tests pass.

- [ ] **Step 4: Commit**

```bash
git add dist/ .gitignore
git commit -m "feat: verify production build passes"
```

> Note: add `dist/` to `.gitignore` if not already present and don't commit built assets.

---

## Self-Review Notes

- All 16 chapters are represented in `cards.json` with bilingual Q/A pairs
- `data-testid` attributes are specified in every component so tests are stable
- `useStudySession` is fully tested (7 tests covering navigation, flip, end, restart)
- `LanguageContext` is fully tested (2 tests)
- App screen transitions are tested (3 tests)
- Frontend-design skill is explicitly invoked before UI implementation
- No placeholder text, no TBD items
- Card count for the `DeckCard` badge: use `deck.cards.length` from `cards.json`
