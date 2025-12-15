# HAM Radio Ecosystem
# 业余无线电 信息源索引

---
## 1. Identity & Callsign (身份与呼号体系)

- [QRZ](https://www.qrz.com)
 
- [RadioID（DMR ID）](https://radioid.net)

- [LoTW（Logbook of The World）](https://lotw.arrl.org/)   
  ARRL 的官方通联确认系统

---
## 2. Networks & Infrastructure（网络与中继体系）

### 2.1 Digital Voice Networks（数字语音网络）

- [BrandMeister（DMR）](https://brandmeister.network/)  
  全球规模最大的 DMR 数字语音网络之一，提供 Talkgroup、跨区域中继与服务器基础设施。

- [TGIF（DMR）](https://tgif.network/)  
  以社区为导向的 DMR 网络，结构相对简化，常用于实验和兴趣型通联。

- [D-STAR](https://www.dstar.org/)  
  Icom 主导的数字语音与数据系统，支持呼号路由和全球反射器网络。

- [YSF / Wires-X（Yaesu System Fusion）](https://systemfusion.yaesu.com/)  
  Yaesu 的 C4FM 数字语音体系，Wires-X 用于实现节点与房间的网络互联。

### 2.2 Voice Linking Networks（语音互联网络）

- [EchoLink](https://www.echolink.org/)  
  通过互联网连接无线电台、中继和客户端的软件系统，支持 PC 与移动设备接入。

- [IRLP（Internet Radio Linking Project）](https://www.irlp.net/)  
  以专用节点为核心的语音互联系统，强调稳定性与实时性。

- [AllStarLink](https://www.allstarlink.org/)  
  基于 Asterisk 的业余无线电语音互联平台，常用于自建节点与中继控制。

- [HamVoIP](https://hamvoip.org/)  
  面向 AllStar 的系统发行版，提供集成化的语音互联与节点管理环境。

### 2.3 Bridging & Infrastructure（桥接与基础设施）

- [DVSwitch](https://dvswitch.groups.io/g/main/wiki)  
  用于桥接多种数字语音协议的工具链，常见于网关与实验性部署。

- [MMDVM（Multi-Mode Digital Voice Modem）](https://github.com/g4klx/MMDVM)  
  多协议数字语音调制解调体系，是 DMR、D-STAR、YSF 等热点与中继的基础组件。
 
---
## 3. Protocols & Services（通信协议与服务）

### 3.1 Digital Voice Protocols（数字语音协议）

- DMR（Digital Mobile Radio）  
  数字语音与数据通信标准，广泛用于业余无线电数字语音网络与中继系统。

- [D-STAR（Digital Smart Technologies for Amateur Radio）](https://www.dstar.org/)  
  面向业余无线电的数字语音与数据协议，支持呼号路由与反射器机制。

- YSF（Yaesu System Fusion / C4FM）  
  Yaesu 提供的数字语音协议体系，常与 Wires-X 网络配合使用。

### 3.2 Weak Signal & Digital Modes（弱信号与数字模式）

- [FT8](https://wsjt.sourceforge.io/)  
  面向极弱信号环境的数字通信模式，当前最活跃的业余无线电数字通联方式之一。

- [WSPR（Weak Signal Propagation Reporter）](https://www.wsprnet.org/)  
  用于探测无线电传播条件的弱信号信标协议与全球报告网络。

- [PSK31](https://www.psk31.com/)  
  经典键盘数字通信模式，适合低功率与窄带条件下使用。

### 3.3 Packet & Messaging Services（分组与消息服务）

- [APRS（Automatic Packet Reporting System）](https://aprs.fi/)  
  用于位置、状态、短消息传输的分组通信系统，基于 AX.25 协议体系。

- [AX.25 Packet Radio](https://www.tapr.org/ax25.html)  
  业余无线电分组通信协议，早期数据通信与 APRS 的基础。

- [Winlink](https://winlink.org/)  
  通过无线电实现电子邮件通信的全球系统，常用于应急与远距离通信。

### 3.4 Positioning & Locator Systems（定位与网格系统）

- [Maidenhead Locator System](https://ham.c5r.app/maidenhead-grid)  
  业余无线电常用的地理网格定位系统，用于通联、竞赛与传播分析。

 
---
## 4. Software & Tools（软件与工具）

### 4.1 Client & Control Software（客户端与控制软件）

- [DroidStar](https://github.com/nostar/DroidStar)  
  跨平台数字语音客户端，可直接接入 DMR、D-STAR、YSF 等网络，无需实体电台。
  - DroidStar Vocoder Servers（语音编解码服务器）
    - `http://pizzanbeer.net/`
    - `http://dudestar.gw8szl.co.uk/Droidstar/`

- [EchoLink](https://www.echolink.org/)  
  通过互联网接入业余无线电语音网络的客户端与节点软件，支持 PC 与移动端。

### 4.2 Hotspot & Node Systems（热点与节点系统）

- [Pi-Star](https://www.pistar.uk/)  
  常用的数字语音热点系统发行版，支持 DMR、D-STAR、YSF 等多种模式。

- [Pi-Star Forum](https://forum.pistar.uk/)  
  Pi-Star 相关配置、故障排查与社区讨论论坛。

- [HamVoIP](https://hamvoip.org/)  
  面向 AllStarLink 的系统发行版，用于构建语音互联节点与中继控制系统。

### 4.3 Digital Mode Software（数字模式软件）

- [WSJT-X](https://wsjt.sourceforge.io/)  
  用于 FT8、WSPR 等弱信号数字通信模式的软件工具。

- [Fldigi](https://www.w1hkj.com/)  
  多模式数字通信软件，支持 PSK、RTTY、Olivia 等多种数字模式。

### 4.4 Radio Programming & Configuration（电台写频与配置）

- [CHIRP](https://chirpmyradio.com/)  
  常见的业余无线电写频与配置软件，支持多品牌电台。

### 4.5 Logging & QSO Management（通联日志与管理）

- [Logbook of The World (LoTW)](https://lotw.arrl.org/)  
  ARRL 提供的官方通联确认系统，用于电子 QSL 与通联验证。

- [Cloudlog](https://www.magicbug.co.uk/cloudlog/)  
  基于 Web 的通联日志系统，支持自建与多设备访问。

### 4.6 Utility & Reference Tools（工具与参考）

- [HAM 小工具（网格定位、缩写解释等）](https://ham.c5r.app)  
  面向业余无线电的辅助工具集合，提供定位、术语与速查功能。

---
## 5. Exams & Licensing（考试与执照）

### 5.1 China（中国）

- 中国工业和信息化部（MIIT）  
  业余无线电管理主管部门  
  https://www.miit.gov.cn/

- 中国无线电协会（CRAC）  
  业余无线电台执照与考试组织  
  https://www.crac.org.cn/

- 题库：[A新](https://exam.ham.upall.cn/?t=a_2025) [B新](https://exam.ham.upall.cn/?t=b_2025) [B模](https://ham-exam.iots.vip) [C新](https://exam.ham.upall.cn/?t=c_2025) 

### 5.2 United States（美国）

- FCC Amateur Radio Service  
  美国业余无线电官方管理机构  
  https://www.fcc.gov/wireless/bureau-divisions/mobility-division/amateur-radio-service

- ARRL Licensing & Exams  
  美国业余无线电考试与执照体系说明  
  https://www.arrl.org/licensing-education-training

- 题库：[T](https://exam.ham.upall.cn/?t=t) [G](https://exam.ham.upall.cn/?t=g) [E](https://exam.ham.upall.cn/?t=e)

### 5.3 Japan（日本）

- JARL（Japan Amateur Radio League）  
  日本业余无线电考试与执照信息入口  
  https://www.jarl.org/English/

- MIC（Ministry of Internal Affairs and Communications）  
  日本无线电与频谱监管机构  
  https://www.soumu.go.jp/english/

### 5.4 United Kingdom（英国）

- Ofcom Amateur Radio  
  英国无线电监管机构（执照发放）  
  https://www.ofcom.org.uk/spectrum/radio-equipment/amateur-radio

- RSGB（Radio Society of Great Britain）  
  英国业余无线电考试与培训体系  
  https://rsgb.org/main/clubs-training/training/

### 5.5 Germany（德国）

- Bundesnetzagentur（BNetzA）  
  德国无线电与频谱监管机构  
  https://www.bundesnetzagentur.de/

- DARC（Deutscher Amateur-Radio-Club）  
  德国业余无线电协会与考试支持  
  https://www.darc.de/

### 5.6 European Union（欧盟，通用参考）

- CEPT / ECC  
  欧洲业余无线电执照互认框架  
  https://www.cept.org/

- CEPT Amateur Radio (T/R 61-01, 61-02)  
  欧洲跨国通联与执照互认规则  
  https://www.cept.org/ecc/topics/amateur-radio


---
## 6. Satellites & Space（卫星与空间通信）

### 6.1 Orbital Data & Tracking（轨道数据与跟踪）

- [Celestrak](https://celestrak.org/NORAD/elements/supplemental/)  
  提供 NORAD TLE（两行根数）数据的权威来源，常用于卫星轨道计算与预测。

- [AMSAT Satellite Status](https://www.amsat.org/status/)  
  业余无线电卫星状态汇总页面，标注当前可用卫星与运行情况。

### 6.2 Satellite Tracking Software & Apps（卫星跟踪软件与应用）

- [GoSatWatch](https://gosoftworks.com/apps/gosatwatch/users-guide/)  
  面向业余卫星通信的跟踪与通联辅助软件，支持多平台。

- [ISS Detector](https://issdetector.com/)  
  用于提醒国际空间站及其他卫星过境时间的移动端应用。

### 6.3 Amateur Satellite Organizations（业余卫星组织）

- [AMSAT](https://www.amsat.org/)  
  国际业余无线电卫星组织，负责业余卫星的设计、发射支持与运营协调。

- [AMSAT-DL](https://amsat-dl.org/)  
  德国业余卫星组织，在业余卫星工程与技术研发方面影响力较大。

### 6.4 Open & Community Satellite Networks（开放与社区卫星网络）

- [SatNOGS](https://satnogs.org/)  
  开源的全球卫星地面站网络，用于接收、记录与共享卫星信号数据。

 
---
## 7. Communities（社区组织）

### 7.1 International & National Organizations（国际 / 国家级组织）

- [AMSAT（Radio Amateur Satellite Corporation）](https://www.amsat.org/)  

- [JARL（Japan Amateur Radio League）](https://www.jarl.org/English/)  

- [ARRL（American Radio Relay League）](https://www.arrl.org/)  
  美国业余无线电协会

- [RSGB（Radio Society of Great Britain）](https://rsgb.org/)  
  英国业余无线电协会


### 7.2 Projects & Technical Communities（项目 / 技术社区）

- [DMR-MARC（Digital Mobile Radio – Motorola Amateur Radio Club）](https://www.dmr-marc.net/)  
  DMR 业余无线电组织

- [SatNOGS（Satellite Networked Open Ground Station）](https://satnogs.org/)  
  开源卫星地面站网络

- [WSJT-X（Weak Signal Communication Software）](https://wsjt.sourceforge.io/)  
  弱信号通信软件项目

- [FreeDV（Free Digital Voice）](https://freedv.org/)  
  开源数字语音项目


### 7.3 General Communities（综合社区）

- [OARC（Online Amateur Radio Community）](https://www.oarc.uk/)

- [HRCC（Ham Radio Crash Course）](https://hamradiocrashcourse.com/)

- [eHam（eHam.net）](https://www.eham.net/)   
  业余无线电社区论坛

- Lids（Lids Amateur Radio Community） Discord


