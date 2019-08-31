import os
import shutil
import subprocess
import glob

#import sys, os
#sys.path.append(os.path.join(os.path.dirname(__file__), 'src', 'math_py', 'analysis'))
#import sync_tasks


import sys
sys.path.insert(0, 'src/math_py')
from json_data import sync_all



def copyDirectory(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

def rmDirectory(src):
    try: 
        shutil.rmtree(src)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not removed. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not removed. Error: %s' % e)

def compileTale(root,subdir,destdir,title):
    copyDirectory('%s/%s' % (root,subdir), '%s/%s' % (destdir,subdir))
    workingDir = '%s/%s' % (destdir,subdir)
    subprocess.call(['pandoc','-t','revealjs','-s',
	'-o','content.html','content.md','--slide-level=2',
	'-V','revealjs-url=../../reveal.js','--metadata', 'pagetitle="%s"' % title,
    	'--mathjax=https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML',
	'-V','theme=white'], cwd=workingDir)    


def build_static(SRC,DEST):
    rmDirectory(DEST)
    os.mkdir(DEST)

    tex_files = os.listdir(SRC)
    print('TeX files under %s are %s' % (SRC,tex_files))
    for ff in tex_files:
        if ff.endswith('.tex'):
            print('Currently processing %s' % ff)
            subprocess.call(['xelatex',ff], cwd=SRC)
    for filename in glob.glob(os.path.join(SRC, '*.pdf')):
        shutil.copy(filename, DEST)
    for filename in glob.glob(os.path.join(SRC, '*.docx')):
        shutil.copy(filename, DEST)



def main(): 
    rmDirectory('target')

    sync_all.main()

    ## Which directories contain reveal.js slides
    resTypes = ['prob', 'exam', 'tale', 'miscellaneous']
    outDirectories = {
        'prob':'files-prob',
        'exam':'files-exam',
        'tale':'files-tale',
        'miscellaneous':'files-misc'
    }

    for resType in resTypes:
        ROOT = 'src/site/%s' % resType
       	OUT_ROOT = '../../workspace-new/linen-tracer-682/'
        themePath = '%s/themes/ddgatve' % ROOT
        subDirectories = set(next(os.walk(ROOT))[1]).difference(set(['themes']))
        for dd in subDirectories:
            print('Processing with pandoc/reveal, dir=%s' % dd)
            #srcPath = '%s/%s/content.md' % (ROOT,dd)
            #destPath = '%s/%s/content.html' % (ROOT,dd)
            workingDir = '%s/%s' % (ROOT,dd)
            # subprocess.call(['landslide','--relative',srcPath,'-t',themePath,'-d',destPath])
       	    subprocess.call(['pandoc','-t','revealjs','-s',
		'-o','content.html','content.md','--slide-level=2',
		'-V','revealjs-url=../../reveal.js','--metadata', 'pagetitle="Uzdevumi"',
    		'--mathjax=https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML',
		'-V','theme=white'], cwd=workingDir)
            copyDirectory('%s/%s' % (ROOT,dd), 'target/%s/%s' % (resType,dd))
        #shutil.copy2('src/site/%s/index.html' % resType, 'target/%s/' % resType)
    ## Emila prezentacijas START
    compileTale('src/emils', 'numtheory-recurrence-relation', 'target/tale', 'Periodiskas virknes')
    compileTale('src/site/miscellaneous', 'r-language-intro', 'target/tale', 'R ievads')

    compileTale('src/site/algorithms', 'tale-lossless-part1', 'target/algorithms-tales', 'Bezzudumu saspiešana - 1')

#    copyDirectory('src/emils/numtheory-recurrence-relation', 'target/tale/numtheory-recurrence-relation')
#    workingDir = 'target/tale/numtheory-recurrence-relation'
#    subprocess.call(['pandoc','-t','revealjs','-s',
#	'-o','content.html','content.md','--slide-level=2',
#	'-V','revealjs-url=../../reveal.js','--metadata', 'pagetitle="Periodiskas virknes"',
#    	'--mathjax=https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML',
#	'-V','theme=white'], cwd=workingDir)    
    ## Emila prezentacijas END
#    copyDirectory('src/site/miscellaneous/r-language-intro', 'target/tale/r-language-intro')
#    workingDir = 'target/tale/r-language-intro'
#    subprocess.call(['pandoc','-t','revealjs','-s',
#	'-o','content.html','content.md','--slide-level=2',
#	'-V','revealjs-url=../../reveal.js','--metadata', 'pagetitle="R ievads"',
#    	'--mathjax=https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML',
#	'-V','theme=white'], cwd=workingDir) 


    for resType in resTypes:
        rmDirectory('%s/%s' % (OUT_ROOT,outDirectories[resType]))
        copyDirectory('target/%s' % resType, '%s/%s' % (OUT_ROOT,outDirectories[resType]))
    rmDirectory('%s/algorithms-tales' % OUT_ROOT)
    copyDirectory('target/algorithms-tales', '%s/algorithms-tales' % OUT_ROOT)



    copyDirectory('src/site/reveal.js', 'target/reveal.js')
    copyDirectory('src/site/tasks', 'target/tasks')
    copyDirectory('src/site/downloads', 'target/downloads')
    #copyDirectory('src/site/exam', 'target/exam')
    copyDirectory('src/site/main', 'target/main')

    DEST_ROOT = '../../workspace-new/linen-tracer-682'
    #build_static('src/site/static', '%s/static' % DEST_ROOT)
    build_static('src/site/numtheory/static', '%s/numtheory-bin' % DEST_ROOT)
    build_static('src/site/algorithms/static', '%s/algorithms-bin' % DEST_ROOT)
    

#def my_main():
#    DEST_ROOT = '../../workspace-new/linen-tracer-682'
#    build_static('src/site/algorithms/static', '%s/algorithms-bin' % DEST_ROOT)
#    build_static('src/site/numtheory/static', '%s/numtheory-bin' % DEST_ROOT)


if __name__ == '__main__':
    my_main()



