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

  @override
  void initState() {
    super.initState();
    FirebaseMessaging.onMessage.listen((RemoteMessage message) {
      Noti = message.notification ?? RemoteNotification();
      String? titleOfNoti = Noti.title ?? '';
      String? bodyOfNoti = Noti.body ?? '';


      print(bodyOfNoti);
      if (titleOfNoti == 'Start') {
        showDialog(
            context: context,
            builder: (context) {
              Future.delayed(Duration(seconds: 5), () {
                Navigator.of(context).pop(true);
              });
              return AlertDialog(
                title: Text('Bắt đầu đọc thẻ',
                  style: TextStyle(color: Colors.blue,
                      fontSize: 30,
                      fontWeight: FontWeight.bold),
                ),
                content: Text('Quá trình khởi động hoàn tất\nBắt đầu đọc thẻ NFC'),
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

        showDialog(
            context: context,
            builder: (context) {
              Future.delayed(Duration(seconds: 3), () {
                Navigator.of(context).pop(true);
              });
              return AlertDialog(
                title: Text('Thông tin quẹt thẻ',
                  style: TextStyle(color: Colors.blue,
                      fontSize: 30,
                      fontWeight: FontWeight.bold),
                ),
                content: Text('- Tên học sinh:  ' + Info[0] + '\n'
                    '- Id học sinh:  ' + Info[1] + '\n'
                    '- Lớp:  ' + Info[2] + '\n'
                    '- Trường:  ' + Info[3] + '\n'
                    '- Ngày giờ quẹt thẻ:  ' + Info[4] + '\n'
                    '- Mã thẻ:  ' + Info[5]),
              );
            }
        );
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Text('');
  }

}
