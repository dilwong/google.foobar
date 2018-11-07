def answer(s):
    for length in range(1, len(s)+1):
        if len(s) % length == 0:
            div = len(s) // length
            test_string = s[0:length]
            for ix in range(div):
                if test_string != s[ix*length : ix*length + length]:
                    break
            else:
                return div
