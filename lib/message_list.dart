// ignore_for_file: require_trailing_commas

import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:flutter/material.dart';

   
   
/// Listens for incoming foreground messages and displays them in a list.
class MessageList extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => _MessageList();
}

class _MessageList extends State<MessageList> {
  //RemoteMessage mymess = RemoteMessage();
  RemoteNotification Noti = RemoteNotification();
  //List<RemoteMessage> mymess = [];
  
  void _showStartDialog(){
	showDialog(
            context: context,
            builder: (context) {
              Future.delayed(Duration(seconds: 30), () {
                Navigator.of(context).pop(true);
              });
              return AlertDialog(
                title: Text('Vui lòng chờ thêm giây lát',
                  style: TextStyle(color: Colors.blue,
                      fontSize: 30,
                      fontWeight: FontWeight.bold),
                ),
                content: Text('- Product version: v0.0.3\n- Sau khi thông báo này ẩn đi, đợi khoảng 10 giây,\nnếu không thấy thông báo "Bắt đầu đọc thẻ NFC",\nvui lòng làm theo các bước sau:\n1) Kiểm tra lại nguồn điện thiết bị, nguồn điện đầu đọc\n2) Kiểm tra giắc cắm đầu đọc\n3) Kiểm tra kết nối mạng\n4) Cuối cùng, khởi động lại thiết bị'),
              );
            }
        );
   }
   
  @override
  void initState() {
    super.initState();
    var _ID = " ";
    var _class = " ";
    var _textSt = TextStyle(
    decoration: TextDecoration.none,
    fontSize: 30,
    color: Colors.white70,
    fontFamily: 'Dosis', fontWeight: FontWeight.w400,
    );
    
    Future(_showStartDialog);
   
        
    FirebaseMessaging.onMessage.listen((RemoteMessage message) {
      Noti = message.notification ?? RemoteNotification();
      String? titleOfNoti = Noti.title ?? '';
      String? bodyOfNoti = Noti.body ?? '';
        
      print(bodyOfNoti);
      if (titleOfNoti == 'Start: Start using NFC reader') {
        showDialog(
            context: context,
            builder: (context) {
              Future.delayed(Duration(seconds: 10), () {
                Navigator.of(context).pop(true);
              });
              return AlertDialog(
                title: Text(bodyOfNoti,
                  style: TextStyle(color: Colors.blue,
                      fontSize: 25,
                      fontWeight: FontWeight.bold),
                ),
                content: Text('BẮT ĐẦU ĐỌC THẺ NFC\nToàn bộ quá trình khởi động đã hoàn tất\nVui lòng quẹt thẻ sau khi thông báo này ẩn đi'),
              );
            }
        );
      }
      
      if (titleOfNoti == 'Error: Reader not connected') {
        showDialog(
            context: context,
            builder: (context) {
              Future.delayed(Duration(seconds: 10), () {
                Navigator.of(context).pop(true);
              });
              return AlertDialog(
                title: Text(bodyOfNoti,
                  style: TextStyle(color: Colors.blue,
                      fontSize: 30,
                      fontWeight: FontWeight.bold),
                ),
                content: Text('Lỗi: Không thể kết nối với đầu đọc, vui lòng làm theo các bước sau:\n1) Kiểm tra lại giắc cắm đầu đọc\n2) Kiểm tra nguồn điện của đầu đọc\n3) Cuối cùng, khởi động lại thiết bị'),
              );
            }
        );
      }
      
      
      if (titleOfNoti == 'Error: Lost connection to OCD server') {
        showDialog(
            context: context,
            builder: (context) {
              Future.delayed(Duration(seconds: 10), () {
                Navigator.of(context).pop(true);
              });
              return AlertDialog(
                title: Text(bodyOfNoti,
                  style: TextStyle(color: Colors.blue,
                      fontSize: 30,
                      fontWeight: FontWeight.bold),
                ),
                content: Text('LỖI: Không thể kết nối với server, vui lòng:\n1) Kiểm tra lại đường truyền mạng\n2) Liên hệ với kĩ thuật viên'),
              );
            }
        );
      }

      if (titleOfNoti == "NFC_card_info") {
        List Info = [];

        int idx = bodyOfNoti.indexOf("|");
        print('idx: $idx');
        Info.add(bodyOfNoti.substring(0, idx).trim());
        print('Info: $Info');
        String Rest = bodyOfNoti.substring(idx + 1);
        print('Rest of string: $Rest');
        print('Info: $Info');

        while (idx != 22) {
          idx = Rest.indexOf("|");
          print('idx: $idx');
          Info.add(Rest.substring(1, idx).trim());
          print('Info: $Info');
          Rest = Rest.substring(idx + 1);
          print('Rest of string: $Rest');
        }
        Info.add(Rest);
        print('Info: $Info');

        showGeneralDialog(
          context: context,
          barrierLabel: "Barrier",
          barrierDismissible: true,
          barrierColor: Colors.black.withOpacity(0.1),
          transitionDuration: Duration(milliseconds: 500),
          pageBuilder: (_, __, ___) {
            Future.delayed(Duration(seconds: 5), () {
              Navigator.of(context).pop(true);
            });
            return Center(
              child: Container(
                padding: EdgeInsets.only (top:0),
                height: 180,
                width: 550,
                margin: EdgeInsets.only(top: 50, left: 750),
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
                        Colors.lightBlue.withOpacity(0.6),
                        Colors.lightBlue.withOpacity(0.0),
                        Colors.lightBlue.withOpacity(0.0),
                        Colors.lightBlue.withOpacity(0.6),
                      ],
                    ),
                    borderRadius: BorderRadius.circular(40),
                ),
                child: SizedBox.expand(
                  child: Row(
                    children: [
                      Column(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Container(
                            margin: EdgeInsets.only(left: 30, right: 30),
                            width: 100, height: 100,
                            decoration: BoxDecoration(
                              color: Colors.white70,
                              shape: BoxShape.circle,
                              border: Border.all(
                                color: Colors.white,
                                width: 2,
                              )
                            ),
                            child: Image.asset('THCS_CG.png', scale: 6,),
                          )
                        ],
                      ),
                      Column(
                        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: <Widget>[
                          Text(
                            Info[0],
                            style: TextStyle(
                              decoration: TextDecoration.none,
                              fontSize: 28,
                              color: Colors.white,
                              fontFamily: 'Dosis', fontWeight: FontWeight.w600,
                            ),
                          ),
                          Text(
                            'ID: '+Info[1],
                            style: _textSt,
                          ),
                          Text(
                            'Lớp: '+Info[2],
                            style: _textSt,
                          ),
                        ],
                      ),
                    ],
                  ),
                ),
              ),
            );
          },
          transitionBuilder: (_, anim, __, child) {
            Tween<Offset> tween;
            if (anim.status == AnimationStatus.reverse) {
              tween = Tween(begin: Offset(-1, 0), end: Offset.zero);
            } else {
              tween = Tween(begin: Offset(1, 0), end: Offset.zero);
            }

            return SlideTransition(
              position: tween.animate(anim),
              child: FadeTransition(
                opacity: anim,
                child: child,
              ),
            );
          },
        );//show dialog
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Text('');
  }

}

