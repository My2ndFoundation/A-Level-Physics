# CLAUDE.md

This is the **highest authority document** for this project. All workflows, skills, and agents must obey it.

---

## 1. Project Mission

This vault is designed to help the learner build a connected understanding of Physics before and during A-Level study.

It is **not**:

- a revision-only vault
- a textbook mirror
- a folder of chapter summaries
- a RAG dump
- a formula sheet
- a collection of long monolithic notes
- a university Physics textbook

The LLM should transform raw materials into a navigable Physics knowledge graph.

The core knowledge flow is:

```text
everyday observation → foundation idea → physical quantity → concept → law/result → model → representation → method → experiment → application → problem type → mistake pattern → source
```

Physics pages should help the learner understand:

```text
what the quantity/concept means
where it came from intuitively
how it connects to GCSE knowledge
how it becomes precise at A-Level
how it is measured
how it is represented mathematically
which law/model applies
how graphs express it
how experiments test it
what assumptions are involved
where mistakes usually happen
where it leads beyond A-Level
```

---

## 2. Physics Continuity Rule

Physics must be treated as a continuous conceptual system, not as an isolated A-Level syllabus.

The vault should support five layers:

```text
everyday intuition → pre-GCSE foundation → GCSE foundation → bridge to A-Level → A-Level OCR H556 core → frontier edge map
```

These layers have different purposes:

| Layer                 | Purpose                                                  | Depth                    |
| --------------------- | -------------------------------------------------------- | ------------------------ |
| Everyday intuition    | Build physical common sense from real-world experience   | simple, intuitive        |
| Pre-GCSE foundation   | Recover basic language, observation, and physical ideas  | simple and clear         |
| GCSE foundation       | Stabilise prerequisite concepts                          | accurate and connected   |
| Bridge to A-Level     | Show how GCSE ideas become more mathematical and precise | transitional             |
| A-Level OCR H556 core | Main examinable Physics knowledge graph                  | detailed                 |
| Frontier edge map     | Show where ideas lead beyond A-Level                     | shallow orientation only |

The A-Level OCR H556 layer is the main detailed layer.

The foundation layers should support understanding, not distract from A-Level.

The frontier layer must remain peripheral.

---

## 3. Frontier Boundary Rule

Frontier pages are allowed and encouraged, but only as orientation maps.

Examples:

```text
Quantum-Mechanics-Map.md
Relativity-Map.md
Particle-Physics-Map.md
Cosmology-Map.md
Semiconductor-Physics-Map.md
Chaos-and-Complexity-Map.md
```

Frontier pages should explain:

- what the field studies
- why it matters
- which A-Level ideas connect to it
- what key ideas exist at the edge
- what not to worry about yet

Frontier pages must not include:

- advanced derivations
- dense university-level mathematical formalism
- long technical explanations
- full quantum mechanics
- full relativity
- full particle physics
- full cosmology
- speculative claims presented as settled fact

The correct depth for frontier pages is:

```text
orientation, not mastery
map, not textbook
curiosity, not syllabus burden
```

---

## 4. Highest-Priority Template Rule

This section is mandatory.

```text
Every page created or substantially updated by an LLM must follow the corresponding template under `_meta/templates/`.

The page type in frontmatter determines the required template.

If a page type and its template conflict with any lower-level instruction, the template wins.

If a future skill omits a required template section, the skill is wrong and must be corrected.

No future ingest, expand, lint, or MOC-building workflow may bypass these templates.
```

