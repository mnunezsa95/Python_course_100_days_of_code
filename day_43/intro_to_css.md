# Introduction to CSS

## Resources

---

## Why do we need CSS?

- Developers wanted to find a way to add styles to HTML documents
- HTML 3.2 introduced new elements & attributes
  - `<font>` element
  - `<center`> element
  - `color`, `size`, etc attributes
- CSS allowed for adding styling sheets (in CSS format) to HTML documents
  - Allowed for separation of concerns (modularity)

## How to add CSS

- CSS can be added in 3 ways:
  1. Inline
     - Coded into the same line as a particular HTML element using a `style` attribute
  ```html
  <!--Uses properties and values-->
  <html style="background:blue"></html>
  ```
  2. Internal
     - Uses a `<style>` element
  ```html
  <body>
    <style>
      html {
        background: red;
      }
    </style>
  </body>
  ```
  3. External
     - Uses an external sheet that holds all style logic
     - Uses a `<link />` tag with both `rel` (relation) and `href` (link) attributes
  ```html
  <link rel="stylesheet" href="index.css" />
  ```
