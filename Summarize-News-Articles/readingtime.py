from constants import AVERAGE_READING_TIME

def readingTime(summary):

    ratio = len(summary)/AVERAGE_READING_TIME
    time = int(round(ratio))

    return time
