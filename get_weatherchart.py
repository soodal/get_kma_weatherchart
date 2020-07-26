 #!/usr/bin/python
import datetime
import urllib.request
import time

d=datetime.datetime
td=datetime.timedelta(days=-1)
today=d.today()
print(today)
targetDate=today

def download_chart(img_url, filename):
    file_path = "%s%s" % ("/data/disk3/weatherchart/", filename)
    try:
        image_on_web = urllib.request.urlopen(img_url)
    #except urllib.error.HTTPError:
    except:
        print('file not found')
        time.sleep(3)
        
        return

    buf = image_on_web.read(100000000)
    if len(buf) != 0:
        downloaded_image = open(file_path, "wb")
        downloaded_image.write(buf)
        downloaded_image.close()
        image_on_web.close()
    return file_path

for i in range(0,30):
    targetDate+=td
    year=int(targetDate.year)
    month=int(targetDate.month)
    day=int(targetDate.day)
    date=targetDate.strftime("%Y%m%d")
    
# 지상일기도 AXAS [00, 12]
    for hour in [str(x).zfill(2) for x in range(0, 24, 12)]:
        kmaSurfUrl = ('http://www.weather.go.kr/repositary/image/cht/img/' \
                'surf_' + date+hour+".png")
        kmaSurfdownfile='surf/surf_' + date+hour+".png"
        download_chart(kmaSurfUrl, kmaSurfdownfile)
        print(kmaSurfdownfile)

# 지상일기도3 ASFE 12시간간격
    for hour in [str(x).zfill(2) for x in range(0, 24, 3)]:
        kmaSfc3Url = ('http://www.weather.go.kr/w/repositary/image/cht/img/' \
                + 'sfc3_' + date+hour+".png")
        kmaSfc3downfile='sfc3/sfc3_' + date+hour+".png"
        download_chart(kmaSfc3Url, kmaSfc3downfile)
        print(kmaSfc3downfile)

# 국지일기도 6시간간격
    for hour in [str(x).zfill(2) for x in range(0, 24, 6)]:
        kmaSfc3Url = ('http://www.weather.go.kr/w/repositary/image/cht/img/' \
                + 'kor1_anlmod_pb4_' + date+hour+".gif")
        kmaSfc3downfile='kor1/kor1_anlmod_pb4_' + date+hour+".png"
        download_chart(kmaSfc3Url, kmaSfc3downfile)
        print(kmaSfc3downfile)


# 보조일기도 가 
    for hour in ['00', '06', '12', '18']:# only for 0 and 12
        kmaAx01Url = 'http://www.weather.go.kr/repositary/image/cht/img/' \
                + 'kim_gdps_anal_axfe01_pb4_' + date + hour + '.gif'
        kmaAx01downfile='aux/kim_gdps_anal_axfe01_pb4_' + date+hour+'.gif'
        download_chart(kmaAx01Url, kmaAx01downfile)
        print(kmaAx01downfile)

# 보조일기도 나
    for hour in ['00', '12']:# only for 0 and 12
        kmaAx02Url = ('http://www.weather.go.kr/repositary/image/cht/img/' \
                +'kim_gdps_anal_axfe02_pb4_' + date+hour+'.gif')
        kmaAx02downfile='aux/kim_gdps_anal_axfe02_pb4_' + date+hour+'.gif'
        download_chart(kmaAx02Url, kmaAx02downfile)
        print(kmaAx02downfile)

# 상층일기도 6시간간격
    for level in ['92', '85', '70', '50', '30', '20', '10']:
        for hour in ['00', '06', '12', '18']:# every 6 hours
            kmaUpUrl = ('http://www.weather.go.kr/repositary/image/cht/img/' \
                    + 'up' + level + '_' + date+hour+".png")
            kmaUpdownfile='up' + level + '/up' + level +'_' + date+hour+".png"
            download_chart(kmaUpUrl, kmaUpdownfile)
            print(kmaUpdownfile)
