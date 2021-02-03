import markdown
import os

foot = '\n        </div>\n    </body>\n</html>'

for i in range (9, 15):
    markdown.markdownFromFile(
    input= str("%02d" % (i)) + 'UIB.md',
    output= 'stage.html',
    encoding='utf8',
    )
    with open('stage.html', 'r') as original: data = original.read()
    with open('template.html', 'r') as template: head = template.read()
    with open(str("%02d" % (i)) + 'UIB.html', "w") as modified: modified.write(head + data + foot)

os.remove("stage.html") 