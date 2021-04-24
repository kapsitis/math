# -*- coding: utf-8 -*-

import os
import shutil
import subprocess
import glob

import csv
import io
import json
import copy
import re
import sys


import sys
sys.path.insert(0, 'src/math_py')
# https://stackoverflow.com/questions/21259070/struggling-to-append-a-relative-path-to-my-sys-path
# https://stackoverflow.com/questions/38012431/how-to-execute-cmd-exe-with-arguments-in-python
#sys.path.append(os.path.join(sys.path[0],'src','math_py'))
from json_data import sync_all
from json_data import make_tasklist_json
#from json_data import data_structures_cpp_grading
from json_data import data_structures_odt_eater

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


def build_coq(srcDir,destDir):
    #vList = ['mybaby.v', 'classical-logic.v']
    v_files = os.listdir(srcDir)
    rmDirectory(destDir)
    os.mkdir(destDir)
    destDirAbsolute = destDir.replace('../../workspace/linen-tracer-682/', 'c:/Users/kalvis.apsitis/workspace/linen-tracer-682/')
    for vff in v_files:
        if vff.endswith('.v'):
            print('Build Coq {}/{} inside {}'.format(srcDir,vff,destDir))
            #subprocess.call(['coqdoc','-d',destDir, vff], cwd=srcDir)
            subprocess.call(['c:/Coq/bin/coqdoc.exe','-d',destDirAbsolute, vff], cwd=srcDir)
    for filename in glob.glob(os.path.join(srcDir, '*.png')):
        shutil.copy(filename, destDir)
    # It is important to copy V files (since ORTUS breaks plaintext)
    for filename in glob.glob(os.path.join(srcDir, '*.v')):
        shutil.copy(filename, destDir)


def build_slides(SRC,DEST):
    rmDirectory(DEST)
    os.mkdir(DEST)
    pptx_files = os.listdir(SRC)
    for ff in pptx_files:
        if ff.endswith('.pptx'):
            shutil.copy('{}/{}'.format(SRC,ff), DEST)



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
            #elif ff.endswith('discrete-math-all-exam-papers.tex'):
            #    print('Processing TEX %s' % ff)
            #    subprocess.call(['xelatex',ff], cwd=SRC)
            else:
                print('Skipping TEX %s' % ff)
    for filename in glob.glob(os.path.join(SRC, '*.pdf')):
        shutil.copy(filename, DEST)
    for filename in glob.glob(os.path.join(SRC, '*.docx')):
        shutil.copy(filename, DEST)
    for filename in glob.glob(os.path.join(SRC, '*.doc')):
        shutil.copy(filename, DEST)
    for filename in glob.glob(os.path.join(SRC, '*.zip')):
        shutil.copy(filename, DEST)
    #copyDirectory('%s/Pictures' % SRC,'%s/Pictures' % DEST)
    skip_directories = ['source-material','static','analysis']
    subDirectories = set(next(os.walk(SRC))[1]).difference(set(skip_directories))
    for dd in subDirectories:
        if os.path.exists('%s/%s' % (DEST,dd)):
            rmDirectory('%s/%s' % (DEST,dd))
        copyDirectory('%s/%s' % (SRC,dd),'%s/%s' % (DEST,dd))


def copy_pdf_only(SRC,DEST):
    for filename in glob.glob(os.path.join(SRC, '*.pdf')):
        shutil.copy(filename, DEST)
    


####################################
## C++ grades only
####################################
def get_csv_local(input_file):
    ROOT = 'c:/Users/kalvis.apsitis/workspace/ddgatve-problems/data-structures/'
    csv_lines = list()
    path = '{}/{}'.format(ROOT,input_file)
    with open(path, mode='r', encoding='utf-8') as csv_in:
        for csv_line in csv_in:
            csv_lines.append(csv_line)
        #csv_lines = csv_in.splitlines()
    result = csv.reader(csv_lines)
    return result




####################################
## These are C++ grades only
####################################
def mainmain(input_file):
    #convert_file()    
    grades = get_csv_local(input_file)    
    grade_list = []
    row_count = 0
    
    all_items = {} 
    for grade in grades:
        row_count += 1
        if row_count == 1:
            continue
        
        studId = grade[4].strip()
        gradeList = list()
        total = 0
        for i in range(5,12):
            g = grade[i].strip()
            gradeList.append(g)
            total += int(g)                    
        strTotal = '{}'.format(total)
        note = grade[12].strip()
        grade_list.append({'studID':studId, 'grades':gradeList, 'total': strTotal, 'notes':note})
        all_items[studId] = {'studID':studId, 'grades':gradeList, 'total': strTotal, 'notes':note}
        
    
    allIDs = all_items.keys()
    allIDsSorted = sorted(allIDs)
    grade_list = []
    for idid in allIDsSorted:
        grade_list.append(all_items[idid])
    return grade_list


