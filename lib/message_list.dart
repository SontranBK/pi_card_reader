import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:cross_connectivity/cross_connectivity.dart';


var DialogShowing = 0; //v10_7
bool startDialogShowing = false;//v10_7

/// Listens for incoming foreground messages and displays them in a list.
class MessageList extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => _MessageList();
}

class _MessageList extends State<MessageList> {
  //RemoteMessage mymess = RemoteMessage();
  RemoteNotification Noti = RemoteNotification();
  //List<RemoteMessage> mymess = [];
  double heightR = 0.0; //v26
  double widthR = 0.0;
  double curR = 0.0;
  String internet_connection_status = '';

  void _showStartDialog() {
    showDialog(
        context: context,
        builder: (context) {
           startDialogShowing = true; //v10_7
          //Future.delayed(Duration(seconds: 10), () {
          //  Navigator.of(context).pop(true);
          //});
          return AlertDialog(
            title: Text(
              'Vui lòng chờ thêm giây lát',
              style: TextStyle(
                  color: Colors.blue,
                  fontSize: 30,
                  fontWeight: FontWeight.bold),
            ),
            content: Text(
                '- Phiên bản của sản phẩm: v1.0.3\n- Hãy quẹt thẻ khi thông báo BẮT ĐẦU ĐỌC THẺ NFC hiện lên\n- Thiết bị sẽ tự khởi động lại nếu khởi động thất bại\n- Nếu thiết bị báo lỗi, vui lòng kiểm tra phần bị báo lỗi (đầu đọc, kết nối mạng, ...)'),
          );
        });
  }

  @override
  Widget build(BuildContext context) {
    heightR = MediaQuery.of(context).size.height / 1080; //v26
    widthR = MediaQuery.of(context).size.width / 1920; //v26
    curR = widthR; //v26
    return Container(
        child: ConnectivityBuilder(
      builder: (context, isConnected, status) => errmsg('$status'),
    )

        //to show internet connection message on isoffline = true.
        );
  }

