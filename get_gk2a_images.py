 #!/usr/bin/python
import datetime
import urllib.request
import time
import os


def round_minute(time, round_to):
    """roundTo is the number of minutes to round to"""
    rounded = time + datetime.timedelta(minutes=round_to/2.)
    rounded -= datetime.timedelta(minutes=rounded.minute % round_to, 
            seconds=rounded.second, 
            microseconds=rounded.microsecond)
    return rounded

def download_chart(img_url, file_path):
    if not os.path.exists(file_path):
        try:
            urllib.request.urlretrieve(img_url, file_path)
        except:
            print('file not found')
            return
    else:
        print('already downloaded')

d=datetime.datetime
timestep = 10
kst2utcTimeDelta = datetime.timedelta(hours=-9)
td=datetime.timedelta(minutes=-timestep)
lktd=datetime.timedelta(minutes=-2)
download_period = datetime.timedelta(days=-360)
print(download_period)
today=d.today() + kst2utcTimeDelta
targetDate=round_minute(today, timestep)
print(today, '===>', targetDate)

downpath = "/data/disk3/weatherchart/"

for itimestep in range(0,int(download_period/td)):
    targetDate += td
    year = int(targetDate.year)
    month = int(targetDate.month)
    day = int(targetDate.day)
    yyyymmdd = targetDate.strftime("%Y%m%d")
    yyyy = targetDate.strftime("%Y")
    mm = targetDate.strftime("%m")
    dd = targetDate.strftime("%d")
    hh = targetDate.strftime("%H")
    mi = targetDate.strftime("%M")


    
    for channel in [
            'vi004', 'vi006', 'vi008', 'nr013', 'nr016', 'sw038',
            'wv063', 'wv069', 'wv073', 'ir087', 'ir096', 'ir105', 'ir112', 
            'ir123', 'ir133', 'rgb-true', 
            #'rgb-natural',
            ]:


        if channel == 'vi006':
            gridsize = '005'
        elif channel == 'vi004' or channel == 'vi008':
            gridsize = '010'
        else:
            gridsize = '020'

        gk2a_path = ('http://nmsc.kma.go.kr/IMG/GK2A/AMI/PRIMARY/L1B/COMPLETE/' 
                + 'EA/' +  yyyy + mm + '/' + dd + '/' + hh 
                + '/gk2a_ami_le1b_' + channel + '_ea' + gridsize + 'lc_'
                + yyyy + mm + dd + hh + mi + '.srv.png')

#http://nmsc.kma.go.kr/IMG/GK2A/AMI/PRIMARY/L1B/COMPLETE/KO/201911/06/05/gk2a_ami_le1b_vi004_ko010lc_201911060520.srv.png
#http://nmsc.kma.go.kr/IMG/GK2A/AMI/PRIMARY/L1B/COMPLETE/KO/201911/06/05/gk2a_ami_le1b_vi006_ko005lc_201911060520.srv.png
#http://nmsc.kma.go.kr/IMG/GK2A/AMI/PRIMARY/L1B/COMPLETE/EA/201911/06/05/gk2a_ami_le1b_vi006_ea005lc_201911060520.srv.png
#http://nmsc.kma.go.kr/IMG/GK2A/AMI/PRIMARY/L1B/COMPLETE/EA/201911/06/05/gk2a_ami_le1b_vi008_ea010lc_201911060520.srv.png
#http://nmsc.kma.go.kr/IMG/GK2A/AMI/PRIMARY/L1B/COMPLETE/EA/201911/06/05/gk2a_ami_le1b_nr013_ea020lc_201911060520.srv.png
#http://nmsc.kma.go.kr/IMG/GK2A/AMI/PRIMARY/L1B/COMPLETE/EA/201911/06/05/gk2a_ami_le1b_nr016_ea020lc_201911060520.srv.png
#http://nmsc.kma.go.kr/IMG/GK2A/AMI/PRIMARY/L1B/COMPLETE/EA/201911/06/05/gk2a_ami_le1b_sw038_ea020lc_201911060520.srv.png
#http://nmsc.kma.go.kr/IMG/GK2A/AMI/PRIMARY/L1B/COMPLETE/EA/201911/06/05/gk2a_ami_le1b_wv063_ea020lc_201911060520.srv.png
#http://nmsc.kma.go.kr/IMG/GK2A/AMI/PRIMARY/L1B/COMPLETE/EA/201911/06/05/gk2a_ami_le1b_wv069_ea020lc_201911060520.srv.png
#http://nmsc.kma.go.kr/IMG/GK2A/AMI/PRIMARY/L1B/COMPLETE/EA/201911/06/05/gk2a_ami_le1b_wv073_ea020lc_201911060520.srv.png
#http://nmsc.kma.go.kr/IMG/GK2A/AMI/PRIMARY/L1B/COMPLETE/EA/201911/06/05/gk2a_ami_le1b_ir087_ea020lc_201911060520.srv.png
#http://nmsc.kma.go.kr/IMG/GK2A/AMI/PRIMARY/L1B/COMPLETE/EA/201911/06/05/gk2a_ami_le1b_ir096_ea020lc_201911060520.srv.png
#http://nmsc.kma.go.kr/IMG/GK2A/AMI/PRIMARY/L1B/COMPLETE/EA/201911/06/05/gk2a_ami_le1b_ir105_ea020lc_201911060520.srv.png
#http://nmsc.kma.go.kr/IMG/GK2A/AMI/PRIMARY/L1B/COMPLETE/EA/201911/06/05/gk2a_ami_le1b_ir112_ea020lc_201911060520.srv.png
#http://nmsc.kma.go.kr/IMG/GK2A/AMI/PRIMARY/L1B/COMPLETE/EA/201911/06/05/gk2a_ami_le1b_ir123_ea020lc_201911060520.srv.png
#http://nmsc.kma.go.kr/IMG/GK2A/AMI/PRIMARY/L1B/COMPLETE/EA/201911/06/05/gk2a_ami_le1b_ir133_ea020lc_201911060520.srv.png
#http://nmsc.kma.go.kr/IMG/GK2A/AMI/PRIMARY/L1B/COMPLETE/EA/201911/06/05/gk2a_ami_le1b_rgb-true_ea020lc_201911060520.srv.png
#http://nmsc.kma.go.kr/IMG/GK2A/AMI/PRIMARY/L1B/COMPLETE/EA/201911/06/05/gk2a_ami_le1b_rgb-natural_ea020lc_201911060520.srv.png


        sat_down_fn = ('sat/gk2a/' + channel + '/gk2a_ami_le1b_' + channel + '_ea' + gridsize + 'lc_'
                + yyyy + mm + dd + hh + mi + '.srv.png')
        sat_down_fp = downpath + sat_down_fn

        if not os.path.isfile(sat_down_fp):
            download_chart(gk2a_path, sat_down_fp)
            print(gk2a_path)
            time.sleep(2)
