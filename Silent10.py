# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
import time, random, sys, re, os, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib2, wikipedia,tempfile,glob,shutil,unicodedata,goslate,urllib3,html5lib
from gtts import gTTS


ke = LINETCR.LINE()
ke.login(token='EvUHPxP02dkveJgFnlne.3gYgoFqhnGt2d8T4Rxr4pG.2a8ZROltuctJFdVU5mSIX+R/SSiLccgjEXQSYG4+8tI=')


ki = LINETCR.LINE()
ki.login(token='EvUHPxP02dkveJgFnlne.3gYgoFqhnGt2d8T4Rxr4pG.2a8ZROltuctJFdVU5mSIX+R/SSiLccgjEXQSYG4+8tI=')
				 
kk = LINETCR.LINE()
kk.login(token='Ev7tiB4bEmmLwFyOKSU6.Q6xIDlEHSbAo5xQ0btG/TG.ON7HfNZAVKauHS7bcC6w7PGyPEc2VFdvoAG6OTGQPBE=')

kc = LINETCR.LINE()
kc.login(token='EvzdlhyhujwcalqoKuxb.j0UXFKRs7dy+/0MJoY6x2W.r09L8afjpe7Xci9MZCLFfsw8wT1NqeFIOwvreyxZ9/I=')

ks = LINETCR.LINE()
ks.login(token='EvxipQCQE6VZLaRZYmi6.z1isnjxuFVqKLrc5MOVULG.74K+WGWxsoZfUaNUpCQ6xBjK1yGcdq7uwu7lDf4znak=')

kt = LINETCR.LINE()
kt.login(token='EvRkIEduO8g9DSsyU5L2.Gf7TsLV4CfuLnq48Pxi4CG.ZAvciuwGp7mO6Jw88YL1A5bvN7j2+NNYBNPIXeh9wWY=')

ka = LINETCR.LINE()
ka.login(token='Ev8xu3vM1OASG5KxvNjd.p1zRh4stv2b2yZf6gJEtZq.P7Y6O+6uePpz77DBK12+c8RArB5IMd4iqrQ1deUqWho=')

kb = LINETCR.LINE()
kb.login(token='EvUzLheKJ3aeizvGEx85.WC83nwBFW3Fe2WGaGduzfq.dQc9/zTfREcMWEsk11MlSvvuZupxqe6cCUnB9ucC4Nc=')

ko = LINETCR.LINE()
ko.login(token='EvwJNZWYDjep2jPOXioe./GMO2qK6yM2XPFA7d5YKVG.JVmpjorS25p7dxe9RnUNLfAxK8l+Yhm6REJeg5xQIH4=')
				 
cl = LINETCR.LINE()
cl.login(token='EvwJNZWYDjep2jPOXioe./GMO2qK6yM2XPFA7d5YKVG.JVmpjorS25p7dxe9RnUNLfAxK8l+Yhm6REJeg5xQIH4=')

satpam = LINETCR.LINE() #satpam
satpam.login(token='EvwJNZWYDjep2jPOXioe./GMO2qK6yM2XPFA7d5YKVG.JVmpjorS25p7dxe9RnUNLfAxK8l+Yhm6REJeg5xQIH4=')


print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage= """
    •◇●☯Menu Bot☯●◇•
😡😡😡😡😡😡😡😡😡
||🛠 ʜɢ - ʜᴇʟᴘ ɢʀᴏᴜᴘ
||🛠 ʜᴀ - ʜᴇʟᴘ ᴀᴅᴍɪɴ
||🛠 ʜᴋ - ʜᴇʟᴘ ᴋɪᴄᴋᴇʀ
||🛠 ʜᴘ - ʜᴇʟᴘ ᴘʀᴏᴛᴇᴄᴛ
||🛠 sᴇᴛ - ɢʀᴏᴜᴘ sᴇᴛᴛɪɴɢs
😡😡😡😡😡😡😡😡😡
    ◇☆●»ֆւՅո ճՓե●☆«◇
 """

hgMessage ="""
•○●☯Help Group☯●○•                          
 😡😡😡😡 😡😡😡😡😡                                                                                                                           
╠❂͜͡➣ Comment:[text]
╠❂͜͡➣ Group name:[text]️
╠❂͜͡➣ Admin on @[name]
╠❂͜͡➣ Expel on @[name]
╠❂͜͡➣ Expelall
╠❂͜͡➣ Steal name    @[name]
╠❂͜͡➣ Steal Bio     @[name]
╠❂͜͡➣ Steal status  @[name]
╠❂͜͡➣ Steal mid     @[name]
╠❂͜͡➣ Steal contact @[name]
╠❂͜͡➣ Steal cover   @[name]
╠❂͜͡➣ Steal pict    @[name]
╠❂͜͡➣ Steal group pict
╠❂͜͡➣ Mimic target @[name]
╠❂͜͡➣ Mimic untarget @[name]
╠❂͜͡➣ Mimic on
╠❂͜͡➣ Midpict:[mid]
╠❂͜͡➣ Copy @[name]
╠❂͜͡➣ gift1-15
╠❂͜͡➣ Spam gift
╠❂͜͡➣ Mimic list
╠❂͜͡➣ Spamg[on/off][no][txt]
╠❂͜͡➣ Spam add:[text]
╠❂͜͡➣ Spam change:[text]
╠❂͜͡➣ Spam start:[number]
╠❂͜͡➣ Me
╠❂͜͡➣ Spam @[name]
╠❂͜͡➣ Mention all
╠❂͜͡➣ Lyric [][]
╠❂͜͡➣ Music [][]
╠❂͜͡➣ Wiki [text]
╠❂͜͡➣ Vidio [text]
╠❂͜͡➣ Youtube [text]
╠❂͜͡➣ Instagram [text]
╠❂͜͡➣ Translate-eng [text]
╠❂͜͡➣ Translate-thai [text]
╠❂͜͡➣ Time
╠❂͜͡➣ Speed
╠❂͜͡➣ Debug speed
╠❂͜͡➣ Creator
╠❂͜͡➣ Owner
╠❂͜͡➣ Responsename
╠❂͜͡➣ Help
╠❂͜͡➣ Cek
╠❂͜͡➣ Ciduk
╠❂͜͡➣ Setlastpoint
╠❂͜͡➣ Viewlastseen
╠❂͜͡➣ Remove chat
╠❂͜͡➣ Details grup:
😡😡😡😡😡😡😡😡😡
      ◇☆●»ֆւՅո ճՓե●☆«◇
"""

hpMessage = """
     🛠🛠Help Protect🛠🛠
 😡😡😡😡😡😡😡😡
╠❂͜͡➣ Turn off bots
╠❂͜͡➣ Bot restart
╠❂͜͡➣ Backup:on/off
╠❂͜͡➣ Protect:low
╠❂͜͡➣ Protect:hight
╠❂͜͡➣ Protect on
╠❂͜͡➣ Cancl on
╠❂͜͡➣ Qr on
╠❂͜͡➣ Joinn on
╠❂͜͡➣ Auto blockqr:on/off
╠❂͜͡➣ Blockinvite:on/off
╠❂͜͡➣ Auto notice:on/off
😡😡😡😡😡😡😡😡😡😡
    ◇☆●»ֆւՅո ճՓե●☆«◇
"""

haMessage ="""
 ️    🛠🛠Help Admin🛠🛠
 😡😡😡😡😡😡😡😡😡😡
╠❂͜͡➣ Ban    @[name]
╠❂͜͡➣ Unban  @[name]
╠❂͜͡➣ Ban group:
╠❂͜͡➣ Del ban:
╠❂͜͡➣ List ban group
╠❂͜͡➣ Banned[send contact]
╠❂͜͡➣ Unbanned[send contact]
╠❂͜͡➣ Ban repeat @[name]
╠❂͜͡➣ Blacklist all
╠❂͜͡➣ Ban cek
╠❂͜͡➣ Clear banlist
╠❂͜͡➣ Add friend @[name]
╠❂͜͡➣ Target @[name]
╠❂͜͡➣ Del target @[name]
╠❂͜͡➣ Target list
╠❂͜͡➣ Invite:[mid]
╠❂͜͡➣ Invite user[contact]
╠❂͜͡➣ Invite me
╠❂͜͡➣ Kuy
╠❂͜͡➣ Join group
╠❂͜͡➣ Masuk
╠❂͜͡➣ Pulang
╠❂͜͡➣ Bye
╠❂͜͡➣ Keluar [own]
╠❂͜͡➣ Leave group:️
╠❂͜͡➣ Auto join:on/off
╠❂͜͡➣ Auto leave:on/off
╠❂͜͡➣ Group list
╠❂͜͡➣ Banlist
╠❂͜͡➣ Admin list
╠❂͜͡➣ Set
╠❂͜͡➣ Auto add:on/off
╠❂͜͡➣ Comment:on/off
╠❂͜͡➣ Gcancel:[number]
╠❂͜͡➣ Pm cast   [text]
╠❂͜͡➣ Broadcast [text]
╠❂͜͡➣ Kembali ke asli
😡😡😡😡😡😡😡😡😡😡
      ◇☆●»ֆւՅո ճՓե●☆«◇
"""

hkMessage ="""
    🛠🛠Help Kickers🛠🛠
 😡😡😡😡😡😡😡😡😡
╠❂͜͡➣ Rejectall
╠❂͜͡➣ Clean invites
╠❂͜͡➣ Clear invites
╠❂͜͡➣ Mulai
╠❂͜͡➣ Bubar️
╠❂͜͡➣ Tampol @
╠❂͜͡➣ Boom @
╠❂͜͡➣ Anu @
╠❂͜͡➣ Nk @
╠❂͜͡➣ Crash
╠❂͜͡➣ Vkick @
╠❂͜͡➣ Kick:[mid]
╠❂͜͡➣ Link open
╠❂͜͡➣ Link close
╠❂͜͡➣ Gurl
╠❂͜͡➣ Recover
😡😡😡😡😡😡😡😡😡
     ◇☆●»ֆւՅո ճՓե●☆«◇
"""

KAC=[cl,ki,kk,kc,ks,kt,ka,kb,ko,ke,satpam]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ks.getProfile().mid
Emid = kt.getProfile().mid
Fmid = ka.getProfile().mid
Gmid = kb.getProfile().mid
Hmid = ko.getProfile().mid
Imid = ke.getProfile().mid
Smid = satpam.getProfile().mid #satpam

protectname = []
protecturl = []
protection = []
autocancel = {}
autoinvite = []
autoleaveroom = []
targets = []
Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Smid]
admin = ["u58714149295f212f741f18624cbba58d","ube297e99e4fe2065c2895823a0022616","ufe4be13b976a5dfcadb6ffda86175907"]
owner = ["u58714149295f212f741f18624cbba58d","ufe4be13b976a5dfcadb6ffda86175907","ube297e99e4fe2065c2895823a0022616"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True, "members":1},
    'leaveRoom':False,
    'timeline':False,
    'autoAdd':False,
    'message':"Thanks for add Me  ◇☆●»ֆւՅո ճՓե●☆«◇\n\nOwner bot : http://line.me/ti/p/~dhenz415",
    "lang":"JP",
    "comment":"",
    "welmsg":"",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "status":False,
    "likeOn":False,
    "pname":True,
    "blacklist":{},
    "whitelist":{},
    "wblacklist":False,
    "dblacklist":False,
    "qr":True,
    "welcomemsg":False,
    "Backup":True,
    "AutoKick":True,
    "protectionOn":True,
    "Protectgr":True,
    "Protectjoin":False,
    "Protectcancl":True,
    "Protectcancel":False,
    "winvite":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
    "atjointicket":True
    }
wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

wait3 = {
    "copy":False,
    "copy2":"target",
    "target":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
}


setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kk.getProfile()
backup = kk.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kc.getProfile()
backup = kc.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ks.getProfile()
backup = ks.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kt.getProfile()
backup = kt.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ka.getProfile()
backup = ka.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kb.getProfile()
backup = kb.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ko.getProfile()
backup = ko.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ke.getProfile()
backup = ke.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus


contact = satpam.getProfile()
backup = satpam.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print error
def sendMessage(self, messageObject):
        return self.Talk.client.sendMessage(0,messageObject)

def sendText(self, Tomid, text):
        msg = Message()
        msg.to = Tomid
        msg.text = text

        return self.Talk.client.sendMessage(0, msg)
