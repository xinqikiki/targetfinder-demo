# Techniques

## TargetFinder

TargetFinder detects interactive targets on the screen and displays their bounding boxes.

## Bubble Cursor

Bubble Cursor expands the effective selection area around the nearest target. The user can click even if the pointer is not exactly inside the target, as long as the bubble selects it.

## DynaSpot

DynaSpot dynamically changes the activation area around the pointer according to movement speed. The spot grows during fast movement and shrinks when the pointer slows down.

## Semantic Pointing

Semantic Pointing modifies pointer behavior near detected targets to make selection easier.

## Ninja Cursors

Ninja Cursors uses gaze to select one cursor among eight distributed cursors. The selected cursor can then be used to click the intended target.

## Platform Support

The code includes platform-specific handling for macOS, Windows, and Linux/X11.

- macOS: uses Quartz and ApplicationServices for click redirection and cursor handling.
- Windows: uses Windows APIs for cursor and mouse settings.
- Linux: targets X11, using X11/XFixes and xinput where needed.

Wayland is not fully supported for cursor hiding and click redirection.