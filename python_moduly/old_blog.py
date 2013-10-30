'''old_blog.zpracuj_odkazy()
parses old 90edges blog and creates redirectional links for GitHub
'''

from bs4 import BeautifulSoup
import vfp
import os

base = 'C:\\Users\\Lenka\\Desktop\\Mirek\\GitHub\\90edg_old_blog'

filename = os.path.join(base, 'src', '90Edges Universe.htm') # source html
sablona = os.path.join(base, 'sablona', 'sablona.html') # template for out-files 
out_dir = os.path.join(base, 'out')

def zpracuj_odkazy():
    '''main function - run this
    '''
    html = vfp.filetostr(filename).decode('utf8')   # str[utf8] -> unicode
    parse(html, odkaz1)

def parse(html, callback):
    sp = BeautifulSoup(html)
    for odkaz in sp('a'):
            if odkaz.get('class') and 'timestamp' in odkaz['class']:
                    callback(odkaz['href'])

def odkaz1(odkaz):
    parts = odkaz.rsplit('/', 2)
    obsah = vfp.filetostr(sablona) % dict(suburl=parts[1]+'/'+parts[2])
    vfp.strtofile(obsah, os.path.join(out_dir, parts[1], parts[2]+'.html'))

if __name__=='__main__':
    zpracuj_odkazy()