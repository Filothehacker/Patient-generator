#!/usr/bin/env python3
"""Generate fictitious patient data matching the existing Excel structure."""

import random
import openpyxl
from datetime import datetime, timedelta, time
from openpyxl import Workbook

# ── Reference data ─────────────────────────────────────────────────────────────

MALE_NAMES   = ["MARIO", "LUCA", "GIUSEPPE", "ANTONIO", "GIOVANNI", "MARCO",
                "ROBERTO", "DAVIDE", "ANDREA", "PAOLO", "FILIPPO", "STEFANO",
                "ALBERTO", "ENRICO", "FEDERICO"]
FEMALE_NAMES = ["MARIA", "ANNA", "LAURA", "FRANCESCA", "ELENA", "SARA",
                "GIULIA", "CHIARA", "VALENTINA", "SIMONA", "ALESSIA",
                "ROBERTA", "MONICA", "PAOLA", "CLAUDIA"]
SURNAMES     = ["ROSSI", "BIANCHI", "FERRARI", "ESPOSITO", "ROMANO",
                "COLOMBO", "RICCI", "MARINO", "GRECO", "BRUNO", "GALLO",
                "CONTI", "DE LUCA", "MANCINI", "COSTA", "GIORDANO",
                "RIZZO", "LOMBARDI", "MORETTI", "BARBIERI"]

DOCTOR_SURNAMES = ["BIANCHI", "FERRARI", "COLOMBO", "RICCI", "CONTI",
                   "MORETTI", "LOMBARDI", "GRECO", "DE LUCA", "GIORDANO"]
DOCTOR_NAMES    = ["Giuseppe", "Andrea", "Marco", "Paolo", "Roberto",
                   "Luca", "Giovanni", "Francesco", "Alberto", "Stefano"]

CITIES_REGIONS = [
    ("MILANO (MI)", "LOMBARDIA"),
    ("VIGEVANO (PV)", "LOMBARDIA"),
    ("BERGAMO (BG)", "LOMBARDIA"),
    ("BRESCIA (BS)", "LOMBARDIA"),
    ("TORINO (TO)", "PIEMONTE"),
    ("GENOVA (GE)", "LIGURIA"),
    ("VENEZIA (VE)", "VENETO"),
    ("PADOVA (PD)", "VENETO"),
    ("BOLOGNA (BO)", "EMILIA-ROMAGNA"),
    ("FIRENZE (FI)", "TOSCANA"),
    ("ROMA (RM)", "LAZIO"),
    ("NAPOLI (NA)", "CAMPANIA"),
    ("BARI (BA)", "PUGLIA"),
    ("PALERMO (PA)", "SICILIA"),
    ("CAGLIARI (CA)", "SARDEGNA"),
]

OPERATIVE_UNITS = [
    "MANO", "ORTOPEDIA", "CHIRURGIA GENERALE", "NEUROCHIRURGIA",
    "CARDIOCHIRURGIA", "UROLOGIA", "GINECOLOGIA", "OCULISTICA",
    "ORL", "CHIRURGIA VASCOLARE",
]

PROCEDURES = [
    (8272,  "INTERVENTO DI PLASTICA SULLA MANO CON INNESTO DI MUSCOLO O FASCIA MUSCOLARE", 45, 70),
    (8122,  "ARTROSCOPIA DEL GINOCCHIO CON RIPARAZIONE DEL MENISCO", 60, 90),
    (5119,  "COLECISTECTOMIA LAPAROSCOPICA", 75, 110),
    (8153,  "PROTESI TOTALE D'ANCA", 120, 160),
    (8154,  "PROTESI TOTALE DI GINOCCHIO", 110, 150),
    (4301,  "APPENDICECTOMIA", 50, 80),
    (6859,  "TIROIDECTOMIA TOTALE", 90, 130),
    (5123,  "ERNIOPLASTICA INGUINALE LAPAROSCOPICA", 60, 90),
    (1322,  "CATARATTA - FACOEMULSIFICAZIONE", 30, 50),
    (3722,  "BYPASS AORTO-CORONARICO", 240, 300),
]

