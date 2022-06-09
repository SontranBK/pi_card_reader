// Copyright (c) 2021, the MarchDev Toolkit project authors. Please see the AUTHORS file
// for details. All rights reserved. Use of this source code is governed by a
// BSD-style license that can be found in the LICENSE file.

import 'package:flutter/material.dart';

import 'package:cross_connectivity/cross_connectivity.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Cross Connectivity Example',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {


  @override
  Widget build(BuildContext context) {
    var status;
    return Scaffold(
      appBar: AppBar(
        title: Text('Cross Connectivity Example'),
      ),
      body: Container(
        child: ConnectivityBuilder(
          builder: (context, isConnected, status) =>
              errmsg(
              "Không kết nối internet! Vui lòng kiểm tra lại mạng!",
              '$status'),
        )

        //to show internet connection message on isoffline = true.
      ),
    );
  }
  Widget errmsg(String text, String show) {
    //error message widget.
    if (show == 'ConnectivityStatus.none') {
      //if error is true then show error message box
      return Container(
        padding: EdgeInsets.all(10.00),
        margin: EdgeInsets.only(bottom: 10.00),
        color: Colors.red,
        child: Row(children: [
          Container(
            margin: EdgeInsets.only(right: 6.00),
            child: Icon(Icons.info, color: Colors.white),
          ), // icon for error message
          Container(
            child: Text(text,
                overflow: TextOverflow.clip,
                style: TextStyle(color: Colors.white)),
            width: 160,
          ),
          //show error message text
        ]),
      );
    } else {
      return Container();
    }
    
  }
}