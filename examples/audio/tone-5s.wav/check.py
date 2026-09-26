import wave

try:
    with wave.open("tone-5s.wav") as w:
        declared = w.getnframes()
        frame_size = w.getsampwidth() * w.getnchannels()
        actual = len(w.readframes(declared)) // frame_size
    note = "truncated or lying header" if actual < declared else "ok"
    print(f"header says {declared} frames, file holds {actual}: {note}")
except (wave.Error, EOFError) as e:
    print("rejected:", str(e) or "the header is cut short")
