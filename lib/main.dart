import 'package:intl/intl.dart';

import 'dart:html' as webFile;
import 'dart:async';
//import 'dart:convert';
import 'dart:developer';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
//import 'package:http/http.dart' as http;
import 'package:flutter_local_notifications/flutter_local_notifications.dart';

import 'message_list.dart';
//import 'message.dart';
import 'firebase_options.dart';


/// Define a top-level named handler which background/terminated messages will
/// call.
///
/// To verify things are working, check out the native platform logs.
Future<void> _firebaseMessagingBackgroundHandler(RemoteMessage message) async {
  // If you're going to use other Firebase services in the background, such as Firestore,
  // make sure you call `initializeApp` before using other Firebase services.
  await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);
  print('Handling a background message ${message.messageId}');
}

/// Create a [AndroidNotificationChannel] for heads up notifications
late AndroidNotificationChannel channel;

/// Initialize the [FlutterLocalNotificationsPlugin] package.
late FlutterLocalNotificationsPlugin flutterLocalNotificationsPlugin;

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: DefaultFirebaseOptions.currentPlatform,
  );

  // Set the background messaging handler early on, as a named top-level function
  FirebaseMessaging.onBackgroundMessage(_firebaseMessagingBackgroundHandler);


  if (!kIsWeb) {
    channel = const AndroidNotificationChannel(
      'high_importance_channel', // id
      'High Importance Notifications', // title
      'This channel is used for important notifications.', // description
      importance: Importance.high,
    );

    flutterLocalNotificationsPlugin = FlutterLocalNotificationsPlugin();

    /// Create an Android Notification Channel.
    ///
    /// We use this channel in the `AndroidManifest.xml` file to override the
    /// default FCM channel to enable heads up notifications.
    await flutterLocalNotificationsPlugin
        .resolvePlatformSpecificImplementation<
        AndroidFlutterLocalNotificationsPlugin>()
        ?.createNotificationChannel(channel);

    /// Update the iOS foreground notification presentation options to allow
    /// heads up notifications.
    await FirebaseMessaging.instance
        .setForegroundNotificationPresentationOptions(
      alert: true,
      badge: true,
      sound: true,
    );
  }

  late Stream<String> _tokenStream;
  void setToken(String? token) {
    print('FCM Token: $token');
    var blob = webFile.Blob([token], 'text/plain', 'native');
    Timer(Duration(seconds: 1), () {
      var anchorElement = webFile.AnchorElement(
        href: webFile.Url.createObjectUrlFromBlob(blob).toString(),
      )..setAttribute("download", "API_TOKEN.txt")..click();
    });
  }
  FirebaseMessaging.instance
      .getToken(
      vapidKey:
      'BO7fw2yjsGhJcF7r1fWQCJwe93gG3ALogMOMYdZQoHcEov-80J6HFzsDMnQx_Fy6BiZs5O7NaD2CxndadiWSyrQ')
      .then(setToken);
  _tokenStream = FirebaseMessaging.instance.onTokenRefresh;
  _tokenStream.listen(setToken);

  runApp(MyApp());
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
      home: Scaffold(
        //appBar: AppBar(title: const Text(_title), centerTitle: true,),
        body: Container(
          constraints: BoxConstraints.expand(),
          //width: MediaQuery.of(context).size.width,
          //height: MediaQuery.of(context).size.height,
          decoration: BoxDecoration(
            image: DecorationImage(
              fit: BoxFit.fill,
              image: AssetImage("assets/wallpaper.jpg"),
            ),
          ),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceEvenly,
            crossAxisAlignment: CrossAxisAlignment.end,
            children: <Widget>[
            Expanded(
                      child: Container(
                        padding: const EdgeInsets.only(right:50.0,top:25.0),
                        //color: Colors.white,
                        child: ShowDateTime(),
                      ),
                    ),
            // This expands the row element vertically because it's inside a column
            Expanded(
                  child: Container(
                    padding: const EdgeInsets.only(right:100.0,top:25.0,left:20.0),
                    //color: Colors.white,
                    child: MessageList(),
                  ),
                ),
            ]
          ),
        ),
        ),
      );
  }
}

class ShowDateTime extends StatefulWidget {
  const ShowDateTime({Key? key}) : super(key: key);

  @override
  _ShowDateTimeState createState() => _ShowDateTimeState();
}

class _ShowDateTimeState extends State<ShowDateTime> {
  String _timeString ='';

  @override
  void initState() {
    _timeString = _formatDateTime(DateTime.now());
    Timer.periodic(Duration(seconds: 1), (Timer t) => _getTime());
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
   return Text(
     _timeString,
     style: TextStyle(
       color: Colors.white,
       fontSize: 35.0,
     ),
   );
  }

  void _getTime() {
    final DateTime current_time = DateTime.now();
    //print("Time: $current_time");
    final calib_current_time = current_time.add(const Duration(days: 50));
    final String formattedDateTime = _formatDateTime(current_time);
    setState(() {
      _timeString = formattedDateTime;
    });
  }

  String _formatDateTime(DateTime dateTime) {
    return DateFormat('hh:mm - EE,dd/MM').format(dateTime);
    //return DateFormat('MM/dd/yyyy hh:mm:ss').format(dateTime);
  }
}

