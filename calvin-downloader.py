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
        print(f'Trying to download {img_filename}')
        with urllib.request.urlopen(f'https://www.gocomics.com/calvinandhobbes/{y}/{m}/{d}') as response:
            html = str(response.read())
            img_url = re.search(r'<meta name=\"twitter:image\" content=\"(https://assets\.amuniversal\.com/.+?)\">', html)[1]

            urllib.request.urlretrieve(img_url, img_filename)
                
            print(f'Downloaded {img_url} at {img_filename}\n')


year = 1985
month = 11
day = 18

print(f'Download images at {os.getcwd()}')

confirmation = input('Are you sure? y/n: ')

if confirmation == 'y' or confirmation == 'Y':
    for i in range(1985, 1996):
        if not os.path.isdir(str(i)):
            print(f'Created directory {i}')
            os.mkdir(str(i))

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
