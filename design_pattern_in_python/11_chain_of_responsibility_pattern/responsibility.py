"""
author: Bhoj Bahadur Karki
Date: 2020-August-15th
Description: Chain of responsibility design pattern

The chain of responsibility pattern is used to achieve loose coupling in software where a
specified request from the client is passed through a chain of objects included in it. It helps in
building a chain of objects. The request enters from one end and moves from one object to another.

This pattern allows an object to send a command without knowing which object will handle the request.

How to implement the chain of responsibility pattern?
We will now see how to implement the chain of responsibility pattern.
"""

class ReportFormat(object):
    PDF = 0
    TEXT = 1


class Report(object):
    def __init__(self, format_):
        self.title = 'Monthly report'
        self.text = ['Things are going', 'really, really well.']
        self.format_ = format_


class Handler(object):
    def __init__(self):
        self.nextHandler = None

    def handle(self, request):
        self.nextHandler.handle(request)


class PDFHandler(Handler):

    def handle(self, request):
        if request.format_ == ReportFormat.PDF:
            self.output_report(request.title, request.text)
        else:
            super(PDFHandler, self).handle(request)

    def output_report(self, title, text):
        print('<html>')
        print(' <head>')
        print(' <title>%s</title>' % title)
        print(' </head>')
        print(' <body>')
        for line in text:
            print(' <p>%s</p>' % line)
        print(' </body>')
        print('</html>')


class TextHandler(Handler):

    def handle(self, request):
        if request.format_ == ReportFormat.TEXT:
            self.output_report(request.title, request.text)
        else:
            super(TextHandler, self).handle(request)

    def output_report(self, title, text):
        print(5 * '*' + title + 5 * '*')
        for line in text:
            print(line)


class ErrorHandler(Handler):
    def handle(self, request):
        print("Invalid request")


if __name__ == '__main__':
    report = Report(ReportFormat.TEXT)
    pdf_handler = PDFHandler()
    text_handler = TextHandler()

    pdf_handler.nextHandler = text_handler
    text_handler.nextHandler = ErrorHandler()
    pdf_handler.handle(report)