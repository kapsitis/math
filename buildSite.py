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

resTypes = ['prob', 'tale']

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
    		'--mathjax="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"',
		'-V','theme=white'], cwd=workingDir)
        copyDirectory('%s/%s' % (ROOT,dd), 'target/%s/%s' % (resType,dd))
copyDirectory('src/site/reveal.js', 'target/reveal.js')