def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._client.sendMessage(M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
        return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e
 
def post_content(self, urls, data=None, files=None):
        return self._session.post(urls, headers=self._headers, data=data, files=files)
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def NOTIFIED_READ_MESSAGE(op):
    print op
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name + datetime.now().strftime(' [%d - %H:%M:%S]')
                wait2['ROM'][op.param1][op.param2] = "・" + Name + " ツ"
        else:
            pass
    except:
        pass
def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait2['readPoint']:
                    if msg.from_ in wait2["ROM"][msg.to]:
                        del wait2["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
          
    except KeyboardInterrupt:
				sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

	if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]: cl.rejectGroupInvitation(op.param1)
            else:
		Inviter = op.param3.replace("^^",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)

	if op.type == 13:
            if mid in op.param3:
              if wait["autoJoin"] == True:
 	        if op.param2 in Bots and admin:
                  cl.acceptGroupInvitation(op.param1)
                  print "BOT 1 Joined"
              else:
                print "autoJoin is Off"

	    if Amid in op.param3:
              if wait["autoJoin"] == True:
		if op.param2 in Bots and admin:
                  ki.acceptGroupInvitation(op.param1)
                  print "BOT 2 Joined"
              else:
                  print "autoJoin is Off"

	    if Bmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots and admin:
                  kk.acceptGroupInvitation(op.param1)
                  print "BOT 3 Joined"
              else:
                  print "autoJoin is Off"

 	    if Cmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots and admin:
                  kc.acceptGroupInvitation(op.param1)
                  print "BOT 4 Joined"
              else:
                  print "autoJoin is Off"

	    if Dmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots and admin:
                  ks.acceptGroupInvitation(op.param1)
                  print "BOT 5 Joined"
              else:
                  print "autoJoin is Off"

	    if Emid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots and admin:
                  kt.acceptGroupInvitation(op.param1)
                  print "BOT 6 Joined"
              else:
                  print "autoJoin is Off"

	    if Fmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots and admin:
                  ka.acceptGroupInvitation(op.param1)
                  print "BOT 7 Joined"
              else:
                  print "autoJoin is Off"

	    if Gmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots and admin:
                  kb.acceptGroupInvitation(op.param1)
                  print "BOT 8 Joined"
              else:
                  print "autoJoin is Off"

	    if Hmid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots and admin:
                  ko.acceptGroupInvitation(op.param1)
                  print "BOT 9 Joined"
              else:
                  print "autoJoin is Off"

	    if Imid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots and admin:
                  ke.acceptGroupInvitation(op.param1)
                  print "BOT 10 Joined"
              else:
                  print "autoJoin is Off"

	    if Smid in op.param3:
              if wait["autoJoin"] == True:
                if op.param2 in Bots and admin:
                  satpam.acceptGroupInvitation(op.param1)
                  print "BOT 11 Joined"
              else:
                  print "autoJoin is Off"

#-------------------------------------------
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n・ " + Name + datetime.today().strftime(' [%d - %H:%M:%S]')
                        wait2['ROM'][op.param1][op.param2] = "・ " + Name
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    pass
            except:
                pass
#-------------------NOTIFIED_READ_MESSAGE----------------
        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
#------------------------------------------
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['pname']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                        try:
                            G = ki.getGroup(op.param1)
                        except:
                            try:
                                G = kk.getGroup(op.param1)
                            except:
                                try:
                                    G = kc.getGroup(op.param1)
                                except:
                                    try:
                                        G = ks.getGroup(op.param1)
				    except:
					try:
                                            G = kt.getGroup(op.param1)
					except:
					    try:
						G = ka.getGroup(op.param1)
					    except:
						try:
						    G = kb.getGroup(op.param1)
						except:
						    try:
							G = ko.getGroup(op.param1)
						    except:
							try:
							    G = ke.getGroup(op.param1)
							except:
							    try:
								G = ku.getGroup(op.param1)
							    except:
								try:
								    G = satpam.getGroup(op.param1)
                                       			        except:
                                           			    pass
                    G.name = wait['pro_name'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                        try:
                            ki.updateGroup(G)
                        except:
                            try:
                                kk.updateGroup(G)
                            except:
                                try:
                                    kc.updateGroup(G)
                                except:
                                    try:
                                        ks.updateGroup(G)
                                    except:
                                        try:
                                            kt.updateGroup(G)
					except:
					    try:
						ka.updateGroup(G)
					    except:
						try:
						    kb.updateGroup(G)
						except:
						    try:
							ko.updateGroup(G)
						    except:
							try:
							    ke.updateGroup(G)
							except:
							    try:
								ku.updateGroup(G)
							    except:
								try:
								    satpam.updateGroup(G)
                                       				except:
                                           			    pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                except:
                                    try:
                                        ks.kickoutFromGroup(op.param1,[op.param2])
                                    except:
                                        try:
                                            kt.kickoutFromGroup(op.param1,[op.param2])
					except:
					    try:
				  		ka.kickoutFromGroup(op.param1,[op.param2])
			  		    except:
			 		        try:
	 					    kb.kickoutFromGroup(op.param1,[op.param2])
						except:
						    try:
							ko.kickoutFromGroup(op.param1,[op.param2])
						    except:
							try:
							    ke.kickoutFromGroup(op.param1,[op.param2])
							except:
							    try:
								ku.kickoutFromGroup(op.param1,[op.param2])
							    except:
								try:
								    satpam.kickoutFromGroup(op.param1,[op.param2])
                                       				except:
                                           			    pass
                                       			        kk.sendText(op.param1,"jngn buka qr njirr-_-")
                                    			        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                                       			        c.contentMetadata={'mid':op.param2}
                                     			        cl.sendMessage(c)

        if op.type == 13:
                if op.param3 in mid:
                    if op.param2 in Amid:
                        G = ki.getGroup(op.param1)
                        G.preventJoinByTicket = False
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        Ticket = ki.reissueGroupTicket(op.param1)

                if op.param3 in Amid:
                    if op.param2 in Bmid:
                        X = kk.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kk.updateGroup(X)
                        Ti = kk.reissueGroupTicket(op.param1)

                if op.param3 in Bmid:
                    if op.param2 in Cmid:
                        X = kc.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kc.updateGroup(X)
                        Ti = kc.reissueGroupTicket(op.param1)
                if op.param3 in Cmid:
                    if op.param2 in Dmid:
                        X = ks.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ks.updateGroup(X)
                        Ti = ks.reissueGroupTicket(op.param1)
                if op.param3 in Dmid:
                    if op.param2 in Emid:
                        X = kt.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kt.updateGroup(X)
                        Ti = kt.reissueGroupTicket(op.param1)
                        ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kt.updateGroup(X)
                        Ti = kt.reissueGroupTicket(op.param1)
                if op.param3 in Emid:
                    if op.param2 in Fmid:
                        X = ka.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ka.updateGroup(X)
                        Ti = ka.reissueGroupTicket(op.param1)
                        kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ka.updateGroup(X)
                        Ti = ka.reissueGroupTicket(op.param1)
		if op.param3 in Fmid:
                    if op.param2 in Gmid:
                        X = kb.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        kb.updateGroup(X)
                        Ti = kb.reissueGroupTicket(op.param1)
                        ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        kb.updateGroup(X)
                        Ti = kb.reissueGroupTicket(op.param1)
		if op.param3 in Gmid:
                    if op.param2 in Hmid:
                        X = ko.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)
                        kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ko.updateGroup(X)
                        Ti = ko.reissueGroupTicket(op.param1)
		if op.param3 in Hmid:
                    if op.param2 in Imid:
                        X = ke.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
                        ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        ke.updateGroup(X)
                        Ti = ke.reissueGroupTicket(op.param1)
		if op.param3 in Imid:
                    if op.param2 in Smid:
                        X = satpam.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        satpam.updateGroup(X)
                        Ti = satpam.reissueGroupTicket(op.param1)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        satpam.updateGroup(X)
                        Ti = satpam.reissueGroupTicket(op.param1)
		if op.param3 in Smid:
                    if op.param2 in mid:
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
                        satpam.acceptGroupInvitationByTicket(op.param1,Ticket)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        Ti = cl.reissueGroupTicket(op.param1)
#=========================================================================
         
                
#===========================================
        if op.type == 32:
            if not op.param2 in Bots and admin:
                if wait["protectionOn"] == True: 
                    try:
                        klist=[ki,kk,kc,ks,kt,ka,kb,ko,ke]
                        kicker = random.choice(klist) 
                        G = kicker.getGroup(op.param1)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        kicker.inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                       print e
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
            if Amid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ki.rejectGroupInvitation(op.param1)
                        else:
                            ki.acceptGroupInvitation(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ki.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ki.cancelGroupInvitation(op.param1, matched_list)
            if Bmid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            kk.rejectGroupInvitation(op.param1)
                        else:
                            kk.acceptGroupInvitation(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        kk.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    kk.cancelGroupInvitation(op.param1, matched_list)
            if Cmid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            kc.rejectGroupInvitation(op.param1)
                        else:
                            kc.acceptGroupInvitation(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        kc.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("^^",',')   
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    kc.cancelGroupInvitation(op.param1, matched_list)

        if op.type == 17:
            if op.param3 in wait["blacklist"]:
                if not op.param2 in Bots and admin: 
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param3])
                    cl.sendText(op.param1,"blacklist users are not allowed to sign in  -_-")
                    c = Message(to=op.param1, from_=None, text=None, contentType=13)
                    c.contentMetadata={'mid':op.param3}
                    cl.sendMessage(c)
        if op.type == 17:
            if wait["Protectjoin"] == True:
              if op.param2 not in Bots and admin:
                if op.param2 in Bots:
                  pass
		elif op.param2 in admin:
                  pass
                elif op.param2 in owner:
                  pass
                else:
                  try:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    ki.sendText(op.param1, "Ketangkis kan wkwkwkwk")
                  except:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    ki.sendText(op.param1, "Ketangkis kan wkwkwkwk")
        if op.type == 11:
            if not op.param2 in Bots and admin:
              if wait["qr"] == True:
                try:
                    klist=[ki,kk,kc,ks,kt,ka,kb,ko,ke]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                except Exception, e:
                    print e
	if op.type == 11:
          if wait["Protectgr"] == True:
            if op.param2 not in Bots and admin:
              G = random.choice(KAC).getGroup(op.param1)
              G.preventJoinByTicket = True
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).updateGroup(G)
        if op.type == 11:
            if not op.param2 in Bots and admin:
              if wait["protectionOn"] == True:
                 try:
                    klist=[ki,kk,kc,ks,kt,ka,kb,ko,ke]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                    kicker.kickoutFromGroup(op.param1,[op.param2])
                    G.preventJoinByTicket = True
                    kicker.updateGroup(G)
                    ki.sendText(op.param1,"jngn songong njirr-_-")
                    c = Message(to=op.param1, from_=None, text=None, contentType=13)
                    c.contentMetadata={'mid':op.param2}
                    ki.sendMessage(c)

                 except Exception, e:
                           print e
        if op.type == 13:
            G = cl.getGroup(op.param1)
            I = G.creator
            if not op.param2 in Bots and admin:
                if wait["protectionOn"] == True:
                    klist=[ki,kk,kc,ks,kt,ka,kb,ko,ke]
                    kicker = random.choice(klist)
                    G = kicker.getGroup(op.param1)
                    if G is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        kicker.cancelGroupInvitation(op.param1, gInviMids)
                        kicker.kickoutFromGroup(op.param1,[op.param2])
                        ki.sendText(op.param1,"jngn rusuh njirr-_-")
                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                        c.contentMetadata={'mid':op.param2}
                        ki.sendMessage(c)
	if op.type == 13:
             if wait["Protectcancl"] == True:
                   if op.param2 not in Bots and admin:
                      group = cl.getGroup(op.param1)
                      gMembMids = [contact.mid for contact in group.invitee]
                      random.choice(KAC).cancelGroupInvitation(op.param1,gMembMids)
	if op.type == 13: #awal 17 ubah 13
             if wait["Protectjoin"] == True:
                   if op.param2 not in admin and Bots : # Awalnya admin doang
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        if op.type == 15:
             if op.param2 in admin and Owner:
                random.choice(KAC).inviteIntoGroup(op.param1,[op.param2])
								
        if op.type == 19:
             if op.param2 in Bots:
                   if op.param3 in admin:
                      random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
										
        if op.type == 19:
             if not op.param2 in Bots:
                   if op.param3 in admin:
                      random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
	if op.type == 19:
             if op.param3 in Smid: #Akun Utama Ke Kick
		      G = random.choice(KAC).getGroup(op.param1)
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      G.preventJoinByTicket = False
                      random.choice(KAC).updateGroup(G)
                      Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
                      satpam.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      G.preventJoinByTicket = True
		      random.choice(KAC).updateGroup(G)
                      satpam.updateGroup(G)
		      satpam.leaveGroup(op.param1)
                      wait["blacklist"][op.param2] = True
	     if op.param3 in mid: #Akun Utama/Selbot Ke Kick
		      G = random.choice(KAC).getGroup(op.param1)
                      G.preventJoinByTicket = False
                      ki.updateGroup(G)
		      Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
		      satpam.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      satpam.kickoutFromGroup(op.param1,[op.param2])
		      G = satpam.getGroup(op.param1)
                      G.preventJoinByTicket = False
                      satpam.updateGroup(G)
		      satpam.reissueGroupTicket(op.param1)
		      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
		      time.sleep(0.01)
		      G.preventJoinByTicket = True
		      ki.updateGroup(G)
                      satpam.updateGroup(G)
		      satpam.leaveGroup(op.param1)
                      wait["blacklist"][op.param2] = True
	     if op.param3 in mid:
		   if op.param2 in Amid:
		      G = ki.getGroup(op.param1)
		      G.preventJoinByTicket = False
		      ki.updateGroup(G)
                      Ticket = ki.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
		      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
     		      time.sleep(0.01)
		      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
		      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
		      time.sleep(0.01)
		      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      G.preventJoinByTicket = True
                      ki.updateGroup(G)
                   else:
		      G = ki.getGroup(op.param1)
                      ki.kickoutFromGroup(op.param1,[op.param2])
                      G.preventJoinByTicket = False
                      ki.updateGroup(G)
                      Ticket = ki.reissueGroupTicket(op.param1)
		      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      G.preventJoinByTicket = True
		      cl.updateGroup(G)
                      ki.updateGroup(G)
                      wait["blacklist"][op.param2] = True
	     if op.param3 in Amid:
                   if op.param2 in Bmid:
                      G = kk.getGroup(op.param1)
                      G.preventJoinByTicket = False
                      kk.updateGroup(G)
                      Ticket = kk.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      G.preventJoinByTicket = True
                      kk.updateGroup(G)
		   else:
                      G = kk.getGroup(op.param1)
                      kk.kickoutFromGroup(op.param1,[op.param2])
                      G.preventJoinByTicket = False
                      kk.updateGroup(G)
                      Ticket = kk.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
	    	      G.preventJoinByTicket = True
                      kk.updateGroup(G)
	     if op.param3 in Bmid:
                   if op.param2 in Cmid:
                      G = kc.getGroup(op.param1)
                      G.preventJoinByTicket = False
                      kc.updateGroup(G)
                      Ticket = kc.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      G.preventJoinByTicket = True
                      kc.updateGroup(G)
                   else:
		      G = kc.getGroup(op.param1)
                      kc.kickoutFromGroup(op.param1,[op.param2])
                      G.preventJoinByTicket = False
                      kc.updateGroup(G)
                      Ticket = kc.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
	  	      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      G.preventJoinByTicket = True
                      kc.updateGroup(G)
	     if op.param3 in Cmid:
                   if op.param2 in Dmid:
                      G = ks.getGroup(op.param1)
                      G.preventJoinByTicket = False
                      ks.updateGroup(G)
                      Ticket = ks.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      G.preventJoinByTicket = True
                      ks.updateGroup(G)
                   else:
		      G = ks.getGroup(op.param1)
                      ks.kickoutFromGroup(op.param1,[op.param2])
                      G.preventJoinByTicket = False
                      ks.updateGroup(G)
                      Ticket = ks.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      G.preventJoinByTicket = True
                      ks.updateGroup(G)
	     if op.param3 in Dmid:
                   if op.param2 in Emid:
                      G = kt.getGroup(op.param1)
                      G.preventJoinByTicket = False
                      kt.updateGroup(G)
                      Ticket = kt.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      G.preventJoinByTicket = True
                      kt.updateGroup(G)
		   else:
                      G = kt.getGroup(op.param1)
                      kt.kickoutFromGroup(op.param1,[op.param2])
                      G.preventJoinByTicket = False
                      kt.updateGroup(G)
                      Ticket = kt.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      G.preventJoinByTicket = True
                      kt.updateGroup(G)
	     if op.param3 in Emid:
                   if op.param2 in Fmid:
                      G = ka.getGroup(op.param1)
                      G.preventJoinByTicket = False
                      ka.updateGroup(G)
                      Ticket = ka.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      G.preventJoinByTicket = True
                      ka.updateGroup(G)
                   else:
		      G = ka.getGroup(op.param1)
                      ka.kickoutFromGroup(op.param1,[op.param2])
                      G.preventJoinByTicket = False
                      ka.updateGroup(G)
                      Ticket = ka.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      G.preventJoinByTicket = True
                      ka.updateGroup(G)
	     if op.param3 in Fmid:
                   if op.param2 in Gmid:
                      G = kb.getGroup(op.param1)
                      G.preventJoinByTicket = False
                      kb.updateGroup(G)
                      Ticket = kb.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      G.preventJoinByTicket = True
                      kb.updateGroup(G)
                   else:
		      G = kb.getGroup(op.param1)
                      kb.kickoutFromGroup(op.param1,[op.param2])
                      G.preventJoinByTicket = False
                      kb.updateGroup(G)
                      Ticket = kb.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      G.preventJoinByTicket = True
		      kb.updateGroup(G)
	     if op.param3 in Gmid:
                   if op.param2 in Hmid:
                      G = ko.getGroup(op.param1)
                      G.preventJoinByTicket = False
                      ko.updateGroup(G)
                      Ticket = ko.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      G.preventJoinByTicket = True
                      ko.updateGroup(G)
                   else:
		      G = ko.getGroup(op.param1)
                      ko.kickoutFromGroup(op.param1,[op.param2])
                      G.preventJoinByTicket = False
                      ko.updateGroup(G)
                      Ticket = ko.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      G.preventJoinByTicket = True
                      ko.updateGroup(G)
	     if op.param3 in Hmid:
                   if op.param2 in Imid:
                      G = ke.getGroup(op.param1)
                      G.preventJoinByTicket = False
                      ke.updateGroup(G)
                      Ticket = ke.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      G.preventJoinByTicket = True
                      ke.updateGroup(G)
                   else:
		      G = ke.getGroup(op.param1)
                      ke.kickoutFromGroup(op.param1,[op.param2])
                      G.preventJoinByTicket = False
                      ke.updateGroup(G)
                      Ticket = ke.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      G.preventJoinByTicket = True
                      ke.updateGroup(G)
	     if op.param3 in Imid:
                   if op.param2 in Jmid:
                      G = ku.getGroup(op.param1)
                      G.preventJoinByTicket = False
                      ku.updateGroup(G)
                      Ticket = ku.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      G.preventJoinByTicket = True
                      ku.updateGroup(G)
                   else:
		      G = ku.getGroup(op.param1)
                      ku.kickoutFromGroup(op.param1,[op.param2])
                      G.preventJoinByTicket = False
                      ku.updateGroup(G)
                      Ticket = ku.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
		      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      G.preventJoinByTicket = True
		      ku.updateGroup(G)
	     if op.param3 in Jmid:
                   if op.param2 in mid:
                      G = cl.getGroup(op.param1)
                      G.preventJoinByTicket = False
                      cl.updateGroup(G)
                      Ticket = cl.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      G.preventJoinByTicket = True
                      cl.updateGroup(G)
                   else:
		      G = cl.getGroup(op.param1)
                      cl.kickoutFromGroup(op.param1,[op.param2])
                      G.preventJoinByTicket = False
                      cl.updateGroup(G)
                      Ticket = cl.reissueGroupTicket(op.param1)
                      cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ks.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kt.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ko.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      ku.acceptGroupInvitationByTicket(op.param1,Ticket)
                      time.sleep(0.01)
                      G.preventJoinByTicket = True
                      cl.updateGroup(G)
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		      random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])

        if op.type == 19:
                if not op.param2 in Bots:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = kk.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass

                    except Exception, e:
                        print e
                if not op.param2 in Bots and admin:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
                if not op.param2 in Bots and admin:
                  if wait["protectionOn"] == True:  
                   try:
                       klist=[ki,kk,kc,ks,kt,ka,kb,ko,ke]
                       kicker = random.choice(klist)
                       G = kicker.getGroup(op.param1)
                       G.preventJoinByTicket = False
                       kicker.updateGroup(G)
                       invsend = 0
                       Ticket = kicker.reissueGroupTicket(op.param1)
                       kl.acceptGroupInvitationByTicket(op.param1,Ticket)
                       time.sleep(0.2)
                       X = kicker.getGroup(op.param1)             
                       X.preventJoinByTicket = True
                       kl.kickoutFromGroup(op.param1,[op.param2])
                       kicker.kickoutFromGroup(op.param1,[op.param2])
                       kl.leaveGroup(op.param1)
                       kicker.updateGroup(X)
                   except Exception, e:
                            print e
                if not op.param2 in Bots and admin:
                    try:
                        gs = ki.getGroup(op.param1)
                        gs = kk.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            pass
                                
                    except Exception, e:
                        print e
                if not op.param2 in Bots and admin:
                  if wait["Backup"] == True:
                    try:
                        random.choice(KAC).inviteIntoGroup(op.param1, [op.param3])
                    except Exception, e:
                        print e
        if op.type == 19:              
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass                   
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
		    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
		    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
		    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
		    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ticket = ki.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
		    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
		    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ticket = kk.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ks.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
		    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
		    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ticket = kc.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        kt.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kt.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kt.updateGroup(X)
                    Ti = kt.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
		    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
		    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ticket = ks.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ka.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ka.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
		    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
		    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kt.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kt.updateGroup(X)
                    Ticket = kt.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
