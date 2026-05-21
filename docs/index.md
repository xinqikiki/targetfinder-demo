# Smart Cursor

Using YOLOv26 + PyQt to build system-wide target facilitation techniques. Credits: Xinqi Tang, Eva-Ly Jerome, Julien Gori. Built on [TargetFinder](https://github.com/AHMEDBENAKOUCHE/target_finder_toolkit).

This page presents short demonstrations of several target selection techniques built around TargetFinder.

## TargetFinder

TargetFinder detects interactive targets on the screen using a YOLO model and displays the corresponding bounding boxes. These detected targets are then used by the interaction techniques below.

<video controls width="100%" src="assets/videos/targetfinder.mp4"></video>

## Bubble Cursor

Bubble Cursor is an area cursor, whose area grows until reaching the closest target. This essentially makes targets larger. Original Bubble Cursor [paper](https://www.tovigrossman.com/papers/chi2005bubblecursor.pdf).

<video controls width="100%" src="assets/videos/bubblecursor.mp4"></video>

## DynaSpot

DynaSpot is an area cursor whose area grows depending on the instantaneous speed. Essentially, it is a Bubble Cursor where the area is modulated by speed. The motivation behind this technique is that more precise selection requires slowing down. Original DynaSpot [paper](https://doi.org/10.1145/1518701.1518911).

<video controls width="100%" src="assets/videos/dynaspot.mp4"></video>

## Ninja Cursor

Ninja Cursor is a technique where one moves not a single cursor but an array of cursors. The actual cursor is selected with gaze. The idea is to first aim “with the eyes”, and perform finer movements with the mouse. Original Ninja Cursor [paper](https://dl.acm.org/doi/pdf/10.1145/1357054.1357201).

<video controls width="100%" src="assets/videos/ninjacursors.mp4"></video>

## Semantic Pointing

Semantic Pointing is a technique which locally dissociates the mapping between physical mouse movements and virtual cursor movements. Concretely, this can make targets look sticky or, on the contrary, repulsive. Original Semantic Pointing [paper](https://doi.org/10.1145/985692.985758).

<video controls width="100%" src="assets/videos/semanticpointing.mp4"></video>

## Link with TargetFinder

This demo project does not duplicate the source code of TargetFinder. Instead, it explicitly imports `target-finder-toolkit` as a dependency. This keeps the demo connected to the main toolkit, so improvements in the main project can be reused by this demo repository.
