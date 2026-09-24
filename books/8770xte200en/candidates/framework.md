# 妗嗘灦/娴佺▼/缁撴瀯鍊欓€?鈥?OmniVista 8770 (8770XTE200EN Ed47)

> 鎻愬彇鍣? framework-extractor锛堝叏閲忔壂鎻忥級 | 鍏ㄥ眬涓婁笅鏂? BOOK_OVERVIEW.md | 鎻愬彇鏃ユ湡: 2026-09-23
>
> 瑕嗙洊鑼冨洿锛氱珷鑺傛帹杩涢€昏緫銆佺鍒扮娴佺▼銆佹搷浣滆彍鍗曡矾寰勩€佺粍浠跺叧绯诲浘绀恒€佸钩鍙?鐣岄潰鍒嗗尯銆傚疄楠岀幆澧冪粰瀹氬€硷紙IP/瀵嗙爜/璐﹀彿/鍙风爜锛変竴寰嬫爣娉?瀹為獙鍙ｅ緞"銆?
```yaml
- id: f01
  title: 鍏ㄤ功璇剧▼鎺ㄨ繘閫昏緫鈥斺€旇骞冲彴 鈫?鎺ヨ妭鐐?鈫?绠＄敤鎴?鍛婅 鈫?澧炲€煎煙 鈫?鍏滃簳缁存姢
  type: flow
  source_pages: p3-705
  source_chapter: 鍏ㄤ功绔犺妭缂栨帓锛圫olution Overview 鈫?鍚勮涔?How-To 閰嶅锛?  source_quote: |
    "LESSON SUMMARY 鉁?General overview 鉁?Network topology 鉁?Architecture 鉁?Virtualization
    鉁?Cross compatibility 鉁?Applications suite 鉁?Setup suite 鉁?Network suite 鉁?Reports suite
    鉁?Directory suite 鉁?8770 WBM client 鉁?Conclusion" (p4)
    "How to 鉁?Install the OmniVista 8770 Server on Windows 2022 Server Operating System" (p65)
  summary: |
    鍏ㄤ功 24 涓涔夌珷 + 27 涓?How-To 瀹為獙绔犳寜涓冩鎺ㄨ繘锛氣憼瑙ｅ喅鏂规姒傝锛堟灦鏋?铏氭嫙鍖?鍏煎鐭╅樀/濂椾欢鍏ㄦ櫙锛夛紱鈶LAB 瀹為獙骞冲彴锛涒憿鏈嶅姟鍣ㄤ笌瀹㈡埛绔畨瑁咃紙2022 涓?2019 涓ゅ骞跺垪 How-To锛夛紱鈶ｈ妭鐐规敞鍐岋紙OXE 澹版槑+鍚屾銆丱XE SSH銆丱XO Connect 澹版槑锛夛紱鈶ょ敤鎴峰紑閫氾紙Users 搴旂敤 Profile/Meta profile/鎵归噺銆乄BM 寮€閫氥€丮anage My Phone锛夛紱鈶ュ憡璀︿綋绯伙紙Alarms 鏋舵瀯銆丱XE 鎺ュ叆銆佸姛鑳藉畾鍒躲€丼NMP Proxy锛変笌鍙鍖?瀹¤锛圱opology 鏍囧噯涓庤嚜瀹氫箟銆丄udit锛夛紱鈶︽姤琛ㄤ换鍔★紙Reports/Scheduler/鑷姩缁存姢锛変笌缁存姢鍏滃簳锛?770 澶囦唤鎭㈠/缁存姢宸ュ叿/NMC 鏈嶅姟/OXE 澶囦唤/璁稿彲/缃戠粶椹卞姩鍣ㄦ槧灏勶級銆傛瘡绔?璁蹭箟鈫扝ow-To"閰嶅锛屾槸瀹為檯浜や粯椤圭洰鐨勬帹鑽愰『搴忋€?  conditions: 鏃犵増鏈墠鎻愶紱鍚?How-To 渚濊禆鍓嶄竴闃舵浜у嚭锛堝鑺傜偣娉ㄥ唽渚濊禆鏈嶅姟鍣ㄥ畨瑁呭畬鎴愶級
  tags: [flow, course-structure, delivery-order]

- id: f02
  title: RLAB 杩滅▼瀹為獙骞冲彴缁撴瀯鈥斺€擯OD 姹?+ 鍏叡璧勬簮鍖?+ 浜旇櫄鏈哄疄渚嬭〃
  type: structure
  source_pages: p41-52
  source_chapter: REMOTE LABS PLATFORM / Introduction & Training Platform & Settings
  source_quote: |
    "Remote Lab allows accessing a pool of virtual machines and hardware (when required)
    hosted in a data center." (p43)
    "OXE 8770_OXE_SETUP csa (physical) csm (main) 192.168.1.1 192.168.1.3 ... OMNIVISTA 8770
    SERVER 8770_OV8770_SRV nms 192.168.1.70" (p47)
  summary: |
    瀹為獙骞冲彴涓ゅ眰锛歅OD 1..n 鐩镐簰鐙珛銆侀厤缃浉鍚岋紱鍏叡 Pod 鎻愪緵 NAS锛堣蒋浠躲€佽鍙級銆侀偖浠舵湇鍔″櫒绛夊叡浜祫婧愩€傛瘡涓?POD 鍐?5 鍙板疄渚嬶紙瀹為獙鍙ｅ緞锛夛細OXE锛坈sa 鐗╃悊 192.168.1.1 / csm 涓荤敤 192.168.1.3锛岀櫥褰?mtcl/swinst/root锛屽瘑鐮?Superuser2580*锛岄寤虹敤鎴?31000 Brad Barkley / 31001 Billy Backman / 31002 Betty Boop锛夈€丱MS/GD锛?92.168.1.13锛宎dmin/root锛夈€丗lexLM 璁稿彲鏈嶅姟鍣紙192.168.1.80锛宺oot/letacla1锛夈€丆lient PC锛?92.168.1.10锛孉dministrator/superuser锛岃 IPDSP + 2 涓?MicroSIP + 1 涓叕缃?MicroSIP + TrapReceiver锛夈€丱mniVista 8770 鏈嶅姟鍣紙nms锛?92.168.1.70锛孉dministrator/superuser锛夈€傜綉鍏?192.168.1.254锛屽唴閮?DNS 192.168.1.250锛屽閮?DNS 10.20.30.250銆傝闂柟寮忎袱绉嶏細Console mode锛堢瀹炰緥銆佽鏈嶅姟鍣紝鏃犻煶棰戯級涓?RDP 杩滅▼妗岄潰锛堝疄楠屽繀鐢紝鍏变韩杞數璇濋煶棰戯級銆?  conditions: 浠呭煿璁幆澧冿紙RLAB锛夛紝鎵€鏈?IP/瀵嗙爜涓哄疄楠屽彛寰勶紱POD 闂翠簰涓嶅彲瑙侊紝NAS 涓庨偖浠舵湇鍔″櫒涓哄叏鐝叡浜?  tags: [structure, lab, rlab, topology]

- id: f03
  title: OmniVista 8770 鎬讳綋鏋舵瀯涓€寮犲浘鈥斺€斿鎴风/鏈嶅姟鍣?琚鑺傜偣鍗忚鍏崇郴
  type: diagram
  source_pages: p6-7
  source_chapter: SOLUTION OVERVIEW / Network topology & Architecture
  source_quote: |
    "8770 Client ... Graphical User Interface (GUI) to manage 8770 applications 鈥?Simultaneous
    access to OmniVista 8770 Server ... HTTPS, LDAP(S) ... IPsec, Corba, TDS, LDAP(S) ...
    CMISE, (S)FTP, Telnet/SSH, LDAP 鈥?OXO Connect ... OMC (FTP, HTTPS)" (p6-7)
  summary: |
    鎷撴墤涓夊眰锛氣憼8770 Client锛坱hick 瀹㈡埛绔紝闇€鐧诲綍瀵嗙爜锛変笌 8770 WBM client锛圚TML 鐩綍璁块棶锛屽厑璁稿尶鍚嶏級缁?LAN 浠?IP 杩為€氭€ц闂?8770 鏈嶅姟鍣紱鈶℃湇鍔″櫒鍐呴儴缁勪欢锛歄V8770 Services銆乄eb Directory銆丮anage My Phone銆丮ariaDB(SQL)銆丩DAP锛涒憿琚鑺傜偣锛歄XE 璧?CMISE/(S)FTP/Telnet/SSH/LDAP锛孫XE SIP 璇濇満璧?HTTPS/SNMP锛孫XO Connect 缁?OMC(FTP,HTTPS)锛孫penTouch 璧?XML Web Services锛坧139 琛ュ厖锛夛紱澶栭儴渚濊禆 SMTP 閭欢銆丼NMP Hypervisor銆丮ass provisioning 鐨?LDAP Client import銆傚崗璁垎宸ユ槸鍏ㄤ功鍚勭珷鐨勫簳灞傦細閰嶇疆璧?CMISE銆佸憡璀﹁蛋 CMISE/Corba銆佹暟鎹彁鍙栬蛋 FTP/SSH銆?  conditions: 鏃犵増鏈墠鎻愶紱OXO Connect 鐨勯厤缃湰浣撳湪 OMC 涓畬鎴愶紙8770 鍙仛绾崇涓庝唬鐞嗭級
  tags: [diagram, architecture, protocols]

- id: f04
  title: 搴旂敤濂椾欢鍏ㄦ櫙鈥斺€斿洓澶у浠?+ WBM 瀹㈡埛绔殑鍔熻兘鍒嗗尯
  type: structure
  source_pages: p10-39
  source_chapter: SOLUTION OVERVIEW / Applications & Setup & Network & Reporting & Directory suites
  source_quote: |
    "Administration Security Maintenance Scheduler 鈥?Server Administration ... Configuration
    Alarms Topology Audit Maintenance 鈥?PCX Administration & Supervision ... Accounting
    Reports Accounting & Performance monitoring ... Directory Web Directory" (p10)
  summary: |
    thick client 鍥涘浠讹細鈶燬etup 濂椾欢锛圓dministration 鏈嶅姟鍣ㄧ鐞?Security 鏉冮檺/8770 Maintenance 鏈嶅姟鍣ㄧ淮鎶?Scheduler 浠诲姟缂栨帓锛夛紱鈶etwork 濂椾欢锛圕onfiguration 鑺傜偣澹版槑閰嶇疆/OXO Connect Supervision/OXO Connect Configuration/Users 鐢ㄦ埛/Devices SIP 璁惧/Alarms 鍛婅/Topology 鎷撴墤/Audit 瀹¤/Maintenance 鑺傜偣缁存姢锛夛紱鈶eporting 濂椾欢锛圓ccount./Traf./VoIP 璁¤垂涓庤瘽鍔?Reports 缁熶竴鎶ュ憡锛夛紱鈶irectory 濂椾欢锛圖irectory LDAP 鐩綍/Web Directory 瀹㈡埛绔級銆俉BM 杞诲鎴风鍥涘簲鐢紙Users/Configuration/Performance/Manage My Phone锛夐渶 Unified Management 璁稿彲銆傚悇濂椾欢涓庡悗缁?How-To 绔犱竴涓€瀵瑰簲锛屾槸鑿滃崟瀵艰埅鐨勬€诲湴鍥俱€?  conditions: Devices 搴旂敤浠呴潰鍚?OXE 鐨?SIP 璁惧锛汷XO Supervision 闇€ OMC 瑁呭湪 8770 鏈嶅姟鍣ㄤ笌姣忎釜瀹㈡埛绔紙p20锛?  tags: [structure, application-suite, menu-map]

- id: f05
  title: 鏈嶅姟鍣ㄥ畨瑁呮祦绋嬩竷姝ラ摼鈥斺€旂郴缁熼厤缃?鈫?蹇呰缁勪欢 鈫?8770 瀹夎 鈫?琛ヤ竵
  type: flow
  source_pages: p57-63, p65-88
  source_chapter: SERVER INSTALLATION / Installation steps & How-To
  source_quote: |
    "Computer Settings / FQDN & IP settings / Mandatory items installation (MariaDB, Microsoft
    Visual C++ Packages) / 8770 Server installation / License / Data collection / Patches
    Installation" (p57)
    "Step #1 Microsoft Visual C++ MariaDB Server & ODBC Driver Installation ... Step #2 License
    & data collection LDAP Oracle DSEE Directory Server ... 8770 Applications Open JRE embedded
    Apache/Wildfly servers" (p60-61)
  summary: |
    瀹夎涓婚摼锛氣憼Windows 鏁版嵁閰嶇疆锛圢TFS 鍒嗗尯銆佽绠楁満鍚?nms + DNS 鍚庣紑 company.com銆侀潤鎬?IP 192.168.1.70锛夛紱鈶″弻鍑?ServerSetup.exe 鍏堣 MariaDB + Visual C++ 鍖咃紙鑷姩锛夛紝閫夎鍙枃浠讹紙License verification 鍏ㄩ儴 Valid锛夈€佸叕鍙稿悕锛堣鍚庝笉鍙敼锛夈€佸洓涓洰褰曪紙C:\8770銆丆:\8770\SunONE銆丆:\8770\data銆丆:\8770_ARC锛夈€侀偖浠舵湇鍔″櫒锛堝彲璺宠繃锛夈€丩DAP 389/LDAPS 636 绔彛銆佺洰褰曠鐞嗗櫒瀵嗙爜銆丄dminNmc 璐︽埛銆佸浗瀹讹紙鍐冲畾璇█/甯佺/绾稿紶锛夈€佽璐规垚鏈腑蹇冩柟寮忥紙瑁呭悗涓嶅彲鏀癸級銆侀閰嶇疆锛堝彲璺宠繃锛夛紱鈶㈠畬鎴愰噸鍚紱鈶ｈˉ涓侊細鎷峰叆 C:\8770\install\patches 鈫?绠＄悊鍛樿繍琛?PatchInstaller.exe 鈫?鏌?Patch_Installer.log 灏鹃儴 "Patch installation terminated: success"锛涒懁棣栨杩炴帴 AdminNmc/superuser 鏀瑰瘑 Superuser01*銆傚墠缃袱浠?Windows 绠＄悊蹇呭仛锛氬叧 IE ESC銆丏efender 鎺掗櫎 C:\8770锛圓larms/Topology 鍚敤鍓嶆彁锛夈€?  conditions: 鏈嶅姟鍣ㄥ繀椤诲厛鎺ュ叆 IP 缃戠粶骞舵湁闈欐€?IP+缃戝叧锛涗笉寰椾粠缃戠粶鐩?iso 鎸傝浇/vSphere 鐩存帴瀹夎锛涘唴瀛樺崰鐢ㄩ』 <85%
  tags: [flow, installation, windows-server, patch]

- id: f06
  title: 瀹㈡埛绔畨瑁呭弻閫氶亾涓庨娆¤繛鎺ュ弬鏁?  type: flow
  source_pages: p94, p96-106
  source_chapter: CLIENT INSTALLATION / How-To
  source_quote: |
    "Client installation 鈥?From the 8770 ISO file / From the 8770 Server -> URL to download
    client installation program / Open JRE embedded" (p94)
    "Enter the following URL: https://<8770 FQDN>/cgi-bin/OmniVista8770Client.exe Be careful,
    the URL is case sensitive!" (p99)
  summary: |
    瀹㈡埛绔幏鍙栦袱娉曪細8770 ISO 鍐?ClientSetup.exe锛堜功涓爣娉?浠呬緵淇℃伅銆佸嬁鎵ц"锛夛紱鎴栦粠鏈嶅姟鍣?Web 涓嬭浇 http(s)://<8770 FQDN>/cgi-bin/OmniVista8770Client.exe锛堝ぇ灏忓啓鏁忔劅锛岄渶绠＄悊鍛樺嚟鎹級銆傚畨瑁呭悜瀵煎厛瑁?Windows 鍖呭啀瑁呬富浣擄紙榛樿鐩綍 C:\Client8770 5.2\锛夛紝鍐呭祵 Open JRE銆傞娆¤繛鎺ワ細Server name 濉?FQDN 鎴?IP銆佺鍙ｈ嚜鍔ㄥ～ LDAPS 636銆丄dminNmc/鍒濆瀵嗙爜鐧诲綍銆佸己鍒舵敼瀵嗭紱Windows Defender 闃茬伀澧欎細鎷︽埅 Zulu Platform x32 妯″潡锛屽繀椤诲厑璁镐笓鐢ㄧ綉缁溿€傛湇鍔″櫒淇℃伅瀛?C:\Users\<璐︽埛>\nmc5_5.2.cfg锛屼笅娆＄洿杈剧櫥褰曢〉銆俉indows 11 build 22572 璧?WMIC 琚純鐢紝闇€鍏堝湪鍙€夊姛鑳戒腑瑁呭洖 WMIC銆?  conditions: 瀹夎璐︽埛闇€鏈湴绠＄悊鍛樻潈闄愶紱瀹㈡埛绔‖浠跺簳绾?4GB RAM / 750MB 鍓╀綑绌洪棿锛堜綆浜庡垯 JVM 鏃犳硶鍚姩锛?  tags: [flow, client-installation, wmic]

- id: f07
  title: Configuration 搴旂敤閰嶇疆鏍戔€斺€擭etwork > Subnetwork > PCX 涓夌骇澹版槑妯″瀷
  type: structure
  source_pages: p111, p118-128, p640-667
  source_chapter: OMNIPCX ENTERPRISE NODE REGISTRATION & OXO Connect node declaration
  source_quote: |
    "CONFIGURATION TREE 鈥?NETWORK / PCX / HARDWARE / DEVICES & USERS / SUB-NETWORKS" (p111)
    "Subnetwork 鈥?Node number Enter a numeric value equal to the OmniPCX Enterprise network*100
    + OmniPCX Enterprise node number. Example: With a network number = 1 and node number = 2,
    you must enter 101" (p123)
  summary: |
    澹版槑璺緞锛欳onfiguration 搴旂敤鍙抽敭 nmc 鏍?鈫?Create > Network锛堝悕绉?ale銆佺綉缁滃彿涓鸿嚜鐢卞彿锛夆啋 鍙抽敭缃戠粶 鈫?Create > Subnetwork锛堝悕绉?abc1銆佸瓙缃戝彿蹇呴』绛変簬 OXE 缃戠粶鍙凤級鈫?鍙抽敭瀛愮綉 鈫?Create > OmniPCX 4400/Enterprise锛堟垨 OXO 绔犵殑 OmniPCX Office锛夈€傝妭鐐瑰叧閿〉绛撅細PCX 椤碉紙鍚嶇О銆佽妭鐐瑰彿=缃戠粶鍙访?00+鑺傜偣鍙枫€両P=OXE 涓荤敤鍦板潃銆丗TP 璐﹀彿 adfexc銆丳rocess configuration 鍕鹃€夈€佸憡璀︽帴鏀舵ā寮?Permanent IP connectivity銆佽璐规柟寮忋€佹垚鏈腑蹇冿級锛汼oftware download 椤碉紙mtcl 缁存姢璐﹀彿锛夛紱Connectivity 椤碉紙SSH/SFTP 鍕鹃€?+ MindTerm 涓绘満鍚嶏級銆侽XO Connect 鍙樹綋锛氳妭鐐瑰彿鐩存帴濉紙濡?80锛岀郴缁熸崲绠楁垚澹版槑鑺傜偣 180锛夈€丗TP password 涓?NMC 璐﹀彿锛圥bxkmc12 瀹為獙鍙ｅ緞 Pbxnmc12锛夈€乂oIP performance process銆丆onnectivity 椤靛～ Omc config password銆?  conditions: Network/Sub-network 鍙湪棣栦釜 PCX 澹版槑鏃堕渶瑕佸垱寤猴紱Network/Subnetwork 瀛楁鑷姩缁ф壙鍕挎墜濉?  tags: [structure, node-registration, configuration-tree]

- id: f08
  title: OXE 鑺傜偣娉ㄥ唽绔埌绔祦绋嬧€斺€斿墠缃牳鏌?鈫?澹版槑 鈫?鍚屾 鈫?瀹炴椂鏍搁獙 鈫?鎺掗殰
  type: flow
  source_pages: p118-128
  source_chapter: OXE node registration (How-To)
  source_quote: |
    "Use the siteid command to display network and node number. ... Node number: 1 ; Network
    number: 1 ;" (p119)
    "Right click on the OXE, Select 'Synchronization > Partial > Global' from the contextual
    menu ... Click 'Apply' to start the synchronization" (p125)
    "If the real-time synchronization doesn't work ... Restart NMC Alarm server service:
    Start -> OmniVista 8770 -> Tools -> Service Manager" (p128)
  summary: |
    浜旀娴佺▼锛氣憼鍓嶇疆锛歋SH 鍒?Call Server 鐢?siteid 鏍稿缃戠粶/鑺傜偣鍙凤紝netadmin -m 閫夐」 5锛圧ole addressing锛夋牳瀵逛富鐢?IP锛堢┖闂村啑浣欐椂璁颁袱涓級锛涒憽澹版槑锛氭寜 f07 涓夌骇鏍戝～鍙傛暟锛坅dfexc 鏁版嵁鎻愬彇璐﹀彿銆乵tcl 缁存姢璐﹀彿銆丼SH 鍚敤锛夛紱鈶㈠悓姝ワ細鍙抽敭 OXE 鈫?Synchronization > Partial > Global锛堟垨 Complete > Separate锛夛紝Scheduler 绐楀彛閫?of the task 鈫?Status 椤?鈫?Apply 鈫?Refresh 鐪嬫棩蹇楋紝鎴愬姛鍚?OXE 涓嬬敓鎴愬悇鍒嗘敮锛涒懀瀹炴椂鏍搁獙锛氬湪 OXE 寤虹敤鎴?31234锛孉larms 搴旂敤 Event 椤靛簲鏀跺埌浜嬩欢锛孋onfiguration 鏍?TelephonicDevices 鍑虹幇璇ョ敤鎴凤紱鈶ゆ帓闅滐細Service Manager 閲嶅惎 NMC Alarm server 鏈嶅姟鍚庨噸寤虹敤鎴烽獙璇併€傛棩蹇楋細鍚屾 NMCSyncLdapPbx_1.log銆佷簨浠?NMCFaultManager_1.log銆?  conditions: 闇€瑕?adfexc/mtcl 鍑嵁涓庣綉缁滃彲杈撅紱鍚屾鍦?Scheduler 绐楀彛鎵ц锛圤K=鍚庡彴鎵ц锛孉pply=鍓嶅彴鐪嬭繘搴︼級
  tags: [flow, oxe, node-registration, synchronization]

- id: f09
  title: OXE SSH 瀹夊叏閾捐矾鈥斺€攏etadmin 鍙俊涓绘満 + MindTerm 瀵嗛挜 + SFTP
  type: flow
  source_pages: p129-136
  source_chapter: OXE SSH (How-To)
  source_quote: |
    "netstat -an | grep :22 ... tcp 0 0 0.0.0.0:22 0.0.0.0:* LISTEN" (p130)
    "11. Security 鈫?1. Firewall (iptables) Configuration 鈫?3. Restricted Access Configuration
    鈫?1. View trusted hosts" (p131)
    "The public key is stored in the folder Users\Administrators\AppData\Roaming\MindTerm\hostkeys." (p134)
  summary: |
    娴佺▼锛氣憼鏍告煡锛歅uTTY SSH 鍒?Call Server锛宻u - 鍚?netadmin -m 閫夐」 2锛圫how current configuration锛夌‘璁?"Security with SSH: yes"锛沶etstat -an | grep :22/:23 楠岃瘉 22 鐩戝惉 23 鍏抽棴锛涢€夐」 11 Security 鈫?1 Firewall 鈫?3 Restricted access 鈫?1 View 鏌ョ湅鍙俊涓绘満娓呭崟锛涒憽8770 渚э細OXE Connectivity 椤靛嬀 SSH connection + 鍞竴涓绘満鍚嶏紙瀛楁瘝寮€澶达紝浠呭瓧姣嶆暟瀛椾笌 . , - _锛夛紱鈶娇鐢細Configuration 鏍戝彸閿?OXE 鈫?Connect锛宮tcl 鐧诲綍锛岄娆℃帴鍙?MindTerm 璁稿彲銆佺‘璁ゅ缓 home 鐩綍/hosts 鐩綍/鍏挜锛岃繛鎺ュ缓绔嬶紱鈶FTP锛歁indTerm Plugins > SFTP File Transfer锛涒懁鍔犲彲淇′富鏈猴細netadmin -m 鈫?11 鈫?1 鈫?3 鈫?2 Add trusted host锛堣緭鍚嶃€亂 鍔犲叆 hosts 搴撱€佽緭 IP锛夛紝鍥炰富鑿滃崟閫?22 Apply modifications锛? 閫€鍑恒€?  conditions: OXE N2 鍙婁互鍓嶉粯璁?telnet 寮€/SSH 鍏抽渶鎵嬪姩鍚敤锛汵3 璧?SSH 榛樿寮€涓斿彲淇′富鏈虹鐞嗗己鍒?  tags: [flow, ssh, security, oxe]

- id: f10
  title: OXO Connect 绾崇娴佺▼鈥斺€斿竷绾挎牳鏌?鈫?OMC 瀹夎杩炴帴 鈫?澹版槑 鈫?鍚屾 鈫?鍦ㄧ嚎/绂荤嚎
  type: flow
  source_pages: p640-667
  source_chapter: OXO Connect node declaration (How-To)
  source_quote: |
    "Use the scrawling bar and select Netw.config. Select IP@CPU. Check the IP address in the
    field called MAIN@. ... 151.1.1.246" (p643)
    "The declaration node managed by the 8770 server is (1x100) + 80 = 180. ... All OXO Connect
    backups managed by the 8770 server will be stored under the following folder:
    C:\8770_ARC\OXO\data\1\1\180" (p658)
    "Right click on OXO Connect, Select Configure > Online mode / Offline mode" (p663-665)
  summary: |
    浜旀娴佺▼锛氣憼甯冪嚎涓?IP 鏍告煡锛歅remium 璇濇満 Menu > Operator锛堝瘑鐮?Letacla1 瀹為獙鍙ｅ緞锛? Expert > Netw.config > IP@CPU 璇?MAIN@锛?51.1.1.246 瀹為獙鍙ｅ緞锛夛紱鈶MC 瀹夎锛氫粠 BP 缃戠珯涓嬭浇 zip 瑙ｅ帇浼犲埌 8770 鏈嶅姟鍣紝绠＄悊鍛樿繍琛?Setup.exe锛堥娆￠渶 .NET Framework锛夛紱鈶MC 杩炴帴锛欵xpert 浼氳瘽 鈫?Communication > Connect 鈫?LAN/WAN 鈫?杈?CPU IP 鈫?鏈嶅姟鍣ㄨ璇?鈫?瑁?OXO 璇佷功鍒?鍙椾俊浠荤殑鏍硅瘉涔﹂鍙戞満鏋?鈫?鏀规墍鏈夐粯璁ゅ瘑鐮侊紙OXO R10 璧峰己鍒讹級鈫?棣栬繛蹇呭～瀹㈡埛淇℃伅锛涒懀澹版槑锛欳onfiguration 搴旂敤鎸?f07 涓夌骇鏍戝缓 OmniPCX Office 鑺傜偣锛圥CX 椤碉細IP銆丗TP password=NMC 璐﹀彿銆佽璐?Detailed accounting銆佹垚鏈腑蹇冦€乂oIP performance锛汣onnectivity 椤碉細Omc config password=installer 瀵嗙爜锛夛紱Preferences > Configuration > OXO Preferences 閰?Secure Shared Directory锛堝～ 8770 鏈嶅姟鍣?Windows 浼氳瘽璐﹀彿 Administrator/superuser锛屼緵澶囦唤鐩綍 \\nms\OXO-databases 璁块棶锛夛紱鍙抽敭 OXO Connect 鈫?Synchronization 瀹屾暣鍚屾骞舵牳瀵圭増鏈彿锛涒懁杩愮淮浼氳瘽锛氬彸閿?鈫?Configure > Online mode锛堢洿杩?OMC Expert锛夋垨 Offline mode锛團ile > Open 鎵撳紑鏈湴鏁版嵁搴撳壇鏈級銆?  conditions: 鑺傜偣鍙?80 缁?(瀛愮綉鍙访?00)+80=180 鎹㈢畻涓哄０鏄庤妭鐐癸紝澶囦唤鐩綍闅忎箣钀藉湪 C:\8770_ARC\OXO\data\1\1\180锛涘叡浜洰褰曞弬鏁伴敊璇椂闇€閲嶅惎 8770 鏈嶅姟鍣?  tags: [flow, oxo-connect, omc, node-registration]

- id: f11
  title: OXE 鐢ㄦ埛寮€閫氫笁灞傛ā鍨嬧€斺€擠irectory 鏉＄洰 / Profile / Meta profile / Key profile
  type: structure
  source_pages: p170-181, p196-210
  source_chapter: USERS APPLICATION & META PROFILES锛堣涔夛級+ 涓や釜 How-To
  source_quote: |
    "USERS TAB 鈥?NONE (DIRECTORY USER) Entry in the DIRECTORY application ... USER has got one
    or several OXE devices OXE (CONNECTION USER)" (p171)
    "Meta profiles are represented by the symbol in the tree structure ... OXE free numbers
    range list + Meta profile name + Meta profile type = OXE + Node Id" (p199)
  summary: |
    Users 閫夐」鍗′袱绫荤敤鎴凤細User type=None锛堢函鐩綍鏉＄洰锛屾棤璁惧鏃犲簲鐢級涓?User type=OXE锛圕onnection 鐢ㄦ埛锛屽甫 OXE 璁惧锛夈€侾rofile 鏈哄埗锛歄XE 渚у缓 Set Function=Profile 鐨勭壒娈婄敤鎴凤紙General Characteristics 椤佃 Profile銆丷ights 椤佃涓変釜 COS銆丄ll 椤佃缁ф壙榛樿鍊硷級锛?770 Users 搴旂敤寤烘埛鏃堕€?profile 鍗崇户鎵垮弬鏁帮紱鍓嶆彁鏄湪 OXE System Parameters 鍕鹃€?"Use profile with auto. recognition"銆侹ey profile锛歴et profile 瀹氫箟 Progr. Keys + Set Profile > Profile Features 鍏宠仈閿姛鑳斤紝寤烘埛鏃堕€?Key Profiles 鑷姩閰嶉敭銆侻eta profile锛堟爲涓甫涓撶敤鍥炬爣锛夛細Meta profile 鍚?+ 鑺傜偣 + OXE 绌洪棽鍙风爜娈碉紙OXE 渚?Free Numbers Ranges List锛屽缓鍚庡繀椤诲悓姝ワ級+ 璁惧绫诲瀷 + OXE profile锛堝彲閫夛級锛屽缓鎴峰彧濉鍚嶅嵆鑷姩鍙栧彿锛堝彇娈靛唴绗竴涓┖闂插彿锛夊苟濉弧 OXE 灞炴€с€侾rofiles 閫夐」鍗℃壙鎷?profile/meta profile 鐨勬樉绀轰笌鍒涘缓鍏ュ彛銆?  conditions: Profile 鍚嶇О蹇呴』澶у啓锛沺rofile 鐢ㄦ埛榛樿涓嶅湪 Users 鏂囦欢澶规樉绀猴紝闇€ Filter "Set Function = Profile"
  tags: [structure, users, profiles, meta-profile]

- id: f12
  title: 鎵归噺寮€閫氭枃浠惰涔夆€斺€斿鍑哄洓娉曘€佸瓧娈靛崰浣嶄笌瀵煎叆鏍搁獙
  type: flow
  source_pages: p211-224, p246-252
  source_chapter: Mass provisioning from Users application锛堣涔?+ How-To锛? WBM 鎵归噺
  source_quote: |
    "Personal and mandatory attributes which can't be provided by the Profile or Metaprofile
    replaced by XXXX to invite the administrator to enter them; Attributes that can be
    automatically computed from Profile or Metaprofile set to NULL" (p216)
    "Action[+;-;#] Replace the # by the + character, to add a new user." (p259)
    "Mass provisioning file generated from thick client cannot be used in WebAdmin and
    vice-et-versa" (p250)
  summary: |
    Users 搴旂敤瀵煎嚭鍥涙硶锛氣憼鍏ㄥ弬瀵煎嚭锛堥€変腑鐢ㄦ埛鍏ㄥ弬鏁帮紝鐢ㄤ簬鏀瑰弬锛夛紱鈶＄┖妯℃澘锛堜粎琛ㄥご锛夛紱鈶㈠崟鐢ㄦ埛妯℃澘 Export user for template锛堥儴鍒嗚〃澶?浼樺寲閿€硷細XXXX=蹇呭～浜哄伐濉€丯ULL=绯荤粺鑷姩銆乤ction 榛樿 ADD锛夛紱鈶ainbow 鐢ㄦ埛鎵归噺锛圤XE 瀵煎嚭鈫掑缓 Rainbow 鐢ㄦ埛锛坋mail,濮撳悕锛夆啋鎸?email+鍙风爜鎸傝澶団啋Rainbow import锛夈€傛枃浠剁紪杈戝悗浠?Users 鏍戞牴鍙抽敭 Import user data锛團rom local drive锛屾枃浠剁被鍨嬮€?All Files锛夛紝Scheduler 鐨?Import user data 浠诲姟鐪嬬豢鎬佷笌 ADD 鎴愬姛銆俉BM 渚э細Export 鎸夐挳锛圱ype 閫?Users data 鎴?Template銆乀XT銆両mmediate锛夛紝鏂囦欢瀛楁 action[+;-;#]锛?=瀵煎嚭鍘熸牱銆?=鏂板銆?=鍒犻櫎锛夛紝import 鍚庣湅 Activity report銆傚鍏ユ牳楠屽弻閫氶亾锛歎sers 鏍戠‘璁ょ敤鎴?+ Scheduler/Activity report 纭浠诲姟鐘舵€併€?  conditions: thick client 涓?WBM 鐨勬壒閲忔枃浠朵簰涓嶉€氱敤锛沇BM 涓嶈兘绉婚櫎璁惧/涓嶈兘绉婚櫎 Connection 鐢ㄦ埛 OT 搴旂敤
  tags: [flow, mass-provisioning, import-export, wbm]

- id: f13
  title: Alarms 搴旂敤鏋舵瀯涓庡缃姸鎬佹満鈥斺€旈噰闆嗛摼 + 鍏骇鑹叉爣 + 鐩稿叧/闈炵浉鍏冲垎娴?  type: diagram
  source_pages: p269-282
  source_chapter: Alarms application锛堣涔夛級
  source_quote: |
    "PCX Collector 鈥?OXE OpenTouch OXO Connect ... Internal Collector ... Fault Manager ...
    Notify server ... Corba for alarms notification, SQL for alarms consultation & actions,
    Trap SNMP" (p272)
    "Critical Red / Major Orange / Minor Yellow / Warning Blue / Indeterminate Purple /
    Cleared White" (p274)
    "Correlated alarm: When the end of the problem can be detected by the PCX ... Uncorrelated
    alarm: Correction must be performed manually by the user" (p277)
  summary: |
    鏋舵瀯閾撅細OXE/OXO/OT 缁?CMISE 鍛婅浜嬩欢 鈫?8770 鍐呴儴 Collector 鈫?Fault Manager 鈫?MariaDB锛圫QL 鏌ヨ涓庢搷浣滐級+ Notify server锛圕orba 閫氱煡瀹㈡埛绔級+ SNMP Proxy锛坱rap 鍙?hypervisor锛? 閭欢/鑴氭湰鍑哄彛銆傚鎴风甯告樉鍛婅璁℃暟鍣紙妗嗚壊=褰撳墠鏈€楂樹弗閲嶇骇锛夈€傚缃姸鎬佹満锛氭椿鍔ㄥ憡璀﹀彲纭锛坅cknowledge锛屼粛娲诲姩銆佽褰曠‘璁や汉涓庡彉鑹诧級鈫?闈炵浉鍏冲憡璀﹀彲娓呴櫎锛坈lear锛岃浆涓嶆椿鍔ㄥ叆鍘嗗彶锛夆啋 鍙垹闄わ紙浠庡簱绉婚櫎锛夆啋 鍙鍚嶏紙 Signature/Action/Remark 涓夊瓧娈碉紝鍓嶄袱椤硅繘鎶ュ憡锛夛紱鐩稿叧鍛婅鐢?PCX 妫€娴嬮棶棰樼粨鏉熻嚜鍔ㄦ竻闄ゃ€備簨浠讹紙Event锛夋棤涓ラ噸绾э紝鍙瀵硅薄鍒涘缓/鍒犻櫎/淇敼銆?  conditions: 杩囨护鍣?Preferences > Alarms > Alarms Filters锛涘巻鍙?娲诲姩涓ょ鏄剧ず鍒囨崲
  tags: [diagram, alarms, architecture, severity]

- id: f14
  title: OXE 鍛婅鎺ュ叆娴佺▼鈥斺€攊ncident manager 鍙傛暟 + incident filter + rstcpl 楠岃瘉
  type: flow
  source_pages: p283-289
  source_chapter: Alarms application - OXE (How-To)
  source_quote: |
    "Network severity: None, Topological network: YES ... Browse to Applications > 1 >
    Incident Manager > 1" (p285)
    "Reset a coupler (rstcpl <Media Gateway number> <Board number>) ... The alarm linked to
    the coupler reset is the alarm #2042." (p285-286)
    "Incident Number 1125 ... Network incident Yes" (p288)
  summary: |
    娴佺▼锛氣憼8770 渚э細OXE 澹版槑 Alarm reception mode=Permanent IP connectivity锛坒07 宸插惈锛夛紱鈶XE 渚э細Configuration 鐣岄潰 Applications > 1 > Incident Manager > 1锛孨etwork severity=None锛堝叏閮ㄤ笂閫侊級+ Topological network=YES锛涒憿楠岃瘉锛歮tcl 浼氳瘽鎵ц rstcpl 4 0 閲嶅惎 coupler锛宨ncvisu -t 3 鏌ユ渶杩?3 鏉′簨浠讹紙#2042 Loss of a GD/GD3 type cpl锛夛紝Alarms 搴旂敤鏍戜腑瀵瑰簲鏉垮崱鍑虹幇 Major #2042锛涒懀瀹氬悜杩囨护锛氬鐗瑰畾浜嬩欢锛堝 mtcl 鐧诲綍 #1125锛夊缓 Incident Filter锛孨etwork incident=Yes 浣垮叾鏃犺 network severity 寮哄埗涓婇€侊紝鍐嶅紑 mtcl 浼氳瘽楠岃瘉 Minor #1125 涓婂睆锛涒懁鏃ュ織锛歂MCFaultManager_1.log 璁板綍 active/cleared 浜嬩欢銆?  conditions: 閮ㄥ垎鏁版嵁搴撲腑 #1125 涓嶅湪榛樿浜嬩欢琛紝闇€鍏堝彸閿?Create 浜嬩欢鍐嶈 Network incident
  tags: [flow, alarms, oxe, incident]

- id: f15
  title: SNMP Proxy 閮ㄧ讲閾锯€斺€擶indows SNMP 鏈嶅姟 鈫?ToolsOmniVista 鍚敤 鈫?hypervisor 澹版槑 鈫?PCX 婵€娲?鈫?杩囨护
  type: flow
  source_pages: p307-324
  source_chapter: Alarms application 鈥?SNMP proxy (How-To)
  source_quote: |
    "Windows SNMP service must be installed, even if you have to disable it to activate the
    one provided by the 8770 server." (p317)
    "Select 4 鈥?SNMP ... Select 1 鈥?SNMP Agent ... NMC SNMP service and agent is disabled.
    Would you like to enable it鈥? (y/n): y" (p315)
    "Data Collection tab, Managed by SNMP proxy Enabled" (p318)
  summary: |
    浜旀閾撅細鈶燬erver Manager 涓?8770 鏈嶅姟鍣ㄥ姞 Windows SNMP Service 鍔熻兘锛圢etsnmp 缁勪欢闅忚锛夛紱鈶oolsOmniVista.exe锛圕:\8770\bin锛夛細directory manager 瀵嗙爜 鈫?y 鍋滄湇鍔?鈫?閫?4 SNMP 鈫?1 SNMP Agent 鈫?y 鍚敤锛堣瀹岃嚜鍔ㄥ仠鐢?Windows SNMP 鏈嶅姟銆佸惎鐢?8770 鑷甫浠ｇ悊锛夛紝鏃ュ織 NMCSnmpAgent_1.log 鍑虹幇 "SNMP agent started"锛涒憿澹版槑 hypervisor锛欰dministration 搴旂敤鍙抽敭 nmc > Create > Hypervisor锛堝悕绉般€両P鈥斺€斾笉鐢?FQDN銆佸崗璁増鏈?V2/V3銆乼rap 绔彛 162锛沄3 鍙﹀～ SHA/MD5 璁よ瘉 + DES/AES128 鍔犲瘑锛夛紱瀹為獙鐢?Client PC 鐨?TrapReceiver 妯℃嫙 V2c hypervisor锛涒懀婵€娲?PBX 鐩戠潱锛欳onfiguration 搴旂敤 OXE Data Collection 椤靛嬀 Managed by SNMP proxy锛岃嚜鍔ㄥ彂 trap "Sending TRAP Add PABX"锛堟爣璇?缃戠粶/瀛愮綉/鑺傜偣 1/1/101锛夛紱鈶よ繃婊わ細Alarms 搴旂敤 Preferences > Alarms > SNMP Filter锛屾寜 Correlation锛圗qual True锛夋垨 Diagnostic锛堝彿鐮佸垪琛ㄥ垎鍙峰垎闅?鑼冨洿杩炲瓧绗︼級杞彂锛屽彲 AND/OR 鍙犲姞绗簩鏉′欢銆傚嵏杞藉弽鍚戞墽琛岋紙浠ｇ悊 disable + 绉婚櫎 Windows SNMP 鍔熻兘 + 閲嶅惎锛夈€?  conditions: V3 澹版槑娴佺▼涔︿腑鏍囨敞"浠呬緵淇℃伅銆佸嬁鎵ц"锛涘嵏杞芥祦绋嬪悓鏍蜂粎淇℃伅
  tags: [flow, snmp, proxy, hypervisor]

- id: f16
  title: Topology 鍙岃鍥句綋绯烩€斺€擲tandard 鑷姩瑙嗗浘 + Custom 缂栬緫鍣?+ 鍛婅閲嶅畾鍚?  type: structure
  source_pages: p325-362
  source_chapter: Topology application锛堣涔?+ 涓や釜 How-To锛?  source_quote: |
    "2 tabs (or views), Standard and Custom ... Structured according to tree structure of the
    Configuration application ... Creation of graphical objects, Links, Text fields, Shapes,
    Edit mode" (p331)
    "Such maps, in a gif format (for example) with the standard size of 1100x793, have to be
    stored on 8770\data\topology\maps." (p337)
    "Right click on the link, Select Redirecting alarms鈥?option ... paste the alarm on the
    field Source Object hierarchy" (p355-358)
  summary: |
    Standard 椤碉細鎸?Configuration 鏍戣嚜鍔ㄧ敓鎴愶紝鏀寔鑳屾櫙鍦板浘锛?gif/.jpeg/.ivl锛岃嚜瀹氫箟鍥?1100x793 鏀?8770\data\topology\maps 鍚庨噸鍚?NMC Service Manager锛夈€佽櫄鎷?ACT 鏄剧ず锛圕onfiguration 纭欢鏍戝彇娑?Virtual equipment 鍕鹃€夊悗閲嶅惎 Topology锛夈€丳references > Topology > Configure 涓夐€夐」锛圧ead saved configuration/Display VPN Links/Display OXE Links/Display 8770 server锛夈€侰ustom 椤碉細Edit mode 涓嬪缓鑷畾涔夎鍥撅紙Create custom view 缁戣绠″璞?鑳屾櫙锛夈€佺綉缁滃厓绱犮€侀摼鎺?鏂硅閾炬帴銆佹爣绛俱€佸杈瑰舰/鐭╁舰搴曡壊锛孌efault view 瀹氶粯璁よ瑙掞紱鍛婅閲嶅畾鍚戯細浠?Configuration 鐣岄潰澶嶅埗瀵硅薄锛堝 GD4 鏉垮崱銆乀0 涓户銆乀DM/IP 鐢ㄦ埛缁堢锛夋垨浠?Alarms 搴旂敤澶嶅埗鍛婅 鈫?Custom 瑙嗗浘鍙抽敭閾炬帴/鍏冪礌 鈫?Redirecting alarms 鈫?绮樿创鍒?Source Object hierarchy 鈫?rstcpl 瑙﹀彂楠岃瘉涓婂睆銆侭ubble/Highlight 涓ょ鍛婅鐩存帴鏍囨敞妯″紡銆?  conditions: Topology 鍙樉绀虹浉鍏冲憡璀︼紱OXE R11.2 璧?IP 璇濇満鐘舵€佸憡璀︼紙incident 386锛変笉鍐嶆槸鍙浉鍏冲憡璀︼紝涓嶈兘鐢ㄤ簬 Topology
  tags: [structure, topology, custom-view, alarm-redirect]

- id: f17
  title: Security 涓夊眰鏉冮檺妯″瀷鈥斺€?770 璐︽埛/缁?鈫?OXE Access Profile 鈫?OXE 渚ц闂帶鍒?  type: structure
  source_pages: p363-412
  source_chapter: Security application锛堣涔?+ How-To锛?  source_quote: |
    "An administrator account can belong to several groups. For each application, the highest
    access level found is used" (p398)
    "11 Access Profiles are available ... 0 YES Gives access to all objects ... 10 YES
    Specially designed for attendant management" (p399)
    "User Name Enter an administrator account, available on Security application, in
    uppercase. (ex: ADMINNMC)" (p408)
  summary: |
    绗竴灞?8770 璐︽埛锛歋ecurity 搴旂敤绠″瘑鐮佺瓥鐣ワ紙quality/闀垮害/鍘嗗彶/棣栫櫥鏀瑰瘑/澶辫触閿佸畾/鏃舵晥 B+C<A锛? Administrators/Groups锛堥瀹氫箟缁勬寜瑙掕壊鎺堟潈锛屾潈闄愮疮鍔犲彇鏈€楂橈級+ 鍗曠櫥褰曞紑鍏筹紙AdminNmc 涓?Normal Administrators 缁勮眮鍏嶏級锛涢瀹氫箟璐﹀彿 AdminNmc锛堝叏鏉冿級銆丄lcatel4059锛堣瘽鍔″彴锛夈€丮SAD8770Admin锛圡SAD 鍚屾锛夈€乀hirdparty8770Admin锛圓PI锛夈€傜浜屽眰 OXE Access Profile锛欳onfiguration 鐣岄潰 Preferences > Configuration > Access Profiles锛?1 涓?profile锛? 鍏ㄩ噺/1 expert/2 usual/3 鐢ㄦ埛绠＄悊/4-9 鑷畾涔?10 璇濆姟鍙帮級锛屾瘡绫诲璞″洓绾?Nothing/Read/Read-Write/All + 灞炴€х骇鏄鹃殣 + Actions 鎺堟潈锛汼ecurity 搴旂敤缁欒处鎴?缁勯厤 Configuration 璁块棶鏃堕€?Access Level锛圢o Access/Configure/All锛? OmniPCX 4400 Access Level锛坧rofile 鍙凤級锛涙敼瀹屽繀椤诲垹瀹㈡埛绔湰鍦?MIB锛圥references > Configuration > Object Model Save锛夐噸杞姐€傜涓夊眰 OXE 渚э細閰嶇疆鐣岄潰 Security and Access Control > User Access Control 寤哄ぇ鍐欒处鍙风櫧鍚嶅崟锛堝墠鎻愶細Connectivity 椤靛惎鐢?Secure access for system management锛夛紝閲嶇疆鐢?telnet锛歮ao off 鈫?multitool SECURITY_ACCESS 閫?10 鈫?mao on銆?  conditions: Access Profiles 鍏?OXE 閫氱敤锛屽缓璁湪鏈€鏂扮増鏈?OXE 涓婄紪杈戯紱profile 鐢ㄦ埛/閿?profile 妫€绱㈤渶鍚屾
  tags: [structure, security, access-profile, domains]

- id: f18
  title: Scheduler 浠诲姟妯″瀷鈥斺€擩ob/Task 鐘舵€佹満涓庝袱绉嶇粍瑁呮柟寮?  type: structure
  source_pages: p460-487
  source_chapter: Scheduler application锛堣涔?+ How-To锛?  source_quote: |
    "Job: Entity including one or more tasks performed simultaneously ... Job items: Idle job /
    Job waiting / Job running ... Task: Executable operation" (p463)
    "Create a new job with a single task Simple job / Include the task in an existing job
    Synchronized task" (p464)
    "When you add another Job, this one is called jobset. But it's only during its creation.
    Once the task has been built, if you refresh this one, you will see that jobset becomes Job." (p487)
  summary: |
    妯″瀷锛歍ask=鍙墽琛屾搷浣滐紙8770 鍐呴儴鎿嶄綔鎴栧閮ㄥ簲鐢級锛孞ob=鍚屾椂鎵ц鐨勪换鍔￠泦鍚堬紙鐘舵€?Idle/Waiting/Running锛夛紱棰勫畾涔?job锛圖aily Job/Weekly Job/8770 Data Backup/RTU Scheduled Reports锛夋壙鎷呮棩甯哥淮鎶ゃ€傜粍瑁呬袱娉曪細浠庢姤鍛?搴旂敤閲?Schedule鈥?鏃堕€?Simple job锛堝崟浠诲姟鐙珛 job锛夋垨 Synchronized task锛堟寕鍏ュ凡鏈?job 褰㈡垚搴忓垪锛夛紱Scheduler 鍐?New Job 鍚庝粠鍏朵粬 job 澶嶅埗/鍓垏浠诲姟绮樿创锛圕ut+Paste 鏀瑰彉浠诲姟褰掑睘瀹炵幇鍏堝悗椤哄簭锛屽"瀹¤鍚屾鈫掑璁℃姤鍛娾啋LDAP 閮ㄥ垎鍚屾"閾撅級銆傚弬鏁伴〉涓夌粍锛歋cheduling锛圖escription/Start Date=Now 鎴?As Scheduled/Maximum start delay/Repeat/Ending date/Exclude Days/Job Owner锛夈€丏ependant Job Options锛圖elay dependant job start/Stop on error 榛樿鍚敤锛夈€丷etry Options锛堥噸璇曟鏁?闂撮殧/鏈€澶ф墽琛屾椂闀匡級銆傛墽琛屾牳楠岋細Execute now + Reports 鍥炬爣鏌ュ悇浠诲姟鎴愬姛鎬併€?  conditions: Maximum start delay 璇箟鈥斺€斿仠鏈洪敊杩囪鍒掓椂闂磋秴杩囪寤惰繜鍒欎换鍔′笉鍐嶈ˉ璺?  tags: [structure, scheduler, job-task]

- id: f19
  title: 鑷姩缁存姢浣撶郴鈥斺€斾簲绫绘暟鎹竻闄ゅ弬鏁?+ Purge job 缁勮 + 棰勫畾涔?job 鎭㈠
  type: flow
  source_pages: p488-502
  source_chapter: Scheduler application - Automatic maintenance (How-To)
  source_quote: |
    "Configure the maintenance parameters to: Delete accounting records older than 15 days,
    Delete the hourly traffic Analysis older than 4 days" (p489)
    "Select 'Scheduler->Weekly Job->Job'. Right click on 'Purge Alarms', select 'Copy'." (p495)
    "it is possible to restore the default configuration by a LDIF import ... select
    DailyJob.ldif or WeeklyJob.ldif ... Restart NMC Scheduler service." (p502)
  summary: |
    浜旂被娓呴櫎鍏ュ彛锛氣憼璁¤垂/璇濆姟锛欰ccount./traf./VoIP 搴旂敤 Preferences > Accounting > Accounting preferences锛圕lean PTP hour old than=灏忔椂绾ц瘽鍔′繚鐣欏ぉ鏁般€丆lean ticketandaffiliated=璁¤垂璁板綍淇濈暀澶╂暟绛?20 浣欓」锛屽惈榛樿鍊艰〃锛夛紱鈶℃姤鍛婏細Reports 搴旂敤 Reports preferences锛圕lean taxa Reports 绛夛級锛涒憿鍛婅锛欰larms 搴旂敤 Purge configuration锛堟寜澶╂暟+鎸夋潯鏁板弻闂革紝瀹為獙淇濈暀 100 鍛婅/100 浜嬩欢锛夛紱鈶ｅ璁★細Audit purge锛堟棩蹇椾繚鐣欏ぉ鏁?瀵煎嚭鏂囦欢瀵垮懡锛夛紱鈶ゆ枃浠跺す锛欰dministration 搴旂敤 NmcArchive锛堟寜 Free disk space 鎴?Directory size 鍙岄槇鍊间骇鐢?minor/major 鍛婅+娓呯悊寤惰繜锛夈€侾urge job 缁勮锛歋cheduler 寤烘柊 job "Purge"锛屼粠 Weekly Job 渚濇澶嶅埗 Purge Alarms 鈫?鏂板瓙 job 绮?Clean PTP/Traff Hist 鈫?鍐嶅祵 Clean accounting锛孍nable 鍚敤锛屽舰鎴?鍛婅娓呴櫎鈫掕瘽鍔℃竻闄も啋璁¤垂娓呴櫎"涓茶閾俱€傝鍒?鏀瑰潖棰勫畾涔夌淮鎶?job 鐨勬仮澶嶏細Administration 搴旂敤 Import LDIF锛圽8770\data\scheduler 涓?DailyJob.ldif/WeeklyJob.ldif锛? 閲嶅惎 NMC Scheduler 鏈嶅姟銆?  conditions: 鍚勪繚鐣欐湡榛樿鍊艰 principle 鏉＄洰锛涙竻闄ょ敱 Daily/Weekly Job 鎸?鍒犻櫎鏉′欢鍦ㄥ簲鐢ㄤ腑閰嶇疆"鎵ц
  tags: [flow, purge, maintenance, scheduler]

- id: f20
  title: 8770 澶囦唤鎭㈠涓?rehosting 娴佺▼鈥斺€斿浠藉洓鍧楀唴瀹?+ 鐗堟湰缁戝畾 + 鎹㈡満鏀瑰潃
  type: flow
  source_pages: p503-521
  source_chapter: 8770 Maintenance application锛堣涔?+ How-To锛?  source_quote: |
    "LDAP data (System configuration and directories databases) / MariaDB database (Accounting,
    VoIP, Traffic, alarms, audit data and reports) / Others data (Customized dictionaries,
    scheduled task, loader data, license file) / RestoreContext.ini file" (p507)
    "A backup is dedicated to a version. It cannot be restored on a server running another
    version." (p510)
    "Comparison of RestoreContext.ini files (current and the one from the backup) will exclude
    the hostname svNMCName and domain svDomain entries." (p512)
  summary: |
    澶囦唤鍐呭鍥涘潡锛歀DAP 鏁版嵁銆丮ariaDB 鏁版嵁銆佸叾浠栵紙瀛楀吀/璁″垝浠诲姟/loader 鏁版嵁/璁稿彲鏂囦欢锛夈€丷estoreContext.ini锛涘浠芥湡闂?8770 涓嶅彲鐢紝榛樿宸叉湁璁″垝澶囦唤锛圵eekly Job 鐨?8770 Data Backup锛夈€傛仮澶嶆祦绋嬶細缁存姢璁剧疆锛圥references > Maintenance > Configuration 瀹氬浠戒綅缃?鍙岄槇鍊煎憡璀?淇濈暀瀵垮懡锛夆啋 Databases - Immediate backup锛堥粯璁ょ洰褰?C:\8770_ARC\8770Backup锛岀洰褰曞悕 YYYYMMDDHHMMSS锛夆啋 Restore - databases锛堝厛鍒犺妭鐐广€佸垹鍛婅锛涙寜 RestoreContext.ini 鐨?nmcVersion 瑁呭悓鐗堟湰鍐嶆仮澶嶏級銆俽ehosting 涓夊満鏅細鏀?IP=澶囦唤鈫掓敼 IP鈫扲estore databases with rehosting锛堣剼鏈洿鏂伴厤缃級锛涙敼 FQDN 鍚屾満=鍗歌浇鈫掓敼 FQDN鈫掑悓鍙傛暟閲嶈锛堝瘑鐮?鐩綍鏍?璺緞涓嶅彉锛夛紱鎹㈡満锛堝惈 FQDN锛?鏂版満鍚屽弬鏁板畨瑁呪啋rehosting 鎭㈠锛圧estoreContext 姣斿鎺掗櫎 svNMCName/svDomain锛夈€?  conditions: 鎭㈠鍓嶅繀椤诲垹闄?Configuration 涓妭鐐逛笌鍏ㄩ儴鍛婅锛涚綉缁滅洏澶囦唤闇€ f28 鐨勭綉缁滈┍鍔ㄥ櫒鏄犲皠
  tags: [flow, backup, restore, rehosting]

- id: f21
  title: NMC 鏈嶅姟浣撶郴鈥斺€擶indows 鏈嶅姟灞?+ Service Manager 鐩戠潱灞?+ 鏃ュ織婊氬姩
  type: structure
  source_pages: p539-567
  source_chapter: NMC services锛堣涔夛級+ NMC services and log files (How-To)
  source_quote: |
    "First, all Windows services linked to 8770 application start in automatic mode (MySQL8770,
    LDAP Console, Oracle Directory Server Enterprise Edition, NMC Service Manager) ... Then,
    NMC Service Manager service launches all 8770 internal services (Apache ... Wildfly)" (p541-542)
    "For 8770 applications, total size of log file is 10 Mo max (2x5Mo)" (p548)
    "https://nms.company.com/nmclog/ 鈥?/nmclog/ is a web alias pointing to log files" (p553)
  summary: |
    涓ゅ眰鏈嶅姟锛歐indows 鏈嶅姟锛圓utomatic 鍚姩锛? 涓€斺€擬ySQL8770銆丩DAP Console锛圖SEE 鎺у埗涓績锛夈€丱racle Directory Server EE锛圠DAP 鐩綍锛夈€丯MC Service Manager锛汵MC 鍐呴儴鏈嶅姟锛圡anual锛岃 Service Manager 鎸変緷璧栭『搴忔媺璧峰苟鐩戠潱锛夌害 20 涓€斺€擜pache銆丯MC Alarm/Audit/CMISE/Communication Server/Executable Launcher/Extractor/GCS Administrator/GCS Config/Java Service Definition/License Server/Loader/Manage My Phone/PBX-LDAP synchronization/Save-Restore/Scheduler/Security Server/SNMP Service銆丱RBacus Notify銆乄ildfly銆備緷璧栬鍒欙細鏈嶅姟鍋滃垯渚濊禆鑰呰繛閿佸仠锛岃捣鍒欒繛閿佽捣锛涜鐩戠潱鏈嶅姟宕╂簝鑷姩閲嶅惎锛堜笉瑕佹墜鍔?Start锛夛紱鍥涗釜 Automatic 鏈嶅姟闇€鎵嬪姩 Start銆係ervice Manager 宸ュ叿锛歋elect+Execute 鍙栨潈鍚庡惎鍋溿€傛棩蹇楋細<瀹夎鐩綍>\log锛圢MC 鏈嶅姟 _1.log/_2.log 鍙屾枃浠舵粴鍔?2脳5MB锛夈€丄pache2\logs銆丼unONE\slapd-8770\logs锛坅ccess/errors锛夛紱璇︾粏璺熻釜缁?Administration 搴旂敤鏈嶅姟鍙傛暟 Argument list 鏀?-TraceType --1锛屾煡瀹屾敼鍥?-TraceType 0锛沇eb 鏌ョ湅 https://<FQDN>/nmclog/锛堢鐞嗗憳鍑嵁锛夈€?  conditions: 璇︾粏璺熻釜妯″紡浼氭嫋鎱㈡湇鍔″櫒锛涢厤缃瓨 Administration 搴旂敤 NMC/OmniVista 8770 > Services
  tags: [structure, nmc-services, logging]

- id: f22
  title: OXE 澶囦唤鎭㈠鏈哄埗鈥斺€攂ck 鍛戒护 + FTP/SFTP 鍙栧洖 + swinst 鎭㈠浜旀
  type: flow
  source_pages: p568-593
  source_chapter: OMNIPCX ENTERPRISE BACKUP锛堣涔夛級+ backup & restore (How-To)
  source_quote: |
    "The 8770 server establishes a Telnet or SSH connection to the OXE for running the backup
    command. Backup files are created in the folder /usr4/BACKUP/IMMED and /usr4/BACKUP/OPS" (p572)
    "Backup files transferred from 8770 server to the OXE ... Manual restoration via swinst tool" (p570)
    "You must stop the telephone application of OXE to be able to restore a database. But by
    stopping such process, you disable the role address facility." (p589)
  summary: |
    澶囦唤閾惧洓姝ワ細鈶燤aintenance 搴旂敤 Preferences > Maintenance > OXE Configuration 瀹氬浠戒綅缃紙榛樿 c:\8770_ARC\OXEBackup锛? Enable PCX automatic backup锛涒憽Configuration 搴旂敤 OXE锛欴ata Collection 椤靛嬀 Automatic database save銆丼oftware download 椤靛～ mtcl銆丆onnectivity 椤靛～ swinst 瀵嗙爜锛涒憿绔嬪嵆澶囦唤锛歁aintenance 鍙屽嚮 PCX 鈥?Backup 鈫?閫夋暟鎹被鍨嬶紙mao/璇煶瀵煎紩/OPS锛夆啋 鐩綍纭 鈫?Simple job 鈫?Start Date=Now锛涜鍒掑浠藉悓璺緞閫?As scheduled + Repeat Daily锛涒懀鏈哄埗锛?770 Telnet/SSH锛坢tcl锛夎繍琛?bck 鍛戒护锛坰winst 瀵嗙爜鎺堟潈锛夆啋 OXE 鐢熸垚 /usr4/BACKUP/IMMED 涓?/usr4/BACKUP/OPS 鏂囦欢 鈫?8770 缁?FTP/SFTP锛坅dfexc锛夊彇鍥?bck_save.log 涓庡浠芥枃浠?鈫?瀛?c:\8770_ARC\OXEBackup\<缃戠粶>\<瀛愮綉>\<鑺傜偣>\<YYYYMMDDhhmmss>銆傛仮澶嶉摼锛歅CX 鈥?Restore 浼?MAO 澶囦唤鍥?OXE /usr4/BACKUP/IMMED 鈫?swinst 浼氳瘽锛欵asy 鑿滃崟 7 鍋滅數璇?鈫?Expert 4 Backup&restore 鈫?3 Restore operations 鈫?1 from cpu disk 鈫?1 IMMEDIATE 鈫?2 Restore mao data锛堜笉鍔犲瘑 securing 濉?n锛夆啋 Expert 6 System management 鈫?2 Autostart management 鈫?1 Set autostart 鈫?Easy 鑿滃崟 8 Start the telephone 鈫?鏍稿鍒犻櫎鐢ㄦ埛宸茶繕鍘熴€?  conditions: OXE N2 鍙婁互鍓?mtcl/adfexc/swinst 榛樿瀵嗙爜 mtcl/adfexc/SoftInst锛汵3 璧峰繀椤诲凡鑷畾涔夛紱鍋滅數璇濆悗 role address 澶辨晥鐢ㄧ墿鐞?IP 杩炴帴
  tags: [flow, oxe-backup, swinst, restore]

- id: f23
  title: 8770 璁稿彲浣撶郴鈥斺€擜CTIS 鍑鸿瘉 鈫?鍥涢亾閿?鈫?License Server 鏍搁獙 鈫?鍙楅檺妯″紡
  type: structure
  source_pages: p594-617
  source_chapter: 8770 LICENSE锛堣涔夛級+ How-To
  source_quote: |
    "1 - The Actis application generates the 8770 license file (.sw8770 extension) ... 4 - The
    service 'NMC License Server' is responsible for controlling the license file integrity" (p597)
    "[Modules] Application locks. A key value > 0 means the application is enabled.
    ... 8770Clients key is the maximum number of simultaneous clients (up to 30)" (p603)
    "When some license thresholds are exceeded, client runs in restricted mode: Only Directory
    and Configuration are accessible" (p606)
  summary: |
    璁稿彲閾句簲鐜細ACTIS 鐢熸垚 <offer id>.sw8770 鈫?瀹夎鏃舵彁渚?鈫?瀛?8770\etc 鏀瑰悕 nmc.license 鈫?NMC License Server 鏍￠獙瀹屾暣鎬?鈫?8770 瀹㈡埛绔寜閿佹樉绀哄簲鐢ㄣ€傛枃浠剁粨鏋勶細[8770]锛堢増鏈?绛惧悕锛夈€乕ALIZE]锛圤XO 閰嶇疆鎺堟潈锛夈€乕OXE AND ICE]锛圤XE 閰嶇疆鎺堟潈 + 8770Handle 鐢虫姤鑺傜偣锛夈€乕Modules]锛堝簲鐢ㄩ攣锛氬竷灏旈敭 Topology/AccountingMonitoring/Audit/Security/ExternalDirectorySynchro锛涚敤鎴锋暟閿?Configuration/Alarms/Accounting/Directory/Performance 绛夛紱8770Clients 骞跺彂瀹㈡埛绔笂闄?30锛汼ecurity 閿?0-5 缁勫悎娴佸畨鍏ㄤ笌 PKI锛夈€傝鍙帶鍒跺弻娉曪細#1 鐢虫姤鑺傜偣锛坰padmin 鍛戒护鏄剧ず OXE OPS 涓殑 Handle 姣斿锛夛紱#2 缁戝畾鏈嶅姟鍣ㄧ壒寰侊紙MAC/IP/ProductID/UUID锛屾敮鎸佸啑浣欏弻鏈哄瓧娈碉級銆傚寘鍨嬶細Start Pack PPU锛圓larms/璁￠噺璺熻釜/缁熶竴绠＄悊 + 鍐呭惈 Configuration 涓?Audit锛夆啋 Full Pack PPU锛堝姞 Performance/Company Directory锛夛紱鐙珛閫夐」 AD Integration銆丮MP銆丄PI Provisioning銆乀opology銆丼NMP Proxy銆乀icket Collector銆丼ecurity銆丮ulti Domain銆傝秴闄愯涓猴細閫艰繎涓婇檺浜х敓鍛婅锛岃秴闄愯繘鍙楅檺妯″紡锛堜粎 Directory+Configuration锛屾湇鍔″櫒涓嶅仠闃叉暟鎹涪澶憋級銆傛洿鏂版祦绋嬶細Service Manager 鍋?NMC Service Manager 鈫?nmc.license 鏀瑰悕 .old 鈫?鏀惧叆鏂版枃浠舵敼鍚?nmc.license 鈫?鍚姩鏈嶅姟 鈫?Help > About 鏍搁獙锛涙棩蹇?NMCLicServer_1.log 鎵撳嵃鍚勬ā鍧楃敤閲忕櫨鍒嗘瘮銆?  conditions: 鍙敮鎸?N-1 璁稿彲鐗堟湰锛圧5.2 鎺ュ彈 15 鎴?16锛夛紱PKI 鐗规€т粠 R5.0 璧蜂笉鍐嶅彲鐢?  tags: [structure, license, locks, actis]

- id: f24
  title: 缃戠粶椹卞姩鍣ㄦ槧灏勬祦绋嬧€斺€旇繙绋嬪叡浜?+ ADM8770 鍚屽悕璐﹀彿 + 鏈嶅姟璐﹀彿娉ㄥ叆
  type: flow
  source_pages: p668-698
  source_chapter: Map network drive (How-To)
  source_quote: |
    "Creation of the REPORTS_ECO et BACKUP_ECO folders on the ecosystem server ... Creation of
    a user account named ADM8770 with access rights on folders previously created" (p669)
    "ExecEx service is linked to report generation facility. SaveRestore service is linked to
    backup & restore facility." (p669)
    "Username Enter account in uppercase preceded with the following characters .\ (i.e.
    .\ADM8770)" (p696)
  summary: |
    鍙屼晶娴佺▼锛氳繙绋嬫湇鍔″櫒渚р€斺€擲erver Manager 寤?AD 璐﹀彿 ADM8770锛堝瘑鐮佷笉寰楁敼銆佷笉杩囨湡锛夛紝寤?C:\REPORTS_ECO 涓?C:\BACKUP_ECO 涓ゆ枃浠跺す锛屽叡浜潈闄愯祴 ADM8770 璇诲啓锛圓dvanced Sharing 闄愬苟鍙戞暟銆佺Щ闄?Everyone锛夈€?770 鏈嶅姟鍣ㄤ晶鈥斺€斿缓鏈湴 ADM8770锛堝叆 Administrators 缁勩€佺Щ鍑?Users 缁勶級銆丩ocal Security Policy 璧?5 椤圭敤鎴锋潈鍒╋紙浠庣綉缁滆闂璁＄畻鏈?浣滀负鏈嶅姟鐧诲綍/浣滀负鎿嶄綔绯荤粺涓€閮ㄥ垎/璋冩暣杩涚▼鍐呭瓨閰嶉/鏇挎崲杩涚▼绾т护鐗岋級锛涙敞閿€ Administrator 浠?ADM8770 鐧诲綍鍚庢槧灏勭綉缁滈┍鍔ㄥ櫒锛圷: \\151.1.1.100\REPORTS_ECO銆乑: \\151.1.1.100\BACKUP_ECO 瀹為獙鍙ｅ緞锛夛紱鏈€鍚?Administration 搴旂敤 Service 鐩綍缁?ExecdEx锛堟姤琛ㄥ鍑猴級涓?SaveRestore锛堝浠芥仮澶嶏級涓ゆ湇鍔￠厤 Nt account锛?\ADM8770 + 瀵嗙爜锛夈€傞獙鏀讹細8770 Maintenance 绔嬪嵆澶囦唤鏃?Search 涓兘鐪嬪埌 BACKUP_ECO/REPORTS_ECO 缃戠粶浣嶇疆銆?  conditions: ADM8770 璐﹀彿瀵嗙爜绛栫暐锛堜笉鍙敼/涓嶈繃鏈燂級涓哄疄楠屽彛寰勶紱涓ゆ湇鍔″櫒璐﹀彿闇€鍚屽悕鍚屽瘑
  tags: [flow, network-drive, services, backup]

- id: f25
  title: 8770 WBM 瀹㈡埛绔叆鍙ｄ笌鍥涘簲鐢ㄥ垎鍖?  type: structure
  source_pages: p151-157, p225-260
  source_chapter: 8770 WBM client 鈥?Configuration & Users application & provisioning
  source_quote: |
    "8770 WBM client: https://nms.company.com:8443 Select the following menu: NETWORK
    MANAGEMENT" (p254)
    "Several web sessions (one per OXE node) available but only one visible at a time" (p157)
    "Users display limit ... number of users displayed per page" (p233)
  summary: |
    鍏ュ彛 https://<FQDN>:8443 涓昏彍鍗曞垎 NETWORK ADMINISTRATION / NETWORK MANAGEMENT 绛夊尯銆傚洓搴旂敤锛氣憼Users锛圢etwork Management 涓嬶級锛氶潰鍖呭睉 + 鍏徃鐩綍鏍?+ 鐢ㄦ埛鎼滅储鏍?+ 缃戞牸鍒嗛〉锛圫ettings 閰嶆瘡椤垫樉绀烘暟/鎼滅储闄愭暟锛? Notification 鑿滃崟锛圗rror/Warning/Success 鍒嗙被娲诲姩鎶ュ憡锛? Help 蹇嵎閿〃锛涘缓鎴峰悜瀵兼寜閫夐」鍗℃笎杩涳紙User 鈫?Main device 鈫?鏈€澶?4 涓?Devices 椤电锛圓LES-Desktop/ALES-Mobile 璁″叆涓婇檺锛夆啋 OpenTouch 鏉冮檺鏃跺姞 Application 鈫?OTC Smartphone/OTC PC 绉诲姩涓庡濯掍綋椤电锛夛紱鈶onfiguration锛氭爲+闈㈠寘灞戝鑸€佸揩鎼?楂樼骇鎼滅储銆乼oaster 涓庨€氱煡鍒楄〃鎶ラ敊銆佷竴娆¤繛涓€涓?OXE銆佸 Web 浼氳瘽鍒囨崲锛涒憿Performance锛歸idget 浠〃鐩樹笌闃堝€艰窡韪紱鈶anage My Phone锛氱粓绔嚜鍔╋紙璇﹁ p261-268锛夈€?  conditions: WBM Users 闇€ Unified Management 璁稿彲锛沇BM Configuration 瀵规湰鍦扮鐞嗗憳鏃犻厤缃潈闄愩€佹棤 SSH/Telnet 鐩磋繛
  tags: [structure, wbm, web-client]
```

