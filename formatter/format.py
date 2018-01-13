#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert a basically formatted HTML file into a formated text file.

Copyright (c) 2018 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

"""


# Metadata, license and copyright
__author__ = "Chris Lunsford"
__author_email__ = "chrlunsf@cisco.com"
__copyright__ = "Copyright (c) 2018 Cisco and/or its affiliates."
__license__ = "Cisco Sample Code License, Version 1.0"


from functools import reduce
import os
import textwrap
from typing import Iterable

import click
import bs4


# Constants
DEFAULT_ENCODING = 'utf-8'
DEFAULT_DOCUMENT_WIDTH = 79
DEFAULT_MARGIN = 0


# Helper Functions
def read_input_file(file_path: str) -> str:
    """Read the text contents of the input file using the default encoding."""
    with open(file_path, 'rt', encoding=DEFAULT_ENCODING) as read_file:
        return read_file.read()


def create_output_file_path(input_file_path):
    """Create and return an output file path based on the input file path."""
    directory, input_filename = os.path.split(input_file_path)
    output_filename = input_filename.rsplit(".", 1)[0] + ".txt"
    return os.path.join(directory, output_filename)


def write_output_file(file_path: str, text: str):
    """Write the text to the output file using the default encoding."""
    with open(file_path, 'wt', encoding=DEFAULT_ENCODING) as write_file:
        write_file.write(text)


def clean(text: str) -> str:
    """Clean a paragraph of text; removing extra whitespace."""
    # text = text.strip()
    # lines = [line for line in text.split('\n') if line]
    # return " ".join(lines)
    return " ".join(text.split())


def indent(text: str, spaces: int) -> str:
    """Indent text by specified number of spaces."""
    return '\n'.join(" " * spaces + line for line in text.split('\n'))


def prefix_and_indent(prefix: str, text: str) -> str:
    """Add the prefix to the first line and indent all subsequent lines."""
    prefix_len = len(prefix)
    output = []
    for line_number, line in enumerate(text.split('\n')):
        if line_number == 0:
            output.append(prefix + line)
        else:
            output.append(" " * prefix_len + line)

    return '\n'.join(output)


def fill_lines(text: str, width: int) -> str:
    """Add trailing whitespace to each line such that len(line) == width."""
    return '\n'.join(
        line + " " * (width - len(line))
        for line in text.split('\n')
    )


def rstrip_lines(text: str) -> str:
    """Remove trailing whitespace from each line in the text."""
    return '\n'.join(line.rstrip() for line in text.split('\n'))


def lines_are_length(lines: [str, Iterable], length: int) -> bool:
    """Verify that each line is the specified length."""
    if isinstance(lines, str):
        lines = lines.split('\n')

    for line in lines:
        if len(line) != length:
            return False

    return True


def center(text: str, width) -> str:
    """Center the provided text within the specified width."""
    wrapper = textwrap.TextWrapper(width=width)

    text_lines = [line.strip() for line in text.split('\n')]

    wrapped_lines = []
    for text_line in text_lines:
        wrapped_lines += wrapper.wrap(text_line)

    centered_lines = ["{:^{width}}".format(line, width=width)
                      for line in wrapped_lines]

    assert lines_are_length(centered_lines, width)

    return '\n'.join(centered_lines) + '\n'


def wrap(text: str, width: int, left_indent: int=0, hanging_indent: int=0,
         right_indent: int=0):
    """Indent and wrap the text."""
    width = width if not right_indent else width - right_indent
    initial_indent = ' ' * left_indent
    subsequent_indent = initial_indent + ' ' * hanging_indent

    wrapped_text = textwrap.fill(
        text,
        width=width,
        initial_indent=initial_indent,
        subsequent_indent=subsequent_indent
    )
    wrapped_text = fill_lines(wrapped_text, width)

    assert lines_are_length(wrapped_text, width)
    return wrapped_text + '\n'


def combine_strings(one: str, two: str) -> str:
    """Combine strings eliminating duplicate blank lines."""
    if len(one) > 2 and one[-2:] == '\n\n' \
            and len(two) >= 1 and two[0] == '\n':
        # String one has a trailing blank line, and string two has a prefixed
        # blank line.  Strip the duplicate blank line.
        return one + two[1:]
    else:
        return one + two


def parse_inline_css(style: str) -> dict:
    """Parse an inline CSS 'style' string into a dictionary."""
    css = {}
    for key_value_str in style.split(';'):
        key, value = key_value_str.split(':')

        key = key.strip()

        value = value.strip()
        try:
            value = int(value)
        except ValueError:
            pass
        try:
            value = float(value)
        except ValueError:
            pass

        css[key] = value
    return css


# Core Functionality
class ElementFormatter(object):
    """Format parsed HTML elements as formatted strings."""

    def __init__(self, element: bs4.PageElement, width: int):
        """Initialize a new formater with a parsed PageElement."""
        self.element = element
        self.width = width

    def __str__(self) -> str:
        """Format a bs4 parsed HTML element into a formatted string."""
        if isinstance(self.element, bs4.NavigableString):
            return self.format_string()
        elif isinstance(self.element, bs4.Tag):
            if self.element.name == 'p':
                return self.format_paragraph()
            elif self.element.name == 'ul':
                return self.format_unordered_list()
            elif self.element.name == 'ol':
                return self.format_ordered_list()
            elif hasattr(self.element, 'children'):
                return self.format_children()
            elif hasattr(self.element, 'string'):
                return self.format_string()
            else:
                print("Unparsable Tag:", self.element)
                return ""
        else:
            print("Unparsed Element:", self.element)
            return ""

    def format_string(self) -> str:
        """Clean and format a NavigableString."""
        assert isinstance(self.element, bs4.NavigableString)
        cleaned_string = clean(str(self.element))
        if cleaned_string:
            return wrap(cleaned_string, self.width)
        else:
            return cleaned_string

    def format_children(self):
        """Format child elements and combine the results."""
        assert isinstance(self.element, bs4.Tag)
        children = (ElementFormatter(child, self.width)
                    for child in self.element.children)
        child_strings = []
        for child in children:
            child_strings.append(str(child))
        return reduce(combine_strings, child_strings)

    def format_paragraph(self) -> str:
        """Format a paragraph tag and return the formatted text."""
        assert isinstance(self.element, bs4.Tag) and self.element.name == 'p'
        if self.element.attrs.get('align') == 'center':
            paragraph_text = center(self.element.get_text(strip=True),
                                    self.width)
        else:
            paragraph_text = wrap(self.element.get_text(strip=True),
                                  self.width)

        if self.element.attrs.get('style'):
            inline_css = parse_inline_css(self.element.attrs['style'])
            if 'margin' in inline_css and inline_css['margin'] == 0:
                # No vertical margin spacing
                return paragraph_text

        # Add vertical margin spacing
        return '\n' + paragraph_text + '\n'

    def format_unordered_list(self) -> str:
        """Format an unordered list and return the formatted string."""
        assert isinstance(self.element, bs4.Tag) and self.element.name == 'ul'
        li_items = self.element.find_all('li')
        item_tag = "* "
        item_tag_length = len(item_tag)
        item_width = self.width - item_tag_length
        list_items = [ElementFormatter(item, item_width) for item in li_items]

        list_text = []
        for li in list_items:
            item_children_text = str(li)

            if item_children_text[0] == '\n':
                vmargin_prefix = '\n'
                start = 1
            else:
                vmargin_prefix = ''
                start = None

            if item_children_text[-2:] == '\n\n':
                vmargin_suffix = '\n'
                stop = -1
            else:
                vmargin_suffix = ''
                stop = None

            item_children_text = item_children_text[start:stop]
            item_text = prefix_and_indent(
                prefix=item_tag,
                text=item_children_text,
            )
            list_text.append(vmargin_prefix + item_text + vmargin_suffix)

        return reduce(combine_strings, list_text)

    def format_ordered_list(self) -> str:
        """Format an ordered list and return the formatted string."""
        assert isinstance(self.element, bs4.Tag) and self.element.name == 'ol'
        li_items = self.element.find_all('li')
        num_items = len(li_items)
        num_col = len(str(num_items))
        item_tag = "{:>{num_col}}. "
        item_tag_length = len(item_tag.format("#", num_col=num_col))
        item_width = self.width - item_tag_length
        list_items = [ElementFormatter(item, item_width) for item in li_items]

        list_text = []
        for item_number, li in enumerate(list_items, start=1):
            item_children_text = str(li)
            vmargin_prefix = '\n' if item_children_text[0] == '\n' else ""
            vmargin_suffix = '\n' if item_children_text[-1] == '\n' else ""
            item_children_text = item_children_text.strip()
            item_text = prefix_and_indent(
                prefix=item_tag.format(item_number, num_col=num_col),
                text=item_children_text,
            )
            list_text.append(vmargin_prefix + item_text + vmargin_suffix)

        return reduce(combine_strings, list_text)


def format_html(input_html: str, document_width: int=DEFAULT_DOCUMENT_WIDTH,
                left_margin: int=DEFAULT_MARGIN,
                right_margin: int=DEFAULT_MARGIN) -> str:
    """Convert a basically formatted HTML string into formatted text.

    Args:
        input_html(str): A basically formatted HTML string.
        document_width(int): The maximum width (number of chars) for the
            formatted output text.
        left_margin(int): The number of spaces the left margin should be
            indented.
        right_margin(int): The number of spaces the right margin should be
            indented.

    Returns:
        str: A string containing the formatted text.

    """
    width = document_width - left_margin - right_margin
    parsed_html = bs4.BeautifulSoup(input_html, "html.parser")
    body = ElementFormatter(parsed_html.body, width)
    document = indent(str(body), left_margin)
    document = rstrip_lines(document)
    return document


@click.command()
@click.argument('input-file', type=click.Path(exists=True), required=True)
@click.argument('output-file', type=click.Path(), required=False)
@click.option('-w', '--document-width', default=DEFAULT_DOCUMENT_WIDTH)
@click.option('-m', '--margin', default=DEFAULT_MARGIN)
@click.option('-l', '--left-margin', type=int)
@click.option('-r', '--right-margin', type=int)
def main(input_file, output_file, document_width, margin, left_margin,
         right_margin):
    """Convert a basically formatted HTML file into a formated text file."""
    left_margin = left_margin or margin
    right_margin = right_margin or margin

    input_html = read_input_file(input_file)

    formatted_text = format_html(
        input_html,
        document_width=document_width,
        left_margin=left_margin,
        right_margin=right_margin,
    )

    output_file = output_file or create_output_file_path(input_file)
    write_output_file(output_file, formatted_text)


if __name__ == '__main__':
    main()
