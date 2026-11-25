# MarkAny — CS330 End-Semester Speaker Script

**Deck:** `markany_cs330_presentation.html`  
**Total runtime:** ~10 minutes  
**Course:** CS330 – Software Engineering | Navrachana University  
**Document:** SRS-MARKANY-V1.0  

**Controls reminder:** `→` / `Space` next · `←` previous · `R` reset · `F` fullscreen · `N` speaker cue overlay (hidden by default)  

---

## Speaking Roster

| Speaker | Slides | Clock | Budget |
|---|---|---|---|
| **Maitra Prajapati** | 01–04 | 0:00 → 3:20 | ~3 min 20 s |
| **Vikas Patanvadiya** | 05–08 | 3:20 → 6:40 | ~3 min 20 s |
| **Rishi Yagnesh Kachhadia** | 09–12 | 6:40 → 10:00 | ~3 min 20 s |

---

## Part A — Maitra Prajapati (Slides 01–04)

### Slide 01 — Title Cover (~40 s)
> “Good morning. We are presenting **MarkAny**, a hybrid classical and deep learning biometric attendance platform for CS330 Software Engineering. I’m **Maitra Prajapati**, with **Vikas Patanvadiya** and **Rishi Yagnesh Kachhadia**. Our faculty guide is **Ujwala Petigara**. The governing document is **SRS-MARKANY-V1.0**, structured to IEEE 830.”

**Cue:** Point to team line + Doc ID. Hand off framing: “This deck follows problem → requirements → design → constraints → conclusion.”

### Slide 02 — Problem & Objectives (~55 s)
> “Traditional classroom attendance fails in four ways: verbal roll-calls burn **10–15 minutes** per lecture; paper and RFID enable **proxy attendance**; fingerprint scanners create **hygiene and hardware friction**; and sheet-to-ERP transcription causes **administrative lag**.  
> MarkAny’s objectives invert each failure: **batch mark 40–50 students in under 2.5 seconds**, defeat spoofing with **512-D ArcFace plus 3D head-turn liveness**, support **three capture modes**, and retain **auditability** through IEEE 830 rigor and immutable logs.”

**Cue:** Left column = pain; right column = measurable goals. Emphasize `< 2.5 s` and anti-spoofing.

### Slide 03 — Scope & Users (~50 s)
> “End-to-end scope is four hops: **WebRTC capture → hybrid CV recognition → audit review and marks → Excel/CSV export**.  
> Primary actor is the **Faculty**—subjects, 6-character join codes, live or group sessions, overrides, CIE marks, exports.  
> **Students** enroll biometrics once with 3–5 poses and can self check-in with liveness.  
> **Administrators** audit `manually_set = 1` trails. **Course evaluators** inspect IEEE 830 traceability, the hybrid CV stack, and our **16/16** passing tests.”

### Slide 04 — Feasibility (~55 s)
> “Feasibility is threefold.  
> **Technical:** CPU-only ONNX at roughly **200 ms/frame**, browser `getUserMedia` so the server never owns camera drivers, dual Supabase/SQLite persistence, and **16/16 tests in 0.43 s**.  
> **Economic:** zero software license cost, zero specialized biometric hardware, and low ops overhead via free-tier Supabase with SQLite offline fallback on existing faculty laptops.  
> **Operational:** regex timetable parsing, one-click group capture under 2.5 s, human-in-the-loop overrides, and submit-ready exports.  
> I’ll hand over to Vikas for functional requirements.”

---

## Part B — Vikas Patanvadiya (Slides 05–08)

### Slide 05 — Major Functional Requirements (~55 s)
> “I’m **Vikas**. MarkAny’s core value is four functional modules.  
> **01 Enrollment (UC-04):** 3–5 poses, SCRFD single-face gate, unit-normalized **512-D ArcFace** vectors.  
> **02 Live & Group (UC-05/06):** 1500 ms live overlays plus batch recognition of **40–50 faces** with archived BLOB evidence.  
> **03 Liveness Check-In (UC-07):** timed mobile window with a **14-frame** head-turn challenge where horizontal nose-to-eye span **Δ ≥ 0.12**.  
> **04 Audit & Reporting (UC-08/10):** confidence roster, `manually_set = 1` toggles, irreversible lock, in-memory `.xlsx`/`.csv`.”

