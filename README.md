# Cookie Beamer

**Cookie** is a standalone, LuaLaTeX-first Beamer theme. It keeps the
asymmetric, numbered visual language of `awesome-beamer`, while adopting the
low-noise configuration habits people like in Metropolis: optional progress
bars, section pages, compact blocks, predictable options, and useful defaults
for technical slides.

## Quick start

Cookie is a single `.sty` file. There is no package installer, scaffold, or
Cookie-specific CLI; put the theme file beside the Beamer document that uses it.
Download it directly:

```sh
curl -LO https://raw.githubusercontent.com/SeniorMars/dotfiles/main/latex_template/cookie-beamer/beamerthemecookie.sty
```

If this repository is already cloned locally, copying the file works too:

```sh
cp /path/to/dotfiles/latex_template/cookie-beamer/beamerthemecookie.sty .
```

Then write your deck:

```tex
\documentclass[aspectratio=169]{beamer}

\definecolor{myaccent}{HTML}{356AE6}
\usetheme[
  accent=myaccent,
  progressbar=foot,
  sectionpage=progressbar,
  subsectionpage=none,
  numbering=fraction,
  block=fill
]{cookie}

\title{My talk}
\author{My name}
\date{\today}

\begin{document}
\maketitle

\section{First section}
\subsection{First idea}
\begin{frame}{A frame title}{A subtitle that clears the divider}
  Hello, cookie.
\end{frame}
\end{document}
```

Build the deck with LuaLaTeX. `latexmk` is convenient because it reruns TeX and
Biber when references, frame counts, or bibliography data change:

```sh
latexmk -lualatex my-talk.tex
```

Inside this repository, use the Makefile or run the same command directly:

```sh
make build
latexmk -lualatex main.tex
```

For the fastest edit loop, keep `latexmk` running in preview-continuous mode:

```sh
make watch
```

If a previous failed build leaves corrupted auxiliary files, force a clean
rebuild by removing generated state and then asking `latexmk` to rebuild:

```sh
make clean
make build
```

The theme does not load `qrcode`. Keeping QR generation out of the deck avoids
large QR matrices in `main.aux`, making rebuilds more reliable and keeping the
auxiliary files smaller.

## Presentation notes

`main.tex` is the dissertation-defense deck. `demo.tex` keeps the broader theme
examples as a reference deck for available Cookie features.

Use `\texttt{...}` for inline software, simulator, and package names such as
`\texttt{HighwayEnv}`, `\texttt{MetaDrive}`, `\texttt{CARLA}`, and
`\texttt{stable-baselines3}`. Avoid `\ttfamily{...}` for inline text because
`\ttfamily` is a font declaration and can leak into following text.

The HighwayEnv simulator slide in `main.tex` uses a compact image grid instead
of `figure`/`subfloat` captions. The layout is:

- two rows with four images each;
- each image is placed in a `.235\textwidth` minipage;
- captions and labels are intentionally omitted to keep the frame clean.

This keeps all simulator screenshots visible on one Beamer frame without
caption overflow. Adjust the minipage width directly if the image set changes.

The MetaDrive maps slide uses three representative vector maps from
`figures/sims/md/maps/`: `image_SC_vector.pdf`, `image_TXT_vector.pdf`, and
`image_rORY_vector.pdf`. They are placed in one row using `.29\textwidth`
minipages.

The CARLA simulator slide uses a two-by-two image grid with `.38\textwidth`
minipages. It includes `road_and_intersection.png`, `intersection.png`,
`highway_enter.png`, and `highway_exit.png` from `figures/sims/carla/`.

The RL Algorithms methodology slide places the algorithm hyperparameter
configuration note inside a `cookiecard` in the right column. Keep this content
compact because the card lives beside the algorithm/action-space list.

The individual-environment results in `main.tex` are split into four
HighwayEnv frames:

- projection matrix only;
- source distribution, `figures/results/single-envs/highway/7_sources.pdf`,
  paired with the best-performing-algorithm portfolio plot,
  `figures/results/single-envs/highway/5_port.pdf`;
- six metafeature slices matching the projection matrix variables:
  `2_lanes_count.pdf`, `2_traffic_density.pdf`,
  `2_baseline_speed_snr.pdf`, `2_baseline_obs_volatility_mean.pdf`,
  `2_state_entropy.pdf`, and `2_action_state_discontinuity_p95.pdf`;
