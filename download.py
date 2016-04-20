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
import tkinter as tk

import config

from gmusicapi import Mobileclient
folder='/home/creaz/Music' #'C:\Users\john\Desktop\Unofficial-Google-Music-API-develop\playlists'
conf = config.config()
working_device_id = conf.get_device_id()
del conf

def prevent_quit(root):
    pass
    #override root.destroy() so we quit too
    root.destroy
    exit(0) #we stop the background code here too!

def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

def ask_for_credentials():
    """Make an instance of the api and attempts to login with it.
    Return the authenticated api.
    """

    # We're not going to upload anything, so the Mobileclient is what we want.
    api = Mobileclient()

    logged_in = False
    attempts = 0

    while not logged_in and attempts < 3:
        conf = config.config()
        
        email = conf.get_email()#raw_input('Email: ')
        password = conf.get_password() #get_pass()

        logged_in = api.login(email, password, Mobileclient.FROM_MAC_ADDRESS)
        attempts += 1

    return api

def dlProgress(count, blockSize, totalSize):
    percent = int(count*blockSize*100/totalSize)
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

def Quit(root):
    root.destroy()
    exit(0)

def App():
    root = tk.Tk()
    message = tk.StringVar()
    message.set("Logging in")
    frame = tk.Frame(root)
    tk.Label(root, textvariable=message).pack()
    tk.Button(root, text="Cancel", command=lambda root=root: Quit(root)).pack()
    root.protocol('WM_DELETE_WINDOW', lambda root=root: prevent_quit(root))
    root.after(500, lambda root=root, message=message: attempt_login(root, message)) #this will start the process after a half a second
    root.mainloop()

def attempt_login(root, message):
    api = ask_for_credentials()
    try:
        begin_login(root, message, api) #TODO: fix this garbage
    except:
        api.logout()

def begin_login(root, message, api):

    if not api.is_authenticated():
        print "Sorry, those credentials weren't accepted."
        message.set("Sorry, those credentials weren't accepted.")
        return

    print 'Successfully logged in.'
    print

    message.set("loading library")

    # Get all of the users songs.
    # library is a big list of dictionaries, each of which contains a single song.
    print 'Loading library...',
    #library = api.get_all_songs()
    print 'done.'
    root.destroy()
    #print len(library), 'tracks detected.'
    #print
    global plist
    global psongs
    plist = list()
    psongs = list()
    ###############
    #NAME OF PLIST#
    ############### #'better electronic', 'sleep', 'hipster party 8/6/15', 
    #pnames = ('2k', 'Download')#'sleep', 'awesome indie', 'epic indie', 'before it breaks', 'sleep', 'hipster party 8/6/15')
    #pname = 'Download' #2k
    all_lists = api.get_all_user_playlist_contents()
    pnames = list()
    for Playlist in all_lists[41:]:
        pnames.append(Playlist['name'])
    llength = len(pnames);
    lcurrent = 0; #current playlist number
    for pname in pnames:
        lcurrent = lcurrent+1;
        playlists = api.get_all_user_playlist_contents() #gets all the playlists
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
            #Usong = convertKeys(Usong)
            #print Usong
            Usong = Usong.get('track', Usong.get(u'track')) #we only want the track portion
            try:
               song['track']['Usong'] = Usong #store unicode for later
               #print(song['track']['title'])
               psongs.append(song['track'])
            except Exception:
               print("failed on song "+str(song))
        #we now have all the playlists
        del playlists
        dsongs = list() #list of songs to download with full metadata
        #working_device_ids = web.get_registered_devices()
        #working_device_id = convert(working_device_ids[0])['id']
        print(working_device_id) #= conf.get_device_id()
       # for song in psongs:
       #     print(song)
       #dsongs.append(song)#api.get_track_info(song)) #add song to list
        dsongs = psongs
        """urllib.poolManager(
            cert_reqs='CERT_REQUIRED',
            ca_certs=certifi.where(),
            )"""
        testfile = urllib.URLopener()
        albumget = urllib.URLopener()
        print(len(dsongs))
        #print(dsongs[0])
        nonList = list()
        song = dsongs[0]
        m3uPath = os.path.join(folder, pname+'.m3u')
        if os.path.exists(m3uPath):
            os.remove(m3uPath) #delete previous list
        with open(m3uPath, 'w') as plistF:
            plistF.write('#EXTM3U\n') #write starting tag
            for i in range(0, len(dsongs), 1):#TODO remove \\ as it confuses the download manager for path in filename
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
			print('error above')
			print(traceback.format_exc())
                        api.logout()
                        exit(0)
		    finally:
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
                            retrev(albumget, song['albumArtRef'][0]['url'], imgLoc)
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
                            #pic = APIC(3, u'image/jpeg', 3, u'Front cover', imagedata) #create APIC Frame
                            #audio.tags.add(pic)
                            audio.save(v1=2)# if 2, ID3v1 tags will be created and/or updated
                            #f = eyed3.id3.Tag()
                            #eyed3.id3.Tag.save(
                            #f.link(filePath)
                            #audiofile.initTag()
                            #f.tag.setVersion([2,3,0])
                            #audiofile.initTag()
                            #audiofile.id3.artist = Usong[u'artist']
                            #f.tag.artist = Usong[u'artist']
                            #f.tag.album = Usong[u'album']
                            #f.tag.album_artist = Usong[u'albumArtist']#TODO fix this
                            #f.tag.title = Usong[u'title']
                            #f.tag.track_num = song.get('trackNumber', 0)
                            #f.tag.genre = Usong.get(u'genre' "")
                            #f.tag.lyrics.set(Usong TODO later... I guess?
                            #f.tag.play_count = song.get('playCount', 0)
                            #if(song['year']!=None):#TODO fixs
                            """try:
                                f.tag.recording_date = song.get('year', None)
                            except:
                                pass
                            f.tag.disc_num = song.get('discNumber', 0) #0x03
                            try:
                                os.remove(folder+'\\albumArtTemp.jpg')
                                print('removed old art temp')
                            except:
                                pass"""
                            #retrev(albumget, song['albumArtRef'][0]['url'], folder+'\\albumArtTemp.jpg')
                            #imagedata = resize_image(folder+'\\albumArtTemp.jpg', 200, 200)
                            #f.tag.images.set(0x08,imagedata,"image/jpeg",None)#3
                            #f.tag.images.set(0x08, None, None, img_url=song['albumArtRef'][0]['url']) #description = u""
                            #print f.tag
                            #f.tag.update()
                            #f.tag.save()#version=ID3_V2_4, preserve_file_time=True)
                        except Exception, err:
                            print('error above')
                            print(traceback.format_exc())
                """except IOError, m:
                    print "had error with this file"
                    nonList.append(song)
                ""try:
                    id3info = ID3(filePath)
                    print id3info
                    id3info['TITLE'] = song['title']
                    id3info['ARTIST'] = song['artist']
                    id3info['ALBUM'] = song['album']
                    id3info['COMPOSER'] = song['composer']
                except InvalidTagError, message:
                    print "Invalid ID3 tag:", message"""
        plistF.close()
    # It's good practice to logout when finished.
    api.logout()
    print 'All done!'
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
def make_valid(fileName):
    fileName = fileName.translate(None, '#%&{}\\<>*?/$!\'\":+`|=.')
    fileName = fileName[:128]
    fileName = re.sub('[^a bcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!-_]', '', fileName)
    return(fileName)

if __name__ == '__main__':
    App()

