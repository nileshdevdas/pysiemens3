"""
a airport application ....
"""
# declaring constants
AIRPORTS = []
SMALL_AIRPORTS = []
LARGE_AIRPORTS = []
MEDIUM_AIRPORTS = []
HELLIPADS = []
BAD_RECORDS = []
def read_airports(file_name):
    """
    This will read the airports and seggregate the types
    :param file_name: This is a string file name
    :return : None
    """
    file = None
    try:
        file = open(file=file_name, mode='r', encoding='utf-8')
        line = file.readline()
        while line:
            line = file.readline()
            # remove all the double quotes
            stripped_line = line.replace("\"", "")
            try:
                cols = stripped_line.split(",")
                if cols[2] == 'small_airport':
                    SMALL_AIRPORTS.append(cols[3])
                elif cols[2] == 'large_airport':
                    LARGE_AIRPORTS.append(cols[3])
                elif cols[2] == 'medium_airport':
                    MEDIUM_AIRPORTS.append(cols[3])
            except Exception as exception_e:
                print(exception_e)
                print("Bad Record....")
            finally:
                print('Done....')
        print(len(SMALL_AIRPORTS))
        print(len(LARGE_AIRPORTS))
        print(len(MEDIUM_AIRPORTS))
    except FileNotFoundError as fne:
        print("Check if you have really provided a correct file ")
        print(fne)
    finally:
        if file:
            file.close()
# invoke the read_airports
read_airports("c:/airports.csv")
