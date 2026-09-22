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

---

# V2 — Pattern Lab, Mathematical Music, and Exploration

## V2 purpose

V1 and V1.1 established the core instrument and polished its existing interactions.

V2 should turn "This Is Math" into a deeper mathematical music playground.

The central idea of V2 is:

> Mathematics should not only be explained by the interface. It should generate
> the geometry, patterns, motion, and music that the user experiences.

V2 should build directly on the existing polygon, vertex, sequence, Canvas,
Web Audio, Math, Challenge, and Surprise Me systems.

Do NOT redesign the application from scratch.

Do NOT remove or substantially change working V1.1 behavior unless necessary
to support V2.

The existing dark minimalist visual identity, glowing polygons, typography,
color system, control style, and overall instrument-like feeling should remain.

V2 should feel like the same application becoming deeper and more capable,
not like a different website.

---

# V2 PRIORITIES

V2 features are divided into three levels.

## MUST HAVE

1. Pattern Lab
2. Mathematical pattern generators
3. Interactive pattern explanation
4. Pattern playback integration
5. Improved vertex/note visualization
6. Smarter Surprise Me
7. First-use guidance

## SECONDARY

8. Sound character controls
9. Pattern transformations
10. Pattern history / recent patterns
11. Improved Challenge Mode integration

## OPTIONAL / ONLY IF STABLE

12. Shareable Pattern Code
13. Additional advanced mathematical pattern types
14. Additional sound presets

Implement MUST HAVE features first.

Do not implement optional features if doing so makes the existing instrument
less reliable, cluttered, or difficult to understand.

---

# 1. PATTERN LAB — MAIN V2 FEATURE

Add a new mode called:

Pattern Lab

Pattern Lab should be the centerpiece of V2.

It should allow users to generate musical/geometric patterns using mathematical
rules instead of manually clicking every vertex.

Pattern Lab should integrate with the existing instrument rather than opening
a completely separate page.

Add a "Pattern Lab" control near the existing Math / Challenge controls.

When opened, display a compact panel that visually matches the existing Math
and Challenge panels.

The panel should not cover the polygon unnecessarily.

---

## Pattern Lab concept

A pattern is a sequence of vertex indices.

For example, on an octagon:

0 → 2 → 4 → 6 → 0

creates one geometric/musical pattern.

Another rule might create:

0 → 3 → 6 → 1 → 4 → 7 → 2 → 5 → 0

The existing sequence and path systems should be reused whenever possible.

Generated patterns should:

- illuminate the corresponding vertices
- play their corresponding notes
- draw their geometric path
- work with sequence tempo
- support Play
- support Loop
- support Stop
- support Clear
- respond to Octave
- respond to Glow

Do not create a completely separate playback engine if the existing Sequencer
can be safely reused or extended.

---

# 2. STEP PATTERNS

The first Pattern Lab generator should be "Step".

The user selects a step size.

Example:

Polygon: Octagon
Step: 2

0 → 2 → 4 → 6 → 0

Step: 3

0 → 3 → 6 → 1 → 4 → 7 → 2 → 5 → 0

Use modular arithmetic:

nextVertex = (currentVertex + step) mod n

where n is the number of polygon vertices.

The generated path should continue until the sequence returns to its starting
state or repeats.

The interface should make the relationship between the rule and resulting
geometry understandable without requiring a long explanation.

Possible compact display:

STEP 3
+3 MOD 8

Do not make the interface feel like a math textbook.

---

# 3. STAR POLYGON PATTERNS

When appropriate, identify step-generated patterns using star polygon notation.

Examples may include patterns related to:

{5/2}
{7/2}
{7/3}
{8/3}

Only show notation when mathematically appropriate.

The user does not need prior knowledge of star polygon notation.

If notation is displayed, provide a short explanation in the Pattern Lab or
Math panel.

Example:

{5/2}

5 vertices, connecting every 2nd vertex.

Do not overwhelm the main interface with notation.

---

# 4. PATTERN PRESETS

In addition to Step mode, provide several mathematical pattern presets.

Recommended initial presets:

- Around
- Skip
- Star
- Mirror
- Bounce

These should generate sequences mathematically.

### Around

Visit consecutive vertices.

Example:

0 → 1 → 2 → 3 → ...

### Skip

Use a step greater than 1.

### Star

Choose a step that produces a visually recognizable star-like path when
possible.

