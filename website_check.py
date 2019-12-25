import urllib
import sys

# this is not perfect. I might need a check for when a website
# throws a 503 error to prevent taking up bandwidth (amazon)

# other known issue: websites that don't exist redirect to cox website
# this throws a 200 response, need to fix

# should try HTTPLIB for HEAD request instead of GET

# colors in terminal
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

# open file, read, and send ping to site
with open('/Users/lukewahlmeier/PycharmProjects/website_check/websites') as fp:
    websites = fp.readlines()
    content = [x.strip() for x in websites]

# http_return codes: 1xx - Informational
#                    2xx - Success (most common when site is up)
#                    3xx - Redirection
#                    4xx - Client Error
#                    5xx - Server Error (most common when site is down)

    for lines in content:
        temp = 'http://www.' + str(lines);
        '"{}"'.format(temp)
        http_return = str(urllib.urlopen(temp).getcode())
        if http_return[0] == '2':
            sys.stdout.write(str(lines))
            prGreen('is up')
        elif http_return[0] == '5':
            sys.stdout.write(str(lines))
            prRed('is down: server error ' + str(http_return))
        elif http_return[0] == '4':
            sys.stdout.write(str(lines))
            prRed('is down: client error ' + str(http_return))
        else:
            sys.stdout.write(str(lines))
            prRed('has this error: ' + str(http_return))

# Users/lukewahlmeier/PycharmProjects/website_check/websites