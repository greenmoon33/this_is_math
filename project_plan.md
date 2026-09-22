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


---

## V1.1 — Polish, UX, and Bug-Fix Pass

V1 functionality is now implemented.

Before adding any major new features, perform a V1.1 pass focused on fixing
visual alignment, making existing interactions understandable, and verifying
that every visible control has a clear purpose.

Do not redesign the application or change its visual identity.

### 1. Fix center-content alignment

The center content currently appears visually off-center for some polygon names,
especially longer names such as Pentagon and Octagon.

The complete center group:

- "Play chord"
- polygon name
- chord/voice information

must remain centered at the exact geometric center of the canvas for EVERY shape.

Do not solve this using individual offsets for different polygon names.

Use a layout that naturally centers content regardless of text width.

The polygon name should:
- remain on one line
- scale down when necessary
- never overflow awkwardly
- remain horizontally and vertically centered
- preserve the existing typography and aesthetic

Test Triangle, Square, Pentagon, Hexagon, and Octagon individually.

### 2. Audit every control

Review every visible control and verify its behavior in the actual code.

Controls currently include:

Shape buttons:
- Triangle
- Square
- Pentagon
- Hexagon
- Octagon

Sequence controls:
- Record
- Play
- Loop
- Stop
- Clear

Other controls:
- Surprise Me
- Math
- Challenge

Sliders:
- Rotation
- Tempo
- Octave
- Glow

For each control:
1. Verify that it performs a meaningful action.
2. Verify that its visual state changes when appropriate.
3. Verify that its purpose is understandable without reading README.md.
4. Remove or redesign any control that is redundant or confusing.
5. Do not leave decorative controls that appear functional but do nothing.

### 3. Improve sequence controls

Record / Play / Loop / Stop currently require too much guessing.

Make the sequence workflow self-explanatory.

Desired workflow:

1. User presses Record.
2. Record clearly enters an active recording state.
3. User clicks polygon vertices.
4. The interface clearly shows that notes are being recorded.
5. User presses Record again or Stop to finish recording.
6. Play becomes useful once a sequence exists.
7. Play visibly enters a playback state while the sequence is playing.
8. Loop clearly indicates whether looping is ON or OFF.
9. Stop immediately stops playback/looping.
10. Clear removes the sequence and drawn pattern.

Add a small but clearly visible sequence indicator near these controls.

Examples:

"RECORDING · 4 NOTES"
"SEQUENCE · 6 NOTES"
"PLAYING · 6 NOTES"
"LOOP ON · 6 NOTES"

Do not rely only on the tiny bottom status bar.

### 4. Disabled control states

Controls that cannot currently do anything should look disabled.

Examples:

- Play should be disabled when no sequence has been recorded.
- Stop should be disabled when nothing is playing or recording.
- Clear should be disabled when there is no sequence or visual pattern.

Use the existing minimalist visual language for disabled states.

Do not remove useful controls simply because they are temporarily unavailable.

### 5. Clarify Loop behavior

Loop must have an obvious state.

When OFF:
"Loop"

When ON:
visually highlight the button using the active/accent style.

If the user enables Loop before pressing Play, make it clear that the next
sequence playback will repeat.

Do not make Loop appear to be a separate playback button if it is only a mode.

### 6. Verify sliders

Test all four sliders and ensure their effects are noticeable and correct.

Rotation:
- changes polygon rotation speed/direction

Tempo:
- changes recorded-sequence playback speed

Octave:
- changes note/chord pitch

Glow:
- changes visual glow intensity

Tempo only affects sequence playback, so make that relationship clearer in the UI
if necessary.

Do not add sliders that do not have a meaningful effect.

### 7. Interaction feedback

Every important user action should provide immediate visual feedback.

Examples:

- clicked vertex pulses
- played note appears briefly
- Record visibly activates
- Play visibly activates during playback
- Loop visibly toggles
- Stop visibly stops animation/playback state
- Clear visibly removes the path
- Surprise Me clearly produces a new state
- Math and Challenge clearly show whether their panels are open

Keep feedback subtle and consistent with the existing aesthetic.

### 8. Preserve V1 functionality

Do not remove working features while fixing V1.1.

Preserve:

- vertex note playback
- full chord playback
- geometric pattern drawing
- sequence recording/playback
- loop playback
- Math panel
- Challenge panel
- Surprise Me
- keyboard controls
- responsive layout
- Web Audio generation

V1.1 should make the existing application clearer and more polished,
not substantially expand its feature set.

### 9. Test before considering V1.1 complete

Manually verify these flows:

A. Select each polygon and verify center alignment.
B. Click every vertex and verify correct sound/feedback.
C. Record 4 vertices → stop → play.
D. Record 4 vertices → enable loop → play → stop.
E. Clear a recorded sequence.
F. Use Surprise Me.
G. Open/close Math.
H. Complete a Challenge question.
I. Change every slider and verify its effect.
J. Test keyboard shortcuts.
K. Test at desktop and narrow/mobile widths.

Fix any discovered regression before considering V1.1 complete.