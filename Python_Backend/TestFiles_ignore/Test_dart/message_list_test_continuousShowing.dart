import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:cross_connectivity/cross_connectivity.dart';

   

bool DialogShowing = false; //v20_6
   
/// Listens for incoming foreground messages and displays them in a list.
class MessageList extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => _MessageList();
}

class _MessageList extends State<MessageList> {
  //RemoteMessage mymess = RemoteMessage();
  RemoteNotification Noti = RemoteNotification();
  //List<RemoteMessage> mymess = [];
  bool DialogShowing = false; //v20_6
  double heightR = 0.0; //v26
  double widthR = 0.0;
  double curR = 0.0;
  String internet_connection_status = '';
  
  async function doStuff(DialogShowing) {
  if (DialogShowing == true) {
      await Navigator.pop(context,true);
      DialogShowing = false;
      print("TRUEEEEEEEEEEEE: ${DialogShowing}!!!!!!!!!!!");
    }
  }


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
                content: Text('- Product version: v1.0.2\n- Sau khi thông báo này ẩn đi, đợi khoảng 30 giây,\nnếu không thấy thông báo "Bắt đầu đọc thẻ NFC",\nvui lòng làm theo các bước sau:\n1) Kiểm tra lại nguồn điện thiết bị, nguồn điện đầu đọc\n2) Kiểm tra giắc cắm đầu đọc\n3) Kiểm tra kết nối mạng\n4) Cuối cùng, khởi động lại thiết bị'),
              );
            }
        );
   }
  @override
  Widget build(BuildContext context) {
    heightR = MediaQuery.of(context).size.height/1080;//v26
    widthR = MediaQuery.of(context).size.width/1920;//v26
    curR = widthR;//v26
    return Container(
        child: ConnectivityBuilder(
          builder: (context, isConnected, status) =>
              errmsg('$status'),
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
          height: 525*heightR, //v26
          width: 715*widthR, //v26
          margin: EdgeInsets.only(right: 20*widthR), //v26
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
            borderRadius: BorderRadius.circular(40*curR), //v26
          ),
        child: Row(
          children: <Widget>[
            Column(
              mainAxisAlignment: MainAxisAlignment.start,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [

                Expanded(
                    child: Container(
                      padding: EdgeInsets.only(left: 50*widthR, top:40*heightR), //v26
                      child: Row(
                          children: [
                            Icon(Icons.signal_wifi_off, color: Colors.red[500],size: 40*curR,),
                            Text('    '),
                            Text('Phát hiện mất kết nối mạng',
                              style: TextStyle(color: Colors.black,
                                  fontSize: 43*curR,
                                  fontWeight: FontWeight.bold),
                            )
                          ]
                      ),
                    ),
                ),
                Expanded(
                    child: Container(
                      padding: EdgeInsets.only(left: 75*widthR, top:14*heightR),
                      child: Text('"Vui lòng kiểm tra kết nối wifi hoặc dây mạng"\n'
                          '"Không thực hiện quẹt thẻ cho đến khi có mạng trở lại"\n'
                          '"Thiết bị sẽ hoạt động bình thường \nsau 10 giây khi có mạng trở lại"',
                        style: TextStyle(color: Colors.black,
                            fontSize: 24*curR,
                            fontWeight: FontWeight.bold,
                            height: 1.5
                        ),
                      ),

                    ),
                ),
                Expanded(
                    child: Container(
                        padding: EdgeInsets.only(left: 325*widthR, top:50*heightR), //v26
                        alignment: Alignment.center,
                        child: CircularProgressIndicator(
                          backgroundColor: Colors.grey,
                          color: Colors.blue,
                          strokeWidth: 5*curR,
                        )
                    )
                ),
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
        showDialog(
            context: context,
            builder: (context) {
              Future.delayed(Duration(seconds: 5), () {
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
                content: Text('Lỗi: Không thể kết nối với đầu đọc, vui lòng làm theo các bước sau:\n1) Kiểm tra lại giắc cắm đầu đọc\n2) Kiểm tra nguồn điện của đầu đọc\n\nThiết bị sẽ tự khởi động lại sau 10 giây'),
              );
            }
        );
      }

      if (titleOfNoti == 'Error: Student Info Not Found') {
        showDialog(
            context: context,
            builder: (context) {
              Future.delayed(Duration(seconds: 5), () {
                Navigator.of(context).pop(true);
              });
              return AlertDialog(
                title: Text(bodyOfNoti,
                  style: TextStyle(color: Colors.blue,
                      fontSize: 30,
                      fontWeight: FontWeight.bold),
                ),
                content: Text('LỖI: Dữ liệu học sinh không hợp lệ, vui lòng kiểm tra lại'),
              );
            }
        );
      }

      if (titleOfNoti == 'Error: Wrong data format') {
        showDialog(
            context: context,
            builder: (context) {
              Future.delayed(Duration(seconds: 5), () {
                Navigator.of(context).pop(true);
              });
              return AlertDialog(
                title: Text(bodyOfNoti,
                  style: TextStyle(color: Colors.blue,
                      fontSize: 30,
                      fontWeight: FontWeight.bold),
                ),
                content: Text('LỖI: Dữ liệu thẻ ghi sai định dạng, vui lòng kiểm tra lại'),
              );
            }
        );
      }


      if (titleOfNoti == 'Hexa not valid') {
        showDialog(
            context: context,
            builder: (context) {
              Future.delayed(Duration(seconds: 5), () {
                Navigator.of(context).pop(true);
              });
              return AlertDialog(
                title: Text(bodyOfNoti,
                  style: TextStyle(color: Colors.blue,
                      fontSize: 30,
                      fontWeight: FontWeight.bold),
                ),
                content: Text('LỖI: Dữ liệu hexa ghi trong thẻ không hợp lệ, vui lòng kiểm tra lại'),
              );
            }
        );
      }
     
      if ((titleOfNoti == 'Error: Lost connection to OCD server')&&(internet_connection_status != 'ConnectivityStatus.none')) {
        showDialog(
            context: context,
            builder: (context) {
              Future.delayed(Duration(seconds: 5), () {
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
        /*
        if (DialogShowing == true) {
          Navigator.pop(context,true);
          DialogShowing = false;
          print("TRUEEEEEEEEEEEE: ${DialogShowing}!!!!!!!!!!!");
        } // v22_06
        */
        doStuff(DialogShowing)
        
        Map<String, dynamic> student_info = jsonDecode(bodyOfNoti);

        print('Name, ${student_info['data']['name']}');
        print('ID, ${student_info["data"]["studentId"]}');
        print('School, ${student_info["data"]["school"]["name"]}');
        print('Class, ${student_info["data"]["clazz"]["name"]}');
	
        if (DialogShowing == false)
        {
        showGeneralDialog(
          context: context,
          barrierLabel: "Barrier",
          barrierDismissible: true,
          barrierColor: Colors.black.withOpacity(0.1),
          //transitionDuration: Duration(milliseconds: 0),
          pageBuilder: (_, __, ___) {
            DialogShowing = true; //v20_6
            print("AAAAAAAAAAAA: ${DialogShowing}!!!!!!!!!!!");
            Future.delayed(Duration(seconds: 10), () {
              Navigator.of(context).pop(true);
              DialogShowing = false; //v20_6
            });
            print("BBBBBBBBBBBB: ${DialogShowing}!!!!!!!!!!!");
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
                                  student_info['data']['name'],
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
                                    'ID: '+student_info["data"]["studentId"],
                                    style: TextStyle(
                                      decoration: TextDecoration.none,
                                      fontSize: 35*curR, //v26
                                      color: Colors.white,
                                      fontFamily: 'Dosis', fontWeight: FontWeight.w400,
                                      height: 1.2,
                                    ),
                                  ),
                                  Text(
                                    'Lớp: '+student_info["data"]["clazz"]["name"],
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
          /*
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
          },*/
        );}
      } //NFC info
      
    });
  }
}