DIAGNOSES = [
    (8860,  "AMPUTAZIONE TRAUMATICA DELLE ALTRE DITA DELLA MANO (COMPLETA) (PARZIALE)"),
    (71536, "ARTROSI DEL GINOCCHIO, NON SPECIFICATA"),
    (57400, "CALCOLOSI DELLA COLECISTI SENZA COLECISTITE"),
    (71500, "COXARTROSI PRIMARIA, NON SPECIFICATA"),
    (71516, "GONARTROSI PRIMARIA, NON SPECIFICATA"),
    (54000, "APPENDICITE ACUTA SENZA MENZIONE DI PERITONITE"),
    (24000, "GOZZO SEMPLICE NON TOSSICO"),
    (55090, "ERNIA INGUINALE UNILATERALE O NON SPECIFICATA, SENZA OSTRUZIONE O GANGRENA"),
    (36600, "CATARATTA SENILE NON SPECIFICATA"),
    (41401, "MALATTIA CORONARICA DEI VASI NATIVI"),
]

PRIORITIES = [
    ("A+", "ENTRO 1 SETTIMANA"),
    ("A",  "ENTRO 30 GIORNI"),
    ("B",  "ENTRO 60 GIORNI"),
    ("C",  "ENTRO 180 GIORNI"),
    ("D",  "ENTRO 12 MESI"),
]

ANESTHESIA = [
    (1, "Anestesia Generale"),
    (2, "Anestesia Spinale"),
    (3, "Anestesia Locale"),
    (4, "Anestesia Peridurale"),
    (5, "Anestesia Loco-Regionale"),
]

ALLERGIES   = ["NESSUNA", "PENICILLINA", "LATTICE", "ASPIRINA", "CONTRASTO IODATO", "NESSUNA", "NESSUNA"]
THERAPIES   = ["Terapia Anticoagulante", "Terapia Antipertensiva", "Terapia Ipoglicemizzante",
               "Nessuna", "Betabloccanti", "Antiaggreganti", "Statine"]
PRE_PACKAGES = [
    (1, "PAC PRERICOVERO STD >= 45 ANNI"),
    (2, "PAC PRERICOVERO STD < 45 ANNI"),
    (3, "PAC PRERICOVERO CARDIOLOGICO"),
    (4, "PAC PRERICOVERO CHIRURGIA MAGGIORE"),
]
OR_ROOMS    = ["A1", "A2", "A3", "B1", "B2", "C1", "C2"]
WARDS       = ["P10", "P11", "P20", "P21", "CHI1", "CHI2", "ORT1"]

MONTH_CODES = "ABCDEHLMPRST"   # Jan–Dec

# ── Helpers ────────────────────────────────────────────────────────────────────

def _cf_consonants(name: str) -> str:
    vowels = "AEIOU"
    c = [ch for ch in name.upper() if ch.isalpha() and ch not in vowels]
    v = [ch for ch in name.upper() if ch.isalpha() and ch in vowels]
    return (c + v + ["X", "X", "X"])[:3]


def codice_fiscale(surname: str, name: str, dob: datetime, gender: str,
                   municipality_code: str = "L892") -> str:
    sc = _cf_consonants(surname)
    nc = _cf_consonants(name)
    yy = str(dob.year)[-2:]
    mm = MONTH_CODES[dob.month - 1]
    dd = dob.day if gender == "M" else dob.day + 40
    dd_str = str(dd).zfill(2)
    raw = "".join(sc) + "".join(nc) + yy + mm + dd_str + municipality_code
    # simplified check-digit (not cryptographically correct, just plausible)
    check = chr(ord("A") + (sum(ord(c) for c in raw) % 26))
    return raw + check


def random_dob(min_age=18, max_age=85) -> datetime:
    today = datetime(2026, 4, 8)
    age   = random.randint(min_age, max_age)
    start = today.replace(year=today.year - age - 1)
    end   = today.replace(year=today.year - age)
    return start + timedelta(days=random.randint(0, 365))


def random_phone() -> int:
    return random.randint(3000000000, 3999999999)


def fmt_short(dt: datetime) -> str:
    """Short Italian-style date string like '26/3/26 7.00'."""
    return f"{dt.day}/{dt.month}/{str(dt.year)[-2:]} {dt.hour}.{str(dt.minute).zfill(2)}"


# ── Patient generator ─────────────────────────────────────────────────────────

