import re
import sys
txt = input()

def blace_opener(text):
    start = text.find("{")
    end = text.find("}")

    upper = text[:start]
    inside = text[start+1:end]
    bottom = text[end+1:]
    inside_list = re.split(",",inside)


    output_list = []
    for word in inside_list:
        output_list += [upper + word + bottom]
    return output_list
flag = True
output = blace_opener(txt)
print (output)
for out in output:
    #print(out)
    if out.find("{")!=-1:
        #print("hoge")
        output.extend(blace_opener(out))


for out in output:
    if out.find("{")==-1:
        print(out)
