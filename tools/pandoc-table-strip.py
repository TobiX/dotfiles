#!/usr/bin/env python3
# from https://gist.github.com/emcconville/56a5da54ce9ac7cfeced
# repaired for newer versions of pandoc
# cf. https://hackage.haskell.org/package/pandoc-types-1.22.2.1/docs/Text-Pandoc-Definition.html

from sys import stdin, stdout, stderr
import json

def flattenTable(content):
    embeddedElements = []
    if len(content) < 6:
        raise NotImplementedError('Sorry, your pandoc is too old')
    rows = []
    if content[3]:  # Headers
        rows.extend(content[3][1])
    if content[4]:  # Bodies
        for body in content[4]:
            rows.extend(body[2])
            rows.extend(body[3])
    if content[5]:  # Footer
        rows.extend(content[5][1])
    for row in rows:
        for cell in row[1]:
            for node in cell[4]:
                embeddedElements.append(node)
    return embeddedElements

def parse(node):
    if isinstance(node, dict):
        rdict = node.copy()
        for attr in node.keys():
            rdict[attr] = parse(rdict[attr])
        return rdict
    if isinstance(node, list):
        rarray = []
        for item in node:
            if isinstance(item, dict) and 't' in item and 'c' in item:
                if item['t'] == 'Table':
                    rarray.extend(parse(flattenTable(item['c'])))
                else:
                    rarray.append(parse(item))
            else:
                rarray.append(parse(item))
        return rarray
    return node



def main():
    jstr = stdin.read()
    tree = json.loads(jstr)
    tree = parse(tree)
    stdout.write(json.dumps(tree))

if __name__ == '__main__':
    main()