- SVM portfolio plot, `6_svm_port.pdf`, paired with the algorithm performance
  table.

Each multiple-environment result uses two frames: one projection frame with
source and best-performing-algorithm plots side by side, followed by a
performance-comparison table frame.

- discrete-action HighwayEnv environments:
  `figures/results/cross-envs/hedisc/7_sources.pdf` and
  `figures/results/cross-envs/hedisc/5_port.pdf`;
- all continuous-action environments:
  `figures/results/cross-envs/allcont/7_sources.pdf` and
  `figures/results/cross-envs/allcont/5_port.pdf`.

## Theme options

| Option | Values | Default |
|---|---|---|
| `accent` | any defined `xcolor` color | `cookieAccentDefault` |
| `progressbar` | `none`, `head`, `frametitle`, `foot` | `foot` |
| `sectionpage` | `none`, `simple`, `progressbar` | `progressbar` |
| `subsectionpage` | `none`, `simple`, `progressbar` | `none` |
| `numbering` | `none`, `counter`, `fraction` | `fraction` |
| `numberrail` | `none`, `section`, `subsection` | `subsection` |
| `numberrailcolor` | `muted`, `accent`, `blue` | `muted` |
| `block` | `transparent`, `fill` | `fill` |
| `background` | `light`, `dark` | `light` |
| `titleformat` | `regular`, `smallcaps`, `allcaps` | `regular` |
| `fonts` | `auto`, `none` | `auto` |
| `mathfonts` | `libertinus`, `none` | `libertinus` |
| `toc` | `none`, `aftertitle` | `none` |
| `closing` | `none`, `contact` | `none` |
| `covered` | `invisible`, `transparent` | `invisible` |
| `notes` | `hide`, `show`, `second`, `only` | `hide` |

`coloraccent=<color>` is accepted as an alias for `accent=<color>`.

The structural number rail uses dimmed accent colors by default so values such
as `1.1` support the title instead of competing with it. Use
`numberrailcolor=accent` for a brighter accent treatment, or
`numberrailcolor=blue` to color the whole rail with `themeColorFive` while
leaving the main accent unchanged.

Section and subsection numbers use `themeColorFive` directly so they remain
blue even when the main accent is changed for title-page artwork or other
structural marks.

Progress bars use `themeColorEleven` (`#5D4037`) for the completed line and a
lightened `themeColorFour` (`#C89B6A`) shade for the remaining/current area.
The active footer section label and frame-title divider use mixes of the same
brown. Contents and section-slide left bars use `themeColorFour`.

Cookie's global progress bar follows numbered sections from Beamer's table of
contents. Starred sections such as `\section*{Extras}` are excluded from the
bar and labels; frames inside them show the progress state clamped to the last
numbered section.

When `progressbar=foot`, the section labels in the footer are PDF links to the
first frame of each numbered section, using the same section start pages as the
table of contents.

The structural number rail is also hidden on frames inside starred sections,
and its reserved title-space is collapsed so those frame titles align to the
left rail position. Ordinary numbered sections keep the rail.

The progress subsection page reports the current subsection and the number of
subsections in its section. Run LuaLaTeX twice after changing the section
structure; `latexmk` handles this automatically.

## LuaLaTeX and fonts

With `fonts=auto`, Cookie selects installed Noto fonts when available:

1. Noto Sans for main text and sans text.
2. Noto Sans Mono for code and monospaced text.
3. TeX Gyre Heros / DejaVu Sans Mono as fallbacks.

With `mathfonts=libertinus`, Cookie loads `unicode-math` and uses Libertinus
Math when available. Text remains in Noto; the Libertinus setup is math-only.
Use `mathfonts=none` before loading a custom math package yourself.

No fonts are bundled. To use your own setup, choose `fonts=none` and load
`fontspec` yourself:

```tex
\usetheme[fonts=none]{cookie}
\usepackage{fontspec}
\setmainfont{Your Text Font}
\setsansfont{Your Sans Font}
\setmonofont{Your Mono Font}
```

## Metadata and title images

All extended title-page fields are optional and safe when empty:

```tex
\cookieemail{you@example.edu}
\cookieuni{Your University}
\cookielocation{Your City}
\cookietagline{A short kicker above the title}
\cookietitleimage{assets/title-image.jpg}
```