####################################
## These are C++ grades only
####################################
def publish_grades():
    ROOT = 'c:/Users/kalvis.apsitis/workspace/ddgatve-problems/data-structures/'
    ODS_FILE = 'students-2020.ods' 
    CSV_FILE = 'data-structures-ex01.csv'
    GRADES_FILE = 'data_structures_grading.json'
    WEBROOT = 'c:/Users/kalvis.apsitis/workspace/linen-tracer-682'


    lines = data_structures_odt_eater.getLines()
    jsonOfLists = data_structures_odt_eater.getJsonOfLists(lines)    
    input_files = ['data-structures-ex01.csv','data-structures-ex02.csv']
    for ii in range(0,len(input_files)):
        grade_list = mainmain(input_files[ii])
        jsonOfLists[ii]['students'] = grade_list
    
    
    mod_fname = '{}/data/{}'.format(WEBROOT,GRADES_FILE)
    with io.open(mod_fname, 'w', encoding='utf8') as mod_file:
        json.dump(jsonOfLists, mod_file, ensure_ascii=False, sort_keys=True, indent=4)
                           



def main(): 
    ###############
    ## TODO: This sync_all.main was disabled; no idea what was wrong
    ########################
    # sync_all.main()
#    resTypes = ['problembase', 'numtheory', 'visualizations','rbs', 'discrete'] 
    make_tasklist_json.main()
    publish_grades()

    resTypes = ['algorithms','rbs','numtheory'] 
    skip_directories = ['source-material','static','questionbase','analysis', 'coq-inductive', 'coq-numbertheory','coq-firstorder', 'coq-predicates', 'coq-propositional', 'coq-sets']


    if os.name=='nt':
        DEST_ROOT = '../../workspace/linen-tracer-682'
        DEST_ABSOLUTE = DEST_ROOT
    else:
        DEST_ROOT = '../../workspace-new/linen-tracer-682'
        DEST_ABSOLUTE = '/home/kalvis/workspace-new/linen-tracer-682'

    DISCRETE_SRC_ROOT = 'c:/Users/kalvis.apsitis/workspace/rbs-discretestructures'
    copy_pdf_only('{}/homework'.format(DISCRETE_SRC_ROOT), '{}/discrete2021-bin'.format(DEST_ABSOLUTE))
    copy_pdf_only('{}/worksheets'.format(DISCRETE_SRC_ROOT), '{}/discrete2021-bin'.format(DEST_ABSOLUTE))
    copy_pdf_only('{}/midterm'.format(DISCRETE_SRC_ROOT), '{}/discrete2021-bin'.format(DEST_ABSOLUTE))
    copy_pdf_only('{}/final'.format(DISCRETE_SRC_ROOT), '{}/discrete2021-bin'.format(DEST_ABSOLUTE))

    for resType in resTypes:
        print('########## Removing dir {}/{}-tales'.format(DEST_ROOT,resType))
        rmDirectory('%s/%s-tales' % (DEST_ROOT,resType))
        SRC_ROOT = 'src/site/%s/slides' % resType
        subDirectories = set(next(os.walk(SRC_ROOT))[1]).difference(set(skip_directories))
        for dd in subDirectories:
            print('##### Copying {}/{} to {}/{}-tales/{}'.format(SRC_ROOT,dd,DEST_ROOT,resType,dd))
            copyDirectory('%s/%s' % (SRC_ROOT,dd), '%s/%s-tales/%s' % (DEST_ROOT,resType,dd))

        rmDirectory('%s/%s-exams' % (DEST_ROOT,resType))
        SRC_ROOT = 'src/site/%s/exams' % resType
        subDirectories = set(next(os.walk(SRC_ROOT))[1]).difference(set(skip_directories))
        for dd in subDirectories:
            print('##### Copying {}/{} to {}/{}-exams/{}'.format(SRC_ROOT,dd,DEST_ROOT,resType,dd))
            copyDirectory('%s/%s' % (SRC_ROOT,dd), '%s/%s-exams/%s' % (DEST_ROOT,resType,dd))
    
    copy_pdf_only('c:/Users/kalvis.apsitis/workspace/math/src/site/numtheory/exams'.format(DISCRETE_SRC_ROOT), '{}/numtheory-exams'.format(DEST_ABSOLUTE))


            
