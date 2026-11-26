# MarkAny — CS330 End-Semester Speaker Script

**Deck:** `index.html` / `markany_cs330_presentation.html`  
**Total runtime:** ~10 minutes · **12 slides**  
**Course:** CS330 – Software Engineering | Navrachana University  
**Document:** SRS-MARKANY-V1.0  

**Controls:** `→` / `Space` next · `←` previous · `R` reset · `F` fullscreen · `N` speaker cue · click diagrams to zoom · `Esc` close zoom  

---

## Speaking Roster

| Speaker | Slides | Clock | Budget |
|---|---|---|---|
| **Vikas Patanvadiya** | 01–05 | 0:00 → 3:35 | ~3 min 35 s |
| **Rishi Yagnesh Kachhadia** | 06–09 | 3:35 → 6:40 | ~3 min 5 s |
| **Maitra Prajapati** | 10–12 | 6:40 → 10:00 | ~3 min 20 s |

---

## Part A — Vikas Patanvadiya (Slides 01–05)

### Slide 01 — Title (~35 s)
MarkAny hybrid biometric attendance · CS330 · Prof. Ujwala Petigara · SRS-MARKANY-V1.0 · team IDs.

### Slide 02 — Problem & Objectives (~45 s)
Four failures (time loss, proxy, hygiene, admin lag) → four objectives (batch &lt;2.5s, ArcFace+liveness, multi-modal, IEEE 830 auditability).

### Slide 03 — Scope & Users (~40 s)
In-scope V1.0 vs post-V1.0 out-of-scope. Actors: Faculty, Student, Admin (`manually_set=1`), Course Evaluator (16/16).

### Slide 04 — Feasibility (~45 s)
Technical / Economic / Operational pillars with verdict bars.

### Slide 05 — Four Modules (~50 s)
UC-04 enrollment → UC-05/06 live+group → UC-07 3D liveness → UC-08/10 audit+export. Hand off to Rishi.

---

## Part B — Rishi Yagnesh Kachhadia (Slides 06–09)

### Slide 06 — Rules + Fig B.7 (~50 s)
BR-5 cosine ≥0.38 · Δ≥0.12 · BR-6 arbitration · UNIQUE idempotency · RBAC audit.

### Slide 07 — NFRs (~40 s)
&lt;250 ms · &lt;2.5 s · &lt;600 ms · 16/16 in 0.43 s.

### Slide 08 — Use Case Fig B.1 (~45 s)
Actors + «include»/«extend». Zoom diagram for labels.

### Slide 09 — Architecture Fig 2.1 (~50 s)
3-tier / four layers. Zoom Fig 2.1. Hand off to Maitra.

---

## Part C — Maitra Prajapati (Slides 10–12)

### Slide 10 — Session Activity B.6 (~55 s)
Open → Capture → Review → Finalize.

### Slide 11 — ERD B.8 + Constraints (~70 s)
Six constraints with mitigations + Chen ERD / UNIQUE keys.

### Slide 12 — Close (~55 s)
v1.0 achievements + roadmap → thank you / viva.

---

## Timing Cheat Card

```
0:00  Vikas    S01 Title
0:35  Vikas    S02 Problem
1:20  Vikas    S03 Scope
2:00  Vikas    S04 Feasibility
2:45  Vikas    S05 Modules
3:35  Rishi    S06 Rules + B.7
4:25  Rishi    S07 NFRs
5:05  Rishi    S08 Use Case
5:50  Rishi    S09 Architecture
6:40  Maitra   S10 Session Activity
7:35  Maitra   S11 ERD + Constraints
8:45  Maitra   S12 Close
10:00 STOP → Viva
```