### Mirror

Generate a symmetric sequence around the polygon.

### Bounce

Travel forward through vertices and then reverse direction.

Keep the preset list small and meaningful.

Do not add presets that are only random animations with no understandable rule.

---

# 5. LIVE PATTERN PREVIEW

When the user changes a Pattern Lab rule, preview the resulting geometry.

The preview may appear as a lower-opacity geometric path inside the polygon.

The user should be able to understand:

"This rule creates THIS shape."

Then Play should animate and sonify that pattern.

The preview should not permanently modify the manually drawn path until the
pattern is applied or played.

Keep preview rendering efficient.

---

# 6. PATTERN INFORMATION

Pattern Lab should calculate useful mathematical properties of the generated
pattern.

Examples:

- number of vertices in the polygon
- step size
- number of unique vertices visited
- number of cycles
- whether every vertex is visited
- pattern length before repeating
- greatest common divisor when relevant

For step patterns, use the mathematical relationship between n and the step.

For example:

gcd(n, step)

can help determine whether a step pattern visits every vertex or separates
into multiple cycles.

Do not simply display the value.

Explain the consequence briefly.

Example:

GCD(8, 3) = 1
Every vertex is visited before the pattern repeats.

Or:

GCD(8, 2) = 2
The pattern splits into 2 repeating cycles.

Keep this explanation compact.

---

# 7. INTERACTIVE MATH CONNECTION

Upgrade Math Mode so that it can explain BOTH:

1. the current polygon
2. the current generated pattern

The existing polygon information should remain.

When a Pattern Lab pattern exists, add a small "Pattern" section.

Possible information:

STEP
3

RULE
+3 mod 8

VISITED
8 / 8

GCD
1

CYCLES
1

This should update automatically when the pattern changes.

The user should be able to see mathematics describing something that is
currently visible and audible on the screen.

That connection is a major goal of V2.

---

# 8. VERTEX LABEL MODE

Add an optional way to display vertex information around the polygon.

Possible modes:

- Off
- Number
- Note

Number mode:

0, 1, 2, 3...

Note mode:

C, E, G...

Labels should appear subtly near each vertex.

They must rotate POSITIONALLY with the polygon but the text itself should remain
upright and readable.

Do not rotate the letters themselves.

This feature is particularly useful in Pattern Lab because users can understand
sequences such as:

0 → 3 → 6 → 1...

without guessing which vertex is which.

Default can remain Off to preserve the clean V1 appearance.

---

# 9. PATTERN PLAYBACK

Pattern Lab patterns should integrate with the existing Sequencer.

When a pattern is applied:

- it becomes a playable sequence
- Play plays the pattern once
- Loop repeats it
- Stop stops it
- Tempo controls playback speed
- Octave changes pitch
- Glow changes visual intensity
- Clear removes it

During playback:

- the active vertex should pulse
- the active edge/path segment should react visually
- the note should appear briefly
- the sequence indicator should describe the current state

Example:

PATTERN · STEP 3 · 8 NOTES

During playback:

PLAYING · STEP 3 · 4 / 8

If looping:

LOOP · STEP 3 · 4 / 8

Do not create duplicate Pattern Lab playback buttons if the existing Play,
Loop, Stop, and Clear controls can handle the workflow cleanly.

---

# 10. ACTIVE EDGE ANIMATION

Improve sequence playback visualization.

Currently vertices react during playback.

In V2, also visually emphasize the connection currently being traversed.

For example:

vertex 2 → vertex 5

should briefly brighten the corresponding line segment.

The rest of the path can remain visible at lower opacity.

This should create the feeling that sound is physically traveling through the
geometry.

Keep the effect elegant rather than flashy.

---

# 11. DIRECTION CONTROL

Allow generated patterns to be played:

- clockwise
- counterclockwise

Direction should affect the generated vertex order.

It should NOT simply reverse the visual rotation of the polygon.

The user should be able to hear and see the difference between:

0 → 1 → 2 → 3

and:

0 → 3 → 2 → 1

where appropriate.

Keep this control inside Pattern Lab rather than adding another permanent
bottom slider.

---

# 12. PATTERN TRANSFORMATIONS

SECONDARY FEATURE.

Allow an existing generated pattern to be transformed without creating a new
pattern manually.

Recommended transformations:

- Reverse
- Rotate Start
- Invert / Mirror when mathematically meaningful

### Reverse

Reverse the sequence order.

### Rotate Start

Change which vertex is considered the starting point while preserving the
pattern structure.

Example:

0 → 2 → 4 → 1 → 3

may become:

2 → 4 → 1 → 3 → 0

These transformations should reuse the existing sequence rather than creating
unrelated random patterns.

---

# 13. SOUND CHARACTER

SECONDARY FEATURE.

V1.1 already supports Octave.

V2 may add a small "Sound" selector with a few synthesized sound characters.

Recommended:

- Soft
- Bright
- Glass
- Warm

These should still be generated entirely using the Web Audio API.

Do not use external audio files.

Do not add dependencies.

Each sound character may adjust:

- oscillator waveform
- filter frequency
- attack
- decay
- gain envelope

Keep the number of presets small.

The default sound should remain close to the current V1.1 sound.

Sound controls should not dominate the interface.

---

# 14. SMARTER SURPRISE ME

Upgrade Surprise Me.

Instead of generating only an arbitrary random sequence, V2 should usually
generate a mathematically interesting pattern.

Possible random choices:

- polygon
- valid step
- preset
- direction
- rotation
- octave
- sound character if implemented

After Surprise Me, briefly identify what was generated.

Example:

SURPRISE
OCTAGON · STEP 3

or:

SURPRISE
PENTAGON · STAR

The user should then be able to inspect the pattern in Pattern Lab or Math Mode.

Randomization should therefore encourage discovery rather than produce
meaningless randomness.

---

# 15. FIRST-USE GUIDANCE

V2 has more depth than V1.1, so provide very lightweight onboarding.

On the user's first interaction/session, show a small non-blocking hint.

Example:

PLAY A VERTEX
or
OPEN PATTERN LAB TO TURN MATH INTO MUSIC

Do not create a long tutorial, modal slideshow, or account-based onboarding.

Optionally provide a small "?" help control.

Help should explain the instrument in approximately 4–6 short steps.

Suggested concepts:

1. Choose a polygon.
2. Click vertices to hear notes.
3. Draw or record a pattern.
4. Use Pattern Lab to generate mathematical patterns.
5. Open Math to understand the geometry.
6. Loop and experiment.

The user should be able to dismiss help immediately.

---

# 16. CHALLENGE MODE V2

Improve Challenge Mode so that it can use Pattern Lab.

Keep existing polygon questions.

Add pattern-based questions when a generated pattern exists.

Examples:

- What vertex comes next?
- How many unique vertices will this pattern visit?
- Which step is this pattern using?
- Will this pattern visit every vertex?
- How many cycles will it create?

Questions must be generated from the actual current pattern.

Do not turn Challenge Mode into a large quiz system.

It should remain a small optional layer over the instrument.

After a correct answer, use the polygon itself to demonstrate the answer when
possible.

---

# 17. PATTERN HISTORY

SECONDARY FEATURE.

Maintain a small in-memory history of recently generated patterns during the
current browser session.

Maximum:

5 recent patterns.

A history entry may contain:

- polygon
- pattern type
- step
- direction
- sequence

Allow the user to restore a recent pattern.

Do not use a database.

Do not require accounts.

Do not persist personal information.

Do not allow history UI to dominate the main interface.

If this creates unnecessary clutter, omit it.

---

# 18. PATTERN CODE

OPTIONAL FEATURE.

If the rest of V2 is stable, create a compact Pattern Code that represents a
generated pattern.

Example concept:

8-S3-CW

Meaning:

8 = octagon
S3 = step 3
CW = clockwise

More complicated patterns may use a similarly compact representation.

The exact format should be deterministic and documented.

Allow users to:

- view the code
- copy the code
- enter a valid code to reconstruct the pattern

Do NOT create accounts, databases, servers, or cloud storage for this feature.

The code should simply encode enough state to reproduce a pattern locally.

Reject malformed codes gracefully.

This feature is optional.

Pattern Lab is more important.

---

# 19. GEOMETRIC / MUSICAL RELATIONSHIP

Where possible, make the connection between geometry and music more visible.

Examples:

When a vertex plays:

- highlight the vertex
- show its note

When an edge is traversed:

- animate the edge

When a sequence repeats:

- subtly indicate completion of the cycle

When a pattern consists of multiple cycles:

- make cycle boundaries understandable visually

Do not claim mathematical relationships between chord harmony and polygon
geometry unless they are actually implemented or mathematically justified.

The geometry generates the sequence structure.

The notes remain the musical mapping assigned to the vertices.

Keep that distinction accurate.

---

# 20. RESPONSIVE V2 DESIGN

Pattern Lab must work at desktop, tablet, and narrow/mobile widths.

Desktop:

Panels may appear beside the polygon when enough space exists.

Mobile:

Panels should move below or overlay carefully without covering essential
controls.

Avoid horizontal scrolling.

Long polygon names must remain centered.

Vertex labels must remain readable.

Pattern Lab controls may wrap or stack.

The central polygon should remain the visual focus.

---

# 21. ACCESSIBILITY V2

Preserve all V1.1 accessibility work.

New controls must include:

- keyboard accessibility
- focus-visible states
- appropriate ARIA labels
- aria-expanded where relevant
- aria-pressed for toggles
- readable contrast
- useful live announcements where state changes matter

Pattern Lab should be usable without a mouse.

Reduced-motion preferences must continue to be respected.

When reduced motion is enabled:

- avoid unnecessary continuous animation
- preserve meaningful interaction feedback
- preserve sound functionality

---

# 22. TECHNICAL ARCHITECTURE

Do not rewrite the entire project solely for V2.

Preserve the current architecture where it is working.

The existing AudioEngine, Sequencer, and Instrument concepts may be extended.

Introduce additional abstractions only when they improve maintainability.

A PatternEngine or equivalent helper is appropriate.

Suggested responsibility:

PatternEngine

- generate step patterns
- generate presets
- calculate cycles
- calculate GCD-related information
- reverse patterns
- rotate starting vertex
- validate generated sequences

Keep mathematical generation independent from Canvas drawing whenever practical.

Canvas rendering should receive pattern data rather than contain the mathematics
inside rendering code.

Avoid unnecessary dependencies.

Prefer vanilla JavaScript and existing browser APIs.

---

# 23. STATE MODEL

V2 introduces more state.

Keep state explicit and understandable.

Possible state categories:

Instrument:
- selected polygon
- rotation
- octave
- glow
- focused vertex

Sequence:
- steps
- recording
- playing
- loop
- playhead

Pattern Lab:
- pattern type
- step
- direction
- preview sequence
- applied sequence

UI:
- open panel
- vertex label mode
- onboarding state

Audio:
- sound character

Avoid duplicating the same state in multiple places.

---

# 24. PERFORMANCE

Maintain smooth Canvas animation.

Do not perform expensive mathematical calculations every animation frame.

Pattern calculations should happen when:

- polygon changes
- pattern rule changes
- step changes
- transformation occurs

Cache/reuse generated pattern data where appropriate.

Continue capping devicePixelRatio where useful.

Avoid unnecessary DOM creation during animation.

Continue cleaning up Web Audio nodes.

Use one reusable AudioContext.

---

# 25. V2 VISUAL RULES

Preserve the existing visual identity.

Keep:

- dark near-black background
- subtle texture/grain
- thin circular guides
- glowing polygon
- polygon-specific accent colors
- DM Mono / Manrope typography
- pill controls
- understated panels
- subtle animations

Do NOT introduce:

- bright white cards
- conventional dashboard layouts
- giant navigation bars
- sidebars full of settings
- emoji-heavy interfaces
- childish game graphics
- gradients unrelated to the current aesthetic
- default Streamlit widgets inside the instrument when custom controls already
  exist

V2 should still look immediately recognizable as "This Is Math."

---

# 26. DO NOT BREAK V1.1

The following existing behavior must continue working:

- Triangle selection
- Square selection
- Pentagon selection
- Hexagon selection
- Octagon selection
- centered polygon names
- full chord playback
- individual vertex playback
- vertex note feedback
- geometric path drawing
- Record
- Finish Recording
- Play
- Loop
- Stop
- Clear
- sequence state indicator
- disabled control states
- Rotation
- Sequence Tempo
- Octave
- Glow
- Surprise Me
- Math panel
- Challenge panel
- keyboard shortcuts
- keyboard vertex navigation
- responsive layout
- accessibility states
- reduced-motion support
- Streamlit Community Cloud compatibility

If a V2 feature causes a regression in one of these systems, fix the regression
before continuing.

