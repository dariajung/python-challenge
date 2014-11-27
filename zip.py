import zipfile
import os.path
import re

def unzip(source, destination):
    with zipfile.ZipFile(source) as zf:
        path = ""
        for member in zf.infolist():
            file_name = member.filename
            path = destination
            zf.extract(member, path)

def traverse_files(source):

    match = ""
    with open("channel/%s.txt" % source) as f:
        data = f.read()
        match = re.search("(Next nothing is )([0-9]+)", data).group(2)

    nothings = [source, match]

    while match:
        with open("channel/%s.txt" % match) as f:
            data = f.read()
            search = re.search("(Next nothing is )([0-9]+)", data)
            if search:
                match = search.group(2)
                nothings.append(match)
            else:
                match = None

    return nothings


def get_comments(source, nothings):
    comments = []
    with zipfile.ZipFile(source) as zf:
        for f in nothings:
            comments.append(zf.getinfo("%s.txt" % f).comment)

    return "".join(comments)


if __name__ == "__main__":
    # file_name = "channel.zip"
    # unzip(file_name, "channel/")

    files = traverse_files("90052")

    print get_comments("channel.zip", files)
