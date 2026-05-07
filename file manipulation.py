import os

folder = "files"

for count, filename in enumerate(os.listdir(folder)):
    ext = filename.split(".")[-1]
    new_name = f"file_{count}.{ext}"
    
    old_path = os.path.join(folder, filename)
    new_path = os.path.join(folder, new_name)
    
    os.rename(old_path, new_path)

print("Files renamed successfully!")
