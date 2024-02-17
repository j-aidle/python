f = int(input())
c = int(input())
#pasar a m/s per igualar totes les unitats
vr = int(input()) * 10/36
vs = int(input()) * 10/36

print('{:.2f}  Hz'.format(round(f*((c+vr)/(c+vs)),2)))