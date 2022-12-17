# md2rm

A **Markdown** to **Root-Me** syntax converter. If you are used to writting your writeups in markdown and later submitting them as solutions on Root-Me, this tool is for you! It should also work with any other content you can post, articles for example. It is implemented as a custom renderer for [marko](https://github.com/frostming/marko).

## Installation

Clone the repository, install the dependencies and here you go!

```bash
> git clone https://github.com/HexPandaa/md2rm
> cd md2rm
> pip3 install -r requirements.txt
```

> You can also use a virtual environment, or just grab the script without cloning the whole repo and install marko directly.

## Usage

If you have some markdown file with the following content (without the missing backtick of course):

```md
# Heading 1

## Heading 2 with `var`

Paragraph with **emphasis** and *italic*.

```c
void main(int argc, char **argv) { 
    printf("code block");
}
``

[link](https://hexpandaa.xyz)

- unordered
- list
1. ordered
2. list

> multiline
> quote
```

You can call the script with your file as argument and it will print the result to stdout.

```c
> ./md2rm.py doc.md
{{{Heading 1}}}

{{## Heading 2 with <code>var</code>}}

Paragraph with {{emphasis}} and {italic}.

<cadre class="c">
void main(int argc, char **argv) { 
    printf("code block");
}
</cadre>

[link->https://hexpandaa.xyz]

-* unordered
-* list

-# ordered
-# list

<quote>
multiline
quote
</quote>
```

You can also store the result in a file with the following:

```bash
> ./md2rm.py doc.md doc.rm
```

## Limitations

Most of the syntax is supported, here's a rundown:

|               | Markdown | Root-Me | Implemented                                                                                        |
| ------------- | -------- | ------- | -------------------------------------------------------------------------------------------------- |
| Headers       | ✅        | ✅       | ✅                                                                                                  |
| Bold          | ✅        | ✅       | ✅                                                                                                  |
| Italic        | ✅        | ✅       | ✅                                                                                                  |
| Code blocks   | ✅        | ✅       | ✅                                                                                                  |
| Inline code   | ✅        | ✅       | ✅                                                                                                  |
| Link          | ✅        | ✅       | ✅                                                                                                  |
| Quotes        | ✅        | ✅       | ✅                                                                                                  |
| Lists         | ✅        | ✅       | 🟠 No nested lists for now, but simple ordered and unordered ones are working.                     |
| Footnotes     | 🔴       | ✅       | 🔴 Footnotes are not defined in the CommonMark specifications, but I may add them as an extension. |
| Inline images | ✅        | 🔴      | 🔴 Root-Me doesn't seem to support inline images, but you can add them as attachements.            |
| TODOs         | 🔴       | ✅       | 🔴 Footnotes are not defined in the CommonMark specifications, but I may add them as an extension. |
