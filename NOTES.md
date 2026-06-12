# CoffeeBucks Notes

## Fixed Header Spacing

When a navbar/header uses `position: fixed`, it floats on top of the page instead of taking up normal space.

That means page content can slide underneath it unless the page reserves space.

Fix:

```css
body {
    margin: 0;
    padding-top: 58px;
}
```

`padding-top` should roughly match the height of the fixed header.

## Margin vs Top

Use `margin-top` when you want normal space between sections.

Avoid using this for basic section spacing:

```css
position: relative;
top: 50px;
```

That visually moves the element, but it does not create normal layout space the same way margin does.

Better:

```css
.special-offers {
    margin-top: 80px;
}
```

## Fixed Elements Can Cover Content

`position: fixed` removes an element from the normal page layout.

That means other content does not know the fixed element is there.

Example:

```css
.site-container {
    position: fixed;
    top: 0;
    width: 100%;
}
```

This keeps the navbar stuck to the top of the screen, but page content may appear behind it.

Fix by adding space to the page:

```css
body {
    padding-top: 58px;
}
```

Use this when:

- The navbar/header is fixed
- The first section starts underneath the navbar
- Content looks hidden behind the top bar

## Footer Overlap

Avoid using `position: fixed` on a footer unless you specifically want it to stay on screen at all times.

For most websites, the footer should stay in normal page flow:

```css
.footer-container {
    width: 100%;
    padding: 12px 0;
    margin-top: 80px;
}
```

Normal footer behavior:

- Content appears first
- Footer appears after the content
- Footer does not cover sections above it

## Horizontal Image Groups

If images stack vertically, check the HTML order.

This stacks because the second image comes after the first image's text:

```html
<img>
<span>Description</span>
<img>
<span>Description</span>
```

Better structure:

```html
<div class="special-offers-grid">
    <section class="special-offer-card">
        <img>
        <span>Description</span>
    </section>

    <section class="special-offer-card">
        <img>
        <span>Description</span>
    </section>
</div>
```

Then make the parent horizontal:

```css
.special-offers-grid {
    display: flex;
    justify-content: center;
    gap: 16px;
    flex-wrap: wrap;
}
```

Main idea:

The parent controls the row.
Each child card keeps its own image and description together.

## Aligning Two Images Horizontally

When two images need to line up side by side, use a parent container with two equal columns.

HTML structure:

```html
<div class="special-offers-grid">
    <section class="special-offer-card">
        <img>
        <span>Description</span>
    </section>

    <section class="special-offer-card">
        <img>
        <span>Description</span>
    </section>
</div>
```

CSS:

```css
.special-offers-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 16px;
    align-items: start;
}
```

Why this works:

- `display: grid` makes the parent control layout
- `repeat(2, minmax(0, 1fr))` creates two equal columns
- Each `.special-offer-card` keeps one image and its description together
- Giving both images the same `height` makes their bottoms align

Responsive version:

```css
@media (max-width: 1000px) {
    .special-offers-grid {
        grid-template-columns: 1fr;
    }
}
```

This keeps the images horizontal on desktop and stacks them on smaller screens.
