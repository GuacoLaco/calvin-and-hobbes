import urllib.request, os, re

def downloadImage(year, month, day):
    y = str(year)
    m = str(month).zfill(2)
    d = str(day).zfill(2)

    img_filename = os.path.join(f'{y}', f'{y}-{m}-{d}.png')
    img_filename = os.path.realpath(img_filename)

    if os.path.isfile(img_filename):
        return

    else:
        print(img_filename)
        with urllib.request.urlopen('https://www.gocomics.com/calvinandhobbes/{y}/{m}/{d}'.format(y=y, m=m, d=d)) as response:
            html = str(response.read())
            img_url = re.search(r'<meta name=\"twitter:image\" content=\"(https://assets\.amuniversal\.com/.+?)\">', html)[1]

            urllib.request.urlretrieve(img_url, img_filename)
                
            print('Downloaded ' + img_url + ' at ' + img_filename)


print(os.getcwd())

year = 1985
month = 11
day = 18

if input('Download images? y/n: ') == 'y':
    while year < 1996:
        try:
            downloadImage(year, month, day)
            day += 1
        except:
            month +=1
            day = 1
            try:
                downloadImage(year, month, day)
                day += 1
            except:
                year += 1
                month = 1
                day = 1
                downloadImage(year, month, day)
                day +=1