---

# 27. IMPLEMENTATION ORDER

Implement V2 incrementally.

Do NOT attempt all features in one large rewrite.

Recommended order:

### Phase 1 — Foundation

1. Review current V1.1 code.
2. Confirm all V1.1 controls still work.
3. Introduce PatternEngine or equivalent mathematical helper.
4. Add Pattern Lab panel shell without changing existing behavior.

### Phase 2 — Core Pattern Lab

5. Implement Step patterns.
6. Implement mathematical cycle detection.
7. Implement GCD-based pattern information.
8. Implement live path preview.
9. Allow generated pattern to load into existing Sequencer.
10. Integrate Play / Loop / Stop / Clear.

At this point, stop and test.

### Phase 3 — Visualization

11. Add vertex Number / Note / Off labels.
12. Add active-edge playback animation.
13. Add pattern completion/cycle feedback.
14. Add direction control.

Stop and test again.

### Phase 4 — Exploration

15. Add Around / Skip / Star / Mirror / Bounce presets.
16. Upgrade Surprise Me to use mathematical patterns.
17. Extend Math Mode with current-pattern information.
18. Extend Challenge Mode with pattern questions.

Stop and test again.

### Phase 5 — Polish

19. Add lightweight first-use guidance.
20. Improve mobile Pattern Lab layout.
21. Test keyboard accessibility.
22. Test reduced motion.
23. Test all V1.1 regression cases.

### Phase 6 — Secondary Features

Only after the core V2 is stable:

24. Add Sound Character presets.
25. Add Reverse / Rotate Start transformations.
26. Add recent Pattern History.

### Phase 7 — Optional

Only if the application remains clean and stable:

27. Add Pattern Code.
28. Consider additional mathematical pattern types.

---

# 28. V2 TESTING CHECKLIST

Before V2 is considered complete, manually verify:

## Existing instrument

A. Select all five polygons.

B. Verify each polygon remains visually centered.

C. Click every vertex.

D. Play every full chord.

E. Draw a manual path.

F. Record → Finish → Play.

G. Record → Loop → Play → Stop.

H. Clear.

I. Test all sliders.

J. Test Math.

K. Test Challenge.

L. Test existing keyboard shortcuts.

---

## Pattern Lab

M. Open and close Pattern Lab.

N. Generate Step 1 for every polygon.

O. Generate Step 2 where valid.

P. Generate several larger steps.

Q. Confirm generated indices are always valid.

R. Confirm patterns stop correctly when their cycle repeats.

S. Confirm GCD/cycle calculations are correct.

T. Confirm live preview matches the applied pattern.

U. Apply pattern → Play.

V. Apply pattern → Loop → Stop.

W. Change sequence tempo.

X. Change octave.

Y. Change glow.

Z. Reverse/change direction.

---

## Pattern accuracy

Test examples manually.

Triangle:
n = 3

Square:
n = 4

Pentagon:
n = 5

Hexagon:
n = 6

Octagon:
n = 8

Verify cases where:

gcd(n, step) = 1

and cases where:

gcd(n, step) > 1

Confirm the interface does not incorrectly claim that every vertex is visited
when the pattern forms multiple cycles.

---

## Responsive testing

Test approximately:

- wide desktop
- normal laptop
- tablet width
- narrow/mobile width

Verify:

- no horizontal overflow
- polygon remains centered
- Pattern Lab remains usable
- panels do not cover essential controls
- labels do not overlap excessively
- controls remain tappable
- text remains readable

---

## Accessibility testing

Verify:

- Tab navigation
- Enter/Space activation
- focus-visible styling
- Canvas keyboard navigation
- Pattern Lab keyboard controls
- screen-reader labels/state attributes
- reduced-motion behavior

---

# 29. V2 DEFINITION OF DONE

V2 is complete when a new user can:

1. Open This Is Math.
2. Choose a polygon.
3. Play its vertices and chord.
4. Open Pattern Lab.
5. Choose a mathematical rule.
6. Immediately see the resulting geometry.
7. Play the pattern as music.
8. Loop and modify it.
9. Open Math and understand why the pattern behaves as it does.
10. Experiment without needing to read README.md.

The strongest V2 experience should be:

"I changed a mathematical rule, the geometry changed, and I could hear the
difference."

That is the core identity of V2.

Do not sacrifice that experience for a larger number of features.