def generate_patient(patient_index: int) -> list:
    gender   = random.choice(["M", "F"])
    name     = random.choice(MALE_NAMES if gender == "M" else FEMALE_NAMES)
    surname  = random.choice(SURNAMES)
    dob      = random_dob()
    city, region = random.choice(CITIES_REGIONS)
    unit     = random.choice(OPERATIVE_UNITS)

    proc_code, proc_desc, surg_dur, room_occ = random.choice(PROCEDURES)
    diag_code, diag_desc                     = random.choice(DIAGNOSES)
    prio_code, prio_desc                     = random.choice(PRIORITIES)
    anesth_code, anesth_desc                 = random.choice(ANESTHESIA)
    pre_pkg_code, pre_pkg_desc               = random.choice(PRE_PACKAGES)

    doc_surname = random.choice(DOCTOR_SURNAMES)
    doc_name    = random.choice(DOCTOR_NAMES)
    doc_code    = random.randint(10, 99)

    patient_id  = random.randint(4000000, 4999999)
    year_suffix = str(patient_index).zfill(6)

    # Key dates (all relative to 2026)
    base   = datetime(2026, 1, 1)
    insert = base + timedelta(days=random.randint(0, 90))
    pre_dt = insert + timedelta(days=random.randint(3, 10))
    surg   = pre_dt + timedelta(days=random.randint(3, 7))
    admit  = surg.replace(hour=7, minute=0)
    upd    = pre_dt + timedelta(days=random.randint(0, 2), hours=random.randint(8, 17))
    discharge = surg + timedelta(days=random.randint(2, 7), hours=random.randint(9, 12))

    cf = codice_fiscale(surname, name, dob, gender,
                        municipality_code=f"L{random.randint(100,999)}")

    email = f"{name.lower()}.{surname.lower().replace(' ', '')}@gmail.com"

    # Build the 59-column row in the exact header order
    row = [
        cf,                                                       # CODICE FISCALE
        patient_id,                                               # ID PAZIENTE
        surname,                                                  # COGNOME
        name,                                                     # NOME
        dob,                                                      # DATA NASCITA
        gender,                                                   # SESSO
        email,                                                    # EMAIL
        random_phone(),                                           # TELEFONO
        "ITALIA",                                                 # NAZIONE RESIDENZA
        city,                                                     # CITTA' RESIDENZA
        f"VIA {random.choice(['ROMA','MILANO','VERDI','MANZONI','DANTE'])} {random.randint(1,150)}",  # INDIRIZZO RESIDENZA
        region,                                                   # REGIONE
        unit,                                                     # UNITA' OPERATIVA
        insert.strftime("%-m/%-d/%Y"),                            # DATA INSERIMENTO IN LISTA
        f"2026/LDA/{year_suffix}",                               # CODICE LISTA ATTESA
        2,                                                        # CODICE STATO LISTA ATTESA
        "3. Prenotazione Completata",                             # DESCRIZIONE STATO LISTA ATTESA
        proc_code,                                                # CODICE ICD9 INTERVENTO
        proc_desc,                                                # DESCRIZIONE ICD9 INTERVENTO
        surg_dur,                                                 # DURATA CHIRURGICA PREVISTA
        room_occ,                                                 # OCCUPAZIONE SALA PREVISTA
        None,                                                     # NOTE INTERVENTO
        diag_code,                                                # CODICE ICD9 DIAGNOSI
        diag_desc,                                                # DESCRIZIONE ICD9 DIAGNOSI
        prio_code,                                                # CODICE PRIORITA'
        prio_desc,                                                # DESCRIZIONE PRIORITA'
        doc_code,                                                 # CODICE MEDICO RICHIEDENTE
        doc_surname,                                              # COGNOME MEDICO RICHIEDENTE
        doc_name,                                                 # NOME MEDICO RICHIEDENTE
        None,                                                     # MATERIALI DI SALA RICHIESTI
        "REPARTO",                                                # DESTINO POST OPERATORIO
        2,                                                        # CODICE ONERE
        "SSR",                                                    # DESCRIZIONE ONERE
        None,                                                     # ENTE ASSICURATIVO
        "ORDINARIO",                                              # CODICE REGIME RICOVERO
        "ORDINARIO",                                              # DESCRIZIONE REGIME RICOVERO
        fmt_short(pre_dt.replace(hour=7)),                        # DATA PRERICOVERO
        pre_pkg_code,                                             # CODICE PACCHETTO PRERICOVERO
        pre_pkg_desc,                                             # DESCRIZIONE PACCHETTO PRERICOVERO
        f"2026/PRE/{year_suffix}",                               # ID PRERICOVERO
        "IDONEO",                                                 # STATO PRERICOVERO
        None,                                                     # NOTE PRERICOVERO
        random.choice(THERAPIES),                                 # TERAPIA ASSUNTA
        anesth_code,                                              # CODICE ANESTESIA
        anesth_desc,                                              # DESCRIZIONE ANESTESIA
        random.choice(ALLERGIES),                                 # ALLERGIA
        random.choice(["SI", "NO"]),                              # RX TORACE RICHIESTO
        random.randint(1, 7),                                     # GG DEGENZA PREVISTI
        fmt_short(upd),                                           # DATA ULTIMO UPDATE
        surg.strftime("%-m/%-d/%Y"),                              # DATA INTERVENTO
        time(random.choice([7, 8, 9, 10, 11, 12]), 0),           # ORA PREVISTA INTERVENTO
        random.choice(OR_ROOMS),                                  # SALA OPERATORIA
        fmt_short(admit),                                         # DATA/ORA RICOVERO
        f"2026/DEG/{year_suffix}",                               # N. CARTELLA CLINICA
        random.choice(WARDS),                                     # REPARTO DEGENZA
        random.randint(1000, 1020),                               # LETTO
        None,                                                     # DATA/ORA TRASFERIMENTO
        None,                                                     # REPARTO DEGENZA POST TRASFERIMENTO
        fmt_short(discharge),                                     # DATA/ORA DIMISSIONE
    ]
    return row