#========================================================================
                if Fmid in op.param3:
                    if op.param2 in Bots and admin:
                        pass                    
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = kb.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
		    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
		    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ka.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ka.updateGroup(X)
                    Ticket = ka.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ko.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
		    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
		    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kb.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kb.updateGroup(X)
                    Ticket = kb.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ke.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    X = ke.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
		    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
		    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ko.updateGroup(X)
                    Ticket = ko.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Jmid in op.param3:
                    if op.param2 in Bots:
                        pass                    
                    try:
                        ku.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client が蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nBecause the client does not exist in the kick regulation or group.\nAdd it to the blacklist.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                            
                    G = ke.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ke.updateGroup(G)
                    Ti = ke.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
		    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
		    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = ke.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    ke.updateGroup(X)
                    Ticket = ke.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Nmid in op.param3:
                    if op.param2 in Bots:
                        pass                   
                    try:
                        ku.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = cl.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    cl.updateGroup(G)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    kt.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)                    
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                    
#============================================================================
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == admin:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            X = cl.getGroup(list_[1])
                            X.preventJoinByTicket = True
                            cl.updateGroup(X)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")
                        
               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Deleted")
                        wait["dblack"] = False
                        
                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already in the blacklist")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"successfully load users into the blacklist")
                        
               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"successfully removed from the blacklist")
                        
                        wait["dblacklist"] = False
                        
                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"⎈ Profile Name :\n" + msg.contentMetadata["displayName"] + "\n\n⎈ Mid :\n" + msg.contentMetadata["mid"] + "\n\n⎈ Status Message :\n" + contact.statusMessage + "\n\n⎈ Pict Status :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n⎈ Cover Status :\n" + str(cu) + "\n\n [☸]➦Powered By: line.me/ti/p/~dhenz415々•┅─────")
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"⎈ Profile Name :\n" + contact.displayName + "\n\n⎈ Mid :\n" + msg.contentMetadata["mid"] + "\n\n⎈ Status Mesage:\n" + contact.statusMessage + "\n\n⎈ Pict Status :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n⎈ Cover Status :\n" + str(cu) + "\n\n [☸]➦Powered By: line.me/ti/p/~dhenz415々•┅─────")
            elif msg.contentType == 16:
                if wait["contact"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URL→\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower() == 'help':
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
	        else:
                    cl.sendText(msg.to,helpMessage)
	    elif msg.text.lower() == 'hg':
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,hgMessage)
                else:
                    cl.sendText(msg.to,hgMessage)
	    elif msg.text.lower() == 'ha':
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,haMessage)
                else:
                    cl.sendText(msg.to,haMessage)
	    elif msg.text.lower() == 'hk':
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,hkMessage)
                else:
                    cl.sendText(msg.to,hkMessage)
	    elif msg.text.lower() == 'hp':
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,hpMessage)
                else:
                    cl.sendText(msg.to,hpMessage)
            elif ("Group name:" in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Group name:","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
            	if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"-> " + _name + " was here")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 ki.sendText(msg.to,"Call my owner to use command !, \n➡Unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     cl.sendText(msg.to,"Done Invite : \n➡" + _name)
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         cl.sendText(msg.to,"Negative, Error detected")
                                         wait["winvite"] = False
                                         break
            elif "Invite: " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite: "," ")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
#-----------------------------++++-----------------
           
#=======================================================
            elif msg.text.lower() == "crash":
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "c33b66e4b7709e54a6fe6eced6e57c157',"}
                cl.sendMessage(msg)
