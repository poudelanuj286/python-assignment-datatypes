def repeats(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1

    dicts = sorted(dict.items(), reverse=True)
    return dicts
print(repeats('google.com'))
