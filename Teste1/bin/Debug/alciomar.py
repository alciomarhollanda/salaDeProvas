import glob

for file in glob.glob('*.txt'):
    lines = tuple(open(file, 'r'))
    arquivo = open('CV_'+file, 'w')
    for line in lines:
        arrayLine = line.split('	')
        arrayLine[0] = arrayLine[0].zfill(7)
        arquivo.writelines(arrayLine)
    arquivo.close()
