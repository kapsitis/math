import requests
import csv
import os
import re

html_preamble = """<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=utf-8"/>
<link rel="stylesheet" type="text/css" href="../static/style.css"/>
<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>
  <!--[if lt IE 9]>
    <script src="//cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv-printshiv.min.js"></script>
  <![endif]-->
</head>

<body>
<h1>Skaitļu teorija: Prasmju analīze</h1>

<table border="0" cellspacing="2">
<tr style="font-size:120%">
<td style="background-color:#de6745;color:white;padding:2px 10px 2px 10px"><a style="color:white" href="../main/index.html">Uz sākumu</a></td>
<td style="background-color:#f1a72c;color:white;padding:2px 10px 2px 10px"><a style="color:white" href="../prob/index.html">Uzdevumi</a></td>
<td style="background-color:#40ce7c;color:white;padding:2px 10px 2px 10px"><b>Prasmes</b></td>
<td style="background-color:#4ca7dc;color:white;padding:2px 10px 2px 10px"><a style="color:white" href="../exam/index.html">Pārbaudes darbi</a></td>
<td style="background-color:#9e69af;color:white;padding:2px 10px 2px 10px"><a style="color:white" href="../downloads/index.html">Lejupielādes</a></td>
</tr>
</table>"""

PRE = '<span class="math inline">\('
POST = '\)</span>'

def get_label_seq(lst):
    the_concat = list()
    for i in range(0,len(lst)):
        int_item = int(lst[i])
        if int_item > 0:
            the_concat.append(lst[i])
    the_result = '.'.join(the_concat)
    the_result = the_result + '.'
    for j in range(len(the_result),9):
        the_result = the_result + '&nbsp;'
    return the_result
    
def escape_math(res):
    res = re.sub('<', '&lt;', res)
    res = re.sub('>', '&gt;', res)
    is_math = False
    
    if re.match('[^ ]+\^[^ ]+', res):
        is_math = True
    if re.match('[^ ]+(&lt;|&gt;)[^ ]+', res):
        is_math = True
    if re.match('[^ ]+_[^ ]+', res):
        is_math = True
    
    if is_math:
        res = '%s%s%s' % (PRE, res, POST)
    #res = re.sub('[^ ]+\^[^ ]+', '%s\g<0>%s' % (PRE,POST),res)
#    res = re.sub('\(a(\+|-)b\)\^n', '%s\g<0>%s' % (PRE,POST),res)
    #res = re.sub('[^ ]+&lt;[^ ]+','%s\g<0>%s' % (PRE,POST), res)
    #res = re.sub('a&lt;b','%s\g<0>%s' % (PRE,POST), res)
    #res = re.sub('b&lt;c','%s\g<0>%s' % (PRE,POST), res)
    return res 


def escape_math_seq(arg):
    words = arg.split()
    result = list()
    for word in words: 
        result.append(escape_math(word))
    return ' '.join(result)

def main(): 
    # Change current directory, if invoked directly
    the_dir = os.getcwd()    
    if the_dir.endswith('/src/math_py/analysis'):
        os.chdir("../../..")
    
    response = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=0&single=true&output=csv')
    assert response.status_code == 200, 'Wrong status code'
    response.encoding = 'utf-8'
    csv_lines = response.text.splitlines()
    tasks = csv.reader(csv_lines)
    with open('src/site/analysis/task-analysis.csv', 'w+') as csv_out:
        for csv_line in csv_lines:
            csv_out.write(csv_line)
            csv_out.write('\n')
    csv_out.close()
    with open('src/site/analysis/index.html', 'w+') as out:
        out.write(html_preamble + '\n\n')
        out.write('<table class="tasks">\n')
        out.write('<colgroup>')
        out.write('  <col class="aaa">')
        out.write('  <col class="bbb">')
        out.write('  <col class="ccc">')
        out.write('</colgroup><tbody>')
        out.write('<tr><th>Prasmes kods</th><th>Apraksts</th><th>Piemēri, t.sk kanoniskie</th></tr>\n')
        nrow = 0
        for row in tasks:
            rowclass = 'odd'
            if nrow % 2 == 0:
                rowclass = 'even' 
            if nrow > 0:
                labels = get_label_seq([row[0],row[1],row[2],row[3],row[4]])
                my_esc = escape_math_seq(row[6])
                out.write('<tr class="%s"><td><code>%s</code> %s</td><td>%s</td><td>Blah</td></tr>\n' % (rowclass, labels, row[5], my_esc))
            nrow = nrow + 1
        out.write('</tbody></table>\n\n</html>')
    out.close()

if __name__ == '__main__':
    main()

