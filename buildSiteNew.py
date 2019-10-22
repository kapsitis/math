import os
import shutil
import subprocess
import glob

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
            fftexmod = os.path.getmtime('%s/%s' % (SRC,ff))
            ffpdf = ff.replace('.tex','.pdf')
            if os.path.isfile('%s/%s' % (SRC,ffpdf)):
                ffpdfmod = os.path.getmtime('%s/%s' % (SRC,ffpdf))
            else: 
                ffpdfmod = -1
            if fftexmod > ffpdfmod:
                print('Processing TEX %s' % ff)
                subprocess.call(['xelatex',ff], cwd=SRC)
            else:
                print('Skipping TEX %s' % ff)
    for filename in glob.glob(os.path.join(SRC, '*.pdf')):
        shutil.copy(filename, DEST)
    for filename in glob.glob(os.path.join(SRC, '*.docx')):
        shutil.copy(filename, DEST)
    #copyDirectory('%s/Pictures' % SRC,'%s/Pictures' % DEST)
    skip_directories = ['source-material','static','analysis']
    subDirectories = set(next(os.walk(SRC))[1]).difference(set(skip_directories))
    for dd in subDirectories:
        if os.path.exists('%s/%s' % (DEST,dd)):
            rmDirectory('%s/%s' % (DEST,dd))
        copyDirectory('%s/%s' % (SRC,dd),'%s/%s' % (DEST,dd))


def main(): 
#    sync_all.main()
    resTypes = ['problembase', 'numtheory', 'algorithms', 'visualizations','rbs']
    skip_directories = ['source-material','static','analysis']

    DEST_ROOT = '../../workspace-new/linen-tracer-682'

    for resType in resTypes:
        rmDirectory('%s/%s-tales' % (DEST_ROOT,resType))
        SRC_ROOT = 'src/site/%s' % resType
        subDirectories = set(next(os.walk(SRC_ROOT))[1]).difference(set(skip_directories))
        for dd in subDirectories:
            print('Processing with pandoc/reveal, dir=%s' % dd)
            workingDir = '%s/%s' % (SRC_ROOT,dd)
       	    subprocess.call(['pandoc','-t','revealjs','-s',
		'-o','content.html','content.md','--slide-level=2',
		'-V','revealjs-url=../../reveal.js','--metadata', 'pagetitle="Uzdevumi"',
    		'--mathjax=https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML',
		'-V','theme=white'], cwd=workingDir)
            copyDirectory('%s/%s' % (SRC_ROOT,dd), '%s/%s-tales/%s' % (DEST_ROOT,resType,dd))

    compileTale('src/emils', 'numtheory-recurrence-relation', '%s/numtheory-tales' % DEST_ROOT, 'Periodiskas virknes')

    rmDirectory('%s/reveal.js' % DEST_ROOT)
    copyDirectory('src/site/reveal.js', '%s/reveal.js' % DEST_ROOT)

    build_static('src/site/visualizations/static', '%s/visualizations-bin' % DEST_ROOT)
    build_static('src/site/numtheory/static', '%s/numtheory-bin' % DEST_ROOT)
    build_static('src/site/algorithms/static', '%s/algorithms-bin' % DEST_ROOT)
    build_static('src/site/problembase/static', '%s/problembase-bin' % DEST_ROOT)
    build_static('src/site/rbs/static', '%s/rbs-bin' % DEST_ROOT)
    build_static('src/site/problembase/static/collections', '%s/problembase-bin/collections' % DEST_ROOT)

    
if __name__ == '__main__':
    main()



