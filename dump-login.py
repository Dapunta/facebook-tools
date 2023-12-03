# Python 3.10
# Made With Mobile, Web, And GraphQL Facebook

#--> Author's Info
Author    = 'Dapunta Khurayra X'
Facebook  = 'Facebook.com/Dapunta.Khurayra.X'
Instagram = 'Instagram.com/Dapunta.Ratya'
Whatsapp  = 'Wa.me/6282245780524'
YouTube   = 'Youtube.com/channel/UCZqnZlJ0jfoWSnXrNEj5JHA'

#--> Import Default Module & Library
import os, sys, random, json, re, concurrent, time, shutil
from concurrent.futures import ThreadPoolExecutor
from random import choice as rc
from random import randrange as rr

#--> Clear Terminal
def clear():
    if 'linux' in sys.platform.lower():os.system('clear')
    elif 'win' in sys.platform.lower():os.system('cls')

#--> Import Extra Module & Library
def mod():
    global requests, bs4, bs
    clear()
    try: import requests
    except Exception as e: os.system('pip install requests'); import requests
    try: import bs4
    except Exception as e: os.system('pip install bs4'); import bs4
    from bs4 import BeautifulSoup as bs
    try: os.mkdir('login')
    except Exception as e: pass
    clear()

#--> Global Variable
DefaultUAWindows = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
RandomUAWindows  = lambda : 'Mozilla/5.0 (Windows NT %s.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/%s.%s.%s.%s Safari/537.36'%(rc(['10','11']),rr(110,201),rr(0,10),rr(0,10),rr(0,10))
HeadersGet  = lambda i=DefaultUAWindows : {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Cache-Control':'max-age=0','Dpr':'1','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':'','Sec-Ch-Ua-Platform':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'none','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent':i}
HeadersPost = lambda i=DefaultUAWindows : {'Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9','Content-Length':'1545','Content-Type':'application/x-www-form-urlencoded','Dpr':'1','Origin':'https://www.facebook.com','Referer':'https://www.facebook.com','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':"",'Sec-Ch-Ua-Full-Version-List':"",'Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Model':"",'Sec-Ch-Ua-Platform':"",'Sec-Ch-Ua-Platform-Version':"",'Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Fetch-Site':'same-origin','User-Agent':i}

#--> Login
class Login():

    #--> Initialization
    def __init__(self):
        self.r = requests.Session()
        self.CekCookies()
        Menu()
    
    #--> Check Cookies
    def CekCookies(self):
        try:
            self.cookie = open('login/cookie.json','r').read()
            req = self.r.get('https://www.facebook.com/profile.php', headers=HeadersGet(), cookies={'cookie':self.cookie}, allow_redirects=True).text
            id, name = list(re.findall('"USER_ID":"(.*?)","NAME":"(.*?)"',str(req))[0])
            if id == '0': self.InputCokies(); id, name = list(re.findall('"USER_ID":"(.*?)","NAME":"(.*?)"',str(req))[0])
            clear()
            print('Login Sebagai %s\n'%(name))
        except Exception as e: self.InputCokies()
    
    #--> Save Cookies
    def InputCokies(self):
        print('Cookie Invalid!')
        time.sleep(2)
        clear()
        cok = input('Input Cookies : ')
        open('login/cookie.json','w').write(cok)
        self.CekCookies()

#--> Logout
def Logout():
    c = input('Yakin Ingin Logout ? [y/t] : ').lower()
    if c=='y':
        try: shutil.rmtree('login'); print('Berhasil Logout\n')
        except Exception as e: print('Gagal Logout\n')
    else: print('Batal Logout\n')

#--> Menu
class Menu():

    #--> Initialization
    def __init__(self):
        self.result = []
        print('[ Dump Menu ]')
        print('[1] Friendlist')
        print('[2] Followers')
        print('[3] Member Group')
        print('[4] Search Name')
        print('[0] Logout')
        x = input('Pilih : ')
        print('')
        if   x in ['0','00','000','z']: Logout()
        elif x in ['1','01','001','a']: self.MenuFriendlist()
        elif x in ['2','02','002','b']: self.MenuFollowers()
        elif x in ['3','03','003','c']: self.MenuMemberGroup()
        elif x in ['4','04','004','d']: self.MenuSearchName()
        elif x in ['5','05','005','e']: pass
        else: print('Isi Yang Benar!'); exit()
        print('\rBerhasil Dump %s ID'%(str(len(self.result))))

    #--> Menu Friendlist
    def MenuFriendlist(self):
        DP = Dump()
        p = input('Masukkan ID/URL Akun Target : ').split(',')
        print('')
        print('Tekan ctrl+c Untuk Berhenti')
        for lk in p:
            try:
                url = ConvertURL(lk)
                DP.Friendlist(url,self.result)
            except Exception as e:
                print('Target : %s'%(lk))
                print('Error, Something Went Wrong!\n')
    
    #--> Menu Followers
    def MenuFollowers(self):
        DP = Dump()
        p = input('Masukkan ID/URL Akun Target : ').split(',')
        print('')
        print('Tekan ctrl+c Untuk Berhenti')
        for lk in p:
            try:
                url = ConvertURL(lk)
                DP.Followers(url,self.result)
            except Exception as e:
                print('Target : %s'%(lk))
                print('Error, Something Went Wrong!\n')

    #--> Menu Member Group
    def MenuMemberGroup(self):
        DP = Dump()
        p = input('Masukkan ID/URL Grup Target : ').split(',')
        print('')
        print('Tekan ctrl+c Untuk Berhenti')
        for lk in p:
            try:
                url = ConvertURL(lk)
                DP.MemberGroup(url,self.result)
            except Exception as e:
                print('Target : %s'%(lk))
                print('Error, Something Went Wrong!\n')

    #--> Menu Search Name
    def MenuSearchName(self):
        DP = Dump()
        p = input('Masukkan Nama : ').split(',')
        print('')
        print('Tekan ctrl+c Untuk Berhenti')
        for lk in p:
            try:
                nm = lk.replace(' ','+')
                url = f'https://www.facebook.com/search/people/?q={nm}'
                DP.SearchName(url,self.result)
            except Exception as e:
                print('Target : %s'%(lk))
                print('Error, Something Went Wrong!\n')

#--> Convert ID To URL
def ConvertURL(i):
    if 'http' in str(i):
        if 'www.facebook.com' in str(i): url = i
        elif 'm.facebook.com' in str(i): url = i.replace('m.facebook.com','www.facebook.com')
        elif 'mbasic.facebook.com' in str(i): url = i.replace('mbasic.facebook.com','www.facebook.com')
    else:
        if 'www.facebook.com' in str(i): url = 'https://' + i
        elif 'm.facebook.com' in str(i): url = 'https://' + i.replace('m.facebook.com','www.facebook.com')
        elif 'mbasic.facebook.com' in str(i): url = 'https://' + i.replace('mbasic.facebook.com','www.facebook.com')
        else:
            if 'facebook.com' in str(i): url = 'https://www.facebook.com' + i.replace('facebook.com','').replace('Facebook.com','')
            else: url = 'https://www.facebook.com/%s'%(i)
    return(url)

#--> Get Data Payload
def GetData(req):
    try:
        act = re.search('"actorID":"(.*?)"',str(req)).group(1)
        hst = re.search('"haste_session":"(.*?)",',str(req)).group(1)
        rev = re.search('{"rev":(.*?)}',str(req)).group(1)
        hsi = re.search('"hsi":"(.*?)",',str(req)).group(1)
        dts = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"',str(req)).group(1)
        jzt = re.search('&jazoest=(.*?)",',str(req)).group(1)
        lsd = re.search('"LSD",\[\],{"token":"(.*?)"',str(req)).group(1)
        spr = re.search('"__spin_r":(.*?),',str(req)).group(1)
        spt = re.search('"__spin_t":(.*?),',str(req)).group(1)
        dta = {'av':act, '__user':act, '__a':'1', '__hs':hst, 'dpr':'1.5', '__ccg':'EXCELLENT', '__rev':rev, '__hsi':hsi, '__comet_req':'15', 'fb_dtsg': dts, 'jazoest': jzt, 'lsd': lsd, '__spin_b':'trunk', '__spin_r':spr, '__spin_t':spt}
        return(dta)
    except Exception as e: return({None})

#--> Dump Method
class Dump():

    #--> Initialization
    def __init__(self):
        self.loop = 1
        self.cookie = open('login/cookie.json','r').read()

    #--> Dump ID From Friendlist
    def Friendlist(self, url, result, r=None, dta=None, cur=None, id_post=None):
        if r==None and cur==None:
            r = requests.Session()
            req = bs(r.get(url,headers=HeadersGet(),cookies={'cookie':self.cookie},allow_redirects=True).content,'html.parser')
            try:
                dta = GetData(req)
                id_post = re.search('{"tab_key":"friends_all","id":"(.*?)"}',str(req)).group(1)
                target_id = re.search('"userID":"(.*?)"',str(req)).group(1)
                target_name = re.search('"__isProfile":"User","name":"(.*?)"',str(req)).group(1)
                print('ID : %s'%(target_id))
                print('Name : %s'%(target_name))
            except Exception as e:
                print('URL : %s'%(url))
                print('Friendlist Private Atau ID Tidak Ditemukan!')
                exit()
        var = {"count":8,"cursor":cur,"scale":1.5,"search":None,"id":id_post}
        dta.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'ProfileCometAppCollectionListRendererPaginationQuery','variables':json.dumps(var),'server_timestamps':True,'doc_id': '6767163196701249'})
        pos = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=HeadersPost(),cookies={'cookie':self.cookie}).json()
        for x in pos['data']['node']['pageItems']['edges']:
            try:
                id   = x['node']['actions_renderer']['action']['client_handler']['profile_action']['restrictable_profile_owner']['id']
                name = x['node']['actions_renderer']['action']['client_handler']['profile_action']['restrictable_profile_owner']['name']
                user = x['node']['url'].split('/')[-1].replace('profile.php?id=','')
                info = x['node']['subtitle_text']['text']
                plot = '%s|%s|%s|%s'%(id,user,name,info)
                if plot in result: pass
                else: result.append(plot)
                print('\rSedang Dump %s ID'%(str(len(result))),end=''); sys.stdout.flush()
            except KeyboardInterrupt: self.loop=0; pass
            except Exception as e: pass
        try:
            jut = pos['data']['node']['pageItems']['page_info']
            if jut['has_next_page'] and self.loop:
                cur = jut['end_cursor']
                self.Friendlist(url, result, r, dta, cur, id_post)
        except KeyboardInterrupt: self.loop=0; pass
        except Exception as e: pass

    #--> Dump ID From Followers
    def Followers(self, url, result, r=None, dta=None, cur=None, id_post=None):
        if r==None and cur==None:
            r = requests.Session()
            req = bs(r.get(url,headers=HeadersGet(),cookies={'cookie':self.cookie},allow_redirects=True).content,'html.parser')
            try:
                dta = GetData(req)
                id_post = re.search('{"tab_key":"followers","id":"(.*?)"}',str(req)).group(1)
                target_id = re.search('"userID":"(.*?)"',str(req)).group(1)
                target_name = re.search('"__isProfile":"User","name":"(.*?)"',str(req)).group(1)
                print('ID : %s'%(target_id))
                print('Name : %s'%(target_name))
            except Exception as e:
                print('URL : %s'%(url))
                print('Followers Private Atau ID Tidak Ditemukan!')
                exit()
        var = {"count":8,"cursor":cur,"scale":1.5,"search":None,"id":id_post}
        dta.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'ProfileCometAppCollectionListRendererPaginationQuery','variables':json.dumps(var),'server_timestamps':True,'doc_id': '6767163196701249'})
        pos = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=HeadersPost(),cookies={'cookie':self.cookie}).json()
        for x in pos['data']['node']['pageItems']['edges']:
            try:
                id   = x['node']['actions_renderer']['profile_actions'][0]['client_handler']['profile_action']['restrictable_profile_owner']['id']
                name = x['node']['actions_renderer']['profile_actions'][0]['client_handler']['profile_action']['restrictable_profile_owner']['name']
                user = x['node']['url'].split('/')[-1].replace('profile.php?id=','')
                info = x['node']['subtitle_text']['text']
                plot = '%s|%s|%s|%s'%(id,user,name,info)
                if plot in result: pass
                else: result.append(plot)
                print('\rSedang Dump %s ID'%(str(len(result))),end=''); sys.stdout.flush()
            except KeyboardInterrupt: self.loop=0; pass
            except Exception as e: pass
        try:
            jut = pos['data']['node']['pageItems']['page_info']
            if jut['has_next_page'] and self.loop:
                cur = jut['end_cursor']
                self.Followers(url, result, r, dta, cur, id_post)
        except KeyboardInterrupt: self.loop=0; pass
        except Exception as e: pass

    #--> Dump ID From Members Group
    def MemberGroup(self, url, result, r=None, dta=None, cur=None, id_group=None):
        if r==None and cur==None:
            r = requests.Session()
            req = bs(r.get(url,headers=HeadersGet(),cookies={'cookie':self.cookie}).content,'html.parser')
            try:
                dta = GetData(req)
                id_group = re.search('"groupID":"(.*?)"',str(req)).group(1)
                name_group = re.search('"meta":{"title":"(.*?)","accessory"',str(req)).group(1)
                print('ID : %s'%(id_group))
                print('Name : %s'%(name_group))
            except Exception as e:
                print('URL : %s'%(url))
                print('Group Private Atau ID Tidak Ditemukan!')
                exit()
        var = {"count":10,"cursor":cur,"groupID":id_group,"recruitingGroupFilterNonCompliant":False,"scale":1.5,"id":id_group}
        dta.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'GroupsCometMembersPageNewMembersSectionRefetchQuery','variables':json.dumps(var),'server_timestamps':True,'doc_id':'6621621524622624'})
        pos = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=HeadersPost(),cookies={'cookie':self.cookie}).json()
        for x in pos['data']['node']['new_members']['edges']:
            try:
                id   = x['node']['id']
                name = x['node']['name']
                user = x['node']['url'].split('/')[-1].replace('profile.php?id=','')
                info = x['node']['bio_text']['text']
                plot = '%s|%s|%s|%s'%(id,user,name,info)
                if plot in result: pass
                else: result.append(plot)
                print('\rSedang Dump %s ID'%(str(len(result))),end=''); sys.stdout.flush()
            except KeyboardInterrupt: self.loop=0; pass
            except Exception as e: pass
        try:
            jut = pos['data']['node']['new_members']['page_info']
            if jut['has_next_page'] and self.loop:
                cur = jut['end_cursor']
                self.MemberGroup(url, result, r, dta, cur, id_group)
        except KeyboardInterrupt: self.loop=0; pass
        except Exception as e: pass
    
    #--> Dump ID From Search Name
    def SearchName(self, url, result, r=None, dta=None, cur=None, bsid=None):
        if r==None and cur==None:
            r = requests.Session()
            req = bs(r.get(url,headers=HeadersGet(),cookies={'cookie':self.cookie}).content,'html.parser')
            try:
                dta = GetData(req)
                bsid = re.search('"bsid":"(.*?)"',str(req)).group(1)
            except Exception as e:
                print('URL : %s'%(url))
                print('Nama Tidak Ditemukan!')
                exit()
        var = {"UFI2CommentsProvider_commentsKey":"SearchCometResultsInitialResultsQuery","allow_streaming":False,"args":{"callsite":"COMET_GLOBAL_SEARCH","config":{"exact_match":False,"high_confidence_config":None,"intercept_config":None,"sts_disambiguation":None,"watch_config":None},"context":{"bsid":bsid,"tsid":None},"experience":{"encoded_server_defined_params":None,"fbid":None,"type":"PEOPLE_TAB"},"filters":[],"text":url.split('=')[-1].replace('+',' ')},"count":5,"cursor":cur,"displayCommentsContextEnableComment":False,"displayCommentsContextIsAdPreview":False,"displayCommentsContextIsAggregatedShare":False,"displayCommentsContextIsStorySet":False,"displayCommentsFeedbackContext":None,"feedLocation":"SEARCH","feedbackSource":23,"fetch_filters":True,"focusCommentID":None,"locale":None,"privacySelectorRenderLocation":"COMET_STREAM","renderLocation":"search_results_page","scale":1.5,"stream_initial_count":0,"useDefaultActor":False,"__relay_internal__pv__IsWorkUserrelayprovider":False,"__relay_internal__pv__IsMergQAPollsrelayprovider":False,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":False,"__relay_internal__pv__CometUFIIsRTAEnabledrelayprovider":False,"__relay_internal__pv__StoriesArmadilloReplyEnabledrelayprovider":False,"__relay_internal__pv__StoriesRingrelayprovider":False}
        dta.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'SearchCometResultsPaginatedResultsQuery','variables':json.dumps(var),'server_timestamps':True,'doc_id':'7704205549605925'})
        pos = r.post('https://www.facebook.com/api/graphql/',data=dta,headers=HeadersPost(),cookies={'cookie':self.cookie}).json()
        for x in pos['data']['serpResponse']['results']['edges']:
            try:
                id   = x['relay_rendering_strategy']['view_model']['loggedProfile']['id']
                name = x['relay_rendering_strategy']['view_model']['loggedProfile']['name']
                user = x['relay_rendering_strategy']['view_model']['loggedProfile']['url'].split('/')[-1].replace('profile.php?id=','')
                info = x['relay_rendering_strategy']['view_model']['primary_snippet_text_with_entities']['text']
                plot = '%s|%s|%s|%s'%(id,user,name,info)
                if plot in result: pass
                else: result.append(plot)
                print('\rSedang Dump %s ID'%(str(len(result))),end=''); sys.stdout.flush()
            except KeyboardInterrupt: self.loop=0; pass
            except Exception as e: pass
        try:
            jut = pos['data']['serpResponse']['results']['page_info']
            if jut['has_next_page'] and self.loop:
                cur = jut['end_cursor']
                self.SearchName(url, result, r, dta, cur, bsid)
        except KeyboardInterrupt: self.loop=0; pass
        except Exception as e: pass

#--> Trigger
if __name__ == '__main__':
    mod()
    Login()