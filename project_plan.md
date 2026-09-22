# This Is Math — Project Plan

## Project concept

"This Is Math" is an interactive web experience that connects geometry, sound,
animation, and mathematical learning.

The current V1 allows users to select a polygon and hear a chord associated with
that shape. Each polygon has its own color, animation, chord, and number of voices.

The goal of V2 is to keep the minimal visual style of V1 while making the website
significantly more interactive, educational, playful, and technically interesting.

---

## Existing project

The project currently uses:

- Python
- Streamlit
- HTML/CSS/JavaScript embedded through Streamlit Components
- Canvas API for geometric animation
- Web Audio API for sound generation

Current files include:

- app.py
- requirements.txt
- README.md

Do not replace the existing concept or visual identity unnecessarily.

---

## Main design philosophy

The experience should feel like an interactive digital instrument rather than
a normal educational website.

Keep:

- dark minimalist interface
- glowing polygon aesthetic
- smooth animation
- geometric visual language
- different accent color for each polygon
- Web Audio generated sounds
- minimal text
- responsive layout

Avoid:

- cluttered Streamlit widgets
- excessive text
- childish educational-game styling
- unnecessary menus
- external APIs
- paid services
- login/accounts
- databases

---

## Core V1 features

### 1. Interactive polygon vertices

Each vertex of the polygon should be individually clickable.

Each vertex corresponds to one note from the polygon's chord.

When clicked:

- play that note
- make the vertex glow/pulse
- create a short visual reaction
- show the note name if appropriate

Clicking the center or another dedicated control should play the full chord.

---

### 2. Geometric chord drawing

Allow users to create visual chords by connecting vertices.

When two vertices are selected, draw a glowing line between them.

The user should gradually be able to create geometric patterns inside the polygon.

Provide a subtle "Clear" control to remove the created pattern.

---

### 3. Sequence / Loop mode

Allow users to record a short sequence of vertex selections.

Controls:

- Record
- Play
- Stop
- Clear

When played back:

- corresponding vertices animate
- notes play
- connecting geometry reacts to the sequence

Keep the system simple and intuitive.

---

### 4. Math information mode

Add an optional Math Mode that explains the mathematics of the currently selected
polygon.

Show information such as:

- number of sides
- number of vertices
- interior angle
- exterior angle
- sum of interior angles
- rotational symmetry

Show formulas when useful.

Example:

Interior angle:
(n - 2) × 180° / n

For a hexagon:
(6 - 2) × 180° / 6 = 120°

This information should appear in a small elegant panel and should not dominate
the main instrument.

---

### 5. Controls

Add subtle controls for:

- rotation speed
- tempo
- octave/pitch
- animation intensity

Controls should visually match the existing design.

Do not use default Streamlit sliders inside the instrument if custom HTML controls
can provide a more cohesive design.

---

### 6. Randomize

Add a "Surprise Me" or Randomize button.

It should choose:

- a random polygon
- a short random vertex sequence
- possibly a different rotation direction or speed

Then animate and play the generated pattern.

---

### 7. Keyboard controls

Add keyboard shortcuts.

Suggested:

3 = Triangle
4 = Square
5 = Pentagon
6 = Hexagon
8 = Octagon

Space = play current chord
R = randomize
C = clear pattern

Make keyboard interactions accessible and prevent unexpected browser behavior.

---

### 8. Challenge Mode

Create an optional educational challenge mode.

Generate simple questions based on the current polygon, such as:

- How many vertices does this polygon have?
- What is its interior angle?
- What is the sum of its interior angles?
- What is its exterior angle?
- How many lines of symmetry does a regular polygon have?

Provide immediate visual feedback.

Do not make this feel like a separate school quiz.
Integrate it into the visual experience.

---

## Technical goals

Refactor the current JavaScript where appropriate so that the project remains
maintainable as features are added.

Prefer reusable functions/classes rather than putting all logic into one large
script.

Separate concerns conceptually:

- polygon geometry
- canvas rendering
- audio engine
- interaction
- sequence/loop state
- educational/math calculations

Avoid unnecessary dependencies.

The application should continue to run on Streamlit Community Cloud.

---

## Accessibility

Improve accessibility where possible:

- keyboard navigation
- focus-visible states
- ARIA labels
- readable contrast
- controls usable without a mouse
- reduced-motion support using prefers-reduced-motion

---

## Responsive behavior

The application must work on:

- desktop
- tablet
- mobile

The polygon should remain centered and usable on smaller screens.

Controls may reorganize vertically on mobile.

---

## Performance

Keep canvas animation smooth.

Avoid creating unnecessary AudioContext instances.

Clean up audio nodes after playback.

Avoid excessive DOM creation during animation.

Cap devicePixelRatio when useful for performance.

---

## V1 priority

Implement in this order:

1. Refactor current code without changing its appearance significantly.
2. Interactive vertices and individual notes.
3. Geometric chord drawing.
4. Sequence/loop system.
5. Math Mode.
6. Keyboard controls.
7. Randomize.
8. Challenge Mode.
9. Accessibility/mobile polish.

Do not attempt to redesign everything at once.

Preserve working V1 behavior while adding features incrementally.