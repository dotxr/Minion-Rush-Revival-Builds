# Minion Rush Revival Builds

The APK and IPA files for [Minion Rush Revival](https://github.com/dotxr/Minion-Rush-Revival), split into parts of up to 45 MiB.

Download them from the site, which puts the parts back together and checks every part: https://dotxr.github.io/minion-rush-revival/

To add or replace a build: `python3 split.py <id> <file>`, then commit `builds/<id>` and `builds.json`.

Each build in `builds.json` has a `status`:

- `stable`: 13.3.0, plays on the revival server.
- `experimental`: the `-offline` 9.6.1b and 9.7.1b builds. The server is built into the app, so they run without internet and everything in the shop costs 1.
- `untested`: built the same way as the offline builds but not played through yet (7.3.0i).

Each build also records `build` (how many times it has been published) and `released` (when, UTC).
