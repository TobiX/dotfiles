#!/usr/bin/env python3
# from https://gist.github.com/emcconville/56a5da54ce9ac7cfeced

from sys import stdin, stdout, stderr
import json


def extractTable(t,c):
    if t == 'Table':
        embeddedElements = []
        # We want to preserver the top-down / left-right order
        for row in c[4]:
            for column in row:
                for el in column:
                    # Check if we have an embedded table
                    if 't' in el and el['t'] == 'Table':
                        embeddedElements.extend(extractTable(el['t'],el['c']))
                    else:
                        # Inject empty block to restore formatting inherited by table
                        block = {'t': 'Plain', 'c': [{'t': 'LineBreak', 'c': []}]}
                        embeddedElements.append(block)
                        embeddedElements.append(el)
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
