from getpass import getpass
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error, ID3NoHeaderError
from mutagen.easyid3 import EasyID3
from mutagen import File #TODO: fix this so I am not importing all of mutagen
import httplib
import os as os
import urllib#3
#import urllib2
#import certifi
from time import sleep
#from ID3 import *
#import eyed3 as eyed3
#from eyed3.id3 import Tag
#from eyed3.id3 import ID3_V2_4
import logging
from PIL import Image
import traceback
import re
#import ssl
import mutagen
import sys

import config
import download_ui as dwn_ui

from gmusicapi import Mobileclient
conf = config.config()
working_device_id = conf.get_device_id() 
folder = conf.get_folder()
problem=False #stores if one thing below does not work
problems=[] #stores what went wrong
if folder=="unset":
    problems.append("folder is not set, set to the directory you want to store the music,")
    problem=True
if working_device_id == "blahid":
    problems.append("device id is not set, get this by running the script get_device_ids.py")
    problem=True
if conf.get_email()=="blahemail":
    problems.append("either username or password is not set")
    problem=True
elif(conf.get_password()=="blahpass"):
    problems.append("either username or password is not set")
    problem=True
if problem:
    print "you must go and edit 'config.cfg' in the main director manually and fix the following things: (this will be fixed in a later version)"
    for Problem in problems:
        print"  "+Problem
    sleep(50000)
    exit(1)
del problem
del problems
del conf

def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

def dlProgress(count, blockSize, totalSize):
    global dialog_ui
    percent = int(count*blockSize*100/totalSize)
    dialog_ui.set_song_progress(percent)
    #sys.stdout.write("\r" + "...%d%%" % percent)
    #sys.stdout.flush()
     
def retrev(testfile, url, filePath):
    try:#testfile.retreive
        urllib.urlretrieve(url, filePath, reporthook=dlProgress)
        print('done')
    except Exception, err:
        print(traceback.format_exc())
        #sleep(10)
        return True
        #retrev(testfile, url, filePath)

def resize_image(filename, width, height):
    im1 = Image.open(filename)
    im1 = im1.resize((width, height), Image.ANTIALIAS)
    im1.save(filename)
    f1 = open(filename, 'rb')
    return(f1.read())

#logs out if there is an error
def attempt_download(api, pnames, dialog):
    try:
        begin_download(api, pnames, dialog) #TODO: fix this garbage
    except Exception, e:
        api.logout()
        print(traceback.format_exc())
        raise(e)

