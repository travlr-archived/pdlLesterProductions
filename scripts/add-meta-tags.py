#!/usr/bin/env python
import os, sys




def func():
    insert_list = []
    insert_list.append("""    <meta http-equiv="content-type" content="text/html; charset=utf-8" />\n""")
    insert_list.append( """    <meta name="robots" content="index, follow" />\n""")
    insert_list.append("""    <meta name="keywords" content="eddy lester, talent, management, magic, magician, corporate event, 
    hypnotist, event planning, speaker, speakers bureau, agency, hypnosis show, convention hypnosis, 
    trade show entertainment, 
    entertainment, fundraising, fundraiser, funny, fun, humor, hilarious, laugh, variety, celebrity, 
    star, performer, videos, pictures, tapes, comedian, fairs, Colleges, prom, graduation, grad nights, nites, 
    high schools, party, Cruises, universities, orientation, picnics, casino, casinos," />\n""")
    insert_list.append("""    <meta name="description" content="Top talent management and production/event 
                            services since 1970. Lester Productions provides acts and shows to 
                            theaters, colleges, casinos, corporate or charity events, etc." />\n""")
    
    for root, dpaths, fpaths in os.walk('/data/dad/web-site/lesterproductions.github.com'):
        for fpath in fpaths:
            if '.html' in fpath:
                f = open(root + '/' + fpath)
                lines = f.readlines()
                f.close()
                for i in range(len(lines)):
                    if '<head>' in lines[i]:
                        for j in range(len(insert_list)):
                            i += 1
                            lines.insert(i+j, insert_list[j])
                        break
                print root + '/' + fpath
                f = open(root + '/' + fpath, 'w')
                f.write(''.join(lines))
                f.close()
                print fpath, 'done'
                            



if __name__ == '__main__':
    func()