def match(pat, txt):
    m = len(pat)
    n = len(txt)
    counter=0
    for i in range(n - m + 1):
        k = 0
        final=0

        while (k < m):
            if (txt[i + k] != pat[k]):
                counter=counter+1
                break
            counter=counter+1
            k += 1

        if (k == m):
            print("PATTERN FOUND AT INDEX ", i)
            print("NUMBER OF COMPARISONS ARE ", counter)
            final=1
            break
    if(final!=1):
        print("NUMBER OF COMPARISONS ARE ("+str(counter)+")")
        print("NO SUCH PATTERN FOUND IN TEXT")

if __name__ == '__main__':
    text = "AAAAC_BBA_ABAA_BBCBBDABBC_ABACABB_BABBA_ABBABBDABB"
    pattern= "ABBDABB"
    match(pattern, text)
