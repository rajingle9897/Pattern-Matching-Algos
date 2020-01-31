def Horspool(pattern, text):
    p = len(pattern)
    t = len(text)
    c=0
    if p > t:
        return -1
    shift = []
    for l in range(256):
        shift.append(p)
    for l in range(p - 1):
        shift[ord(pattern[l])] = p - l - 1
    shift = tuple(shift)
    l = p - 1
    while l < t:
        j = p - 1; i = l
        while j >= 0 and text[i] == pattern[j]:
            c=c+1
            j -= 1; i -= 1
        if j == -1:
            return i + 1,c
        c=c+1
        l += shift[ord(text[l])]
    return -1,c
if __name__ == '__main__':
    text = "AAAAC_BBA_ABAA_BBCBBDABBC_ABACABB_BABBA_ABBABBDABB"
    pattern = "ABBDABB"
    s,counter = Horspool(pattern, text)
    if s > -1:
        print('PATTER FOUND AT INDEX',s)
        print("NUMBER OF COMPARISIONS ARE", counter)
    else:
        print("NUMBER OF COMPARISIONS ARE", counter)
        print("NO SUCH PATTERN FOUND IN TEXT")