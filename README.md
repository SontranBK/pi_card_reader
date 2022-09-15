# ***A customized IoT devices with NFC readers supported***: reader_pi_display

## 1. Getting Started

This project is a feature-customized IoT device, built on Pi-familly devices (Orange Pi, Raspberry Pi, Banana Pi), with NFC readers supported. It aimes to use for organization check-in-out, e-identification, ...

This product has been commercialized, not under research process. 

Now our device supports following readers:
- Duali DE-950
- AB Circle CIR315A and CIR315B

## 2. Updates and releases!!!

* 【May 17, 2022】 version 0.0.3 (Pre-release)
* 【Jun 03, 2022】 version 1.0.0
* 【Jun 07, 2022】 version 1.0.1
* 【Jun 27, 2022】 version 1.0.2
* 【Sep 15, 2022】 version 1.0.3

***For more detail about features in each version, please check out [product releases](https://github.com/SontranBK/pi_card_reader/releases)***

## 3. Reproduce process

- For reproducing a new "reader_pi_display" device on a Raspberry Pi 4 2GB RAM, refer to [Setup folder](Tools_And_Docs/Setup_Software)
- For offline update (version 1.0.3 or newest one) on a published device, refer to [Update code folder](Tools_And_Docs/Update_Source_Code)


## 4. Developing documents and tools

- For Duali DE-950 and AB Circle CIR315A, CIR315B development guides and drivers, refer to [AB Circle driver](Tools_And_Docs/AB_Driver), [AB Circle docs](Tools_And_Docs/ABCircle_ScriptTool), [Duali DE-950 docs](Tools_And_Docs/DualCard) and [Protocol](Tools_And_Docs/Protocol_Dev_Guide)
- For all test files, refer to [Test files folder](TestFiles_Ignored)

## 5. Techincal developing details:

This product is developed based on these tech:
- Front-end software: written in pure Dart, Flutter framework. Front-end pubished on Web app with Firebase included. If Firebase supports desktop, front-end can be built on any-OS desktop. Refer to [Front end Web app](lib)
- Back-end software: written in Python (with NFC reader module, client-server API, lite database supported, auto-boot feature, internet condition checking, ...). Refer to [Back end](Python_Backend)
- Firmware-OS-related: written in Bash script (mainly for auto-boot frontend, backend features). Refer to [Firmware-OS](Bash_Script)

## 6. Authors and credits:

In research and development process, all credits go to ***Son Tran BK and CTARG LAB members***, in EEE, HUST (Hanoi University of Science and Technology), Ha Noi, Viet Nam

