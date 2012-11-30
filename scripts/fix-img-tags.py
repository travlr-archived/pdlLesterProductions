#!/usr/bin/env python
import os, sys




def func():    
    for root, dpaths, fpaths in os.walk('/data/dad/web-site/lesterproductions.github.com'):
        for fpath in fpaths:
            if '.html' in fpath:
                f = open(root + '/' + fpath)
                lines = f.readlines()
                f.close()
                #lines.insert(0, '<?xml version="1.0" encoding="UTF-8"?>'_
                nlines = len(lines)
                print 'nlines:', nlines,' -', fpath
                for i in range(nlines):
                    #if 'alt=\"Image not available\">' in lines[i]:
                        #print
                        #print lines[i]
                        #print '---'
                        #lines[i] = lines[i].replace('alt="Image not available"', '')
                        #print lines[i]
                    print 'i:', i
                    try:
                        if '<title>' in lines[i]:
                            lines[i] = '<title>Lester Productions | Eddy Lester</title>\n'
                        elif 'Lester Productions | Eddy Lester' in lines[i]:
                            lines.pop(i)
                        elif '</title>' in lines[i]:
                            lines.pop(i)
                    except IndexError(i):
                        pass
                #print root + '/' + fpath
                f = open(root + '/' + fpath, 'w')
                f.write(''.join(lines))
                f.close()
                #print fpath, 'done'
                            



if __name__ == '__main__':
    func()