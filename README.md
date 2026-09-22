# This Is Math

An interactive geometric chord instrument built with Streamlit, Canvas, and the Web Audio API.

Choose a triangle, square, pentagon, hexagon, or octagon. Each form produces its own
animated geometry and musical harmony directly in the browser. Play individual
vertices, draw patterns between notes, record and loop sequences, or explore the
mathematics behind each regular polygon.

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

## Run locally

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

Connect this GitHub repository at [share.streamlit.io](https://share.streamlit.io),
select `app.py` as the entry point, and deploy. No secrets, external APIs, or audio
assets are required.
