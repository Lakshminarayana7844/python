def isomorohic(s,t):
    if len(s)!=len(t):
        print("false")
    s_map={}
    t_map={}
    for i in range(len(s)):
        s_char=s[i]
        t_char=t[i]
        if s_char in s_map:
            if s_map[s_char]!=t_char:
                print("false")
            else:
                if t_char in t_map:
                    print("false")
                s_map[s_char]=t_char
                t_map[t_char]=s_char
    print("true")
