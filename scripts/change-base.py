#!/usr/bin/env python
import os, sys




def func(host):
    for root, dpaths, fpaths in os.walk('/data/dad/web-site/lesterproductions.github.com'):
        for fpath in fpaths:
            if '.html' in fpath:
                f = open(root + '/' + fpath)
                lines = f.readlines()
                f.close()
                for i in range(len(lines)):
                    if 'base' in lines[i]:
                        if '<!--' in lines[i]:
                            lines[i] = ''
                            continue
                        if host == 'local':
                            lines[i] = '        <base href="file:///data/dad/web-site/lesterproductions.github.com/"/>\n'
                        elif host == 'remote':
                            lines[i] = '        <base href="http://lesterproductions.net"/>\n'
                print root + '/' + fpath
                f = open(root + '/' + fpath, 'w')
                f.write(''.join(lines))
                f.close()
                print fpath, 'done'
                            
                            
                        
                
    
def usage():
    print
    print 'usage:'
    print '\t' + sys.argv[0] + '[local|remote]'
    print


if __name__ == '__main__':
    if not len(sys.argv) == 2:
        print usage()
        exit(1)
    else:
        func(sys.argv[1])




















