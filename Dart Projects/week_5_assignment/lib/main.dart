import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Simple Flutter App',
      home: Scaffold(
        appBar: AppBar(
          title: Text('Simple Flutter App'),
          centerTitle: true,
        ),
        body: Center(
          child: Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                  'Welcome to My Flutter App!',
                  style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
                  textAlign: TextAlign.center,
                ),
                SizedBox(height: 20),
                ElevatedButton(
                  onPressed: () {
                    print('Button was clicked!');
                  },
                  child: Text('Click Me'),
                ),
                SizedBox(height: 20),
                Image.network(
                  'https://flutter.dev/assets/images/shared/brand/flutter/logo/flutter-lockup.png',
                  height: 150,
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
