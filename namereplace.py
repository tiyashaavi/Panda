import os

print("Listing PHP file:")

a="GBSG"
b=input("Enter the new string to replace GBSG : ")
dpath="C:\\xampp\\htdocs\\changes\\"+a.upper()+"\\"
for dirpath, dirnames, filenames in os.walk(dpath):
    for filename in filenames:
        old_path=os.path.join(dirpath, filename)
        if (filename.endswith(".php")):
            with open(old_path, 'r') as file:
                file_contents = file.read()
                updated_contents = file_contents.replace(a.upper(), b.upper())
                final_contents = updated_contents.replace(a.lower(), b.lower())
            with open(old_path, 'w') as file:
                file.write(final_contents)
                file.close()
        if (filename.endswith(".php") and (a in str(filename))):
            newfilename=str(filename).replace(a.upper(),b.upper())
            new_path=os.path.join(dirpath, newfilename)
            os.rename(old_path,new_path)
        
