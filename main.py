'''
Main method, for reading and writing to files as well
'''


def run():
    if not (path.exists("track_log") and path.isdir("track_log")):
        os.mkdir("track_log")
    current_date = datetime.date.today()
    if not path.exists("track_log/" + current_date.strftime("%d-%m-%Y") + ".json"):
        print("this")
        file = open("track_log/" +
                    current_date.strftime("%d-%m-%Y") + ".json", "w+")
        activity_list = []
    else:
        file = open("track_log/" +
                    current_date.strftime("%d-%m-%Y") + ".json", "w+")
        activity_list = read_file(file)
    track(activity_list)


run()
