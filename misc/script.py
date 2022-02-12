import os, shutil

def rename_and_move_file(file, new_name, dir):
    if os.path.isfile(file):
        src = os.path.realpath(file)
        dest = os.path.realpath(dir)
        os.rename(src, new_name) 
        if not os.path.isdir(dest):
            os.mkdir(dest)  
        try:
            shutil.move(src=new_name, dst=os.path.join(dest, new_name))   
        except Exception as e:
            raise e
    else:
        print('Error: The specified file could not be found. Please check file name.')