# ── Build workbook ─────────────────────────────────────────────────────────────

HEADERS = [
    "CODICE FISCALE", "ID PAZIENTE", "COGNOME", "NOME", "DATA NASCITA",
    "SESSO", "EMAIL", "TELEFONO", "NAZIONE RESIDENZA", "CITTA' RESIDENZA",
    "INDIRIZZO RESIDENZA", "REGIONE", "UNITA' OPERATIVA",
    "DATA INSERIMENTO IN LISTA", "CODICE LISTA ATTESA",
    "CODICE STATO LISTA ATTESA", "DESCRIZIONE STATO LISTA ATTESA",
    "CODICE ICD9 INTERVENTO", "DESCRIZIONE ICD9 INTERVENTO",
    "DURATA CHIRURGICA PREVISTA ", "OCCUPAZIONE SALA PREVISTA ",
    "NOTE INTERVENTO", "CODICE ICD9 DIAGNOSI", "DESCRIZIONE ICD9 DIAGNOSI",
    "CODICE PRIORITA' LISTA ATTESA", "DESCRIZIONE PRIORITA' LISTA ATTESA",
    "CODICE MEDICO RICHIEDENTE", "COGNOME MEDICO RICHIEDENTE",
    "NOME MEDICO RICHIEDENTE", "MATERIALI DI SALA RICHIESTI",
    "DESTINO POST OPERATORIO", "CODICE ONERE", "DESCRIZIONE ONERE",
    "ENTE ASSICURATIVO", "CODICE REGIME RICOVERO", "DESCRIZIONE REGIME RICOVERO",
    "DATA PRERICOVERO", "CODICE PACCHETTO PRERICOVERO",
    "DESCRIZIONE PACCHETTO PRERICOVERO", "ID PRERICOVERO", "STATO PRERICOVERO",
    "NOTE PRERICOVERO", "TERAPIA ASSUNTA", "CODICE ANESTESIA",
    "DESCRIZIONE ANESTESIA", "ALLERGIA", "RX TORACE RICHIESTO",
    "GG DEGENZA PREVISTI", "DATA ULTIMO UPDATE", "DATA INTERVENTO",
    "ORA PREVISTA INTERVENTO", "SALA OPERATORIA", "DATA/ORA RICOVERO",
    "N. CARTELLA CLINICA", "REPARTO DEGENZA", "LETTO",
    "DATA/ORA TRASFERIMENTO", "REPARTO DEGENZA POST TRASFERIMENTO",
    "DATA/ORA DIMISSIONE",
]

random.seed(42)

wb = Workbook()
ws = wb.active
ws.title = "Sheet1"

ws.append(HEADERS)

for i in range(1, 11):
    ws.append(generate_patient(i))

output_path = "/Users/filippofocaccia/Desktop/Patient-generator/patient.xlsx"
wb.save(output_path)
print(f"Saved 10 patients to {output_path}")
