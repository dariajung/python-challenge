import pickle

if __name__ == "__main__":
    filename = "banner.p"
    try:
        with open(filename, "rb") as f:
            message = pickle.load(f)
            #print message
    except:
        print "something went wrong"

    full_message = []

    for x in message:
        for y in x:
            full_message.append(y[0]*y[1])
        full_message.append("\n")

    print "".join(full_message)
