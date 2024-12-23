class TextElement:
    def render(self, indentation=0):
        raise NotImplementedError

    def get_content(self, indentation=0):
        raise NotImplementedError


class Heading(TextElement):
    def __init__(self, level, text):
        self.level = level
        self.text = text

    def render(self, indentation=1):
        return ' ' * (indentation * 2) + '#' * self.level + ' ' + self.text + '\n'

    def get_content(self, indentation=0):
        return ' ' * (indentation * 2) + self.text


class Paragraph(TextElement):
    def __init__(self, content):
        self.content = content

    def render(self, indentation=2):
        return ' ' * (indentation * 2) + self.content + '\n'

    def get_content(self, indentation=0):
        return ''  # No content to return for paragraph


class Image(TextElement):
    def __init__(self, alt_text, url):
        self.alt_text = alt_text
        self.url = url

    def render(self, indentation=2):
        return ' ' * (indentation * 2) + f'![{self.alt_text}]({self.url})' + '\n'

    def get_content(self, indentation=0):
        return ''


class Link(TextElement):
    def __init__(self, text, url):
        self.text = text
        self.url = url

    def render(self, indentation=2):
        return ' ' * (indentation * 2) + f'[{self.text}]({self.url})' + '\n'

    def get_content(self, indentation=0):
        return ''