| Page type in frontmatter | Required template | Default folder |
|---|---|---|
| `foundation` | `_meta/templates/foundation-template.md` | `02_Foundations/` |
| `common-sense` | `_meta/templates/common-sense-template.md` | `02_Foundations/Everyday-Physics/` |
| `frontier-map` | `_meta/templates/frontier-map-template.md` | `12_Frontier-Maps/` |
| `physical-quantity` | `_meta/templates/physical-quantity-template.md` | `03_Physical-Quantities/` |
| `concept` | `_meta/templates/concept-template.md` | `04_Concepts/` |
| `law-result` | `_meta/templates/law-result-template.md` | `05_Laws-and-Results/` |
| `model` | `_meta/templates/model-template.md` | `06_Models/` |
| `method` | `_meta/templates/method-template.md` | `07_Methods/` |
| `representation` | `_meta/templates/representation-template.md` | `08_Representations/` |
| `experiment-practical` | `_meta/templates/experiment-practical-template.md` | `09_Experiments-and-Practicals/` |
| `application` | `_meta/templates/application-template.md` | `10_Applications/` |
| `problem-type` | `_meta/templates/problem-type-template.md` | `11_Problems/Problem-Types/` |
| `worked-example` | `_meta/templates/worked-example-template.md` | `11_Problems/Worked-Examples/` |
| `mistake-pattern` | `_meta/templates/mistake-pattern-template.md` | `11_Problems/Mistake-Patterns/` |
| `source` | `_meta/templates/source-template.md` | `13_Sources/` |
| `moc` | `_meta/templates/moc-template.md` | `01_MOCs/` or `00_Home/` |

Future skills must explicitly read the relevant template before writing pages of that type.

---

## 5. Non-Negotiable Rules

### 5.1 raw/ is read-only

- Never edit, rename, reformat, or delete files under `raw/`.
- Treat raw files as immutable source input.
- If raw content has errors, record them in the source page or log; do not fix raw files.

### 5.2 Do not reproduce copyrighted textbooks or long book passages

- No full chapter copying.
- No long verbatim extracts.
- No long reproduced worked examples from copyrighted books.
- No bulk copying of exercise sets.
- Use paraphrase, short formula-level excerpts, page/section references, question references, and source traceability.
- Source pages should be metadata and extraction records, not copied source material.

### 5.3 Search before creating pages

- Always search existing pages, filenames, and aliases before creating a new page.
- One physical object, concept, law, model, method, representation, or common misconception should have one canonical page.
- Alternative names go into `aliases`.

Examples:

```text
Newton's Second Law
Newton-Second-Law
F = ma
F=ma
```

should not become duplicate pages. Use one canonical page and aliases.

### 5.4 Never silently overwrite

If a new source differs from an existing page in:

- notation
- definition scope
- assumptions
- model limits
- sign convention
- graph interpretation
- practical method
- syllabus emphasis
- mathematical level
- GCSE vs A-Level simplification
- frontier vs A-Level interpretation

then preserve the difference as a source variation block instead of silently overwriting.

Use this format:

```markdown
> ⚠️ Source variation:
> This source presents the idea differently from [[Existing-Page]].
> Difference: ...
> Action: preserved as a variant, not silently overwritten.
```

### 5.5 Broad topic pages are MOCs only

Forbidden as content pages:

```text
Mechanics.md
Electricity.md
Waves.md
Quantum.md
Fields.md
Practical-Skills.md
Motion.md
Forces.md
Circuits.md
Materials.md
Energy.md
```

Allowed as MOCs:

```text
Mechanics-MOC.md
Electricity-MOC.md
Waves-MOC.md
Quantum-Physics-MOC.md
Fields-MOC.md
Practical-Skills-MOC.md
Motion-MOC.md
Forces-MOC.md
Circuits-MOC.md
Materials-MOC.md
Energy-MOC.md
```

### 5.6 Atomic page size control

- A normal atomic page should usually be 300–800 words.
- If a page becomes too broad, split it.
- A page should have one central purpose.
- If a page tries to explain a full textbook chapter, it is wrong.
- Frontier pages may be slightly longer as maps, but must remain shallow.

### 5.7 Frontmatter is required

Every non-MOC content page must have frontmatter with at least:

```yaml
type:
subject: physics
tags:
level:
status:
aliases:
sources:
```

### 5.8 MOCs are navigation pages

MOCs should:

- organise links
- expose structure
- help exploration
- connect related pages
- show prerequisite relationships
- show cross-topic relationships

MOCs should not:

- become textbooks
- contain long explanations
- duplicate content from atomic pages

### 5.9 Wikilinks are mandatory

All created or updated pages must use wikilinks for related quantities, concepts, laws, models, methods, representations, experiments, applications, problem types, common-sense pages, foundation pages, frontier maps, and mistakes.

Use canonical filenames as link targets.

### 5.10 Physics must connect maths, experiment, and intuition

Every relevant physics page should connect:

```text
everyday intuition
conceptual meaning
mathematical relationship
graphical representation
experimental measurement
assumptions / limits
typical exam problem type
common misconception
```

### 5.11 No auto-commit

Do not run `git commit` unless explicitly asked.

Leave the working tree dirty for human review.

---

## 6. Page Types

Canonical page types:

```text
moc
source
foundation
common-sense
frontier-map
physical-quantity
concept
law-result
model
method
representation
experiment-practical
application
problem-type
worked-example
mistake-pattern
glossary
```

### `foundation`

A prerequisite idea from pre-GCSE, GCSE, or bridge-to-A-Level Physics.

Examples:
- [[Force]]
- [[Energy]]
- [[Speed]]
- [[From-Speed-to-Velocity]]
- [[From-Weight-to-Gravitational-Field-Strength]]

### `common-sense`

An everyday observation or intuitive explanation that builds physical common sense.

Examples:
- [[Why-Seatbelts-Matter]]
- [[Why-Metal-Feels-Colder-Than-Wood]]
- [[Why-Objects-Keep-Moving-in-Space]]
- [[Why-Ice-Floats]]

### `frontier-map`

A shallow map of a modern or advanced Physics area beyond A-Level.

Examples:
- [[Quantum-Mechanics-Map]]
- [[Relativity-Map]]
- [[Particle-Physics-Map]]
- [[Cosmology-Map]]
- [[Semiconductor-Physics-Map]]

### `physical-quantity`

A measurable physical quantity with symbol, unit, definition, measurement method, and relationships.

Examples:
- [[Velocity]]
- [[Acceleration]]
- [[Force]]
- [[Momentum]]
- [[Electric-Field-Strength]]

### `concept`

A physical idea, phenomenon, or conceptual object.

Examples:
- [[Wave-Particle-Duality]]
- [[Internal-Resistance]]
- [[Superposition]]
- [[Photoelectric-Effect]]

### `law-result`

A law, principle, equation, conservation rule, named result, or known relationship.

Examples:
- [[Newton-Second-Law]]
- [[Conservation-of-Momentum]]
- [[Ohms-Law]]
- [[Snells-Law]]

### `model`

An idealised physical model or modelling framework.

Examples:
- [[Constant-Acceleration-Model]]
- [[Point-Mass-Model]]
- [[Ideal-Gas-Model]]
- [[Simple-Harmonic-Oscillator]]

### `method`

A procedure or technique used to solve, analyse, estimate, measure, or derive something.

Examples:
- [[Resolving-Forces]]
- [[Using-SUVAT-Equations]]
- [[Finding-Gradient-from-a-Graph]]
- [[Applying-Conservation-of-Energy]]

### `representation`

A form in which a physical idea is represented.

Examples:
- [[Velocity-Time-Graph]]
- [[Free-Body-Diagram]]
- [[Circuit-Diagram]]
- [[Ray-Diagram]]
- [[Phasor-Diagram]]

### `experiment-practical`

An experiment, required practical, measurement method, apparatus technique, uncertainty analysis, or practical skill.

Examples:
- [[Measuring-Young-Modulus]]
- [[Measuring-Acceleration-Due-to-Gravity]]
- [[Determining-Internal-Resistance]]
- [[Using-a-Micrometer]]

### `application`

A context where physics ideas are applied to a real system, technology, exam scenario, or cross-subject model.