`\cookietitleimage` clips an image into the colored title-page wedge. Standard
Beamer `\titlegraphic{...}` also works.

The closing slide can include contact details and the Cookie penguin:

```tex
\cookieclosingtitle{Thank you}
\cookieclosingtext{Questions?}
\makeclosing
```

Add `closing=contact` to insert the closing slide automatically.

The default closing slide uses a light `cookiePaper` background, the same
`cookieTitleBar` left bar as contents and section slides, `themeColorFive` for
the question prompt, and `cookieProgressLine` for the small closing rule.

## Background images on ordinary frames

Use frame keys for a local, full-canvas background:

```tex
\begin{frame}[
  bgimage=assets/photo.jpg,
  bgfit=cover,
  bgoverlay=cookieInk,
  bgoverlayopacity=.56
]{A readable photo slide}
  Content goes here.
\end{frame}
```

Available frame keys:

| Key | Values / meaning |
|---|---|
| `bgimage` | image filename |
| `bgfit` | `cover`, `contain`, or `stretch` |
| `bgopacity` | image opacity from `0` to `1` |
| `bgoverlay` | any defined color |
| `bgoverlayopacity` | wash opacity from `0` to `1` |

The frame keys only draw the image and wash. For a dark photo slide, set local
text colors yourself:

```tex
{
\setbeamercolor{normal text}{fg=white,bg=}
\setbeamercolor{frametitle}{fg=white,bg=}
\begin{frame}[bgimage=assets/photo.jpg,bgoverlay=cookieInk,bgoverlayopacity=.56]{Title}
  \color{white}
  Content goes here.
\end{frame}
}
```

The settings reset after the frame. A global image is also available:

```tex
\cookiebackgroundimage{assets/photo.jpg}
% subsequent frames
\cookieclearbackgroundimage
```

## Components

Cookie uses ordinary Beamer components and adds a few small helpers:

```tex
\cookiekicker{Small uppercase label}
\cookiebadge{compact badge}
\cookieseparator
\cookiecheck
\cookiecross
\cookiepenguin[scale=.55]
```

A light card works well in columns:

```tex
\begin{cookiecard}[title=Result]
  Compact supporting content.
\end{cookiecard}
```

A themed `listings` code card requires no shell escape:

```tex
\begin{frame}[fragile]{Code}
  \begin{cookiecode}[title=Example]{C}
int square(int x) {
  return x * x;
}
  \end{cookiecode}
\end{frame}
```

For ordinary `lstlisting`, select the supplied style:

```tex
\lstset{style=cookie}
```

Algorithms use `algorithm2e` with Cookie's line numbers, keywords, captions,
and comments:

```tex
\begin{frame}{Algorithm}
  \begin{algorithm}[H]
    \caption{Projected gradient descent}
    \KwIn{Objective $f$, feasible set $C$, initial point $x_0$}
    \KwOut{Approximate minimizer $x_t$}
    \For{$t = 0,1,\ldots,T-1$}{
      $g_t \leftarrow \nabla f(x_t)$\tcp*{gradient}
      $x_{t+1} \leftarrow \Pi_C(x_t-\eta_t g_t)$\;
    }
    \Return $x_T$\;
  \end{algorithm}
\end{frame}
```

Cookie loads `algorithm2e` with `ruled`, `vlined`, and `linesnumbered` when it
is available. Load `algorithm2e` before the theme if a deck needs different
package options.

A quote card is intended for short transitions or a single load-bearing idea:

```tex
\begin{cookiequote}[Donald Knuth]
  Science is what we understand well enough to explain to a computer.
\end{cookiequote}
```

The `wide` environment gives diagrams and tables extra horizontal room:

```tex
\begin{wide}
  % wide content
\end{wide}
```

Three-column slides use standard Beamer layout and inherit Cookie's spacing:

```tex
\begin{columns}[T,onlytextwidth]
  \column{.29\textwidth} ...
  \column{.36\textwidth} ...
  \column{.29\textwidth} ...
\end{columns}
```

## Agenda, overlays, and animations

A reusable agenda frame is available independently of `toc=aftertitle`:

```tex
\makeagenda
\makeagenda[currentsection]
```

For this defense deck, `\makeagenda` renders the Contents slide with a
full-height left accent bar and a vertically centered section list. Section
title pages use the same left bar, with the section number and section title on
one shared baseline.