def begin_download(api, pnames, dialog):


    # Get all of the users songs.
    # library is a big list of dictionaries, each of which contains a single song.
    print 'Loading library...',
    #library = api.get_all_songs()
    print 'done.'
    #print len(library), 'tracks detected.'
    #print
    global dialog_ui
    dialog_ui = dwn_ui.Ui_Download()
    dialog_ui.setupUi(dialog)
    dialog.open()#.show()
    global plist
    global psongs
    plist = list()
    psongs = list()
    all_lists = api.get_all_user_playlist_contents()
    llength = len(pnames);
    lcurrent = 0; #current playlist number
    for pname in pnames:
        lcurrent = lcurrent+1;
        playlists = api.get_all_user_playlist_contents() #gets all the playlists
        dialog_ui.set_overall_progress(int((float(lcurrent)/llength)*100)) #set overall progress
        dialog_ui.set_overall_label("("+str(lcurrent-1)+' of '+str(llength)+"): "+str(pname))
        dialog_ui.set_playlist_label(str(pname))
        for playlist in playlists:
            if(playlist['name']==pname):
                plist = playlist['tracks'] #save the id
                #print plist
                break
        #print playlists[0]
        print("playlist "+str(lcurrent)+"/"+str(llength)+" "+str(pname)+" length=" + str(len(plist)))
        #print plist
        psongs = list()
        for Usong in plist:
            song = convert(Usong)
            print song
            #Usong = convertKeys(Usong)
            #print Usong
            Usong = Usong.get('track', Usong.get(u'track')) #we only want the track portion
            try:
               song['track']['Usong'] = Usong #store unicode for later
               #print(song['track']['title'])
               psongs.append(song['track'])
            except Exception, err:
               print("failed on song "+str(song))
               print(traceback.format_exc())
               #raise(err)
        #we now have all the playlists
        del playlists #TODO: fix this constantly regetting of the playlists
        dsongs = list() #list of songs to download with full metadata
        #working_device_ids = web.get_registered_devices()
        #working_device_id = convert(working_device_ids[0])['id']
        dsongs = psongs
        """urllib.poolManager(
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where(),
            )"""
        testfile = urllib.URLopener() #FIXME: stop reinitializing all the time
        albumget = urllib.URLopener() #FIXME: "
        print(len(dsongs))
        #print(dsongs[0])
        nonList = list()
        song = dsongs[0]
        m3uPath = os.path.join(folder, pname+'.m3u')
        if os.path.exists(m3uPath):
            os.remove(m3uPath) #delete previous list
        with open(m3uPath, 'w') as plistF:
            plistF.write('#EXTM3U\n') #write starting tag
            number_of_songs = len(dsongs)
            for i in range(0, number_of_songs, 1):#TODO remove \\ as it confuses the download manager for path in filename
                dialog_ui.set_playlist_progress(int((float(i)/number_of_songs)*100))
                dialog_ui.set_playlist_label("("+str(i)+" of "+str(number_of_songs)+") in "+pname)
                song = dsongs[i]
                songLength = int(song["durationMillis"])/1000 #convert from miliseconds to seconds
                plistF.write('#EXTINF:' + str(songLength) + ',' + str(song['title']) + '\n')
                fileName = make_valid(song['title'])+'.mp3'
                relPath = make_valid(song['artist']) + '/' + make_valid(song['album']) + '/' + fileName
                plistF.write(relPath + '\n')
                filePath = os.path.join(folder, os.path.join(make_valid(song['artist']), os.path.join(make_valid(song['album']), fileName)))
                albumFolder = os.path.split(filePath)[0] #TODO: make this before making filePath and use this way below for album art download
                if not os.path.exists(albumFolder):
                    os.makedirs(albumFolder)       #create structure
                if not os.path.exists(filePath):
                    url="" #placeholder to stop garbage collector
                    try:
                        url = api.get_stream_url(song['storeId'], working_device_id)
                    except Exception, err:
                        #TODO: add to failed list
                        print('error above')
                        print(traceback.format_exc())
                        #api.logout()#we could not do this I guess
                    finally:
                        Usong = song['Usong']
                        dialog_ui.set_downloading_label('Song')
                        dialog_ui.set_song_name(song['title'])
                        dialog_ui.set_album_name(song['album'])
                        dialog_ui.set_artist_name(song['artist'])
                        dialog_ui.set_genre_name(song['genre'])
                        print("downloading \'" + song['title'] + '\' from album \"' + song['album'] + "\"")
                    if not retrev(testfile, url, filePath):#testfile.retrieve(url, filePath)
                        try:
                            try:
                                meta2 = EasyID3(filePath)
                                #print('before: ' + str(meta2))
                                #meta = mutagen.id3.ID3
                                #audiofile = eyed3.load(filePath)
                                #f = audiofile
                                Usong = song['Usong']
                                meta2['title'] = Usong[u'title']
                                meta2['artist'] = Usong[u'artist']
                                meta2['genre'] = Usong.get(u'genre' "")
                                #meta2['tracknumber'] = int(song.get('trackNumber', 0))
                                #print('after: ' + str(meta2))
                                meta2.save()
                            except mutagen.id3.ID3NoHeaderError:
                                meta2 = mutagen.File(filePath, easy=True)
                                meta2.add_tags() #create the tag
                                #print('before: ' + str(meta2))
                                #meta = mutagen.id3.ID3
                                #audiofile = eyed3.load(filePath)
                                #f = audiofile
                                Usong = song['Usong']
                                meta2['title'] = Usong[u'title']
                                meta2['artist'] = Usong[u'artist']
                                meta2['genre'] = Usong.get(u'genre' "")
                                #meta2['tracknumber'] = int(song.get('trackNumber', 0))
                                #print('after: ' + str(meta2))
                                meta2.save()
                            audio = MP3(filePath)#, ID3=ID3)
                            imgLoc = os.path.split(filePath)[0] + 'cover.jpg'
                            dialog_ui.set_downloading_label('album cover')
                            retrev(albumget, song['albumArtRef'][0]['url'], imgLoc)
                            dialog_ui.set_downloading_label('waiting')
                            #imagedata = resize_image(imgLoc, 200, 200)
                            imgF = open(imgLoc, 'rb')
                            imagedata = imgF.read()
                            imgF.close() #good practice
                            #f.tag.images.set(0x08,imagedata,"image/jpeg",None)#3
                            audio.tags.add(
                                APIC(
                                    encoding=3, #3 for utf-8
                                    mime='image/jpeg', #or image/png
                                    type=3, #3 for cover image
                                    desc=u'Cover',
                                    data=imagedata
                                )
                            )
                        except Exception, err:
                            print('error above')
                            print(traceback.format_exc())
        plistF.close()
    print 'All done!'
    dialog.destroy()
def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
    
def convertKeys(input):#only does the keys
    if isinstance(input, dict):
        return {(convert(key), value) for (key, value) in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

#turns the song name/album/artist into something that can be a path (without characters that would cause problems)
def make_valid(fileName):
    fileName = fileName.translate(None, '#%&{}\\<>*?/$!\'\":+`|=.')
    fileName = fileName[:128]
    fileName = re.sub('[^a bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!-_]', '', fileName)
    return(fileName)

if __name__ == '__main__':
    pass #TODO: write something here to test