#-----------------=============================   
            elif msg.text in ["Gue"]:
	      if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                cl.sendMessage(msg.to,"line.me/ti/p/~dhenz415")
            elif msg.text.lower() == 'gift1':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '1'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text.lower() == 'gift2':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '2'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text.lower() == 'gift3':
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '3'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text.lower() == 'gift4':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '4'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text.lower() == 'gift5':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '5'}
                msg.text = None
                kd.sendMessage(msg)
            elif msg.text.lower() == 'gift6':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}
                msg.text = None
                ke.sendMessage(msg)
            elif msg.text.lower() == 'spam gift':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                cl.sendMessage(msg)
                ks.sendMessage(msg)
                kt.sendMessage(msg)
                kt.sendMessage(msg)
#=================================================
            
#==================================================
            elif "All rename:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("All rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kc.getProfile()
                    profile.displayName = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = ks.getProfile()
                    profile.displayName = string
                    ks.updateProfile(profile)
                if len(string.decode('utf-8')) <= 20:
                    profile = kt.getProfile()
                    profile.displayName = string
                    kt.updateProfile(profile)
                    cl.sendText(msg.to,"change name: "+string+"\nsucces")
            elif msg.text.lower() == 'Allbio:':
              if msg.from_ in owner:
                string = msg.text.lower().replace("allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ks.getProfile()
                    profile.statusMessage = string
                    ks.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kt.getProfile()
                    profile.statusMessage = string
                    kt.updateProfile(profile)
                    cl.sendText(msg.to,"successfully turn it into: " + string + "")
            elif "Bot1 rename:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot1 rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"change name: "+string+"\nsucces")
            elif "Bot2 rename:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot2 rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ki.getProfile()
                    profile.displayName = string
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"change name: "+string+"\nsucces")
            elif "Bot3 rename:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot3 rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = kc.getProfile()
                    profile.displayName = string
                    kc.updateProfile(profile)
                    kc.sendText(msg.to,"change name: "+string+"\nsucces")
            elif "Bot4 rename:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot4 rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = kk.getProfile()
                    profile.displayName = string
                    kk.updateProfile(profile)
                    kk.sendText(msg.to,"change name: "+string+"\nsucces")
            elif "Bot5 rename:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot5 rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = ks.getProfile()
                    profile.displayName = string
                    ks.updateProfile(profile)
                    ks.sendText(msg.to,"change name: "+string+"\nsucces")
            elif "Bot6 rename:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Bot6 rename:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = kt.getProfile()
                    profile.displayName = string
                    kt.updateProfile(profile)
                    kt.sendText(msg.to,"change name: "+string+"\nsucces")    
#==================================================
            elif 'lyric ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    songname = msg.text.lower().replace('lyric ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        cl.sendText(msg.to, hasil)
                except Exception as wak:
                        cl.sendText(msg.to, str(wak))
            elif 'wiki ' in msg.text.lower():
              if msg.from_ in admin:
                  try:
                      wiki = msg.text.lower().replace("wiki ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please Click link\n"
                              pesan+=wikipedia.page(wiki).url
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
            elif msg.text.lower() == 'bot restart':
              if msg.from_ in admin:
                    print "[Command]Like executed"
                    try:
                        cl.sendText(msg.to,"Restarting...")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
            elif msg.text.lower() == 'ifconfig':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
              if msg.from_ in admin:
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    cl.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
            elif 'instagram ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    instagram = msg.text.lower().replace("instagram ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html5lib')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    user = "Name: " + text[-2] + "\n"
                    user1 = "Username: " + text[-1] + "\n"
                    followers = "Followers: " + text[0] + "\n"
                    following = "Following: " + text[2] + "\n"
                    post = "Post: " + text[4] + "\n"
                    link = "Link: " + "https://www.instagram.com/" + instagram
                    detail = "======INSTAGRAM INFO USER======\n"
                    details = "\n======INSTAGRAM INFO USER======"
                    cl.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    cl.sendImageWithURL(msg.to, text1[0])
                except Exception as njer:
                	cl.sendText(msg.to, str(njer))
            elif 'music ' in msg.text.lower():
              if msg.from_ in admin:
                try:
                    songname = msg.text.lower().replace('music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))
            elif 'clean invites' in msg.text.lower():
               if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        random.choice(KAC).cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting。")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#================================================================================
            elif 'clear invites' in msg.text.lower():
	      if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        random.choice(KAC).cancelGroupInvitation(msg.to,[_mid])
                        cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif 'link open' in msg.text.lower():
              if msg.from_ in admin:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    uye.updateGroup(X)
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"done")
                    else:
                        uye.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")
#===========================================================================
         
            elif 'link close' in msg.text.lower():
              if msg.from_ in admin:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    uye.updateGroup(X)
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"done")
                    else:
                        uye.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")

	    elif "jointicket " in msg.text.lower():
                rplace=msg.text.lower().replace("jointicket ")
                if rplace == "on":
			          wait["atjointicket"]=True
                elif rplace == "off":
                        wait["atjointicket"]=False
                cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
	    elif '/ti/g/' in msg.text.lower():
                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                links = link_re.findall(msg.text)
                n_links=[]
                for l in links:
                        if l not in n_links:
                                n_links.append(l)
                for ticket_id in n_links:
                        if wait["atjointicket"] == True:
                                group=cl.findGroupByTicket(ticket_id)
                                random.choice(KAC).acceptGroupInvitationByTicket(group.mid,ticket_id)
                                random.choice(KAC).sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
#============================================================
            elif msg.text.lower() == 'ginfo':
              if msg.from_ in admin:
                ginfo = cl.getGroup(msg.to)
                try:
                    gCreator = ginfo.creator.displayName
                except:
                    gCreator = "Error"
                if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                        sinvitee = "0"
                    else:
                        sinvitee = str(len(ginfo.invitee))
                msg.contentType = 13
                msg.contentMetadata = {'mid': ginfo.creator.mid}
                cl.sendText(msg.to,"[display name]\n" + str(ginfo.name) + "\n[Group Id]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\nmembers:" + str(len(ginfo.members)) + "\nInvitation:" + sinvitee + "")
                cl.sendMessage(msg)
#------------------------_--------------------------------------
 
#===============================================================
            elif msg.text in ["Glist"]:
                gs = cl.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (cl.getGroup(i).name + " | [ " + str(len (cl.getGroup(i).members)) + " ]")
                cl.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")

            elif msg.text in ["S1glist"]:
                gs = ki.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (ki.getGroup(i).name + " | [ " + str(len (ki.getGroup(i).members)) + " ]")
                ki.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S2glist"]:
                gs = kk.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (kk.getGroup(i).name + " | [ " + str(len (kk.getGroup(i).members)) + " ]")
                kk.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
            elif msg.text in ["S3glist"]:
                gs = kc.getGroupIdsJoined()
                L = "☫『 Groups List 』☫\n"
                for i in gs:
                    L += "[⭐] %s \n" % (kc.getGroup(i).name + " | [ " + str(len (kc.getGroup(i).members)) + " ]")
                kc.sendText(msg.to, L + "\nTotal Group : [ " + str(len(gs)) +" ]")
 
            elif "Invite me" in msg.text:
              if msg.from_ in owner:
                         gid = cl.getGroupIdsJoined()
		         for i in gid:
			        cl.findAndAddContactsByMid(msg.from_)
                                cl.inviteIntoGroup(i,[msg.from_])
			        cl.sendText(msg.to, "successfully invited you to all groups")

            elif "Steal group pict" in msg.text:
              if msg.from_ in admin:
					group = cl.getGroup(msg.to)
					path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                        cl.sendImageWithURL(msg.to,path)
            elif "Turn off bots" in msg.text:
               if msg.from_ in owner:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass
#==================================================================
            elif "Steal bio" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = cl.getContact(key1)
                cu = cl.channel.getCover(key1)
                try:
                    cl.sendText(msg.to,contact.statusMessage)
                except:
                    cl.sendText(msg.to,contact.statusMessage)
            elif msg.text in ["Creator"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'ufdc20b3a00b5e8f31e4f91017eb361b0'}
                cl.sendMessage(msg)
		msg.contentMetadata = {'mid': 'ufdc20b3a00b5e8f31e4f91017eb361b0'}
		cl.sendMessage(msg)
		msg.contentMetadata = {'mid': 'ufdc20b3a00b5e8f31e4f91017eb361b0'}
		cl.sendMessage(msg)
                cl.sendText(msg.to," add owner Silent bot : line.me/ti/p/~dhenz415")
            elif "Admin on @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Admin on @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.append(target)
                                cl.sendText(msg.to,"succes add to adminlist")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"owner permission required.")
            elif msg.text.lower() == 'admin list':
              if msg.from_ in admin:
                if admin == []:
                       cl.sendText(msg.to,"The adminlist is empty")
                else:
                        cl.sendText(msg.to,"loading...")
                        mc = ""
                        gh = ""
                        for mi_d in owner:
                            mc += "->" +cl.getContact(mi_d).displayName + "\n"
		        for mi_d in admin:
			    gh += "->" +cl.getContact(mi_d).displayName + "\n"				
                        cl.sendText(msg.to,"=======OWNER=======\n\n" + mc + "\n=======ADMIN=======\n\n" + gh +"\n=====================\n")
                        print "[Command]Stafflist executed"
            elif "Expel on @" in msg.text:
                if msg.from_ in owner:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Expel on @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                admin.remove(target)
                                cl.sendText(msg.to,"Succes remove admin from adminlist")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"owner permission required.")
#==========================================================
            elif 'bot mid' in msg.text.lower():
               if msg.from_ in admin:
			cl.sendText(msg.to,mid)
			ki.sendText(msg.to,Amid)
			kk.sendText(msg.to,Bmid)
			kc.sendText(msg.to,Cmid)
			ks.sendText(msg.to,Dmid)
			kt.sendText(msg.to,Emid)
