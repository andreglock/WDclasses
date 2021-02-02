import markdown

foot = '\n        </div>\n    </body>\n</html>'

for i in range (6, 9):
    markdown.markdownFromFile(
    input='0' + str(i) + 'BDL.md',
    output= 'stage.html',
    encoding='utf8',
    )
    with open('stage.html', 'r') as original: data = original.read()
    with open('template.html', 'r') as template: head = template.read()
    with open('0' + str(i - 1) + 'BDL.html', "w") as modified: modified.write(head + data + foot)