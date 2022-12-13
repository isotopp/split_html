#! /usr/bin/env python

import bs4.element
import click
import re


class SplitHTML:
    def __init__(self, html: str, chapterstart: int = 1, filetype="html"):
        """ Construct a SplitHTML object.
        ``html`` is the text of the HTML file to split.
        ``chapterstart`` is a start value for the chapter counter (Default: 1)
        """
        self.html = html
        self.chapternumber = chapterstart
        self.filetype = filetype

        self.chaptername = ""
        self.lines: list[bs4.element.Tag] = []

    def chapter_as_slug(self) -> str:
        """ Generate a slug string from the current ``self.chaptername``.

        Only the characters ``[a-zA-Z0-9_]`` are retained.
        All other characters are turned into ``-``.
        All characters are turned into lower case.
        """
        ret = re.sub(r"[^a-zA-Z0-9_]", "-", self.chaptername)
        ret = re.sub(r"-+", "-", ret)
        ret = ret.lower()
        return ret

    def write_chapter(self):
        """ Write the lines to a file named after the chapter. """
        if self.chaptername == "":
            return

        slug = self.chapter_as_slug()
        name = f"{self.chapternumber:02}-{slug}.{self.filetype}"
        with open(name, "w") as w:
            for line in self.lines:
                w.write(str(line))

        self.lines = []
        self.chapternumber += 1

    def process(self):
        """ Actually process the HTML, driving the entire thing. """
        soup = bs4.BeautifulSoup(self.html, "html.parser")
        if soup.body:
            bodycontent = soup.body.contents
        else:
            raise ValueError("Inputfile has no <body> Tag.")

        for element in bodycontent:
            if element.name == "h1":
                self.write_chapter()
                self.chaptername = element.text
                print(f"New Chapter: {self.chapternumber}: {self.chaptername}")

            self.lines.append(element)

        self.write_chapter()


@click.command()
@click.argument('infile', type=click.File('r'))
@click.option('--chapterstart', '--cs', default=1)
@click.option('--filetype', default="html")
def main(infile, chapterstart: int, filetype: str):
    html: str = infile.read()
    split_html = SplitHTML(html=html, chapterstart=chapterstart, filetype=filetype)
    split_html.process()


if __name__ == '__main__':
    main()
