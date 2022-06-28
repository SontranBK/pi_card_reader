import 'package:flutter/material.dart';
import 'package:reader_pi_display/message_list.dart';
import 'dart:ui';
import 'message_list.dart';
import 'show_date_time.dart';
import 'package:flutter/services.dart' show rootBundle;
//import 'package:flutter/services.dart';
import 'dart:convert';

class Homepage extends StatefulWidget {
  const Homepage({Key? key}) : super(key: key);

  @override
  _HomepageState createState() => _HomepageState();
}

class _HomepageState extends State<Homepage> {
  /* put json file in assets folder:

  flutter:
    assets:
      - ui_auto_update.json
  */
  String school_name = "";
  String logoURL = "";
  String backgroundURL = "";

  // Fetch content from the json file
  Future<void> readJson() async {
    final String response = await rootBundle.loadString('assets/ui_auto_update.json');
    final data = await json.decode(response);
    print('data: ${data}');
    setState(() {
      school_name = data["data"]["name"];
      logoURL = data["data"]["logoUrl"];
      backgroundURL = data["data"]["backgroundUrl"];
    });
  }


  double heightR = 0.0; //v26
  double widthR = 0.0;
  double curR = 0.0;
  @override
  Widget build(BuildContext context) {

    readJson();
    print('Tên trường: ${school_name}');
    print('Link logo: ${logoURL}');
    print('Link background: ${backgroundURL}');

    double heightR, widthR; //v26
    heightR = MediaQuery.of(context).size.height / 1080; //v26
    widthR = MediaQuery.of(context).size.width / 1920; //v26
    var curR = widthR; //v26
    return Scaffold(
      body: Container(
          constraints: BoxConstraints.expand(),
          decoration: BoxDecoration(
            image: DecorationImage(
              // you can change line 26 into "fit: BoxFit.fill"
              fit: BoxFit
                  .fill, //v26 It's fill properties in last ver, for keeping ratio when scaling windows
              scale: 1, //v26
              // image: AssetImage("assets/background.jpg"),
              image: NetworkImage(backgroundURL),
            ),
          ),
          child: Container(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.start,
              children: [
                Column(
                  mainAxisAlignment: MainAxisAlignment.start,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Container(
                       // color: Colors.blueAccent,
                        padding: EdgeInsets.only(
                            left: 95 * widthR, top: 60 * heightR), //v26
                        child: Row(
                          children: [
                            // Image.asset('logo.png',scale: 3.5/curR,),
                             Image.network(logoURL,scale: 3.5*curR,),//v26
                            Text(
                              //'  TRƯỜNG TIỂU HỌC PHAN CHU TRINH',
                              '  ' + school_name,
                              style: TextStyle(
                                fontFamily: 'Dosis', fontSize: 48 * widthR,
                                fontWeight: FontWeight.bold, //v26
                                color: Colors.blue[900],
                              ),
                            ),
                            Expanded(
                                child: Container(
                                  // color: Colors.purple,
                                  padding:
                                  EdgeInsets.only(left: 300 * widthR), //v26
                                  //color: Colors.white,
                                  child: ShowDateTime(),
                                ),
                            )
                          ],
                        )
                    ),
                    Container(
                      child: Row(
                        children: [

                          Expanded(
                              child: Column(
                                children: [
                                  Container(
                                    height: 500 * heightR, //v26
                                    width: 700 * widthR, //v26
                                    margin: EdgeInsets.only(left: 575 * widthR,top: 100*heightR), //v26
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
                                          Colors.greenAccent.withOpacity(0.0),
                                          Colors.greenAccent.withOpacity(0.0),
                                          Colors.greenAccent.withOpacity(0.0),
                                          Colors.greenAccent.withOpacity(0.0),
                                        ],
                                      ),
                                    ),
                                    child: SizedBox.expand(
                                      child: MessageList(),
                                    ),
                                  ),
                                  Container(
                                    // color: Colors.blue,
                                    //v26
                                    padding: EdgeInsets.only(right: 100 * widthR,left: 300*widthR), //v26
                                    margin: EdgeInsets.only(left: 275 * widthR,),
                                    child: Text(
                                      '" Tri thức là chìa khóa mở cửa tương lai"',
                                      style: TextStyle(
                                        decoration: TextDecoration.none,
                                        fontFamily: 'Dosis', fontSize: 40 * curR,
                                        fontWeight: FontWeight.bold, //v26
                                        color: Colors.blue[900],
                                      ),
                                    ),
                                  )
                                ],
                              ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),

              ],
            ),
          )),
    );
  }
}
