import shutil, errno
import os
import sys


directory = os.path.dirname(os.path.abspath(__file__))
if getattr(sys, 'frozen', False):
    directory = os.path.dirname(sys.executable)
elif __file__:
    directory = os.path.dirname(__file__)

src_g = os.path.join(directory, 'Resource_example')
dst_g = os.path.join(directory, 'Output')

nameLib_g = "Example"

def copy_any_thing(src_p, dst_p):
    if os.path.isdir('Output'):
        shutil.rmtree("Output")
        print("Removed folder Successfully")
        shutil.copytree(src_p, dst_p)
        print("Copied folder Successfully")
        # os.remove("Output") # remove file
    else:
        try:
            shutil.copytree(src_p, dst_p)
            print("Copied folder Successfully")
        except OSError as exc: # python >2.5
            if exc.errno in (errno.ENOTDIR, errno.EINVAL):
                shutil.copy(src_p, dst_p)
            else: raise

def input_name():
    global nameLib_g
    nameLib_g = input('Please enter library name: ')
    print('Your library is: ', nameLib_g)

def handle_change_name():
    if len(os.listdir('Output')) == 0:
        print("Directory is empty")
    else:
        input_name();
        # rename folder
        os.rename("Output/my_library", "Output/"+str(nameLib_g))

        os.rename('Output/'+str(nameLib_g)+'/my_library.cpp', "Output/"+str(nameLib_g)+"/"+str(nameLib_g)+".cpp")
        replace_str('my_library', nameLib_g, "Output/"+str(nameLib_g)+"/"+str(nameLib_g)+".cpp")
        os.rename('Output/'+str(nameLib_g)+'/my_library.h', "Output/" + str(nameLib_g) + "/" + str(nameLib_g) + ".h")
        replace_str('MY_LIBRARY', nameLib_g.upper(), "Output/"+str(nameLib_g)+"/"+str(nameLib_g)+".h")

def replace_str(old_txt, new_txt, path):
    # Read in the file
    with open(path, 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(old_txt, new_txt)

    # Write the file out again
    with open(path, 'w') as file:
        file.write(filedata)


def main():
    print("Create lib for Arduino")
    copy_any_thing(src_g,dst_g);
    handle_change_name()

if __name__ == "__main__":
    main()