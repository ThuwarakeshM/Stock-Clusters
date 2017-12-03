import pandas as pd
import pandas_datareader.data as web
from datetime import datetime


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


start = datetime(2012, 11, 1)
end = datetime(2017, 11, 1)


def get_data(token):
    try:
        print(bcolors.OKBLUE + '{0} : trying to fetch data for {1}'.format(datetime.now(), token))
        f = web.DataReader(token, 'yahoo', start, end)
        f.name = token
        print(bcolors.OKGREEN + '{0} : fetching completed!'.format(datetime.now()))
        return f
    except:
        print(bcolors.WARNING + '{0} : fetching FAILED for token {1}!'.format(datetime.now(), token))
        return


try:
    print(bcolors.OKBLUE + '{0} : trying to fetch token list from wiki'.format(datetime.now()))
    tokens = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    tokens = tokens[0]
    tokens = list(tokens[tokens.columns[0]])[1:]
except:
    print(bcolors.FAIL + '{0} : FAILED to fetch token list from wiki'.format(datetime.now()))

def fetch_data(tokens):
    for token in tokens:
        try:
            print(bcolors.OKBLUE + '{0} : Trying to fetch data for token {1}'.format(datetime.now(), token))
            data = get_data(token)
            print(bcolors.OKGREEN + '{0} : Fetching data for token {1} completed!'.format(datetime.now(), token))
            data.to_csv('/home/ubuntu/data/{0}.csv'.format(token))
            print(bcolors.OKGREEN + '{0} : writing data for token {1} completed!'.format(datetime.now(), token))
        except:
            print(bcolors.WARNING + '{0} : processing for token {1} Failed!'.format(datetime.now(), token))
            failed_tokens.append(token)
            pass
    return

failed_tokens = []
fetch_data(tokens)
tokens = failed_tokens
failed_tokens = []
fetch_data(tokens)
tokens = failed_tokens
failed_tokens = []
fetch_data(tokens)


