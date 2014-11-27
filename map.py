# g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr
# ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.


# abcdefghijklmnopqrstuvwxyz

# k -> m
# o -> q
# e -> g


def create_dict():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    num = {}
    reverse = {}
    count = 0

    for letter in alpha:
        num[letter] = count
        reverse[count] = letter
        count += 1

    return (num, reverse)


def translate(_dict, rev_dict, string):

    new_str = ""

    for char in string:
        if char in _dict:
            value = (_dict[char] + 2) % 26
            translated = rev_dict[value]
        else:
            translated = char

        new_str += translated

    return new_str


if __name__ == "__main__":
    (mapping, rev_mapping) = create_dict()

    string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.\
        bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. \
        sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    print translate(mapping, rev_mapping, "map")
