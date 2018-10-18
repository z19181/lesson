import maya.cmds as mc

def get_all_sg_nodes():
    '''
    '''
    sg_nodes = mc.ls(typ='shadingEnige')
    return sg_nodes



def get_selct_sg_nodes():
    '''
    '''
    pass


def export_sg_nodes(sg_nodes,file_path):
    '''
    '''



def export_all_sg_nodes(file_path):
    '''
    '''
    export_all_sg_nodes(get_all_sg_nodes(),file_path)



def export_selct_sg_nodes(file_path):
    '''
    '''
    export_selct_sg_nodes(get_selct_sg_nodes(),file_path)