#        for dd in subDirectories:
#            print('Processing with pandoc/reveal, dir=%s' % dd)
#            workingDir = '%s/%s' % (SRC_ROOT,dd)
#       	    subprocess.call(['pandoc','-t','revealjs','-s',
#		'-o','content.html','content.md','--slide-level=2',
#		'-V','revealjs-url=../../reveal.js','--metadata', 'pagetitle="Uzdevumi"',
#    		'--mathjax=https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML',
#		'-V','theme=white'], cwd=workingDir)
#           copyDirectory('%s/%s' % (SRC_ROOT,dd), '%s/%s-tales/%s' % (DEST_ROOT,resType,dd))

#    compileTale('src/emils', 'numtheory-recurrence-relation', '%s/numtheory-tales' % DEST_ROOT, 'Periodiskas virknes')

    rmDirectory('%s/reveal.js' % DEST_ROOT)
    rmDirectory('%s/reveal.js.40' % DEST_ROOT)
    
    copyDirectory('src/site/reveal.js', '%s/reveal.js' % DEST_ROOT)
    copyDirectory('src/site/reveal.js.40', '%s/reveal.js.40' % DEST_ROOT)    
    #build_slides('src/site/data-structures/slides', '%s/data-structures-tales' % DEST_ROOT)

#    build_static('src/site/visualizations/static', '%s/visualizations-bin' % DEST_ROOT)
#    build_static('src/site/numtheory/static', '%s/numtheory-bin' % DEST_ROOT)
    build_static('src/site/algorithms/static', '%s/algorithms-bin' % DEST_ROOT)
    build_static('src/site/numtheory/static', '%s/numtheory-bin' % DEST_ROOT)
    build_static('src/site/numtheory/exams', '%s/numtheory-exams' % DEST_ROOT)
    #fall2020-homeworks
#    build_static('src/site/problembase/static', '%s/problembase-bin' % DEST_ROOT)
#    build_static('src/site/rbs/static', '%s/rbs-bin' % DEST_ROOT)
    build_static('src/site/discrete/static', '%s/discrete-bin' % DEST_ROOT)
    build_static('src/site/discrete/static/homeworks', '%s/discrete-bin/homeworks' % DEST_ROOT)
    build_static('src/site/discrete/questionbase', '%s/discrete-bin/questionbase' % DEST_ROOT)
    build_static('src/site/data-structures/assignments', '%s/data-structures-assignments/' % DEST_ROOT)
    build_static('src/site/data-structures/static', '%s/data-structures-bin/' % DEST_ROOT)
    build_coq('src/site/discrete/coq-competitions', '%s/discrete-bin/coq-competitions' % DEST_ABSOLUTE)
    build_coq('src/site/discrete/coq-inductive', '%s/discrete-bin/coq-inductive' % DEST_ABSOLUTE)
    build_coq('src/site/discrete/coq-numbertheory', '%s/discrete-bin/coq-numbertheory' % DEST_ABSOLUTE)
    build_coq('src/site/discrete/coq-predicates', '%s/discrete-bin/coq-predicates' % DEST_ABSOLUTE)
    build_coq('src/site/discrete/coq-propositional', '%s/discrete-bin/coq-propositional' % DEST_ABSOLUTE)
    build_coq('src/site/discrete/coq-sets', '%s/discrete-bin/coq-sets' % DEST_ABSOLUTE)
    build_coq('src/site/discrete2021/coq-assignments', '%s/discrete2021-bin/coq-assignments' % DEST_ABSOLUTE)
    build_coq('src/site/discrete2021/coq-firstorder', '%s/discrete2021-bin/coq-firstorder' % DEST_ABSOLUTE)
    build_coq('src/site/discrete2021/coq-propositional', '%s/discrete2021-bin/coq-propositional' % DEST_ABSOLUTE)
    build_coq('src/site/discrete2021/coq-numbertheory', '%s/discrete2021-bin/coq-numbertheory' % DEST_ABSOLUTE)
    build_coq('src/site/discrete2021/coq-induction', '%s/discrete2021-bin/coq-induction' % DEST_ABSOLUTE)
    build_coq('src/site/discrete2021/coq-relations', '%s/discrete2021-bin/coq-relations' % DEST_ABSOLUTE)
    build_coq('src/site/discrete2021/coq-lists', '%s/discrete2021-bin/coq-lists' % DEST_ABSOLUTE)
    build_coq('src/site/discrete2021/coq-stringsearch', '%s/discrete2021-bin/coq-stringsearch' % DEST_ABSOLUTE)
    
    
#    build_static('src/site/datasearch/static', '%s/datasearch-bin' % DEST_ROOT)
#    build_static('src/site/problembase/static/collections', '%s/problembase-bin/collections' % DEST_ROOT)

    
if __name__ == '__main__':
    main()



