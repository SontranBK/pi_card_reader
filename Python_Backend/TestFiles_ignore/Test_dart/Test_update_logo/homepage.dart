import 'package:flutter/material.dart';
import 'package:reader_pi_display/message_list.dart';
import 'dart:ui';
import 'message_list.dart';
import 'show_date_time.dart';
import 'package:flutter/services.dart' show rootBundle;


class Homepage extends StatefulWidget {
  const Homepage({Key? key}) : super(key: key);

  @override
  _HomepageState createState() => _HomepageState();
}

class _HomepageState extends State<Homepage> {
  /* put json file in assets folder:

  flutter:
    assets:
      - json_data.json
  */

  Future<String> getJson() {
  return rootBundle.loadString('json_data.json');
  }

  double heightR = 0.0; //v26
  double widthR = 0.0;
  double curR = 0.0;
  @override
  Widget build(BuildContext context) {
    var UI_update_info = json.decode(await getJson());

    //Map<String, dynamic> UI_update_info = jsonDecode(await getJson());

    print('Tên trường: ${UI_update_info["data"]["name"]}');
    print('Link logo: ${UI_update_info["data"]["logoUrl"]}');
    print('Link background: ${UI_update_info["data"]["backgroundUrl"]}');

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
              image: AssetImage("assets/background.jpg"),
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
                            Image.asset('logo.png',scale: 3.5/curR,),
                            // Image.network(UI_update_info["data"]["logoUrl"],scale: 3.5*curR,),//v26
                            Text(
                              '  TRƯỜNG TIỂU HỌC PHAN CHU TRINH',
                              //'  ' + UI_update_info["data"]["name"],
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