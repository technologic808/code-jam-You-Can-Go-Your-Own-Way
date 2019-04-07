t = int(input()) # read number of test cases
for i in range(1, t + 1):
    n = int(input()) # read size of grid (which doesnt really matter for my solution)
    lydia = str(input())
    lydiaList = list(lydia)
    nonLydiaList = lydiaList
    for idx,j in enumerate(lydiaList):
        if j == 'S':
            nonLydiaList[idx] = 'E'
        if j == 'E':
            nonLydiaList[idx] = 'S'

    nonLydia = ''.join(nonLydiaList)
    print("Case #{}: {}".format(i, nonLydia))
    # check out .format's specification for more formatting options
