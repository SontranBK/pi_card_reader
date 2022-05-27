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
  double heightR = 0.0; //v26
  double widthR = 0.0;
  double curR = 0.0;
  
  void _showStartDialog(){
	showDialog(
            context: context,
            builder: (context) {
              Future.delayed(Duration(seconds: 10), () {
                Navigator.of(context).pop(true);
              });
              return AlertDialog(
                title: Text('Vui lòng chờ thêm giây lát',
                  style: TextStyle(color: Colors.blue,
                      fontSize: 30,
                      fontWeight: FontWeight.bold),
                ),
                content: Text('- Product version: v0.0.3\n- Sau khi thông báo này ẩn đi, đợi khoảng 30 giây,\nnếu không thấy thông báo "Bắt đầu đọc thẻ NFC",\nvui lòng làm theo các bước sau:\n1) Kiểm tra lại nguồn điện thiết bị, nguồn điện đầu đọc\n2) Kiểm tra giắc cắm đầu đọc\n3) Kiểm tra kết nối mạng\n4) Cuối cùng, khởi động lại thiết bị'),
              );
            }
        );
   }
  @override
  Widget build(BuildContext context) {
    heightR = MediaQuery.of(context).size.height/1080;//v26
    widthR = MediaQuery.of(context).size.width/1920;//v26
    curR = widthR;//v26
    return Text('');
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
            return Container(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  Container(
                    padding: EdgeInsets.only(top: 180*heightR, right: 177*heightR), //v26
                    child: Text(
                      'Xin chào!',
                      style: TextStyle(
                        decoration: TextDecoration.none,
                        fontSize: 190*curR, //v26
                        color: Colors.white,
                        fontFamily: 'Dosis', fontWeight: FontWeight.w400,
                      ),
                    ),
                  ),
                  Container(
                    height: 250*heightR, //v26
                    width: 745*widthR, //v26
                    margin: EdgeInsets.only(right: 100*widthR), //v26
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
                          Colors.lightBlue.withOpacity(0.05),
                          Colors.lightBlue.withOpacity(0.05),
                          Colors.lightBlue.withOpacity(0.6),
                        ],
                      ),
                      borderRadius: BorderRadius.circular(30*curR), //v26
                    ),
                    child: SizedBox.expand(
                      child: Row(
                        children: [
                          Column(
                            mainAxisAlignment: MainAxisAlignment.center,
                            children: [
                              Container(
                                margin: EdgeInsets.only(left: 25*widthR, right: 25*heightR),//v26
                                width: 140*widthR, height: 140*heightR,//v26
                                decoration: BoxDecoration(
                                    color: Colors.white60,
                                    shape: BoxShape.circle,
                                    border: Border.all(
                                      color: Colors.white,
                                      width: 2,
                                    )
                                ),
                                child: Image.asset('logo.png', scale: 4/curR,), //v26
                              )
                            ],
                          ),
                          Column(
                            mainAxisAlignment: MainAxisAlignment.start,
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: <Widget>[
                              Container(
                                padding: EdgeInsets.only(top: 30*heightR, bottom: 20*heightR), //v26
                                child: Text(
                                  Info[0],
                                  style: TextStyle(
                                    decoration: TextDecoration.none,
                                    fontSize: 50*curR, //v26
                                    color: Colors.white,
                                    fontFamily: 'Dosis', fontWeight: FontWeight.w500,
                                  ),
                                ),
                              ),
                              Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text(
                                    'ID: '+Info[1],
                                    style: TextStyle(
                                      decoration: TextDecoration.none,
                                      fontSize: 35*curR, //v26
                                      color: Colors.white,
                                      fontFamily: 'Dosis', fontWeight: FontWeight.w400,
                                      height: 1.2,
                                    ),
                                  ),
                                  Text(
                                    'Lớp: '+Info[2],
                                    style: TextStyle(
                                      decoration: TextDecoration.none,
                                      fontSize: 35*curR, //v26
                                      color: Colors.white,
                                      fontFamily: 'Dosis', fontWeight: FontWeight.w400,
                                      height: 1.2,
                                    ),
                                  ),
                                ],
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
      }
    });
  }


}