#=======================================================
            elif "Translate-eng " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-eng ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except Exception as error:
                    cl.sendText(msg.to,(error))
            elif "Translate-jp" in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-jp ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'jp')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate jp'
                except Exception as error:
                    cl.sendText(msg.to,(error))
            elif "Translate-th " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-th ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'th')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate th'
                except Exception as error:
                    cl.sendText(msg.to,(error))
            elif "Translate-idn " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.replace("Translate-id ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    cl.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except Exception as error: 
                    cl.sendText(msg.to,(error))          

            elif "Say " in msg.text:
              if msg.from_ in  admin:
				bctxt = msg.text.replace("Say ","")
				cl.sendText(msg.to,(bctxt))
				kk.sendText(msg.to,(bctxt))
				kc.sendText(msg.to,(bctxt))
				ki.sendText(msg.to,(bctxt))
				ks.sendText(msg.to,(bctxt))
				kt.sendText(msg.to,(bctxt))
            
#======================================
            elif "TL:" in msg.text:
              if msg.from_ in admin:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            
#=================================================================
            elif msg.text in ["Protect:hight","protect:hight"]:
              if msg.from_ in admin:
                if wait["protectionOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into high protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Auto blockqr:off","auto blockqr:off"]:
              if msg.from_ in admin:
                if wait["qr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO Off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Welcome message:on"]:
              if msg.from_ in admin:
                if wait["welcomemsg"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message on")
            elif msg.text in ["Auto blockqr:on","auto blockqr:on"]:
              if msg.from_ in admin:
                if wait["qr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already on\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["qr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protection QR PRO On\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Welcome message:off"]:
              if msg.from_ in admin:
                if wait["welcomemsg"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Protect:low","Protect:low"]:
              if msg.from_ in admin:
                if wait["protectionOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["protectionOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"turned into low protection\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Namelock:on" in msg.text:
              if msg.from_ in admin:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ.")
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
                    wait['pname'][msg.to] = True
                    wait['pro_name'][msg.to] = cl.getGroup(msg.to).name
            elif "Namelock:off" in msg.text:
              if msg.from_ in admin:
                if msg.to in wait['pname']:
                    cl.sendText(msg.to,"ƬƲƦƝ ƠƑƑ.")
                    del wait['pname'][msg.to]
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")
					
            elif "Blockinvite:on" == msg.text:
              if msg.from_ in admin:
				gid = msg.to
				autocancel[gid] = "poni"
				cl.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƝ")
            elif "Blockinvite:off" == msg.text:
              if msg.from_ in admin:
				try:
					del autocancel[msg.to]
					cl.sendText(msg.to,"ƤƦƠƬЄƇƬ ƖƝƔƖƬƛƬƖƠƝ ƠƑƑ")
				except:
					pass
#================================================================           
            elif msg.text in ["Invite user"]:
              if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact")
#============================================================
            elif "Steal mid" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                cl.sendText(msg.to,"Mc: " + key1)
            elif "Steal contact" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
            elif "Mc:" in msg.text:
              if msg.from_ in admin:
                mmid = msg.text.replace("Mc:","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
#=======================================================
            elif msg.text in ["Auto notice:on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already activated")
                    else:
                        cl.sendText(msg.to,"enable notifications")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already activated")
                    else:
                        cl.sendText(msg.to,"enable notifications")
            elif msg.text in ["Protect on","protect on"]:
	      if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"Done")
                else:
                    wait["Protectjoin"] = True
		    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
	    elif msg.text in ["Protect off","protect off"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
	    elif msg.text in ["Cancl on","cancl on"]:
	      if msg.from_ in admin:
                if wait["Protectcancl"] == True:
		    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan On")
                    else:
                        cl.sendText(msg.to,"done")
	    elif msg.text in ["Cancl off","cancl off"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
		    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel Semua Undangan Off")
                    else:
                        cl.sendText(msg.to,"done")
	    elif msg.text in ["Joinn On","joinn on"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == True:
		    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancel"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
	    elif msg.text in ["Joinn Off","joinn off"]:
              if msg.from_ in admin:
                if wait["Protectcancel"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Yang Cancel Undangan Tidak Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
                else:
		    wait["Protectcancel"] = False
                    if wait["lang"] == "JP":
		        cl.sendText(msg.to,"Yang Cancel Undangan Tidak Kami Kick")
                    else:
                        cl.sendText(msg.to,"done")
	    elif msg.text in ["Qr on","qr on"]:
              if msg.from_ in admin:
		if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
		    else:
                        cl.sendText(msg.to,"done")
                else:
	  	    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
			cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
	    elif msg.text in ["Qr off","qr off"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
#=========================================================================
            elif msg.text in ["Auto notice:off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already unactivated")
                    else:
                        cl.sendText(msg.to,"disable notifications")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already unactivated")
                    else:
                        cl.sendText(msg.to,"disable notifications")

            elif msg.text in ["Auto join:on"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"")
                    else:
                        cl.sendText(msg.to,"already activated")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"enable auto koin")
                    else:
                        cl.sendText(msg.to,"")
            elif msg.text in ["Auto join:off"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already unactivated")
                    else:
                        cl.sendText(msg.to,"desable auto join")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already unactivated")
                    else:
                        cl.sendText(msg.to,"desable auto join")

            elif "Gcancel:" in msg.text:
              if msg.from_ in admin:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + " The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")

	    elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Join on","Auto join on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
	        else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
	    elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Join off","Auto join off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
              if msg.from_ in admin:
		if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Auto leave:on"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"要了开。")
            elif msg.text in ["Auto leave:off"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
#===============================================================
            
            elif msg.text in ["Auto like:on"]:
              if msg.from_ in admin:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["Auto like:off"]:
              if msg.from_ in admin:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
#==========================================================

            elif msg.text in ["Settings","Set"]:
              if msg.from_ in admin:
            	print "Setting pick up..."
                md="⚝▪☆●Silent Bot●☆▪⚝ Settings\n\n"
                if wait["likeOn"] == True: md+="Auto like : on\n"
                else:md+="Auto like : off\n"
                if wait["winvite"] == True: md+="Invite : on\n"
                else:md+="Invite : off
                if wait["pname"] == True: md+="Namelock : on\n"
                else:md+="Namelock : off\n"
                if wait["contact"] == True: md+="Notice : on\n"
                else: md+="Notice : off\n"
                if wait["autoJoin"] == True: md+="Auto join : on\n"
                else: md +="Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+="Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "Group cancel : off\n"
                if wait["leaveRoom"] == True: md+="Auto leave : on\n"
                else: md+="Auto leave : off\n"
                if wait["clock"] == True: md+="Clock Name : on\n"
                else:md+="Clock Name : off\n"
                if wait["autoAdd"] == True: md+="Auto add : on\n"
                else:md+="Auto add : off\n"
                if wait["commentOn"] == True: md+="Comment : on\n"
                else:md+="Comment : off\n"
                if wait["Backup"] == True: md+="Backup : on\n"
                else:md+="Backup : off\n"
                if wait["qr"] == True: md+="Protect QR : on\n"
                else:md+="Protect QR : off\n"
                if wait["welcomemsg"] == True: md+="welcome message : on\n"
                else:md+="welcome message : off\n"
                if wait["protectionOn"] == True: md+="Protection : hight\n\n"+ datetime.today().strftime('%H:%M:%S')
                else:md+="Protection : low\n\n"+ datetime.today().strftime('%H:%M:%S')
		if wait["Protectcancel"] == True: md+="[•]Protect Cancel [On]\n"
                else: md+="[•]Protect Cancel [Off]\n"
		if wait["Protectgr"] == True: md+="[•]Protect QR [On]\n"
                else: md+="[•]Protect QR [Off]\n"
		if wait["Protectjoin"] == True: md+="[•]Protect Group [On]\n"
                else: md+="[•]Protect Group [Off]\n"
		if wait["Protectcancl"] == True: md+="[•]Protect Invite [On]\n"
                else: md+="[•]Protect Invite [Off]\n"
		if wait["autoJoin"] == True: md+="[•]Auto Join [On]\n"
                else: md +="[•]Auto Join [Off]\n"
                cl.sendText(msg.to,md)
#========================================
#------------------------------------------------
            elif "Time" in msg.text:
              if msg.from_ in admin:
                  cl.sendText(msg.to,datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["PING","Ping","ping"]:
              if msg.from_ in admin:
                ki.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􀜁􀅔  Har Har")
                kk.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􀜁􀅔  Har Har")
                kc.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􀜁􀅔  Har Har")
		ks.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􀜁􀅔  Har Har")
		kt.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􀜁􀅔  Har Har")
		cl.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􀜁􀅔  Har Har")
            elif "Info @" in msg.text:
              if msg.from_ in admin:
                nama = msg.text.replace("Info @","")
                target = nama.rstrip(' ')
                tob = cl.getGroup(msg.to)
                for g in tob.members:
                    if target == g.displayName:
                        gjh= cl.getContact(g.mid)
                        try:
                            cover = cl.channel.getCover(g.mid)
                        except:
                            cover = ""
                        cl.sendText(msg.to,"[Display Name]:\n" + gjh.displayName + "\n[Mid]:\n" + gjh.mid + "\n[BIO]:\n" + gjh.statusMessage + "\n[pict profile]:\nhttp://dl.profile.line-cdn.net/" + gjh.pictureStatus + "\n[Cover]:\n" + str(cover))
                    else:
                        pass
#-----------------------------------------------
            elif msg.text in ["Backup:on"]:
              if msg.from_ in admin:
                if wait["Backup"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"backup has been active\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"backup has been enable\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"backup has been active\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"backup has been enable\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Backup:off"]:
              if msg.from_ in admin:
                if wait["Backup"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"backup has been unactive\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"backup has been desable\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["Backup"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"backup has been unactive\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"backup has been desable\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Rejectall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All Invites has been Rejected")
                else:
                    cl.sendText(msg.to,"拒绝了全部的邀请。")
           
            elif msg.text in ["Auto add:on"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"success activated")
                    else:
                        cl.sendText(msg.to,"success activated")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"success activated")
                    else:
                        cl.sendText(msg.to,"success activated")
            elif msg.text in ["Auto add:off"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"success unactivated")
                    else:
                        cl.sendText(msg.to,"success unactivated")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"success unactivated")
                    else:
                        cl.sendText(msg.to,"success unactivated")
#========================================
#========================================
            elif "Update welcome:" in msg.text:
              if msg.from_ in admin:
                wait["welmsg"] = msg.text.replace("Update welcome:","")
                cl.sendText(msg.to,"update welcome message succes"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Check welcome message"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"yor bot message\n\n" + wait["welmsg"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["welmsg"])
            elif "Message:" in msg.text:
              if msg.from_ in admin:
                wait["message"] = msg.text.replace("Message:","")
                cl.sendText(msg.to,"bot message\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Add message:" in msg.text:
              if msg.from_ in admin:
                wait["message"] = msg.text.replace("Add message:","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    cl.sendText(msg.to,"done。\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Check message"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"yor bot message\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["message"])
            elif "Comment:" in msg.text:
              if msg.from_ in admin:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
              if msg.from_ in admin:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)

            elif msg.text in ["Comment:on"]:
              if msg.from_ in admin:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Comment:off"]:
              if msg.from_ in admin:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text in ["Check comment"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"message comment\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    uye = random.choice(KAC)
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        uye.updateGroup(x)
                    gurl = uye.reissueGroupTicket(msg.to)
                    uye.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        uye.sendText(msg.to,"Can not be used outside the group")
                    else:
                        uye.sendText(msg.to,"Not for use less than group")
#-------------------------------------------------------
            elif "Gift @" in msg.text:
                _name = msg.text.replace("Gift @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                    	msg.contentType = 9
                        msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                        msg.text = None
                        cl.sendMessage(msg,g)
#===========================================
            elif msg.text.lower() == 'responsename':
              if msg.from_ in admin:
                profile = cl.getProfile()
                text = profile.displayName + " "
                cl.sendText(msg.to, text)
                profile = ki.getProfile()
                text = profile.displayName + " " 
                ki.sendText(msg.to, text)
                profile = kk.getProfile()
                text = profile.displayName + " "
                kk.sendText(msg.to, text)
                profile = kc.getProfile()
                text = profile.displayName + " "
                kc.sendText(msg.to, text)
                profile = ks.getProfile()
                text = profile.displayName + " "
                ks.sendText(msg.to, text)
                profile = kt.getProfile()
                text = profile.displayName + " "
                kt.sendText(msg.to, text)
                profile = kk.getProfile()
                text = profile.displayName + " "
                ka.sendText(msg.to, text)
                profile = kc.getProfile()
                text = profile.displayName + " "
                kb.sendText(msg.to, text)
                profile = ks.getProfile()
                text = profile.displayName + " "
                ko.sendText(msg.to, text)
                profile = kt.getProfile()
                text = profile.displayName + " "
                ke.sendText(msg.to, text)

	    elif msg.text in ["Absen","Respon"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"A")
                ki.sendText(msg.to,"B")
                kk.sendText(msg.to,"C")
                kc.sendText(msg.to,"D")
		ks.sendText(msg.to,"E")
                ka.sendText(msg.to,"F")
                kb.sendText(msg.to,"G")
		ko.sendText(msg.to,"H")
                ke.sendText(msg.to,"I")
		kt.sendText(msg.to,"J")
		random.choice(KAC).sendText(msg.to,"Semua Udah Hadir Boss\nSiap Protect Group\nAman Gak Aman Yang Penting Anu")
#========================================
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist s")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "・" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)

            elif msg.text in ["Clock:on","Clock on","Jam on","Jam:on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"[%H:%M]")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done")

            elif msg.text in ["Clock:off","Clock off","Jam off","Jam:off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done")

            elif "Cc: " in msg.text:
                n = msg.text.replace("Cc: ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Changed to:\n\n" + n)
            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"[%H:%M]")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Refresh to update")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock")

#========================================
            elif "Steal cover @" in msg.text:
              if msg.from_ in admin:            
                print "[Command]dp executing"
                _name = msg.text.replace("Steal cover @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            cu = cl.channel.getCover(target)
                            path = str(cu)
                            cl.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"
            elif "Midpict:" in msg.text:
              if msg.from_ in admin:
                umid = msg.text.replace("Midpict:","")
                contact = cl.getContact(umid)
                try:
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                except:
                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                try:
                    cl.sendImageWithURL(msg.to,image)
                except Exception as error:
                    cl.sendText(msg.to,(error))
                    pass
            elif "Steal pict " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    msg.contentType = 0
                    steal0 = msg.text.replace("Steal pict ","")
                    steal1 = steal0.lstrip()
                    steal2 = steal1.replace("@","")
                    steal3 = steal2.rstrip()
                    _name = steal3
                    group = cl.getGroup(msg.to)
                    targets = []
                    for g in group.members:
                        if _name == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                try:
                                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                except:
                                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                                try:
                                    cl.sendImageWithURL(msg.to,image)
                                except Exception as error:
                                    cl.sendText(msg.to,(error))
                                    pass
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                else:
                    cl.sendText(msg.to,"Tidak bisa dilakukan di luar grup")
            elif "copyyy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("copy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               cl.CloneContactProfile(target)
                               cl.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
            elif "copy1 @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("copy1 @","")
                   _nametarget = _name.rstrip('  ')
                   gs = kk.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       kk.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               kk.CloneContactProfile(target)
                               kk.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
            elif "copy2 @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("copy2 @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ki.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ki.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ki.CloneContactProfile(target)
                               ki.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
            elif "copy3 @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("copy3 @","")
                   _nametarget = _name.rstrip('  ')
                   gs = kc.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       kc.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               kc.CloneContactProfile(target)
                               kc.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
            elif "copy4 @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("copy4 @","")
                   _nametarget = _name.rstrip('  ')
                   gs = ks.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       ks.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               ks.CloneContactProfile(target)
                               ks.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
            elif "copy5 @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("copy5 @","")
                   _nametarget = _name.rstrip('  ')
                   gs = kt.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       kt.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               kt.CloneContactProfile(target)
                               kt.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
            elif msg.text in ["Backup","backup"]:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    cl.sendText(msg.to, "Refreshed.")
                except Exception as e:
                    cl.sendText(msg.to, str(e))
            elif msg.text in ["Gcreator:inv"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       print "success inv gCreator"
                    except:
                       pass
            elif "Copyyy @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("Copy @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Tidak Ada Target Copy")
                        else:
                            for target in targets:
                                try:
                                    cl.CloneContactProfile(target)
                                    ki.CloneContactProfile(target)
                                    kk.CloneContactProfile(target)
                                    kc.CloneContactProfile(target)
                                    ks.CloneContactProfile(target)
                                    kt.CloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profile")
                                except Exception as e:
                                    print e
            elif msg.text in ["Kembali ke asli"]:
                try:
                    cl.updateDisplayPicture(backup.pictureStatus)
                    cl.updateProfile(backup)
                    ki.updateDisplayPicture(backup.pictureStatus)
                    ki.updateProfile(backup)
                    kk.updateDisplayPicture(backup.pictureStatus)
                    kk.updateProfile(backup)
                    kc.updateDisplayPicture(backup.pictureStatus)
                    kc.updateProfile(backup)
                    ks.updateDisplayPicture(backup.pictureStatus)
                    ks.updateProfile(backup)
                    kt.updateDisplayPicture(backup.pictureStatus)
                    kt.updateProfile(backup)
                    cl.sendText(msg.to, "Backup Astro Sukses")
                except Exception as e:
                    cl.sendText(msg.to, str (e))

#===============================================
            elif msg.text in ["Sp","Speed"]:
              if msg.from_ in admin:
                cl.sendText(msg.to, "wait...")
                start = time.time()
                time.sleep(0.0001)
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
		ki.sendText(msg.to, "%sseconds" % (elapsed_time))
		kk.sendText(msg.to, "%sseconds" % (elapsed_time))
		kc.sendText(msg.to, "%sseconds" % (elapsed_time))
		ks.sendText(msg.to, "%sseconds" % (elapsed_time))
		ka.sendText(msg.to, "%sseconds" % (elapsed_time))
		kb.sendText(msg.to, "%sseconds" % (elapsed_time))
		ko.sendText(msg.to, "%sseconds" % (elapsed_time))
		ke.sendText(msg.to, "%sseconds" % (elapsed_time))
		kt.sendText(msg.to, "%sseconds" % (elapsed_time))
                print "[Command]Speed palsu executed"
           
            elif "Blacklist all" in msg.text:
              if msg.from_ in admin:
                  if msg.toType == 2:
                       print "ok"
                       _name = msg.text.replace("Blacklist all","")
                       gs = cl.getGroup(msg.to)
                       cl.sendText(msg.to,"Semua Telah Di Hapus")
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                                targets.append(g.mid)
                       if targets == []:
                            cl.sendText(msg.to,"Maaf")
                       else:
                           for target in targets:
                               if not target in Bots:
                                   try:
                                       wait["blacklist"][target] = True
                                       f=codecs.open('st2__b.json','w','utf-8')
                                       json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       cl.sendText(msg.to,"Success Boss")
                                   except:
                                       cl.sentText(msg.to,"Berhasil Dihapus")
            elif msg.text in ["Ban cek","Cekban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = "[⎈]Mid Blacklist [⎈]"
                    for mm in matched_list:
                        cocoa += "\n" + mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif "Details grup: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("/DetailsGroup: ","")
                    if gid in [""," "]:
                        cl.sendText(msg.to,"Grup id tidak valid")
                    else:
                        try:
                            groups = cl.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[" + groups.name + "]\n -+GroupID : " + gid + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n -+GroupPicture : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            cl.sendText(msg.to,h)
                        except Exception as error:
                            cl.sendText(msg.to,(error))#-------------------------------------------------------
            
            #--------------------------------------------------------
	    elif "Ban group: " in msg.text:
		grp = msg.text.replace("Ban group: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in Creator:
		    for i in gid:
		        h = cl.getGroup(i).name
			if h == grp:
			    wait["BlGroup"][i]=True
			    cl.sendText(msg.to, "Success Ban Group : "+grp)
			else:
			    pass
		else:
		    cl.sendText(msg.to, "Khusus Creator")
#--------------------------------------------------------
            elif msg.text in ["List ban","List ban group"]:
		if msg.from_ in admin:
                    if wait["BlGroup"] == {}:
                        ki.sendText(msg.to,"nothing")
                        kk.sendText(msg.to,"nothing")
                        kc.sendText(msg.to,"nothing")
                    else:
                        mc = ""
                        for gid in wait["BlGroup"]:
                            mc += "-> " +cl.getGroup(gid).name + "\n"
                        ki.sendText(msg.to,"===[Ban Group]===\n"+mc)
		else:
		    cl.sendText(msg.to, "Khusus Admin")
#--------------------------------------------------------
	    elif msg.text in ["Del ban: "]:
		if msg.from_ in admin:
		    ng = msg.text.replace("Del ban: ","")
		    for gid in wait["BlGroup"]:
		        if cl.getGroup(gid).name == ng:
			    del wait["BlGroup"][gid]
			    cl.sendText(msg.to, "Success del ban "+ng)
		        else:
			    pass
		else:
		    cl.sendText(msg.to, "Khusus Admin")
#--------------------------------------------------------
            elif "Join group: " in msg.text:
		ng = msg.text.replace("Join group: ","")
		gid = cl.getGroupIdsJoined()
		try:
		    if msg.from_ in Creator:
                        for i in gid:
                            h = cl.getGroup(i).name
		            if h == ng:
		                cl.inviteIntoGroup(i,[Creator])
			        cl.sendText(msg.to,"Success join to ["+ h +"] group")
			    else:
			        pass
		    else:
		        cl.sendText(msg.to,"Khusus Creator")
		except Exception as e:
		    cl.sendMessage(msg.to, str(e))
#--------------------------------------------------------
	    elif "Leave group: " in msg.text:
		ng = msg.text.replace("Leave group: ","")
		gid = cl.getGroupIdsJoined()
		if msg.from_ in Creator:
                    for i in gid:
                        h = cl.getGroup(i).name
		        if h == ng:
			    cl.sendText(i,"Bot di paksa keluar oleh owner!")
		            cl.leaveGroup(i)
			    ki.leaveGroup(i)
			    kk.leaveGroup(i)
			    kc.leaveGroup(i)
			    ks.leaveGroup(i)
                            kt.leaveGroup(i)
                            ka.leaveGroup(i)
                            kb.leaveGroup(i)
			    ko.leaveGroup(i)
                            ke.leaveGroup(i)
			    ku.leaveGroup(i)
			    cl.sendText(msg.to,"Success left ["+ h +"] group")
			else:
			    pass
		else:
		    cl.sendText(msg.to,"Khusus Creator")
            elif "Set member: " in msg.text:
		if msg.from_ in admin:
		    jml = msg.text.replace("Set member: ","")
		    wait["Members"] = int(jml)
		    cl.sendText(msg.to, "Jumlah minimal member telah di set : "+jml)
		else:
		    cl.sendText(msg.to, "Khusus Admin")
            #--------------------------------------------------------
	    elif "Add all" in msg.text:
		if msg.from_ in admin:
		    thisgroup = cl.getGroups([msg.to])
		    Mids = [contact.mid for contact in thisgroup[0].members]
		    mi_d = Mids[:33]
		    cl.findAndAddContactsByMids(mi_d)
		    cl.sendText(msg.to,"Success Add all")
		else:
		    cl.sendText(msg.to, "Khusus Admin")
#--------------------------------------------------------
	    elif "Recover" in msg.text:
		thisgroup = cl.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		cl.createGroup("Recover", mi_d)
		cl.sendText(msg.to,"Success recover")
            elif "Anu " in msg.text:
              if msg.from_ in admin:
                ulti0 = msg.text.replace("Anu ","")
                ulti1 = ulti0.rstrip()
                ulti2 = ulti1.replace("@","")
                ulti3 = ulti2.rstrip()
                _name = ulti3
                gs = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                gs.preventJoinByTicket = False
                cl.updateGroup(gs)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                satpam.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.2)
                targets = []
                for s in gs.members:
                        if _name in s.displayName:
                                targets.append(s.mid)
                if targets ==[]:
                        sendMessage(msg.to,"user does not exist")
                        pass
                else:
                        for target in targets:
                                try:
                                        satpam.kickoutFromGroup(msg.to,[target])
                                        satpam.leaveGroup(msg.to)
                                        print (msg.to,[g.mid])
                                except:
                                        satpam.sendText(msg.t,"Ter ELIMINASI....")
                                        satpam.sendText(msg.to,"WOLES brooo....!!!")
                                        satpam.leaveGroup(msg.to)
                                        gs = cl.getGroup(msg.to)
                                        gs.preventJoinByTicket = True
                                        cl.uldateGroup(gs)
                                        gs.preventJoinByTicket(gs)
                                        cl.updateGroup(gs)
#========================================
            elif msg.text in ["Bot1 backup run"]:
                if msg.from_ in admin:
                    wek = cl.getContact(mid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('mydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('mysm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('myps.txt',"w")
                    u.write(a)
                    u.close()
                    cl.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot2 backup run"]:
                if msg.from_ in admin:
                    wek = ki.getContact(Amid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('mgydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('myesm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('mypfs.txt',"w")
                    u.write(a)
                    u.close()
                    ki.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot3 backup run"]:
                if msg.from_ in admin:
                    wek = kk.getContact(Bmid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('msgydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('mysfdgm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('gymyps.txt',"w")
                    u.write(a)
                    u.close()
                    kk.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot4 backup run"]:
                if msg.from_ in admin:
                    wek = kc.getContact(Cmid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('jhmydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('myhfsm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('mypfhs.txt',"w")
                    u.write(a)
                    u.close()
                    kc.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot5 backup run"]:
                if msg.from_ in admin:
                    wek = ks.getContact(Dmid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('madydn.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('mysgjm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('myrdps.txt',"w")
                    u.write(a)
                    u.close()
                    ks.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
            elif msg.text in ["Bot6 backup run"]:
                if msg.from_ in admin:
                    wek = kt.getContact(Emid)
                    a = wek.pictureStatus
                    r = wek.displayName
                    i = wek.statusMessage
                    s = open('mydnsgv.txt',"w")
                    s.write(r)
                    s.close()
                    t = open('jhmysm.txt',"w")
                    t.write(i)
                    t.close()
                    u = open('myiyps.txt',"w")
                    u.write(a)
                    u.close()
                    kt.sendText(msg.to, "backup has been active")
                    print wek
                    print a
                    print r
                    print i
#----------------------------------------------
            elif "Bot1 clone " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = cl.getContact(target)
                        X = contact.displayName
                        profile = cl.getProfile()
                        profile.displayName = X
                        cl.updateProfile(profile)
                        cl.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = cl.getProfile()
                        lol.statusMessage = Y
                        cl.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        cl.updateProfilePicture(P)
                    except Exception as e:
                        cl.sendText(msg.to, "Failed!")
                        print e
            elif "Bot2 clone " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = ki.getContact(target)
                        X = contact.displayName
                        profile = ki.getProfile()
                        profile.displayName = X
                        ki.updateProfile(profile)
                        ki.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = ki.getProfile()
                        lol.statusMessage = Y
                        ki.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        ki.updateProfilePicture(P)
                    except Exception as e:
                        ki.sendText(msg.to, "Failed!")
                        print e
            elif "Bot3 clone " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = kk.getContact(target)
                        X = contact.displayName
                        profile = kk.getProfile()
                        profile.displayName = X
                        kk.updateProfile(profile)
                        kk.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = kk.getProfile()
                        lol.statusMessage = Y
                        kk.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        kk.updateProfilePicture(P)
                    except Exception as e:
                        kk.sendText(msg.to, "Failed!")
                        print e
            elif "Bot4 clone " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = kc.getContact(target)
                        X = contact.displayName
                        profile = kc.getProfile()
                        profile.displayName = X
                        kc.updateProfile(profile)
                        kc.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = kc.getProfile()
                        lol.statusMessage = Y
                        kc.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        kc.updateProfilePicture(P)
                    except Exception as e:
                        kc.sendText(msg.to, "Failed!")
                        print e
            elif "Bot5 clone " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = ks.getContact(target)
                        X = contact.displayName
                        profile = ks.getProfile()
                        profile.displayName = X
                        ks.updateProfile(profile)
                        ks.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = ks.getProfile()
                        lol.statusMessage = Y
                        ks.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        ks.updateProfilePicture(P)
                    except Exception as e:
                        ks.sendText(msg.to, "Failed!")
                        print e
            elif "Bot6 clone " in msg.text:
              if msg.from_ in admin:
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = kt.getContact(target)
                        X = contact.displayName
                        profile = kt.getProfile()
                        profile.displayName = X
                        kt.updateProfile(profile)
                        kt.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = kt.getProfile()
                        lol.statusMessage = Y
                        kt.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        kt.updateProfilePicture(P)
                    except Exception as e:
                        kt.sendText(msg.to, "Failed!")
                        print e

#=================================================
            elif "Bot1 backup" in msg.text:
                if msg.from_ in admin:
                        try:
                            h = open('mydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = cl.getProfile()
                            profile.displayName = x
                            cl.updateProfile(profile)
                            i = open('mysm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = cl.getProfile()
                            cak.statusMessage = y
                            cl.updateProfile(cak)
                            j = open('myps.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            cl.updateProfilePicture(p)
                            cl.sendText(msg.to, "Succes")
                        except Exception as e:
                            cl.sendText(msg.to,"Gagagl!")
                            print e
            elif "Bot2 backup" in msg.text:
                 if msg.from_ in admin:
                        try:
                            h = open('mgydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = ki.getProfile()
                            profile.displayName = x
                            ki.updateProfile(profile)
                            i = open('myesm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = ki.getProfile()
                            cak.statusMessage = y
                            ki.updateProfile(cak)
                            j = open('mypfs.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            ki.updateProfilePicture(p)
                            ki.sendText(msg.to, "Succes")
                        except Exception as e:
                            ki.sendText(msg.to,"Gagagl!")
                            print e
            elif "Bot3 backup" in msg.text:
                if msg.from_ in admin:
                        try:
                            h = open('msgydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = kk.getProfile()
                            profile.displayName = x
                            kk.updateProfile(profile)
                            i = open('mysfdgm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = kk.getProfile()
                            cak.statusMessage = y
                            kk.updateProfile(cak)
                            j = open('gymyps.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            kk.updateProfilePicture(p)
                            kk.sendText(msg.to, "Succes")
                        except Exception as e:
                            kk.sendText(msg.to,"Gagagl!")
                            print e
            elif "Bot4 backup" in msg.text:
                if msg.from_ in admin:
                        try:
                            h = open('jhmydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = kc.getProfile()
                            profile.displayName = x
                            kc.updateProfile(profile)
                            i = open('myhfsm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = kc.getProfile()
                            cak.statusMessage = y
                            kc.updateProfile(cak)
                            j = open('mypfhs.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            kc.updateProfilePicture(p)
                            kc.sendText(msg.to, "Succes")
                        except Exception as e:
                            kc.sendText(msg.to,"Gagagl!")
                            print e
            elif "Bot5 backup" in msg.text:
                if msg.from_ in admin:
                        try:
                            h = open('madydn.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = ks.getProfile()
                            profile.displayName = x
                            ks.updateProfile(profile)
                            i = open('mysgjm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = ks.getProfile()
                            cak.statusMessage = y
                            ks.updateProfile(cak)
                            j = open('myrdps.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            ks.updateProfilePicture(p)
                            ks.sendText(msg.to, "Succes")
                        except Exception as e:
                            ks.sendText(msg.to,"Gagagl!")
                            print e
            elif "Bot6 backup" in msg.text:
                if msg.from_ in admin:
                        try:
                            h = open('mydnsgv.txt',"r")
                            name = h.read()
                            h.close()
                            x = name
                            profile = kt.getProfile()
                            profile.displayName = x
                            kt.updateProfile(profile)
                            i = open('jhmysm.txt',"r")
                            sm = i.read()
                            i.close()
                            y = sm
                            cak = kt.getProfile()
                            cak.statusMessage = y
                            kt.updateProfile(cak)
                            j = open('myiyps.txt',"r")
                            ps = j.read()
                            j.close()
                            p = ps
                            kt.updateProfilePicture(p)
                            kt.sendText(msg.to, "Succes")
                        except Exception as e:
                            kt.sendText(msg.to,"Gagagl!")
                            print e
#=================================================
            elif msg.text == "Cek":
              if msg.from_ in admin:
                    cl.sendText(msg.to, "Set point.")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                           pass
                    now2 = datetime.now()
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M')
                    wait2['ROM'][msg.to] = {}
                    print wait2
            elif msg.text == "Ciduk":
              if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                        cl.sendText(msg.to, "╔═══════════════%s\n╠════════════════\n%s╠═══════════════\n║Readig point creation:\n║ [%s]\n╚════════════════"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "anda slah ketik-_-")
						
#========================================
#---------------FUNGSI RATAIN GRUP TANPA KICK SESAMA BOT/Admin/Bots----------#
	    elif "Mulai" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Mulai","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    cl.sendText(msg.to,"Maaf gk Sopan")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
		        kr.sendText(msg.to,"Tidak ditemukan")
                    else:
		        for target in targets:
                          if not target in Bots:
                            if not target in admin:
                               try:
                                klist=[ki,kk,kc,ks,kt,ka,kb,ko,ke]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                               except:
                                cl.sendText(msg,to,"Makasih")

            elif "Bubar" in msg.text:
	      if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Bubar","")
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    cl.sendText(msg.to,"Maaf low gk sopan ")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        kr.sendText(msg.to,"tidak ditemukan")
                    else:
                        for target in targets:
                          if not target in Bots:
                            if not target in admin:
                               try:
                                klist=[ki,kk,kc,ks,kt,ka,kb,ko,ke]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                               except:
                                cl.sendText(msg.to,"Group dibersihkan")
#================================================
#========================================
            elif msg.text.lower() == 'welcome':
              if msg.from_ in admin:
                ginfo = cl.getGroup(msg.to)
                random.choice(KAC).sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                random.choice(KAC).sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
#=========================================
            elif msg.text in ["Mimic on","mimic on"]:
                    if wait3["copy"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Mimic On")
                    else:
                    	wait3["copy"] = True
                    	if wait["lang"] == "JP":
                    		cl.sendText(msg.to,"Mimic On")
                        else:
    	                	cl.sendText(msg.to,"Already on")
            elif msg.text in ["Mimic off","mimic:off"]:
                    if wait3["copy"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Mimic Off")
                    else:
                    	wait3["copy"] = False
                    	if wait["lang"] == "JP":
                    		cl.sendText(msg.to,"Mimic Off")
                        else:
	                    	cl.sendText(msg.to,"Already on")
            elif msg.text in ["Target list"]:
                        if wait3["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in wait3["target"]:
                                mc += "✔️ "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if wait3["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                wait3["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                wait3["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            elif "Target @" in msg.text:
                        target = msg.text.replace("Target @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                wait3["target"][t] = True
                            cl.sendText(msg.to,"Target added")
            elif "Del target @" in msg.text:
                        target = msg.text.replace("Del target @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                del wait3["target"][t]
                            cl.sendText(msg.to,"Target deleted")
#=======================================
#-------------------Fungsi spam start--------------------------
            elif "Spam change: " in msg.text:
              if msg.from_ in admin:
                wait["spam"] = msg.text.replace("Spam change: ","")
                cl.sendText(msg.to,"spam changed")

            elif "Spam add: " in msg.text:
              if msg.from_ in admin:
                wait["spam"] = msg.text.replace("Spam add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"spam changed")
                else:
                    cl.sendText(msg.to,"Done")

            elif "Spam: " in msg.text:
              if msg.from_ in admin:
                strnum = msg.text.replace("Spam: ","")
                num = int(strnum)
                for var in range(0,num):
                    cl.sendText(msg.to, wait["spam"])

#-------------------Fungsi spam finish----------------------------
#-----------------------------------------------
#-----------------------------------------------
         #   elif 'apakah' in msg.text.lower():
          #    if msg.from_ in admin:
           #     tanya = msg.text.lower().replace("apakah","")
           #     jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
           #     jawaban = random.choice(jawab)
            #    cl.sendText(msg.to,jawaban)
            
#================================================
#===============================================
#=================================================
            elif "Spam " in msg.text:
                if msg.from_ in admin:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                   #Keke cantik <3
                   if txt[1] == "on":
                        if jmlh <= 10000:
                             for x in range(jmlh):
                                   cl.sendText(msg.to, teks)
                        else:
                               cl.sendText(msg.to, "Out of range! ")
                   elif txt[1] == "off":
                         if jmlh <= 10000:
                               cl.sendText(msg.to, tulisan)
                         else:
                               cl.sendText(msg.to, "Out of range! ")
#-----------------------------------------------
            elif "Steal mid @" in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Steal mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
#-------------------------------------------------
            elif "Pm cast " in msg.text:
              if msg.from_ in owner:
					bctxt = msg.text.replace("Pm cast ", "")
					t = cl.getAllContactIds()
					for manusia in t:
						cl.sendText(manusia,(bctxt))
            elif "Broadcast " in msg.text:
              if msg.from_ in owner:
					bctxt = msg.text.replace("Broadcast ", "")
					n = cl.getGroupIdsJoined()
					for manusia in n:
						cl.sendText(manusia,(bctxt +"\n\n\nbroadcasted by:" + cl.getContact(msg.from_).displayName))
										 
#========================================
            elif msg.text in ["Beb","Say"]:
              if msg.from_ in admin:
					G = cl.getGroup(msg.to)
					info = cl.getGroup(msg.to)
					G.preventJoinByTicket = False
					cl.updateGroup(G)
					invsend = 0
					Ticket = cl.reissueGroupTicket(msg.to)
					cl.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.0001)
					ki.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.0001)
					kk.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.0001)
					kc.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.0001)
                                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                                        time.sleep(0.0001)
					kt.acceptGroupInvitationByTicket(msg.to,Ticket)
                                        time.sleep(0.0001)
					ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                        time.sleep(0.0001)
					kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                        time.sleep(0.0001)
					ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                                        time.sleep(0.0001)
                                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                        time.sleep(0.0001)
					G = cl.getGroup(msg.to)
					G.preventJoinByTicket = True
					random.choice(KAC).updateGroup(G)
					print "All_Kickers_Ok!"
					G.preventJoinByTicket(G)
					random.choice(KAC).updateGroup(G)

	    elif msg.text in ["Masuk"]:
              if msg.from_ in admin:
                                        G = ki.getGroup(msg.to)
                                        info = ki.getGroup(msg.to)
                                        G.preventJoinByTicket = False
                                        ki.updateGroup(G)
                                        invsend = 0
					Ticket = cl.reissueGroupTicket(msg.to)
                                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                                        time.sleep(0.0001)
                                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                        time.sleep(0.0001)
                                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.0001) 
					ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                                        time.sleep(0.0001)
					kt.acceptGroupInvitationByTicket(msg.to,Ticket)
                                        time.sleep(0.0001)
                                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                                        time.sleep(0.0001)
                                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.0001)
                                        ko.acceptGroupInvitationByTicket(msg.to,Ticket)
					time.sleep(0.0001)
                                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                        time.sleep(0.0001)
					satpam.acceptGroupInvitationByTicket(msg.to,Ticket)
                                        time.sleep(0.0001)
                                        G = cl.getGroup(msg.to)
                                        G.preventJoinByTicket = True
                                        random.choice(KAC).updateGroup(G)
                                        print "All_Kickers_Ok!"
                                        G.preventJoinByTicket(G)
                                        random.choice(KAC).updateGroup(G)
#=====================================================================================
          
            elif msg.text in ["Keluar"]:
              if msg.from_ in owner:
				gid = cl.getGroupIdsJoined()
				for i in gid:
					cl.leaveGroup(i)
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kc.leaveGroup(i)
					ks.leaveGroup(i)
					kt.leaveGroup(i)
					ka.leaveGroup(i)
                                        kb.leaveGroup(i)
                                        ko.leaveGroup(i)
					ke.leaveGroup(i)
				if wait["lang"] == "JP":
					ki.sendText(msg.to,"bye-bye")
				else:
					cl.sendText(msg.to,"He declined all invitations")
            elif msg.text in ["Putus"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     cl.leaveGroup(msg.to)
                     ki.leaveGroup(msg.to)
                     kk.leaveGroup(msg.to)
                     kc.leaveGroup(msg.to)
		     ks.leaveGroup(msg.to)
                     ka.leaveGroup(msg.to)
                     kb.leaveGroup(msg.to)
                     ko.leaveGroup(msg.to)
		     ke.leaveGroup(msg.to)
                     kt.leaveGroup(msg.to)
                except:

                     pass
	    elif msg.text in ["Balik"]:
              if msg.from_ in admin:
		if msg.toType == 2:
                   X = cl.getGroup(msg.to)
		try:
                     ki.leaveGroup(msg.to)
                     kk.leaveGroup(msg.to)
                     kc.leaveGroup(msg.to)
                     ks.leaveGroup(msg.to)
                     kt.leaveGroup(msg.to)
                     ka.leaveGroup(msg.to)
                     kb.leaveGroup(msg.to)
                     ko.leaveGroup(msg.to)
                     ke.leaveGroup(msg.to)
		     cl.leaveGroup(msg.to)
                     satpam.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Ptooottt"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                   X = cl.getGroup(msg.to)
                try:
                     cl.sendMessage(msg.to,"bye-bye")
                     cl.leaveGroup(msg.to)
                except:
                     pass
            elif msg.text in ["Nk "]:
              if msg.from_ in admin:                                        
                       mk0 = msg.text.replace("Nk ","")
                       mk1 = mk0.lstrip()
                       mk2 = mk1.replace("@","")
                       mk3 = mk2.rstrip()
                       _name = mk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for h in gs.members:
                           if _name in h.displayName:
                              targets.append(h.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                               try:
                                 if msg.from_ not in target:
                                   ki.kickoutFromGroup(msg.to,[target])
                               except:
			           ki.kickoutFromGroup(msg.to,[target])
								
#==========================================
            elif "youtube " in msg.text.lower():
                if msg.from_ in admin:
                   query = msg.text.split(" ")
                   try:
                       if len(query) == 5:
                           isi = yt(query[2])
                           hasil = isi[int(query[1])-1]
                           cl.sendText(msg.to, hasil)
                       else:
                           isi = yt(query[1])
                           cl.sendText(msg.to, isi[0])
                   except Exception as e:
                       cl.sendText(msg.to, str(e))
            elif 'Vidio ' in msg.text:
	      if msg.from_ in admin:
                try:
                    textToSearch = (msg.text).replace('Vidio ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    ght=('https://www.youtube.com' + results['href'])
		    cl.sendVideoWithURL(msg.to,ght)
                except:
                    cl.sendText(msg.to,"Could not find it")
            #-------------------------------------------------
            elif "/say-jp " in msg.text:
                say = msg.text.replace("/say-jp ","")
                lang = 'jp'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#------------------------------------------------
            elif "/say-en " in msg.text:
                say = msg.text.replace("/say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                cl.sendAudio(msg.to,"hasil.mp3")
#-----------------------------------------------
            elif "/say " in msg.text:
                 psn = msg.text.replace("/say ","")
                 tts = gTTS(psn, lang='id', slow=False)
                 tts.save('tts.mp3')
                 cl.sendAudio(msg.to, 'tts.mp3')
#-----------------------------------------------
            elif "Siapa " in msg.text:
    		tanya = msg.text.replace("Siapa ","")
    		jawab = ("Dia yg kebanyakan micin"," Dia gila")
    		jawaban = random.choice(jawab)
		tts = gTTS(text=jawaban, lang='en')
		tts.save('tts.mp3')
    		cl.sendAudio(msg.to,'tts.mp3')
#==========================================
            elif "Dosa @" in msg.text:
                tanya = msg.text.replace("Dosa @","")
                jawab = ("60%","70%","80%","90%","100%","Tak terhingga")
                jawaban = random.choice(jawab)
                tts = gTTS(text=jawaban, lang='en')
                tts.save('tts.mp3')
                cl.sendText(msg.to,"Dosanya adalah cek voice ini")
                cl.sendAudio(msg.to,'tts.mp3')
#==========================================
            
#==========================================
            #elif "/ " in msg.text.lower():
                #txt = msg.text.replace("kedapkedip ", "")
                #t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                #t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
               # cl.sendText(msg.to, t1 + txt + t2)
#-------Cek sider biar mirip kek siri-----------------------------
            elif "Setlastpoint" in msg.text:
                subprocess.Popen("echo '' > dataSeen/"+msg.to+".txt", shell=True, stdout=subprocess.PIPE)
                #cl.sendText(msg.to, "Checkpoint checked!")
                cl.sendText(msg.to, "Set the lastseens' point(｀・ω・´)\n\n" + datetime.now().strftime('%H:%M:%S'))
                print "Setlastpoint"
#--------------------------------------------
            elif "Viewlastseen" in msg.text:
	        lurkGroup = ""
	        dataResult, timeSeen, contacts, userList, timelist, recheckData = [], [], [], [], [], []
                with open('dataSeen/'+msg.to+'.txt','r') as rr:
                    contactArr = rr.readlines()
                    for v in xrange(len(contactArr) -1,0,-1):
                        num = re.sub(r'\n', "", contactArr[v])
                        contacts.append(num)
                        pass
                    contacts = list(set(contacts))
                    for z in range(len(contacts)):
                        arg = contacts[z].split('|')
                        userList.append(arg[0])
                        timelist.append(arg[1])
                    uL = list(set(userList))
                    for ll in range(len(uL)):
                        try:
                            getIndexUser = userList.index(uL[ll])
                            timeSeen.append(time.strftime("%d日 %H:%M:%S", time.localtime(int(timelist[getIndexUser]) / 1000)))
                            recheckData.append(userList[getIndexUser])
                        except IndexError:
                            conName.append('nones')
                            pass
                    contactId = cl.getContacts(recheckData)
                    for v in range(len(recheckData)):
                        dataResult.append(contactId[v].displayName + ' ('+timeSeen[v]+')')
                        pass
                    if len(dataResult) > 0:
                        grp = '\n• '.join(str(f) for f in dataResult)
                        total = '\nThese %iuesrs have seen at the lastseen\npoint(｀・ω・´)\n\n%s' % (len(dataResult), datetime.now().strftime('%H:%M:%S') )
                        cl.sendText(msg.to, "• %s %s" % (grp, total))
                    else:
                        cl.sendText(msg.to, "Sider ga bisa di read cek setpoint dulu bego tinggal ketik\nSetlastpoint\nkalo mau liat sider ketik\nViewlastseen")
                    print "Viewlastseen"
#==========================================
            elif ("Boom " in msg.text):
                                if msg.from_ in owner:
                                        targets = []
                                        key = eval(msg.contentMetadata["MENTION"])
                                        key["MENTIONEES"][0]["M"]
                                        for x in key["MENTIONEES"]:
                                                targets.append(x["M"])
                                        for target in targets:
                                                try:
                                                        kk.kickoutFromGroup(msg.to,[target])
                                                except:
                                                        cl.sendText(msg.to,"Done")
 	    elif "Tampol " in msg.text:
				 if msg.from_ in owner:
                                        key = eval(msg.contentMetadata["MENTION"])
                                        key["MENTIONEES"][0]["M"]
                                        targets = []
                                        for x in key["MENTIONEES"]:
                                               targets.append(x["M"])
                                        for target in targets:
                                                try:
                                                        kc.kickoutFromGroup(msg.to,[target])
                                                        cl.sendText(msg.to,"Sukses Menampol Dia!")
                                                except:
                                                    pass
            elif ("Vkick" in msg.text):
				if msg.from_ in owner:
					targets = []
					key = eval(msg.contentMetadata["MENTION"])
					key["MENTIONEES"][0]["M"]
					for x in key["MENTIONEES"]:
						targets.append(x["M"])
					for target in targets:
						try:
							ks.kickoutFromGroup(msg.to,[target])
						except:
							cl.sendText(msg.to,"Done")
#-----------------------------------------------------------

                	    
            
            elif "Ban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[BL]ok"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Success Masuk daftar orang bejat Boss")
                            except:
                                cl.sendText(msg.to,"Error")
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[WL]ok"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Sudah di keluarkan dari daftar bejat Boss")
                            except:
                                cl.sendText(msg.to,"There was no blacklist user")
            elif msg.text in ["Clear banlist"]:
              if msg.from_ in admin:
				wait["blacklist"] = {}
				cl.sendText(msg.to,"succes clear all banlist")
				
            elif msg.text in ["Banned"]:
              if msg.from_ in admin:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
            
            elif msg.text in ["Unbanned"]:
              if msg.from_ in admin:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact to ban")
			
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing") 
                else:
                    cl.sendText(msg.to,"blacklist user list")
                    mc = "[⎈]Blacklist User[⎈]\n"
                    for mi_d in wait["blacklist"]:
                        mc += "[✗] " + cl.getContact(mi_d).displayName + " \n"
                    cl.sendText(msg.to, mc + "")
           
            
#=============================================
           
# ----------------- BAN MEMBER BY TAG 2TAG ATAU 10TAG MEMBER
            elif ("Ban repeat " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned ")
                   except:
                      pass        
#============================================
            #elif msg.text in ["Clear"]:
                #if msg.toType == 2:
                    #group = cl.getGroup(msg.to)
                    #gMembMids = [contact.mid for contact in group.invitee]
                    #for _mid in gMembMids:
                        #random.choice(KAC).cancelGroupInvitation(msg.to,[_mid])
                    #cl.sendText(msg.to,"Clear boss!!!")
            elif msg.text.lower() in ["Ats","Tag","mention all"]:
              if msg.from_ in admin:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 500:
                    mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                    cnt = Message()
                    cnt.text = "Done : " + str(jml) +  " Members"
                    cnt.to = msg.to
                    cl.sendMessage(cnt)           
                      
#===========================================
        if op.param3 == "1":
            if op.param1 in protectname:
                group = cl.getGroup(op.param1)
                try:
					group.name = wait["pro_name"][op.param1]
					cl.updateGroup(group)
					cl.sendText(op.param1, "Groupname protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass
#------------------------------------------------------------------------------------
        if op.type == 32:
			OWN = ""
			if op.param2 in Bots and admin:
				pass
			else:
				Inviter = op.param3.replace("",',')
				InviterX = Inviter.split(",")
				contact = cl.getContact(op.param2)
				ki.kickoutFromGroup(op.param1,[op.param2])
				kk.kickoutFromGroup(op.param1,[op.param2])
				kc.kickoutFromGroup(op.param1,[op.param2])
				ks.kickoutFromGroup(op.param1,[op.param2])
				kt.kickoutFromGroup(op.param1,[op.param2])
				ka.kickoutFromGroup(op.param1,[op.param2])
				kb.kickoutFromGroup(op.param1,[op.param2])
				ko.kickoutFromGroup(op.param1,[op.param2])
				ke.kickoutFromGroup(op.param1,[op.param2])
				wait["blacklist"][op.param2] = True
				f=codecs.open('st2__b.json','w','utf-8')
				json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)

        elif "@"+cl.getProfile().displayName in msg.text:
            try:
                tanya = msg.text.replace("@"+cl.getProfile().displayName,"")
                jawab = ("Jgn Tag Si "+cl.getProfile().displayName+"Ta cipok luh..!!","Berisik jgn tag si "+cl.getProfile().displayName+" dia lagi asyik ngocok...!!!")
                jawaban = random.choice(jawab)
                random.choice(KAC).sendText(msg.to,jawaban)
                random.choice(KAC).kickoutFromGroup(msg.to,[msg.from_])
            except:
                pass
#===========================================
        if op.type == 55:
            try:
				if op.param1 in wait2['readPoint']:
					Name = cl.getContact(op.param2).displayName
					if Name in wait2['readMember'][op.param1]:
						pass
					else:
						wait2['readMember'][op.param1] += "\n╠" + Name
						wait2['ROM'][op.param1][op.param2] = "╠" + Name
				else:
					cl.sendText
            except:
                pass
						
						
#------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def autoSta():
    count = 1
    while True:
        try:
           for posts in cl.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   cl.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ki.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kk.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kc.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   ks.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   kt.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          cl.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ki.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          kk.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          kc.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          ks.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
                          kt.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread1 = threading.Thread(target=autoSta)
thread1.daemon = True
thread1.start()
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()
    
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev,  5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
