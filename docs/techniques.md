# Techniques

The techniques demonstrated here are implemented as system-wide target facilitation tools built around [TargetFinder](https://github.com/AHMEDBENAKOUCHE/target_finder_toolkit).

## TargetFinder

TargetFinder uses YOLOv26 + PyQt to detect interactive targets on the screen and display their bounding boxes. The detected targets can then be used by target-aware pointing techniques.

## Bubble Cursor

Bubble Cursor is an area cursor whose area grows until reaching the closest target. This makes targets effectively larger and allows the user to select a target without placing the pointer exactly inside it.

Reference: [The Bubble Cursor: Enhancing Target Acquisition by Dynamic Resizing of the Cursor's Activation Area](https://www.tovigrossman.com/papers/chi2005bubblecursor.pdf)

## DynaSpot

DynaSpot is an area cursor whose area grows depending on instantaneous pointer speed. It behaves like a Bubble Cursor modulated by speed: the activation area expands during fast movement and shrinks when the pointer slows down, because precise selection usually requires slower motion.

Reference: [DynaSpot: Speed-Dependent Area Cursor](https://doi.org/10.1145/1518701.1518911)

## Semantic Pointing

Semantic Pointing locally dissociates the mapping between physical mouse movements and virtual cursor movements. This changes the control-display ratio near targets, making some targets feel sticky or, on the contrary, repulsive.


## Ninja Cursor

Ninja Cursor uses several distributed cursors instead of a single cursor. In this implementation, gaze is used to select the active cursor: the user first aims with the eyes, then performs finer movements with the mouse.

Reference: [Ninja Cursors: Using Multiple Cursors to Assist Target Acquisition on Large Screens](https://dl.acm.org/doi/pdf/10.1145/1357054.1357201)

## Platform Support

The code includes platform-specific handling for macOS, Windows, and Linux/X11.

- macOS: uses Quartz and ApplicationServices for click redirection and cursor handling.
- Windows: uses Windows APIs for cursor and mouse settings.
- Linux: targets X11, using X11/XFixes and xinput where needed.

Wayland is not fully supported for cursor hiding and click redirection.
