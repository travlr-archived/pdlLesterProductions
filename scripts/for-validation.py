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
                for i in range(len(lines)):
                    
                    if '<html>' in lines[i] and not 'xmlns' in lines[i]:
                        lines[i] = '<html xmlns="http://www.w3.org/1999/xhtml">'
                        continue
                    elif '"/>' in lines[i]:
                        lines[i].replace('"/>', '" />')
                    elif '<br>' in lines[i] and not '</br>' in lines[i] and not '</br>' in lines[i+1]:
                        lines[i].replace('<br>', '<br />')
                        
                    elif '<hr>' in lines[i] and not '</hr>' in lines[i] and not '</hr>' in lines[i+1]:
                        lines[i].replace('<hr>', '<hr />')
                        
                    if '<u>' in lines[i] or '</u>' in lines[i]:
                        print
                        print '#' * 40
                        slist = list(lines[i])
                        
                        
                        for j in range(nchars):
                            nchars = len(slist)
                            if nchars - j < 3:
                                break
                            if slist[j] == '<' and slist[j+1] == 'u' and slist[j+2] == '>':
                                slist.pop(j+2)
                                slist.pop(j+1)
                                slist.pop(j)
                                print 'Removed <u> from line:', i, 'of:', fpath
                        nchars = len(slist)
                        for j in range(nchars):
                            nchars = len(slist)
                            if nchars - j <4:
                                break
                            if slist[j] == '<' and slist[j+1] == '/' and slist[j+2] == 'u' and slist[j+3] == '>':
                                slist.pop(j+3)
                                slist.pop(j+2)
                                slist.pop(j+1)
                                slist.pop(j)
                                print 'Removed \'</u>\' from line:', i, 'of:', fpath
                        lines[i] = ''.join(slist)
                        print '#' * 40
                        print
                    if '<img' in lines[i]:
                        slist = list(lines[i])
                        nchars = len(slist)
                        img_tag = False
                        for j in range(nchars):
                            if not img_tag and slist[j] == '<' and slist[j+1] == 'i' and slist[j+2] == 'm' and slist[j+3] == 'g':
                                img_tag = True
                            if img_tag:
                                if slist[j] == '>':
                                    slist.pop()
                                    nstr = 'alt=\"Image not available\">'
                                    nstrlist = list(nstr)
                                    slist.extend(nstrlist)
                        lines[i] = ''.join(slist)

                    if '&nbsp' in lines[i]:
                        slist = list(lines[i])
                        nchars = len(slist)
                        for j in range(nchars):
                            if slist[j] == '&' and slist[j+1] == 'n' and slist[j+2] == 'b' and slist[j+3] == 's' and slist[j+4] == 'p' and slist[j+5] != ';':
                                slist.insert(j+5, ';')
                        lines[i] = ''.join(slist)
                    
                    if 'target="_self"' in lines[i]:
                        lines[i] = lines[i].replace(' target="_self"','')
                            
                print root + '/' + fpath
                f = open(root + '/' + fpath, 'w')
                f.write(''.join(lines))
                f.close()
                print fpath, 'done'
                            



if __name__ == '__main__':
    func()