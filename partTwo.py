import os

compare_list = []
unmatch_list = []

#compared two files (list of path) and return the list of unmatched
def unmatch_finder(list1, list2):
    
    unmatch_count = 0
    print("STEP 2")
    print("Getting datas...\n")

    while os.path.exists(list2) is False:
        list2 = input("Enter the file that conain the list of the pic you want to keep : ")

    with open(list2, "r") as file:
        lines = file.readlines()
        for line in lines:
            #remove \n 
            line = line.replace("\n", "")
            compare_list.append(line)
    

    print("Done.\nLooking for useless files...")
    for path in list1:
        if (path in compare_list) is False:
            print(path)
            unmatch_count += 1
            unmatch_list.append(path) 

    print("\nDone.\n" + str(unmatch_count) + " useless files.\n")
    return unmatch_list
