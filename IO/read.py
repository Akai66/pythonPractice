#文件读写
with open('../README.md','r') as f:
    # print(f.read())
    # for line in f.readlines():
    #     print(line.strip())
    while True:
        line = f.readline()
        if line:
            print(line.strip())
        else:
            break
