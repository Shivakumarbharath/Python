from pytube import YouTube

url=input('Enter the link to Link download')
type1=int(input('1.Video\n2.Audio'))
mime_type=''
if type1==1:
    mime_type='video'
elif type1==2:
    mime_type='audio'
else:
    print('Please select appropriatly')
    exit()

type2=int(input('1.mp4\n2.webm'))

if type2 == 1:
    mime_type += '/mp4'
elif type2 == 2:
    mime_type += '/webm'
else:
    print('Please select appropriatly')
    exit()

res_query=int(input('Select Resolution\n1.144p\n2.240p\n3.360p\n4.480p\n5.720p\n6.1080p'))




name=input('Name Of the file? : ')

try:
    yt=YouTube(url)
except:
    print('Couldnt connect')
    exit()

if type1==2:
    stream=yt.streams.filter(mime_type=mime_type).first()
    stream.download()
    print("Download successfull")
    exit()
def resolution():
    res=''
    if res_query==1:
        res='144p'
    elif res_query==2:
        res='240p'

    elif res_query==3:
        res='360p'
    elif res_query==4:
        res='480p'

    elif res_query==5:
        res='720p'

    elif res_query==6:
        res='1080p'
    else:
        print('Enter appropriate resolution')
        exit()
res=resolution()
stream=yt.streams.filter(mime_type=mime_type,res=res)
if stream==[]:
    print('Resolution of {} is not availible for download\nPlease try with different resolution')
    res=resolution()

else:
    stream.first().download(filename=name)
    print("Download successfull")