  Widget errmsg(String show) {
    internet_connection_status = show;
    //error message widget.
    if (show == 'ConnectivityStatus.none') {
      //if error is true then show error message box
      return Container(
        height: 365 * heightR, //v26
        width: 700 * widthR, //v26
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.centerLeft,
            end: Alignment.centerRight,
            stops: [
              0.5,
              0.33,
              0.68,
              0.99,
            ],
            colors: [
              Colors.white.withOpacity(1.0),
              Colors.white.withOpacity(1.0),
              Colors.white.withOpacity(1.0),
              Colors.white.withOpacity(1.0),
            ],
          ),
          borderRadius: BorderRadius.circular(40 * curR), //v26
        ),
        child: Row(
          children: <Widget>[
            Column(
              mainAxisAlignment: MainAxisAlignment.start,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Expanded(
                  child: Container(
                    padding: EdgeInsets.only(
                        left: 75 * widthR, top: 50 * heightR), //v26
                    child: Row(children: [
                      Icon(
                        Icons.signal_wifi_off,
                        color: Colors.red[500],
                        size: 40 * curR,
                      ),
                      Text('    '),
                      Text(
                        'Phát hiện mất kết nối mạng',
                        style: TextStyle(
                            color: Colors.black,
                            fontSize: 38 * curR,
                            fontWeight: FontWeight.bold),
                      )
                    ]),
                  ),
                ),
                Expanded(
                  child: Container(
                    padding:
                        EdgeInsets.only(left: 105 * widthR, top: 20 * heightR),
                    child: Text(
                      '"Vui lòng kiểm tra kết nối wifi hoặc dây mạng"\n'
                      '"Không thực hiện quẹt thẻ \ncho đến khi có mạng trở lại"\n'
                      '"Thiết bị sẽ hoạt động bình thường \nsau 10 giây khi có mạng trở lại"',
                      style: TextStyle(
                          color: Colors.black,
                          fontSize: 25 * curR,
                          fontWeight: FontWeight.bold,
                          height: 1.5),
                    ),
                  ),
                ),
                Expanded(
                    child: Container(
                        padding: EdgeInsets.only(
                            left: 325 * widthR, top: 50 * heightR), //v26
                        alignment: Alignment.center,
                        child: CircularProgressIndicator(
                          backgroundColor: Colors.grey,
                          color: Colors.purple,
                          strokeWidth: 5 * curR,
                        ))),
              ],
            )
          ],
        ),
      );
    } else {
      return Container();
    }
  }

  @override
  void initState() {
    super.initState();

    Future(_showStartDialog);

    FirebaseMessaging.onMessage.listen((RemoteMessage message) {
      Noti = message.notification ?? RemoteNotification();
      String? titleOfNoti = Noti.title ?? '';
      String? bodyOfNoti = Noti.body ?? '';

      print(bodyOfNoti);
      if (titleOfNoti == 'Start: Start using NFC reader') {
        if (startDialogShowing == true) { //v10_7
           Navigator.of(context).pop(true);//v10_7
           startDialogShowing = false;//v10_7
         } //v10_7
        showDialog(
            context: context,
            builder: (context) {
              Future.delayed(Duration(seconds: 5), () {
                Navigator.of(context).pop(true);
              });
              return AlertDialog(
                title: Text(
                  bodyOfNoti,
                  style: TextStyle(
                      color: Colors.blue,
                      fontSize: 25,
                      fontWeight: FontWeight.bold),
                ),
                content: Text(
                    'BẮT ĐẦU ĐỌC THẺ NFC\nToàn bộ quá trình khởi động đã hoàn tất\nVui lòng quẹt thẻ sau khi thông báo này ẩn đi'),
              );
            });
      }

      if (titleOfNoti == 'Error: Reader not connected') {
        showDialog(
            context: context,
            builder: (context) {
              Future.delayed(Duration(seconds: 5), () {
                Navigator.of(context).pop(true);
              });
              return AlertDialog(
                title: Text(
                  bodyOfNoti,
                  style: TextStyle(
                      color: Colors.blue,
                      fontSize: 30,
                      fontWeight: FontWeight.bold),
                ),
                content: Text(
                    'Lỗi: Không thể kết nối với đầu đọc, vui lòng làm theo các bước sau:\n1) Kiểm tra lại giắc cắm đầu đọc\n2) Kiểm tra nguồn điện của đầu đọc\n\nThiết bị sẽ tự khởi động lại sau 10 giây'),
              );
            });
      }

      if (titleOfNoti == 'Error: Student Info Not Found') {
        showDialog(
            context: context,
            builder: (context) {
              Future.delayed(Duration(seconds: 5), () {
                Navigator.of(context).pop(true);
              });
              return AlertDialog(
                title: Text(
                  bodyOfNoti,
                  style: TextStyle(
                      color: Colors.blue,
                      fontSize: 30,
                      fontWeight: FontWeight.bold),
                ),
                content: Text(
                    'LỖI: Dữ liệu học sinh không hợp lệ, vui lòng kiểm tra lại'),
              );
            });
      }

      if (titleOfNoti == 'Error: Wrong data format') {
        showDialog(
            context: context,
            builder: (context) {
              Future.delayed(Duration(seconds: 5), () {
                Navigator.of(context).pop(true);
              });
              return AlertDialog(
                title: Text(
                  bodyOfNoti,
                  style: TextStyle(
                      color: Colors.blue,
                      fontSize: 30,
                      fontWeight: FontWeight.bold),
                ),
                content: Text(
                    'LỖI: Dữ liệu trong thẻ sai định dạng, vui lòng kiểm tra lại'),
              );
            });
      }

      if (titleOfNoti == 'Hexa not valid') {
        showDialog(
            context: context,
            builder: (context) {
              Future.delayed(Duration(seconds: 5), () {
                Navigator.of(context).pop(true);
              });
              return AlertDialog(
                title: Text(
                  bodyOfNoti,
                  style: TextStyle(
                      color: Colors.blue,
                      fontSize: 30,
                      fontWeight: FontWeight.bold),
                ),
                content: Text(
                    'LỖI: Dữ liệu hexa không hợp lệ, vui lòng kiểm tra lại'),
              );
            });
      }

      if ((titleOfNoti == 'Error: Lost connection to OCD server') &&
          (internet_connection_status != 'ConnectivityStatus.none')) {
        showDialog(
            context: context,
            builder: (context) {
              Future.delayed(Duration(seconds: 5), () {
                Navigator.of(context).pop(true);
              });
              return AlertDialog(
                title: Text(
                  bodyOfNoti,
                  style: TextStyle(
                      color: Colors.blue,
                      fontSize: 30,
                      fontWeight: FontWeight.bold),
                ),
                content: Text(
                    'LỖI: Không thể kết nối với server, vui lòng:\n1) Kiểm tra lại đường truyền mạng\n2) Liên hệ với kĩ thuật viên'),
              );
            });
      }

      if (titleOfNoti == "NFC_card_info") {
        if (startDialogShowing == true || DialogShowing >=1) { //v10_7
          Navigator.of(context).pop(true); //v10_7
          startDialogShowing = false; //v10_7
        } //v10_7
        Map<String, dynamic> student_info = jsonDecode(bodyOfNoti);

        print('Name, ${student_info['data']['name']}');
        print('ID, ${student_info["data"]["studentId"]}');
        print('School, ${student_info["data"]["school"]["name"]}');
        print('Class, ${student_info["data"]["clazz"]["name"]}');

        showGeneralDialog(
          context: context,
          barrierLabel: "Barrier",
          barrierDismissible: false,
          barrierColor: Colors.black.withOpacity(0.1),
          transitionDuration: Duration(milliseconds: 500),
          pageBuilder: (_, __, ___) {
            DialogShowing++; //v20_6
            Future.delayed(Duration(seconds: 5), () { //v10_7
              if (DialogShowing == 1) {
                Future.delayed(Duration(seconds: 5), () {
                  if (DialogShowing == 1) {
                    Navigator.of(context).pop(true);
                  }
                  DialogShowing--;
                });
              }
              else DialogShowing--;
            });
            return Container(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Container(
                    padding: EdgeInsets.only(left: 1000*widthR,top: 300*heightR),
                    // color: Colors.black,
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.start,
                      crossAxisAlignment: CrossAxisAlignment.end,
                      children: [
                        Container(
                          child: Container(                       
                            // color: Colors.red,
                            child: Text(
                              "XIN CHÀO",
                              style: TextStyle(
                                decoration: TextDecoration.none,
                                fontSize: 100 * curR, //v26
                                color: Colors.blue[900],
                                fontFamily: 'Dosis',
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                          ),
                        ),    
                      ],
                    ),
                  ),
                  Container(
                    margin: EdgeInsets.only(left: 875*widthR,top: 10*heightR),
                    height: 265 * heightR, //v26
                    width: 700 * widthR, //v26
                    decoration: BoxDecoration(
                      gradient: LinearGradient(
                        begin: Alignment.centerLeft,
                        end: Alignment.centerRight,
                        stops: [
                          0.0,
                          0.33,
                          0.68,
                          0.99,
                        ],
                        colors: [
                          Colors.greenAccent.withOpacity(0.6),
                          Colors.greenAccent.withOpacity(0.25),
                          Colors.greenAccent.withOpacity(0.25),
                          Colors.greenAccent.withOpacity(0.6),
                        ],
                      ),
                      borderRadius: BorderRadius.circular(10 * curR), //v26
                    ),
                    child: SizedBox.expand(
                      child: Row(
                        children: [
                          Container(
                            margin: EdgeInsets.only(
                                left: 15 * widthR, right: 45 * heightR), //v26
                            width: 140 * widthR,
                            height: 140 * heightR, //v26
                            decoration: BoxDecoration(
                                color: Colors.white,
                                shape: BoxShape.circle,
                                border: Border.all(
                                  color: Colors.greenAccent,
                                  width: 2 * curR,
                                )),
                            child: Image.asset(
                              'Meta_edu.png',
                              scale: 5 / curR,
                            ),
                          ),
                          Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(
                                student_info['data']['name'],
                                style: TextStyle(
                                  decoration: TextDecoration.none,
                                  fontSize: 50 * curR,
                                  color: Colors.red[600],
                                  fontFamily: 'Dosis',
                                  fontWeight: FontWeight.bold,
                                  height: 1.8,
                                ),
                              ),
                              Text(
                                'ID: '+student_info["data"]["studentId"],
                                style: TextStyle(
                                  decoration: TextDecoration.none,
                                  fontSize: 35 * curR,
                                  color: Colors.red,
                                  fontFamily: 'Dosis',
                                  fontWeight: FontWeight.w400,
                                  height: 1.4,
                                ),
                              ),
                              Text(
                                'Lớp: '+student_info["data"]["clazz"]["name"],
                                style: TextStyle(
                                  decoration: TextDecoration.none,
                                  fontSize: 35 * curR,
                                  color: Colors.red,
                                  fontFamily: 'Dosis',
                                  fontWeight: FontWeight.w400,
                                  height: 1.4,
                                ),
                              )
                            ],
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            );
          },
          transitionBuilder: (_, anim, __, child) {
            Tween<Offset> tween;
            if (anim.status == AnimationStatus.reverse) {
              tween = Tween(begin: Offset(1, 0), end: Offset.zero); //v26
            } else {
              tween = Tween(begin: Offset(1, 0), end: Offset.zero); //v26
            }

            return SlideTransition(
              position: tween.animate(anim),
              child: FadeTransition(
                opacity: anim,
                child: child,
              ),
            );
          },
        );
      } //NFC info
    });
  }
}