# UIB - Fonts and boxes

## Quick tip- Google Fonts for custom fonts## Everything is a box!- Easy to see with inspecting and setting Dev tools CSS
  - `* { border: 1px solid red !important; }`
  - `div { border: 1px solid blue !important; }`
  - `span { border: 1px solid green !important; }`

## Containing content- Semantic elements, let's learn a few
  - `<main>`
  - represents the main content of a page
  - often combined with "skipnav" technique
  - nav = your navigation menu
    - `<nav>` - semantic element used for wrapping your navigation section
  - used for wrapping your main content
  - "shrink wrapping" / wrapping
    - put all of your content inside the main
  - often you can have classes and/or ids for your main element
    - <main class="container"></main>
  - One (visible) main per page## Stop content busting out of its box!    width: 40vw;       /* Set box width */
    height: 40vh;      /* Set box height */
    margin: auto;      /* Center this box inside its parent box */
    overflow: hidden;  /* Prevent content from overflowing out of the box! */