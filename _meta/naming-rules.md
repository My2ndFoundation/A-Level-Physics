# Naming Rules

- Use canonical, specific filenames.
- Use hyphenated filenames.
- Broad topics must be MOCs only.
- Avoid duplicate pages.
- Add aliases for alternative names, equation names, GCSE wording, everyday wording, and common phrasing.
- Use page names that are stable and readable.
- Prefer Physics names over exam-question wording for core knowledge pages.
- Use `Why-...` filenames for common-sense pages.
- Use `...-Map.md` filenames for frontier maps.

## Good Names

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

## Bad Names

These are too broad as content pages and must be MOCs instead:

```text
Mechanics.md
Waves.md
Electricity.md
Graphs.md
Practical.md
Fields.md
Quantum.md
Energy.md
Motion.md
Forces.md
Circuits.md
Materials.md
```

Allowed MOC forms: `Mechanics-MOC.md`, `Waves-MOC.md`, `Electricity-MOC.md`, etc.

## Aliases

One physical object, concept, law, model, method, representation, or misconception gets **one** canonical page. Alternative names go into the `aliases` frontmatter field and `.state/aliases.tsv`.

Example: `Newton's Second Law`, `Newton-Second-Law`, `F = ma`, `F=ma` → one page (`Newton-Second-Law.md`) with the rest as aliases.