## 浠诲姟瑕嗙洊鑷锛坱ask 鈫?id 鏄犲皠锛?
| task_id | 瀵瑰簲 framework 鏉＄洰 |
|---|---|
| task-01/02 | f05 |
| task-03 | f06 |
| task-04 | f07銆乫08 |
| task-05 | f09 |
| task-06 | 锛堟搷浣滄墜娉曠被锛屼富浣撳湪 case锛涚粨鏋勪晶鐢?f07 閰嶇疆鏍戣鐩栵級 |
| task-07/08/09 | f11銆乫12 |
| task-10 | f12銆乫25 |
| task-11 | f07銆乫10 |
| task-12 | f14 |
| task-13 | f13 |
| task-14 | f15 |
| task-15/16 | f16 |
| task-17 | f17 |
| task-18 | 锛堟祦绋嬪湪 case c18锛涙灦鏋勭敱 f13/f17 渚у啓锛?|
| task-19 | 锛堟祦绋嬪湪 case c19锛涙姤鍛婂ぇ灏忛檺鍒惰 principle锛?|
| task-20 | f18 |
| task-21 | f19 |
| task-22 | f20 |
| task-23 | 锛堟祦绋嬪湪 case c23锛?|
| task-24 | f21 |
| task-25 | f22 |
| task-26 | f23 |
| task-27 | f24 |
| task-28 | f03銆乫04銆乫23 |
