import zipfile
import os.path


def unzip(source, destination):
    with zipfile.ZipFile(source) as zf:
        path = ""
        for member in zf.infolist():
            file_name = member.filename
            path = destination
            zf.extract(member, path)


if __name__ == "__main__":
    file_name = "channel.zip"
    unzip(file_name, "channel/")