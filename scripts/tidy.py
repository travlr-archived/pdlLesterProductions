#!/usr/bin/env python
from tidylib import tidy_document
import os



def func():    
    for root, dpaths, fpaths in os.walk('/data/dad/web-site/lesterproductions.github.com'):
        for fpath in fpaths:
            if 'trixx/website' in root:
                continue
            if not 'mckerrows' in root:
                continue
            if '.html' in fpath:
                f = open(root + '/' + fpath)
                docstring = f.read()
                f.close()
                opts = {'indent-spaces' : 4, 'tidy-mark' : 1, 'alt-text' : 'Image not available',
                        'wrap' : 150, 'wrap-attributes' : False, 'sort-attributes' : 'alpha',
                        'vertical-space' : True, 'markup' : True}
                document, errors = tidy_document(docstring, options=opts)

                #print root + '/' + fpath
                f = open(root + '/' + fpath, 'w')
                f.write(document)
                f.close()
                print fpath
                #if errors:
                    #print
                    #print fpath
                    #print errors


if __name__ == '__main__':
    func()
