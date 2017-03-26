import urllib.request
from html.parser import HTMLParser


class Lou1110Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.dept_ids = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, val in attrs:
                if attr == 'href':
                    self.dept_ids.append(val)



# class LouParser(HTMLParser):
#     def __init__(self):
#         self.stack = []
#         super(HTMLParser, self).__init__()
#
#     def handle_starttag(self, tag, attrs):
#         print("Start tag:", tag)
#         for attr in attrs:
#             print("     attr:", attr)
#
#     def handle_data(self, data):
#         print("Data     :", data)
#
#
# def lou_mine():
#     with urllib.request.urlopen('http://rabi.phys.virginia.edu/mySIS/CC2/CS.html') as response:
#         html = response.read()
#     parser = LouParser()
#     parser.feed(html)


if __name__ == '__main__':
    lou1110_dept_ids()
