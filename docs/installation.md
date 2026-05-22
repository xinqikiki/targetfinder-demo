# Installation

## Requirements

- Python 3.10+
- macOS, Windows, or Linux/X11
- A webcam for Ninja Cursors
- Camera permission for gaze-based techniques
- Accessibility/Input Monitoring permission may be required on macOS
- X11 is recommended on Linux. Wayland is not fully supported for cursor hiding and click redirection.

## Clone the demo repository

```bash
git clone https://github.com/xinqikiki/targetfinder-demo.git
cd targetfinder-demo
```

## Create a virtual environment

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

## Install the demo dependencies

```bash
pip install -e .
```

This installs `target-finder-toolkit[gaze]` from the main TargetFinder repository. The demo repository does not duplicate the toolkit code.

The default demo installation includes the dependencies needed by the gaze-based Ninja Cursors technique, including `webeyetrack`, `tensorflow`, and `mediapipe`. This makes the installation heavier, but allows all demo examples to run from the same environment.

## Run the examples

### TargetFinder

```bash
python examples/run_targetfinder.py
```

### Bubble Cursor

```bash
python examples/run_bubble.py
```

### DynaSpot

```bash
python examples/run_dynaspot.py
```

### Semantic Pointing

```bash
python examples/run_semantic.py
```

### Ninja Cursors

```bash
python examples/run_ninja.py
```

Ninja Cursors requires a webcam and may need camera permission before it can track gaze. On first run, model weights may be downloaded or initialized depending on the main toolkit configuration.

## Notes

- On macOS, allow Terminal or your Python app in Accessibility and Input Monitoring if cursor control or click redirection does not work.
- On Windows, run commands from PowerShell inside the activated virtual environment.
- On Linux, use an X11 session when possible. Wayland may block cursor hiding or synthetic click behavior.
