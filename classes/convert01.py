import markdown
import os

foot = '\n        </div>\n    </body>\n</html>'

for i in range (1, 10):
    print(str('%02d' % (i)) + 'BDL.md is input', end = '    ')
    markdown.markdownFromFile(
    input = '0' + str(i) + 'BDL.md',
    output = 'stage.html',
    encoding = 'utf8',
    )
    with open('stage.html', 'r') as original: data = original.read()
    with open('template.html', 'r') as template: head = template.read()
    with open('0' + str(i) + 'BDL.html', 'w') as modified: modified.write(head + data + foot)
    print('0' + str(i) + 'BDL.html' + ' made')

for i in range (10, 36):
    print(str('%02d' % (i)) + 'UIB.md is input', end='    ')
    markdown.markdownFromFile(
    input = str('%02d' % (i)) + 'UIB.md',
    output = 'stage.html',
    encoding = 'utf8',
    )
    with open('stage.html', 'r') as original: data = original.read()
    with open('template.html', 'r') as template: head = template.read()
    with open(str("%02d" % (i)) + 'UIB.html', 'w') as modified: modified.write(head + data + foot)
    print(str("%02d" % (i)) + 'UIB.html' + ' made')

os.remove('stage.html')
print('stage.html removed')