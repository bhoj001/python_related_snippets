""""
Purpose: to create and view html files.
date: 2020/July/24th
link: https://programminghistorian.org/en/lessons/creating-and-viewing-html-files-with-python#lesson-goals
motivation: Let's do raw python, build already existing project with raw python.
"""

with open('helloworld.html', 'w+') as f:
    message = """\
    <html>
        <head></head>
        <body>
            <p>Bhoj Bahadur Karki</p>
        </body>
    </html>
    """

    f.write(message)



