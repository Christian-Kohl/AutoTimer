'''
This file gives the linux support for this repo, next section is for imports
'''
import sys
from os import path
import os
import subprocess
import re
import datetime

'''
Gives the raw information of the current window
'''


def get_active_window_raw():
    '''
    returns the details about the window not just the title
    '''
    root = subprocess.Popen(
        ['xprop', '-root', '_NET_ACTIVE_WINDOW'], stdout=subprocess.PIPE)
    stdout, stderr = root.communicate()

    m = re.search(b'^_NET_ACTIVE_WINDOW.* ([\w]+)$', stdout)
    if m != None:
        window_id = m.group(1)
        window = subprocess.Popen(
            ['xprop', '-id', window_id, 'WM_NAME'], stdout=subprocess.PIPE)
        stdout, stderr = window.communicate()
    else:
        return None

    match = re.match(b"WM_NAME\(\w+\) = (?P<name>.+)$", stdout)
    if match != None:
        ret = match.group("name").strip(b'"')
        return ret
    return None


'''
This is the method to actually track the windos, and subsequently output information
'''


def track():
    new_information = None
    new_window = None
    last_change = datetime.datetime.now()
    current_window, current_information = get_active_window_title()
    while(True):
        if new_information != current_information:
            current_window, current_information = new_window, new_information
            this_change
            tab = get_url(current_information, current_window) if current_window in [
                "Firefox", "Chrome"] else None
            print(current_information)
            print(tab)
        new_window, new_information = get_active_window_title()


'''
This method identifies the current web browser, and subsequently gets the website's name
'''


def get_url(curr_inf, curr_win):
    if curr_win in ["Chrome"]:
        tab = get_chrome_url(curr_inf)
    elif curr_win in ["Firefox"]:
        tab = get_firefox_url(curr_inf)
    else:
        tab = None
    return tab


'''
Gets the information of the url in chrome, can be extended to browser that have a similar information output
'''


def get_chrome_url(detail_full):
    '''
    instead of url the name of the website and the title of the page is returned seperated by '/'
    '''
    detail_list = detail_full.split(' - ')
    detail_list.pop()
    detail_list = detail_list[::-1]
    _active_window_name = 'Google Chrome -> ' + " / ".join(detail_list)
    return _active_window_name


'''
Gets the information of the url in Firefox, can be extended to browser that have a similar information output
'''


def get_firefox_url(detail_full):
    '''
    instead of url the name of the website and the title of the page is returned seperated by '/'
    '''
    detail_list = detail_full.split(' - ')
    detail_list.pop()
    detail_list = detail_list[::-1]
    _active_window_name = " / ".join(detail_list)
    return _active_window_name


'''
Gets the title of the currently active window, also outputs the raw new_information
'''


def get_active_window_title():
    full_detail = get_active_window_raw()
    detail_list = None if full_detail is None else full_detail.decode(
        "utf-8").split(" ")
    if detail_list is None:
        return None, None
    else:
        new_window_name = detail_list[-1]
        return new_window_name, full_detail.decode("utf-8")


'''
Reads the .json file, so that previous infotmation from this day can be stored
'''


def read_file():
    return


'''
Writes to the current day's file
'''


def write_file():
    return


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
