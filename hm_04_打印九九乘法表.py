# 用9行9列的概念来实现
row = 1
while row <= 9:
    col = 1
    while col <= row:
        # 格式化输出，用-2d表示靠左对齐
        print("%d*%d=%d" % (row, col, row * col), end="\t")
        col += 1
    print()  # 输出一个换行
    row += 1

#
for i in range(1, 10):
    for j in range(1, i+1):
        print("%d*%d=%d" % (j, i, j*i), end="\t")
    print()