# Embed webm

Anki addon that lets you paste or drag-and-drop .webm videos directly into the Anki editor.
Instead of opening an external player, the file is inserted as a normal HTML5 \<video\> element and plays inline in your cards.

## Configuration

`videoHTMLAttributes` controls which HTML attributes are added to the created \<video\> tag.

Each key becomes an HTML attribute on the generated \<video\> tag (see supported attributes: [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)).
Values can be strings or booleans: `true` value includes the attribute as boolean flag, while `false` excludes it.

Default config:

```json
{
  "videoHTMLAttributes": {
    "controls": true,
    "controlslist": "nodownload",
    "autoplay": true,
    "loop": false,
    "muted": false
  }
}
```
