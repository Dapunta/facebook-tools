import os, sys, requests, re, json, random

DefaultUAWindows   = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
HeadersGetWindows  = lambda i=DefaultUAWindows : {'Host':'www.facebook.com','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9, id-ID,id;q=0.8','Cache-Control':'max-age=0','Dpr':'2','Pragma':'akamai-x-cache-on, akamai-x-cache-remote-on, akamai-x-check-cacheable, akamai-x-get-cache-key, akamai-x-get-extracted-values, akamai-x-get-ssl-client-session-id, akamai-x-get-true-cache-key, akamai-x-serial-no, akamai-x-get-request-id,akamai-x-get-nonces,akamai-x-get-client-ip,akamai-x-feo-trace','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'"Not_A Brand";v="8", "Chromium";v="120"','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'"Windows"','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Ch-Ua-Model':'','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','Priority':'u=0, i','User-Agent':i}
HeadersPostWindows = lambda i=DefaultUAWindows : {'Host':'www.facebook.com','Accept':'*/*','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US,en;q=0.9, id-ID,id;q=0.8','Content-Type':'application/x-www-form-urlencoded','Origin':'https://www.facebook.com','Sec-Ch-Prefers-Color-Scheme':'dark','Sec-Ch-Ua':'"Not_A Brand";v="8", "Chromium";v="120"','Sec-Ch-Ua-Mobile':'?0','Sec-Ch-Ua-Platform':'"Windows"','Sec-Ch-Ua-Full-Version-List':'','Sec-Ch-Ua-Platform-Version':'','Sec-Fetch-Dest':'empty','Sec-Fetch-Mode':'cors','Sec-Ch-Ua-Model':'','Sec-Fetch-Site':'same-origin','User-Agent':i}

bold_putih = '\033[1m\033[38;5;15m'
bold_merah = '\033[1m\033[38;5;196m'
bold_cyan  = '\033[1m\033[38;5;87m'
bold_lime  = '\033[1m\033[38;5;118m'

def clear(): os.system('clear' if 'linux' in sys.platform.lower() else 'cls')

def GetData(req):
    try:
        av = re.search(r'"actorID":"(.*?)"',str(req)).group(1)
        __user = av
        __a = str(random.randrange(1,6))
        __hs = re.search(r'"haste_session":"(.*?)"',str(req)).group(1)
        __ccg = re.search(r'"connectionClass":"(.*?)"',str(req)).group(1)
        __rev = re.search(r'"__spin_r":(.*?),',str(req)).group(1)
        __spin_r = __rev
        __spin_b = re.search(r'"__spin_b":"(.*?)"',str(req)).group(1)
        __spin_t = re.search(r'"__spin_t":(.*?),',str(req)).group(1)
        __hsi = re.search(r'"hsi":"(.*?)"',str(req)).group(1)
        fb_dtsg = re.search(r'"DTSGInitialData",\[\],{"token":"(.*?)"}',str(req)).group(1)
        jazoest = re.search(r'jazoest=(.*?)"',str(req)).group(1)
        lsd = re.search(r'"LSD",\[\],{"token":"(.*?)"}',str(req)).group(1)
        Data = {'av':av,'__user':__user,'__a':__a,'__hs':__hs,'dpr':'1.5','__ccg':__ccg,'__rev':__rev,'__spin_r':__spin_r,'__spin_b':__spin_b,'__spin_t':__spin_t,'__hsi':__hsi,'__comet_req':'15','fb_dtsg':fb_dtsg,'jazoest':jazoest,'lsd':lsd}
        return(Data)
    except Exception as e: return({})

class ColakColek():

    def __init__(self, cookie):
        self.cookie = cookie
        self.r = requests.Session()
        self.req = self.r.get('https://web.facebook.com/me', headers=HeadersGetWindows(), cookies={'cookie':self.cookie}, allow_redirects=True).text.replace('\\','')
        self.data = GetData(self.req)
        tab_key = re.search(r'{"tab_key":"friends_all","id":"(.*?)"}',str(self.req)).group(1)
        self.DumpFriendlist(self.data.copy(), tab_key, None)

    def DumpFriendlist(self, data, tabkey, cursor):
        try:
            data.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'ProfileCometAppCollectionListRendererPaginationQuery','variables':json.dumps({"count":8,"cursor":cursor,"scale":2,"search":None,"id":tabkey}),'server_timestamps':True,'doc_id':'6709724792472394'})
            pos = self.r.post('https://www.facebook.com/api/graphql/', data=data, headers=HeadersPostWindows(), cookies={'cookie':self.cookie}).json()
            for x in pos['data']['node']['pageItems']['edges']:
                try:
                    rw = x['node']['actions_renderer']['action']['client_handler']['profile_action']['restrictable_profile_owner']
                    id, nm, un = str(rw['id']), str(rw['name']), str(x['node']['url']).replace('https://www.facebook.com/','').replace('profile.php?id=','')
                    # fm = '{}|{}|{}'.format(id, un, nm)
                    self.ExeColek(id, nm)
                except Exception as e: continue
            if pos['data']['node']['pageItems']['page_info']['has_next_page']:
                end_cursor = pos['data']['node']['pageItems']['page_info']['end_cursor']
                self.DumpFriendlist(data, tabkey, end_cursor)
        except KeyboardInterrupt: pass
        except Exception as e: pass

    def ExeColek(self, id, name):
        try:
            data = self.data.copy()
            data.update({'fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'PokesMutatorPokeMutation','variables':json.dumps({"input":{"client_mutation_id":"1","actor_id":data.get('__user'),"user_id":id}}),'server_timestamps':True,'doc_id':'5028133957233114'})
            pos = self.r.post('https://www.facebook.com/api/graphql/', data=data, headers=HeadersPostWindows(), cookies={'cookie':self.cookie}).json()
            if pos['data']['user_poke']['user']['poke_status'] == 'PENDING': print('{}Berhasil {}Mencolek {}{}{}'.format(bold_lime, bold_putih, bold_cyan, name, bold_putih))
            else: print('{}Gagal {}Mencolek {}{}{}'.format(bold_merah, bold_putih, bold_cyan, name, bold_putih))
        except Exception as e: print('{}Gagal {}Mencolek {}{}{}'.format(bold_merah, bold_putih, bold_cyan, name, bold_putih))

if __name__ == '__main__':
    clear()
    cookie = input('Masukkan Cookie : ')
    print('')
    ColakColek(cookie)