### Slide 06 — Workflows & Business Rules (~55 s)
> “Operationally, a session flows: **timetable regex → join code and capacity guard → multi-modal capture → finalize lock**.  
> Four SE guarantees matter most:  
> **BR-5** accepts a match only if cosine similarity **≥ 0.38**;  
> **BR-6** arbitrates duplicates by highest confidence;  
> **BR-4 / BR-2 / BR-3** enforce idempotency via composite UNIQUE and block writes outside the active `open_until` window;  
> **BR-1 / BR-7** bind RBAC with salted **PBKDF2 SHA-256**, 30-day tokens, and permanent override trails.”

**Cue:** Pause on 0.38 and UNIQUE—viva bait.

### Slide 07 — Non-Functional Requirements (~45 s)
> “Benchmarks from the SRS: live frames under **250 ms**, 50-face groups under **2.5 s**, 14-frame liveness under **600 ms**, and **16/16** tests in **0.43 s**.  
> We scale on commodity CPUs with client-side WebRTC and stateful-free bearer tokens. Privacy keeps only non-invertible embeddings; live frames stay in volatile RAM. Reliability includes Supabase→SQLite failover and 1500 ms thermal throttling.”

### Slide 08 — UML Use Case Diagram (~45 s)
> “This use-case model is the SRS §4 contract. Faculty owns timetable, subjects, live/group marking, review, and export. Students own enrollment biometrics and mobile check-in. Shared use cases cover auth and CIE marks.  
> Dashed **≪include≫** edges force Face Match into UC-05/06/07 and Liveness into UC-07. **≪extend≫** Manual Override is conditional on UC-08.  
> UC-01–UC-10 sit inside the runtime boundary; **UC-11 Classical Baseline** is verified by the Course Evaluator on the modules slide.  
> Rishi will continue with architecture.”

---

## Part C — Rishi Yagnesh Kachhadia (Slides 09–12)

### Slide 09 — System Architecture (~55 s)
> “I’m **Rishi**. MarkAny is a **3-tier design** with **four core layers** and **zero OS camera-driver lock-in**.  
> **Presentation tier:** React 19 plus WebRTC client capture. **Application tier:** Flask REST gateway on **port 5050** with RBAC, regex parsing, and idempotency. The backend then splits into **CV Inference**—the **Hybrid Verification Engine** (SCRFD, ArcFace, 3D liveness) plus the **Classical Vision Baseline**—and **Data Persistence**, a unified `store.py` DAL that fails over from Supabase PostgreSQL to SQLite.”

**Cue:** Emphasize “3-tier / four layers” if asked. Gesture through the staggered stack top→bottom.

### Slide 10 — Core Modules & Schema (~55 s)
> “Vision is dual-track. The production deep engine runs ONNX on CPU: SCRFD, ArcFace 512-D, cosine ≥ 0.38, liveness Δ ≥ 0.12. The classical baseline implements luminosity grayscale, Gaussian convolution, CDF equalization, **3,776-D LBP** at Euclidean 0.65, and Bresenham rasterization.  
> Schema has **10 tables** in three groups—identity/biometrics, academics, attendance/audit—with CASCADE on embeddings, UNIQUE join codes, and UNIQUE attendance keys. Dual-mode DAL auto-fails to `data/attendance.db`.”

### Slide 11 — Constraints & Limitations (~45 s)
> “We are explicit about constraints from SRS §2.5/2.7: CPU-only execution, WebRTC secure-context rules, lighting above roughly **150 lux**, first-run **~330 MB** buffalo_l download, client-only capture, and macOS port/expat quirks. Each has a concrete mitigation—ONNX quantization, localhost/HTTPS, multi-pose plus override, local cache, Base64 REST payloads, and permanent **port 5050**.”

