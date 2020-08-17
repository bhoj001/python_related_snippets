
""""
Purpose: to create and view html files and open in browser automatically.
date: 2020/July/24th
link: https://programminghistorian.org/en/lessons/creating-and-viewing-html-files-with-python#lesson-goals
motivation: Let's do raw python, build already existing project with raw python.
"""
import webbrowser
import os

file_name = "helloworld2.html"
with open(file_name, 'w+') as f:
    message = """\
    <html>
        <head></head>
        <body>
            <p>Bhoj Bahadur Karki</p>
        </body>
    </html>
    """

    f.write(message)






# file name
current_directory = os.path.dirname(os.path.abspath(__file__))
# prints: current dir= D:\2020\python_job_prepartion\python_in_web but we need D:/2020/... forward slash is
# required so we replace \ with / in the path
path_with_forward_slash = current_directory.replace("\\", "/") # replace \ with /
# print("current dir=",current_directory)
# print("current dir=",x)
print("getcwd=",os.getcwd()) # this also get the same this as current_directory
# file_path ="file:///D:/2020/python_job_prepartion/python_in_web/{0}".format(file_name)
file_path ="file:///{0}/{1}".format(path_with_forward_slash,file_name)

webbrowser.open_new_tab(file_path)