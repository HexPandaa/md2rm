#!/usr/bin/env python3

import marko
import argparse
import sys

__author__ = "HexPandaa"
__version__ = "1.0"
__repository__ = "https://github.com/HexPandaa/md2rm"

class RootMeRenderer(marko.renderer.Renderer):
    
    def render_heading(self, element: marko.block.Heading) -> str:
        """
        md: "# Level 1 heading\n"
        rm: "{{{Level 1 heading}}}\n"

        md: "## Level 2 heading\n"
        rm: "{{## Level 2 heading}}\n"
        """
        hashes = "#" * element.level + " " if element.level > 1 else ""
        result = f"{{{{{ hashes }{ self.render_children(element) }}}}}"
        if element.level == 1:
            result = f"{{{result}}}"  # Add the extra brackets
        return result + "\n"

    def render_raw_text(self, element: marko.inline.RawText) -> str:
        """
        md: "simple string"
        ex: "simple string"
        """
        return element.children

    def render_blank_line(self, element: marko.block.BlankLine) -> str:
        """
        md: "\n"
        rm: "\n"
        """
        return "\n"
    
    def render_code_span(self, element: marko.inline.CodeSpan) -> str:
        """
        md: "`something`"
        rm: "<code>something</code>"
        """
        return f"<code>{element.children}</code>"

    def render_fenced_code(self, element: marko.block.FencedCode) -> str:
        """
        md:
        "```lang
        line1
        line2
        ...
        ```"
        rm:
        "<cadre class="lang">
        line1
        line2
        ...
        </cadre>\n"
        """
        return f"<cadre class=\"{element.lang}\">\n{ self.render_children(element) }</cadre>\n"

    def render_paragraph(self, element: marko.block.Paragraph) -> str:
        """
        md: "simple string"
        rm: "simple string"
        """
        return self.render_children(element) + "\n"

    def render_emphasis(self, element: marko.inline.Emphasis) -> str:
        """
        md: "*simple string*"
        rm: "{{{simple string}}}"
        """
        return f"{{{ self.render_children(element) }}}"

    def render_strong_emphasis(self, element: marko.inline.StrongEmphasis) -> str:
        """
        md: "**simple string**"
        rm: "{{simple string}}"
        """
        return f"{{{{{ self.render_children(element) }}}}}"

    def render_link(self, element: marko.inline.Link) -> str:
        """
        md: "[title](link)"
        rm: "[title->link]"
        """
        return f"[{ self.render_children(element) }->{ element.dest }]"

    def render_list(self, element: marko.block.List) -> str:
        """
        md:
        "- unordered
        - list"
        rm:
        "-* unordered
        -* list"

        md:
        "1. ordered
        2. list"
        rm:
        "-# ordered
        -# list"

        note: currently does not properly support nested lists
        """
        result = ""
        bullet = "-#" if element.ordered else "-*"

        list_item: marko.block.ListItem
        for list_item in element.children:
            result += f"{bullet} {self.render(list_item)}"  # newline will be added by the inner paragraph
        
        return result

    def render_quote(self, element: marko.block.FencedCode) -> str:
        """
        md:
        "> multiline
        > quote\n"
        rm:
        "<quote>
        multine
        quote
        </quote>\n"
        """
        return f"<quote>\n{ self.render_children(element) }</quote>\n"

    def render_line_break(self, element: marko.inline.LineBreak) -> str:
        """
        md: "\n
        rm: "\n"
        """
        return "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="md2rm: A Markdown to Root-Me syntax converter.",
        epilog=f"v{__version__}, {__repository__}")
    parser.add_argument("input", type=argparse.FileType(mode="r"),
                        help="markdown file")
    parser.add_argument("output", nargs="?", type=argparse.FileType(mode="w"), default=sys.stdout,
                        help="output file. default: stdout")

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()
    return args


def main(args: argparse.Namespace) -> None:
    parser = marko.Markdown(renderer=RootMeRenderer)
    # markdown = parser.parse(args.input.read())
    # result = parser.render(markdown)
    result = parser.convert(args.input.read())
    args.output.write(result)

if __name__ == "__main__":
    main(parse_args())