Examples:
- [[Projectile-Motion]]
- [[Medical-Imaging]]
- [[Particle-Accelerators]]
- [[Capacitor-Timing-Circuits]]

### `problem-type`

A recurring exam or practice problem pattern.

Examples:
- [[Calculate-Resultant-Force]]
- [[Interpret-a-Velocity-Time-Graph]]
- [[Find-Internal-Resistance-from-a-Graph]]

### `worked-example`

A short, original or paraphrased worked solution tied to a source reference.

### `mistake-pattern`

A recurring misunderstanding, error, or trap.

Examples:
- [[Confusing-Mass-and-Weight]]
- [[Forgetting-Vector-Direction]]
- [[Using-Distance-Instead-of-Displacement]]
- [[Mixing-Up-Series-and-Parallel-Circuits]]

### `source`

A provenance record for raw material, textbook chapter, specification section, paper, practical guide, or external source.

### `moc`

A map of content. It organises links but does not replace atomic notes.

---

## 7. Folder Semantics

```text
00_Home/                         Global entry points
01_MOCs/                         Human-readable maps
02_Foundations/                  Everyday, pre-GCSE, GCSE, and bridge-to-A-Level foundations
03_Physical-Quantities/          Measurable quantities, units, dimensions
04_Concepts/                     Physical ideas and phenomena
05_Laws-and-Results/             Laws, principles, equations, conservation rules
06_Models/                       Idealised systems and modelling assumptions
07_Methods/                      Procedures and problem-solving techniques
08_Representations/              Graphs, diagrams, notations, visual forms
09_Experiments-and-Practicals/   Practical skills, measurements, uncertainties
10_Applications/                 Applied contexts and cross-topic models
11_Problems/                     Worked examples, problem types, mistakes, extensions
12_Frontier-Maps/                Shallow maps of advanced and modern Physics
13_Sources/                      Source records and provenance
_meta/                           Project control layer, templates, workflows, rules
raw/                             Immutable source input
.state/                          Operational state
```

---

## 8. Tags

### Learning-layer tags

```text
everyday-physics
common-sense
pre-gcse
gcse-foundation
bridge-to-a-level
a-level-core
frontier
edge-map
modern-physics
intuition
misconception
```

### Syllabus tags

```text
foundations-of-physics
practical-skills
forces-and-motion
electrons-waves-and-photons
newtonian-world
astrophysics-and-cosmology
particles-and-medical-physics
mechanics
materials
electricity
waves
quantum-physics
particles
fields
thermal-physics
nuclear-physics
medical-physics
astrophysics
```

### Exam board tags

```text
ocr-h556
ocr-physics-a
a-level-physics
gcse-physics
```

### Topic tags

```text
units
dimensions
uncertainty
vectors
graphs
kinematics
forces
newtons-laws
moments
momentum
energy
power
circular-motion
simple-harmonic-motion
materials
stress-strain
electric-circuits
resistance
capacitors
waves
superposition
interference
diffraction
standing-waves
photoelectric-effect
quantum
electric-fields
gravitational-fields
magnetic-fields
radioactivity
nuclear-decay
medical-imaging
cosmology
relativity
semiconductors
technology-link
history-of-physics
```

### Learning tags

```text
year-1
year-2
core
extension
bridge
advanced
maths-link
further-maths-link
computer-science-link
practical
graph-skill
modelling
```

### Page function tags

```text
definition
formula
graph
diagram
experiment
required-practical
problem-solving
mistake-pattern
source
moc
frontier-map
```

---

## 9. Naming Rules

Use clear hyphenated filenames.

Canonical filename examples:

