import os
import shutil
import subprocess


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



def main(): 
    rmDirectory('target')

    ## Which directories contain reveal.js slides
    resTypes = ['prob', 'tale', 'miscellaneous']

    for resType in resTypes:
        ROOT = 'src/site/%s' % resType
        themePath = '%s/themes/ddgatve' % ROOT
        subDirectories = set(next(os.walk(ROOT))[1]).difference(set(['themes']))
        for dd in subDirectories:
            print('Processing with pandoc/reveal, dir=%s' % dd)
            srcPath = '%s/%s/content.md' % (ROOT,dd)
            destPath = '%s/%s/content.html' % (ROOT,dd)
            workingDir = '%s/%s' % (ROOT,dd)
            # subprocess.call(['landslide','--relative',srcPath,'-t',themePath,'-d',destPath])
       	    subprocess.call(['pandoc','-t','revealjs','-s',
		'-o','content.html','content.md','--slide-level=2',
		'-V','revealjs-url=../../reveal.js','--metadata', 'pagetitle="Uzdevumi"',
    		'--mathjax=https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML',
		'-V','theme=white'], cwd=workingDir)
            copyDirectory('%s/%s' % (ROOT,dd), 'target/%s/%s' % (resType,dd))
        shutil.copy2('src/site/%s/index.html' % resType, 'target/%s/' % resType)
    copyDirectory('src/site/reveal.js', 'target/reveal.js')
    copyDirectory('src/site/analysis', 'target/analysis')
    copyDirectory('src/site/downloads', 'target/downloads')
    copyDirectory('src/site/exam', 'target/exam')
    copyDirectory('src/site/main', 'target/main')
    ## Compile all TEX files under "static"
    ROOT = 'src/site/static'
    tex_files = os.listdir(ROOT)
    print('xxxx %s' % tex_files)
    for ff in tex_files:
        if ff.endswith('.tex'):
            print('Currently processing %s' % ff)
            subprocess.call(['xelatex',ff], cwd=ROOT)
    copyDirectory(ROOT, 'target/static')
    shutil.copy2('src/site/index.html', 'target/')



if __name__ == '__main__':
    main()



