import datetime
def start():
    starttime = datetime.datetime.now()
    return starttime
#long running
def end():
    endtime = datetime.datetime.now()
    return endtime
def timeuse(starttime, endtime):

    return (endtime - starttime).seconds