```text
02_Foundations/Everyday-Physics/Why-Seatbelts-Matter.md
02_Foundations/GCSE-Foundations/Force.md
02_Foundations/Bridge-to-A-Level/From-Speed-to-Velocity.md
03_Physical-Quantities/Acceleration.md
04_Concepts/Internal-Resistance.md
05_Laws-and-Results/Newton-Second-Law.md
06_Models/Constant-Acceleration-Model.md
07_Methods/Resolving-Forces.md
08_Representations/Velocity-Time-Graph.md
09_Experiments-and-Practicals/Required-Practicals/Measuring-Young-Modulus.md
10_Applications/Projectile-Motion.md
11_Problems/Problem-Types/Interpret-a-Velocity-Time-Graph.md
11_Problems/Mistake-Patterns/Confusing-Mass-and-Weight.md
12_Frontier-Maps/Quantum-Mechanics-Map.md
```

Avoid vague filenames (`Mechanics.md`, `Waves.md`, `Electricity.md`, `Graphs.md`, `Practical.md`, `Fields.md`, `Quantum.md`, `Energy.md`). Those must be MOCs.

See `_meta/naming-rules.md` for full naming rules.

---

## 10. Ingestion Workflow Standard

Required order:

```text
Step 1 — Read raw source end-to-end
Step 2 — Identify candidate Physics knowledge objects
Step 3 — Search aliases and existing pages
Step 4 — Read the corresponding templates from `_meta/templates/`
Step 5 — Classify the source layer: everyday / pre-GCSE / GCSE / bridge / A-Level / frontier
Step 6 — Produce checkpoint summary for the user
Step 7 — Wait for user confirmation before writing wiki files
Step 8 — Create or update source page
Step 9 — Create or update atomic pages using the required templates
Step 10 — Update relevant MOCs
Step 11 — Update index.md
Step 12 — Append log.md
Step 13 — Append .state/ingested.tsv
Step 14 — Report pages touched and unresolved issues
Step 15 — Do not auto-commit
```

**No wiki files should be written before the checkpoint is accepted.**

**Future skills must not skip Step 4.**

---

## 11. Source Handling

Source pages should record:

- source title
- source type
- file path under raw
- author / publisher if known
- exam board if applicable
- learning layer
- chapter / section / page references if available
- extracted foundations
- extracted common-sense ideas
- extracted physical quantities
- extracted concepts
- extracted laws/results
- extracted models
- extracted methods
- extracted representations
- extracted experiments/practicals
- extracted applications
- extracted problem types
- extracted mistake patterns
- extracted frontier links
- notes on copyright limitations
- links to generated or updated wiki pages

Source pages must not contain full copyrighted source text.

---

## 12. Physics-Specific Quality Rules

Physics pages should avoid becoming formula-only notes.

Every suitable page should answer:

```text
What does this physically mean?
What prior intuition does it build on?
What GCSE knowledge does it depend on?
What changes at A-Level?
What quantities are involved?
What assumptions are being made?
What equation or relationship applies?
What graph or diagram represents it?
How could it be measured?
What are the common traps?
Which problem types use it?
Where does this lead beyond A-Level?
```

For equations:

- define every symbol
- state units
- state scalar/vector nature where relevant
- state conditions
- link to related quantities and laws

For graphs:

- identify axes
- explain gradient
- explain area under curve where relevant
- explain intercepts
- state common misreadings

For experiments:

- identify independent, dependent, and control variables
- identify apparatus
- identify method
- identify uncertainty sources
- identify safety and limitations if relevant
- explain graph use if applicable

For frontier maps:

- keep the page shallow
- avoid advanced derivations
- connect back to A-Level pages
- explicitly state what is out of scope

---

## 13. Lint and Maintenance

The LLM should periodically detect:

- orphan pages
- missing aliases
- duplicate pages
- overly broad pages
- missing frontmatter
- missing source trace
- broken wikilinks
- MOCs not updated
- mentioned-but-missing quantities or concepts
- problem types without related methods
- methods without worked examples
- concepts without applications
- equations without units
- laws without conditions
- graphs without gradient/area interpretation
- experiments without variables or uncertainty
- physical quantities without SI unit
- frontier pages that go too deep
- A-Level pages missing GCSE/foundation links
- common-sense pages not linked to A-Level ideas
- pages not following their required `_meta/templates/` template