### Slide 12 — Conclusion & Roadmap (~45 s)
> “v1.0 is complete: all SRS TBDs resolved, **16/16** tests green, and classroom marking under **2.5 seconds** without proxy roll-call. Post-1.0 roadmap from Appendix C targets FCM push alerts, Canvas/Moodle webhooks, and Edge-AI terminals on Raspberry Pi 5 or Jetson.  
> Thank you—we’re open for viva questions.”

---

## High-Probability Viva Q&A (×10)

Grounded in `CS330_SRS_Group_7.pdf`. Keep answers crisp; cite the rule/ID when possible.

### Q1. Why IEEE 830 for this project?
**A:** IEEE 830 gives a standard SRS structure (purpose, overall description, external interfaces, system features, NFRs). MarkAny uses it so evaluators can trace every UC/REQ to an implemented module and test.

### Q2. How does MarkAny decide a face is a known student?
**A:** ArcFace produces unit-normalized 512-D embeddings. A match is accepted **iff cosine similarity ≥ 0.38 (BR-5)**; otherwise the detection is labeled Unknown.

### Q3. How do you stop photo / replay spoofing?
**A:** UC-07 runs a **14-frame 3D head-turn challenge**. The horizontal nose-to-eye span must satisfy **Δ ≥ 0.12**; static prints and screen replays fail the dynamic landmark test.

### Q4. What is the Classical Vision Baseline, and why does it exist?
**A:** Pure Python/NumPy implementations of luminosity grayscale, 2D Gaussian convolution, CDF histogram equalization, LBP (3,776-D, Euclidean 0.65), and Bresenham line drawing. It is the syllabus-aligned baseline that sits beside the production deep engine inside the Hybrid Verification Engine—not a separate product name.

### Q5. How is attendance idempotent?
**A:** **BR-4** plus schema constraint `UNIQUE(student_id, session_date, session_id)` guarantee at most one Present mark per student per session, even under retries or duplicate detections.

### Q6. What happens if two faces match the same student in one frame?
**A:** **BR-6** — highest confidence claims the student ID; the secondary detection is forced to Unknown to prevent double-marking artifacts.

### Q7. Why don’t you store recognition photos?
**A:** Privacy NFR: only non-invertible 512-D embeddings are retained for matching. Live frames are processed in volatile RAM and discarded. Group-session evidence BLOBs are explicit audit artifacts under faculty control, not a continuous photo archive of every frame.

### Q8. Why port 5050 instead of Flask’s default 5000?
**A:** On macOS, AirPlay Receiver commonly binds **5000**. SRS Appendix C / REQ-TBD-3 permanently allocates **5050**, with `run-backend.sh` wrapping environment quirks.

### Q9. How does offline mode work?
**A:** Unified DAL in `store.py` prefers Supabase PostgreSQL and automatically fails over to local SQLite3 at `data/attendance.db`, preserving core attendance workflows without cloud connectivity.

### Q10. What proves the implementation is “done” for v1.0?
**A:** Appendix C states all TBDs are **RESOLVED** (decision margin 0.38, liveness Δ ≥ 0.12, port 5050). The automated backend suite reports **16/16 passing in 0.43 s**, and the working prototype meets the &lt; 2.5 s group-marking performance claim.

---

## Timing Cheat Card (print / phone)

```
0:00  Maitra   S01 Title
0:40  Maitra   S02 Problem / Objectives
1:35  Maitra   S03 Scope / Users
2:25  Maitra   S04 Feasibility
3:20  Vikas    S05 Functional Modules
4:15  Vikas    S06 Workflows / BR
5:10  Vikas    S07 NFRs
5:55  Vikas    S08 UML
6:40  Rishi    S09 Architecture
7:35  Rishi    S10 Engines / Schema
8:30  Rishi    S11 Constraints
9:15  Rishi    S12 Close + Thank You
10:00 STOP → Viva
```

**Buffer rule:** If any speaker runs long, cut Slide 03 actor prose first, then Slide 07 card bullets—never cut BR-5 / Δ≥0.12 / 16/16.