The footer uses a global section progress rail above the bottom bar instead of
the old deck-wide frame progress line. The bottom bar labels only the main
section names. The rail draws one equal sector per main section, fills completed
sections, marks the current position with a dot, and subdivides only the active
section when that section has subsections.

A Metropolis-style emphasis frame is available:

```tex
\begin{frame}[standout,noframenumbering]
  One idea per slide.
\end{frame}
```

Useful TikZ styles are included:

```tex
cookie node
cookie accent node
cookie arrow
visible on=<2->
muted on=<3>
```

Cookie includes a foreground modal compatible with old awesome-beamer slides:

```tex
\begin{modal}<3>[Key detail]
  This card appears on overlay 3.
\end{modal}
```

The explicit name `cookiemodal` is equivalent. Standard Beamer commands such as
`\pause`, `\only`, `\uncover`, `\onslide`, `onlyenv`, and item overlays work
unchanged. Two compact helpers are available:

```tex
\cookiereveal<2->{content}  % like \uncover, preserving space
\cookiefocus<3>{content}    % muted except on overlay 3
```

Choose `covered=transparent` to make ordinary covered material faintly visible.
The full demo includes an animated, three-layer system diagram whose geometry
stays fixed while the visual focus changes.

## Speaker notes

Cookie uses native Beamer `\note{...}` commands and adds a styled note page.
Choose the output mode in the theme options:

```tex
\usetheme[notes=second]{cookie} % presenter-style PDF with note content
```

```tex
\begin{frame}{Main claim}
  The audience sees this.

  \note{
    \begin{itemize}
      \item Open with the motivating question.
      \item Spend 45 seconds here.
      \item Transition to the implementation diagram.
    \end{itemize}
  }
\end{frame}
```

`notes=show` emits note pages after slides, `notes=only` emits only note pages,
and `notes=hide` creates the ordinary audience deck.

In `main.tex`, speaker notes can be written in the source and hidden from the
audience PDF with `notes=hide`. The first Reinforcement Learning slide includes
an example note. For rehearsal, use `notes=second` for a presenter PDF or
`notes=show` to inspect the styled note pages after each slide. Cookie's note
pages intentionally omit the current-slide preview because presenter tools can
already show the current and next slide.

## Citations and bibliography

Cookie does not replace the standard bibliography stack. The demo uses
BibLaTeX and Biber:

```tex
\usepackage[backend=biber,style=authoryear]{biblatex}
\addbibresource{refs.bib}

% later
A cited claim \parencite{my-source}.

\begin{frame}[allowframebreaks]{References}
  \printbibliography[heading=none]
\end{frame}
```

The theme styles bibliography colors and markers while leaving citation style
and data ownership to BibLaTeX.

For this thesis defense deck, citations that should be visible on the same slide use:

```tex
A cited claim \slidecite{my-source}.
```

Use `\slidecite` for the compact in-text citation, then place
`\slidereferences{my-source}` once near the end of the frame. The full reference
list is drawn in tiny text directly above the footer, spanning almost the full
slide width and independent of the frame's columns or main content layout.

The placement is controlled in `bib_helpers.tex`:

```tex
text width=.89\paperwidth
at ([xshift=.055\paperwidth,yshift=.055\paperheight]current page.south west)
```

`text width` is the available line width for the reference block. Increase it to
use more horizontal space, or decrease it to wrap earlier. `xshift` moves the
left edge of the reference block from the left side of the slide. `yshift` moves
the bottom edge up from the bottom of the slide; increase it to move references
up, decrease it to move them closer to the footer.

## Blocks and old decks

Cookie uses standard Beamer block syntax:

```tex
\begin{block}{Standard Beamer title}
  ...
\end{block}
```

## Files

- `beamerthemecookie.sty` - the theme.
- `demo.tex` / `demo.pdf` - blocks, theorem/proof, math, code, overlays,
  system diagrams, quotes, notes source, citations, QR closing, three-column
  composition, and image backgrounds.
- `refs.bib` - bibliography data used by the demo.
- `.latexmkrc` - local demo builds with LuaLaTeX and Biber.

## License and credit

Cookie is released under the BSD 3-Clause License. Its visual direction and
migration interface are based in part on Lukas Pietzschmann's
`awesome-beamer`, also BSD-3-Clause. Metropolis inspired the option surface and
progress-bar approach. See `LICENSE` for notices.
