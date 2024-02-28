# Intermediate CSS

## Resources

---

## CSS Colors

- CSS accepts colors in different formats:
  - Named colors -> writing the name of the color
  ```css
  h1: {
    background-color: red;
  }
  ```
  - rgba -> uses a combination of red, green and blue each out 255
  ```css
  h1: {
    background-color: rgb(93, 56, 145);
  }
  ```
  - Hexcode -> uses a # followed by color code
  ```css
  h1: {
    background-color: #5d3891;
  }
  ```

## Font Properties

- Font Size -> can be set by using different ways
  - Pixels (px) which is about 1/96th of an inch or 0.26 mm
  - Point (pt) which is about 1/72nd of an inch or 35mm
  - em which renders to 100% of parent size
    - Example: if a `<footer>` element with a font-size of 40px, and a nested `<h2>` element nested inside with a font-size of 2em, then it would have a font-size of 80px because 40 \* 2
  - rem which is 100% of the root
    - Example: if we set a have a root `<html>` element of 16px and set an `<h2>` later down the line to 2rem, then it would have a size of 32px
- Font Weight -> can be set using different ways
  - Keywords: such as `normal`, `bold`, etc
  - Relative to parent: such as `lighter` or `bolder`
  - Number: using a number between 100-900 (100 is min, 900 is max)
- Font Family -> determines the font face
  - Font family is set using the name of the font (internal or download)
  - Fonts with more than three words use a comma ("Times New Roman")
  ```css
  h1 {
    font-family: Helvetica, sans-serif;
  }
  ```
- Text Alignment
  - Used to set the the start alignment of the text
