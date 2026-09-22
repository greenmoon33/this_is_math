# This Is Math

An interactive mathematical music instrument built with Streamlit, Canvas, and the Web Audio API.

Choose a triangle, square, pentagon, hexagon, or octagon. Each form produces its own
animated geometry and musical harmony directly in the browser. Play individual
vertices, draw patterns between notes, record and loop sequences, or explore the
mathematics behind each regular polygon. Pattern Lab turns modular arithmetic and
symmetry rules into visible, playable sequences.

## Using the instrument

- Click a vertex to play its note and add it to the geometric pattern.
- Click the polygon's center—or press Space—to play the full chord.
- Press Record, play up to 32 vertices, then press Finish Recording or Stop.
  Play becomes available when the sequence is ready. Loop is a playback mode:
  turn it on, then press Play. Stop ends recording or playback, and Clear removes
  both the sequence and its drawn pattern.
- Use Math for polygon formulas and Challenge for short contextual questions.
- Use Surprise Me to generate a shape, direction, and musical pattern.
- Rotation controls speed and direction; Sequence Tempo affects playback speed;
  Octave changes pitch; Glow changes visual intensity.
- Keyboard shortcuts: `3`, `4`, `5`, `6`, or `8` select shapes; `R` randomizes;
  `C` clears. Focus the Canvas and use arrow keys plus Enter to play vertices.

## Pattern Lab

Open **Pattern Lab** to preview a mathematical path without changing your manual
drawing. Choose a rule, direction, and optional vertex labels, then press **Use
pattern**. The existing Play, Loop, Stop, Clear, Sequence Tempo, Octave, and Glow
controls operate on the generated sequence.

Available rules:

- **Step** repeatedly adds a chosen step modulo the polygon's vertex count.
- **Around** visits consecutive vertices.
- **Skip** connects every second vertex.
- **Star** chooses a coprime step that forms a regular star where one exists.
- **Mirror** alternates symmetric vertex pairs.
- **Bounce** moves around the polygon and then reverses direction.

For a Step pattern, Pattern Lab reports `gcd(n, step)`, the unique vertices in one
orbit, and the number of cycles. For example, Step 3 on an octagon visits all eight
vertices because `gcd(8, 3) = 1`; Step 2 visits four vertices in each of two cycles.
Math Mode reflects the current preview, and Challenge Mode can ask questions about
that generated pattern.

## Run locally

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

Connect this GitHub repository at [share.streamlit.io](https://share.streamlit.io),
select `app.py` as the entry point, and deploy. No secrets, external APIs, or audio
assets are required.
