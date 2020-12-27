from os import walk


def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

#Loop throug directories and add all files in list (with the path)
def list_files(path="uploads"):
    files_path = []
    tempor = []
    print("STEP 1")
    print("Listing files...")
    for root, dirs, files in walk(path):
        
        if len(files) > 0:
            
            result = []
            for file in files:

                test = file.find(".")
                tempor.append(file[:test])

                #find all declinate pics create by WP (exemple_pic.jpg | exemple_pic-250x250.jpg ...)
                matching = [s for s in tempor if file[:test] in s]

                if len(matching) < len(result):
                    bubbleSort(result)
                    combined_string = root + "/" + result[0] + extension
                    combined_string = combined_string.replace("\\", "/")
                    files_path.append(combined_string)
                    result = []
                    
                #do not forget the last one
                elif file == files[-1]:
                    bubbleSort(matching)
                    combined_string = root + "/" + matching[0] + extension
                    combined_string = combined_string.replace("\\", "/")
                    files_path.append(combined_string)
                else:
                    extension = file[test:]
                    result = matching
            
    print("Done.\n")
    
    with open("all_images.txt", "w", encoding="utf-8") as my_file:
        for path in files_path:
            my_file.write(path + "\n")

    print("Results are stored in --> all_images.txt\n\n")
    return files_path