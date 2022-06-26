import 'package:flutter/cupertino.dart';
import 'package:flutter/painting.dart';
import 'package:intl/intl.dart';

import 'dart:html' as webFile;
import 'dart:async';
import 'dart:developer';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:reader_pi_display/homepage.dart';

import 'message_list.dart';
//import 'message.dart';
import 'firebase_options.dart';
import 'package:flutter/rendering.dart';
import 'homepage.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  static const String _title = 'Bảng thông tin quẹt thẻ';

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Thông tin ra vào',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Homepage(),
    );
  }
}


