import pytest
from text_elements import Heading, Paragraph, Image, Link

def test_heading_render():
    heading = Heading(1, "Test Heading")
    assert heading.render() == "# Test Heading\n"

def test_paragraph_render():
    paragraph = Paragraph("This is a test paragraph.")
    assert paragraph.render() == "  This is a test paragraph.\n"

def test_image_render():
    image = Image("alt text", "http://example.com/image.png")
    assert image.render() == "  ![alt text](http://example.com/image.png)\n"

def test_link_render():
    link = Link("Test Link", "http://example.com")
    assert link.render() == "  [Test Link](http://example.com)\n"
