def prefixFunction(s):
    p = [0 for _ in range(len(s))]
    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[i] != s[k]:
            k = p[k - 1]
        if s[i] == s[k]:
            k += 1
        p[i] = k
    return p


def kmp(p, t):
    pl = len(p)
    tl = len(t)
    answer = []
    p = prefixFunction(f"{p}#{t}")
    # cnt = 0
    for i in range(tl):
        if p[pl + i + 1] == pl:
            answer.append(i - pl)
            # cnt += 1
    return answer


def main():
    with open("input_p.txt", "r") as p:
        with open("input_t.txt", "r") as t:
            p = p.read()
            t = t.readlines()
            for string in t:
                print(kmp(p, string))


if __name__ == "__main__":
    main()
