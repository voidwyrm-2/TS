SEP = '/'

print('grabbing input...')
with open('linsti-in.txt', 'rt') as fin: file = fin.read()
sfile = file.split('\n')

print('stitching...')
out = ''
for lin in sfile:
    print(lin)
    out = out + lin + SEP
#print(out)
print('saving stitched lines')
with open('linsti-out.txt', 'at') as fo: fo.write(f'{out}\n\n\n')
print('stitching complete!')