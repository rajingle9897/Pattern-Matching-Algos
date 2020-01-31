def match(pat, txt):
    p = len(pat)
    t = len(txt)
    counter=0
    FOUND=0
    ff = [0] * p
    j = 0
    failurefunction_find(pat, p, ff)
    k = 0
    while k < t:
        if(FOUND==1):
            break
        if pat[j] == txt[k]:
            counter=counter+1
            k += 1
            j += 1
        if j == p:
            print("PATTER FOUND AT INDEX " + str(k - j))
            FOUND=1
            print("NUMBER OF COMPARISIONS ARE " + str(counter))
            j = ff[j - 1]
        elif k < t and pat[j] != txt[k]:
            counter=counter+1
            if j != 0:
                j = ff[j - 1]
            else:
                k += 1
    return FOUND,counter

def failurefunction_find(pat, p, ff):
    l = 0
    ff[0]
    o = 1
    while o < p:
        if pat[o] == pat[l]:
            l += 1
            ff[o] = l
            o += 1
        else:
            if l != 0:
                l = ff[l - 1]
            else:
                ff[o] = 0
                o += 1

text = "AAAAC_BBA_ABAA_BBCBBDABBC_ABACABB_BABBA_ABBABBDABB"
pattern = "ABBDABB"
x,c=match(pattern, text)
if (x == 0):
    print("NUMBER OF COMPARISIONS ARE ",c)
    print("NO SUCH PATTERN FOUND IN TEXT ")



