#!/usr/bin/env python
import os, sys




def func():    
    for root, dpaths, fpaths in os.walk('/data/dad/web-site/lesterproductions.github.com'):
        for fpath in fpaths:
            if '.html' in fpath:
                f = open(root + '/' + fpath)
                lines = f.readlines()
                f.close()
                for i in range(len(lines)):
                    if 'http-equiv' in lines[i]:
                        first = lines[i]
                        second = lines[i+1]
                        lines[i] = second
                        lines[i+1] = first
                        break
                print root + '/' + fpath
                f = open(root + '/' + fpath, 'w')
                f.write(''.join(lines))
                f.close()
                print fpath, 'done'
                            



if __name__ == '__main__':
    func()