#!/usr/bin/env python3
# from https://gist.github.com/emcconville/56a5da54ce9ac7cfeced
# repaired for newer versions of pandoc
# cf. https://hackage.haskell.org/package/pandoc-types-1.22.2.1/docs/Text-Pandoc-Definition.html

from sys import stdin, stdout, stderr
import json

def extractTable(t, c):
    if t == 'Table':
        embeddedElements = []
        if len(c) < 6:
            raise NotImplementedError('Sorry, your pandoc is too old')
        rows = []
        if c[3]:  # Headers
            rows.extend(c[3][1])
        if c[4]:  # Bodies
            for body in c[4]:
                rows.extend(body[2])
                rows.extend(body[3])
        if c[5]:  # Footer
            rows.extend(c[5][1])
        for row in rows:
            for cell in row[1]:
                for node in cell[4]:
                    # Check if we have an embedded table
                    if 't' in node and node['t'] == 'Table':
                        embeddedElements.extend(extractTable(node['t'], node['c']))
                    else:
                        # Inject empty block to restore formatting inherited by table
                        block = {'t': 'Plain', 'c': [{'t': 'LineBreak', 'c': []}]}
                        embeddedElements.append(block)
                        embeddedElements.append(node)
        return embeddedElements
    return None

def parse(node, func):
    if isinstance(node, dict):
        rdict = node.copy()
        for attr in node.keys():
            rdict[attr] = parse(rdict[attr], func)
        return rdict
    elif isinstance(node, list):
        rarray = []
        for item in node:
            if isinstance(item, dict) and 't' in item and 'c' in item:
                res = func(item['t'], item['c'])
                if isinstance(res, list):
                    for rt in res:
                        rarray.append(parse(rt, func))
                else:
                    rarray.append(parse(item, func))
            else:
                rarray.append(parse(item, func))
        return rarray
    else:
        return node



def main():
    jstr = stdin.read()
    tree = json.loads(jstr)
    tree = parse(tree, extractTable)
    stdout.write(json.dumps(tree))

if __name__ == '__main__':
    main()
