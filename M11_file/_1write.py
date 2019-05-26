with open("lang.txt","w") as f:
    f.write("python\n")
    f.write("java\n")
    f.write("c++\n")
# with open("lang.txt","w") as f:#先刪除后覆蓋
#     f.write("java\n")
#     f.write("C#\n")
#     f.write("Ruby\n")
with open("lang.txt","a") as f:
    f.write("python\n")
    f.write("java\n")
    f.write("c++\n")


with open("lang.txt","a") as f:
    # f.writelines("python\n")
    # f.writelines("java\n")
    # f.writelines("c++\n")
    lines= ["python\n","java\n","c++\n"]
    f.writelines(lines)
