print("This is the module that conatins two methods, one for renaming the files and secondly for extract the common name from the bunch of files." )


def f1(file_name, ext = '.docx'):
    """
    Renaming the files so that they don't have any '(' and ')' in them.
    """
    cut_len = 0

    for i in range(len(file_name)):
        if file_name[i].isnumeric():
            cut_len = i
            for j in range(i, len(file_name)):
                if not file_name[j].isnumeric():
                    cut_len1 = j
                    break
            break
    
    file_name_new = file_name[:cut_len1] + '_' + file_name[cut_len:cut_len1] + ext
    os.rename(file_name, file_name_new)
    
    return file_name_new 
    
    
def f2(file_name, ext = ".docx"):
    """
    Choosing the directory name for the same types of documents.
    Like 'Programming Assignments' for programming assignments and 'Assignments' for assignments.
    """
    
    cut_len = len(file_name) - len(ext)
    
    for i in range(len(file_name)):
        if file_name[i].isnumeric():
            cut_len = i
            break
            
    dir = file_name[:cut_len].replace('_', '')
    
    return dir