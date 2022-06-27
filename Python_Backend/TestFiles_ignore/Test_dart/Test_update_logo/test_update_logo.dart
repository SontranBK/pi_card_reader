import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:cross_connectivity/cross_connectivity.dart';

 /*  

Bản tin json bắn lên từ python sẽ như sau, dart sẽ nhận được json này:

{
"errorCode":"00",
"errorMessage":"",
"data":
  {
  "name":"Meta edu",
  "logoUrl":"http://api.metaedu.edu.vn/api/attachments/preview?id=1",
  "backgroundUrl":"http://api.metaedu.edu.vn/api/attachments/preview?id=2"
  }
}

*/


// NHỚ THÊM FIREBASE CÁC THỨ VÀO BÊN TRÊN NHÉ, THÊM ĐẦY ĐỦ CODE FIREBASE
// CODE TIẾP VÀO FILE MESSAGE LIST HOẶC CODE GIỐNG TRONG ĐÓ

  @override
  void initState() {
    super.initState();
   
        
    FirebaseMessaging.onMessage.listen((RemoteMessage message) {
    Noti = message.notification ?? RemoteNotification();
    String? titleOfNoti = Noti.title ?? '';
    String? bodyOfNoti = Noti.body ?? '';

    // Ở CODE PYTHON, LÚC BẮN JSON LÊN THÌ NHỚ ĐỂ TITLE LÀ "Update_Logo_Background"

    if (titleOfNoti == "Update_Logo_Background") {
      Map<String, dynamic> UI_update_info = jsonDecode(bodyOfNoti);

      print('Tên trường: ${UI_update_info["data"]["name"]}');
      print('Link logo: ${UI_update_info["data"]["logoUrl"]}');
      print('Link background: ${UI_update_info["data"]["backgroundUrl"]}');

      // SAU ĐÓ, LẤY 3 BIẾN Ở DƯỚI, ĐƯA VÀO LINK CỦA LOGO, BACKGROUND VÀ TÊN STRING CỦA TRƯỜNG
      // UI_update_info["data"]["name"]
      // UI_update_info["data"]["logoUrl"]
      // UI_update_info["data"]["backgroundUrl"]

      // KHI BẮN TỪ PYTHON LÊN, CỐ GẮNG BẮN ÍT NHẤT 2 BẢN TIN JSON KHÁC NHAU
      // DÙNG BỪA LINK NÀO ĐÓ CŨNG ĐƯỢC
      // KẾT QUẢ MONG MUỐN: KHI BẮN TỪ PYTHON LÊN LÀ BACKGROUND, LOGO, TÊN PHẢI ĐỔI.

      }



