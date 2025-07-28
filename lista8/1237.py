def maiorSubstring(s1,s2):
    for i in range(len(s2), 0, -1):        
        for j in range(0, len(s2)-i+1):
            if s1.find(s2[j:j+i]) != -1:
                return i
            
    return 0

while True:

    try:

        string1 = input()
        string2 = input()

        if len(string2) > len(string1):
            string1, string2 = string2, string1

        print(maiorSubstring(string1, string2))
        
    except EOFError:
        break
    

# while True:

#     try:
#         string1 = input()
#         string2 = input()

#         if len(string2) > len(string2):
#             string1,string2 = string2, string1

#         encontrou = False

#         for i in range(len(string2), 0, -1):
#             if encontrou:
#                 break
#             for j in range(0,len(string2)-i + 1):
#                 if string1.find(string2[j:j + i]) != -1:
#                     print(i)
#                     encontrou = True 
#                     break 
#         if not encontrou:
#             print(0)
#     except EOFError:
#         break