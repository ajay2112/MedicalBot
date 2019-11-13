import 'package:flutter_chat_demo/login.dart';
import 'package:flutter_chat_demo/dialogflow_v2.dart';
import 'package:flutter/material.dart';

void main() => runApp(new MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return new MaterialApp(
      title: 'Example Dialogflow Flutter',
      theme: new ThemeData(
      primarySwatch: Colors.blue,
      ),
      home: new MyHomePage(title: 'Medical Assistant'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => new _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
//   @override
//   Widget build(BuildContext context) {
//     return new Scaffold(
//       appBar: new AppBar(
//         title: new Text(widget.title),
//       ),
//       body: new Column(children: <Widget>[
//         new Container(
//           margin: EdgeInsets.all(10.0),
//           child: new RaisedButton(
//             onPressed: () {
//               Navigator.push(
//                 context,
//                 MaterialPageRoute(builder: (context) => LoginScreen()),
//               );
//             },
//             child: Text("Chat with a Doctor"),
//           ),
//         ),
//         new Container(
//           margin: EdgeInsets.all(10.0),
//           child: new RaisedButton(
//             onPressed: () {
//               Navigator.push(
//                 context,
//                 MaterialPageRoute(builder: (context) => HomePageDialogflowV2()),
//               );
//             },
//             child: Text("Ask Nemo"),
//           ),
//         )
//       ]),
//     );
//   }
// }
  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      appBar: new AppBar(
        title: new Text(widget.title),
      ),
      body: new Container(
        decoration: new BoxDecoration(color:Colors.white), 
      child: new Center(
        child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              new Container(
                margin: EdgeInsets.all(10.0),
                child: new RaisedButton(
                  padding: const EdgeInsets.all(8.0),
                  textColor: Colors.white,
                  color: Colors.green,
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(builder: (context) => LoginScreen()),
                    );
                  },
                  child: new Text("Chat with Doctor"),
                ),
              ),
              new Container(
                margin: EdgeInsets.all(10.0),
                child: new RaisedButton(
                  onPressed: () {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                          builder: (context) => HomePageDialogflowV2()),
                    );
                  },
                  textColor: Colors.white,
                  color: Colors.red,
                  padding: const EdgeInsets.all(10.0),
                  child: new Text(
                    "Ask Nemo",
                  ),
                ),
              )
            ]),
      ),
      ),
    );
  }
}
