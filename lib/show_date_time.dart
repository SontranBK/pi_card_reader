import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'dart:ui';
import 'dart:async';

class ShowDateTime extends StatefulWidget {
  const ShowDateTime({Key? key}) : super(key: key);

  @override
  _ShowDateTimeState createState() => _ShowDateTimeState();
}

class _ShowDateTimeState extends State<ShowDateTime> {
  String _timeString ='';
  String _gio = ' ', _thu = ' ', _ngay = ' ', _thang =  ' ';
  var weekday = {'Mon':'Thứ Hai', 'Tue':'Thứ Ba', 'Wed':'Thứ Tư', 'Thu':'Thứ Năm', 'Fri':'Thứ Sáu', 'Sat':'Thứ Bảy', 'Sun':'Chủ Nhật'};

  @override
  void initState() {
    _timeString = _formatDateTime(DateTime.now());
    Timer.periodic(Duration(seconds: 1), (Timer t) => _getTime());
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    double widthR; // v26
    widthR = MediaQuery.of(context).size.width/1920; // v26
    return Text(
      _timeString,
      style: TextStyle(
        fontFamily: 'Dosis', fontWeight: FontWeight.bold,
        color: Colors.red[600],
        fontSize: 48.0*widthR, // v26
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
    String _time_dis = ' ';
    _gio = DateFormat('hh:mm').format(dateTime);
    _thu = weekday[DateFormat('EEE').format(dateTime)].toString();
    _time_dis = _gio +' - '+ _thu+', '+DateFormat('dd').format(dateTime) + ' thg ' +DateFormat('MM').format(dateTime);
    return _time_dis;
  }

}
