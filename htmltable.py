#####creates a html table

arr1 = ['1','2','3']
arr2 = ['a','b','c']
arr3 = ['z','y','z']

def table(*args):
    zipped = list(zip(*args))
    html='<table>'
    for x in zipped:
        html=html+'<tr>'
        for y in x:
            html=html+(f"<td>{y}</td>")
        html = html + '</tr>'
    html = html + '</table>'
    return html

print(table(arr1,arr3,arr2))
