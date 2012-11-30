#!/usr/bin/env python
import os, sys




def func():
    for root, dpaths, fpaths in os.walk('/data/dad/web-site/lesterproductions'):
        for fpath in fpaths:
            if '.html' in fpath:
                f = open(root + '/' + fpath)
                lines = f.readlines()
                f.close()
                for i in range(len(lines)):
                    if '<a' in lines[i]:
                        for j in range(len(lines[i])):
                            if lines[i][j] == '<' and lines[i][j+1] == 'a' and lines[i][j+2] == ' ' and lines[i][j+3] != 't':
                                fpart = ''.join(lines[i][:j+3])
                                lpart = ''.join(lines[i][j+3:])
                                npart = 'target=\"_self\"'
                                lines[i] = fpart + npart + ' ' + lpart
                                break
                print root + '/' + fpath
                f = open(root + '/' + fpath, 'w')
                f.write(''.join(lines))
                f.close()
                print fpath, 'done'
                            
                            
                            
                        
                
    



if __name__ == '__main__':
    func()




















