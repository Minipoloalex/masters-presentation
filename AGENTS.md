# Agent Instructions

## Project Context
- **Goal:** Make a presentation for my master thesis. You, the agent, is focused on making the template according to my instructions.
- **Context:** a presentation for the defense of a dissertation project.
- **Repository Structure:**
  * `main.tex`: code file;
  * `beamerthemecookie.sty`: style file;
  * `figures/`: folder containing all figures (e.g., Reinforcement Learning diagram);
  * `README.md`: contains information about the template. You should update it with new changes so that you can consult it anytime for accurate information;

## Coding Standards & Rules
- Use `snake_case` variables when applicable.
- Do not try to hide errors or try to "cleanily fail". It only creates doubt if it is actually behaving as intended or not. It is better to get an error, allowing me to fix it, then degrade and make me not know it

## Compiling
- Check the project's `Makefile`
