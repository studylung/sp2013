import os

class Wdir:
    drive = 'c'
    file_head = ''
    temp = ''
    test_dir_name = ''
    test_name = ''
    input_pgm_dir = ''
    temp_pgm = ''
    
def init(imgdata):
    wdir = Wdir()
    cdir = os.path.abspath('..')
    workx = ''
    
    if imgdata.workmode == 'single':
        workx =  cdir + '\\image\\' + imgdata.tname + '\\work_sing'
        vrml = cdir + '\\image\\' + imgdata.tname + '\\vrml_sing'
        featx = cdir + '\\image\\' + imgdata.tname + '\\feat_sing'

    elif imgdata.workmode == 'comb':
        workx =  cdir + '\\image\\' + imgdata.tname + '\\work_comb'
        vrml = cdir + '\\image\\' + imgdata.tname + '\\vrml_comb'
        featx = cdir + '\\image\\' + imgdata.tname + '\\feat_comb'

    elif imgdata.workmode == 'augm':
        workx =  cdir + '\\image\\' + imgdata.tname + '\\work_augm'
        vrml = cdir + '\\image\\' + imgdata.tname + '\\vrml_augm'
        featx = cdir + '\\image\\' + imgdata.tname + '\\feat_augm'

    elif imgdata.workmode == 'lowe':
        workx =  cdir + '\\image\\' + imgdata.tname + '\\work_lowe'
        vrml = cdir + '\\image\\' + imgdata.tname + '\\vrml_lowe'
        featx = cdir + '\\image\\' + imgdata.tname + '\\feat_lowe'

    else:
        print 'unknown workmode\\n'

    if not os.path.exists(workx):
        os.mkdir(workx)
    if not os.path.exists(vrml):
        os.mkdir(vrml)
    if not os.path.exists(featx):
        os.mkdir(featx)

    wdir.work = workx + '\\'
    wdir.vrml = vrml + '\\'
    wdir.output_feature_dir = featx + '\\'

    print wdir.work
    print wdir.vrml
    print wdir.output_feature_dir
