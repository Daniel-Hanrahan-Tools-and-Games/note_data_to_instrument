
char strNoteData;

void PlayNotes(char strNote) {
  // note off
  if(strNote == '0') {
    analogWrite(3, LOW);
  }
  // note a octave 1
  if(strNote == '1') {
    analogWrite(3, 1.13);
  }
  // note a#/b| octave 1
  if(strNote == '2') {
    analogWrite(3, 2.26);
  }
  // note b octave 1
  if(strNote == '3') {
    analogWrite(3, 3.39);
  }
  // note c octave 1
  if(strNote == '4') {
    analogWrite(3, 4.52);
  }
  // note c#/d| octave 1
  if(strNote == '5') {
    analogWrite(3, 5.65);
  }
  // note d octave 1
  if(strNote == '6') {
    analogWrite(3, 6.78);
  }
// note d#/e| octave 1
  if(strNote == '7') {
    analogWrite(3, 7.91);
  }
  // note e octave 1
  if(strNote == '8') {
    analogWrite(3, 8.104);
  }
  // note f octave 1
  if(strNote == 'q') {
    analogWrite(3, 9.117);
  }
  // note f#/g| octave 1
  if(strNote == 'w') {
    analogWrite(3, 10.130);
  }
  // note g octave 1
  if(strNote == 'e') {
    analogWrite(3, 11.143);
  }
  // note g# octave 1/a| octave 2
  if(strNote == 'r') {
    analogWrite(3, 12.156);
  }
  // note a octave 2
  if(strNote == 't') {
    analogWrite(3, 13.169);
  }
  // note a#/b| octave 2
  if(strNote == 'y') {
    analogWrite(3, 14.182);
  }
  // note b octave 2
  if(strNote == 'u') {
    analogWrite(3, 15.195);
  }
  // note c octave 2
  if(strNote == 'i') {
    analogWrite(3, 16.208);
  }
  // note c#/d| octave 2
  if(strNote == 'o') {
    analogWrite(3, 17.221);
  }
  // note d octave 2
  if(strNote == 'p') {
    analogWrite(3, 18.234);
  }
// note d#/e| octave 2
  if(strNote == '[') {
    analogWrite(3, 19.247);
  }
  // note e octave 2
  if(strNote == ']') {
    analogWrite(3, 20.260);
  }
  // note f octave 2
  if(strNote == 'a') {
    analogWrite(3, 21.273);
  }
  // note f#/g| octave 2
  if(strNote == 's') {
    analogWrite(3, 22.286);
  }
  // note g octave 2
  if(strNote == 'd') {
    analogWrite(3, 23.299);
  }
  // note g# octave 2/a| octave 3
  if(strNote == 'f') {
    analogWrite(3, 24.312);
  }
  // note a octave 3
  if(strNote == 'g') {
    analogWrite(3, 25.325);
  }
  // note a#/b| octave 3
  if(strNote == 'h') {
    analogWrite(3, 26.338);
  }
  // note b octave 3
  if(strNote == 'j') {
    analogWrite(3, 27.350);
  }
  // note c octave 3
  if(strNote == 'k') {
    analogWrite(3, 28.363);
  }
  // note c#/d| octave 3
  if(strNote == 'l') {
    analogWrite(3, 29.376);
  }
  // note d octave 3
  if(strNote == ';') {
    analogWrite(3, 30.389);
  }
// note d#/e| octave 3
  if(strNote == 'z') {
    analogWrite(3, 31.402);
  }
  // note e octave 3
  if(strNote == 'x') {
    analogWrite(3, 32.415);
  }
  // note f octave 3
  if(strNote == 'c') {
    analogWrite(3, 33.428);
  }
  // note f#/g| octave 3
  if(strNote == 'v') {
    analogWrite(3, 34.441);
  }
  // note g octave 3
  if(strNote == 'b') {
    analogWrite(3, 35.454);
  }
  // note g# octave 3/a| octave 4
  if(strNote == 'n') {
    analogWrite(3, 36.467);
  }
  // note a octave 4
  if(strNote == 'm') {
    analogWrite(3, 37.480);
  }
  // note a#/b| octave 4
  if(strNote == ',') {
    analogWrite(3, 38.493);
  }
  // note b octave 4
  if(strNote == '.') {
    analogWrite(3, 39.506);
  }
  // note c octave 4
  if(strNote == '/') {
    analogWrite(3, 40.519);
  }
  // note c#/d| octave 4
  if(strNote == '`') {
    analogWrite(3, 41.532);
  }
  // note d octave 4
  if(strNote == '~') {
    analogWrite(3, 42.545);
  }
// note d#/e| octave 4
  if(strNote == '!') {
    analogWrite(3, 43.558);
  }
  // note e octave 4
  if(strNote == '@') {
    analogWrite(3, 44.571);
  }
  // note f octave 4
  if(strNote == '#') {
    analogWrite(3, 45.584);
  }
  // note f#/g| octave 4
  if(strNote == '$') {
    analogWrite(3, 46.597);
  }
  // note g octave 4
  if(strNote == '%') {
    analogWrite(3, 47.610);
  }
  // note g# octave 4/a| octave 5
  if(strNote == '^') {
    analogWrite(3, 48.623);
  }
  // note a octave 5
  if(strNote == '&') {
    analogWrite(3, 49.636);
  }
  // note a#/b| octave 5
  if(strNote == '*') {
    analogWrite(3, 50.649);
  }
  // note b octave 5
  if(strNote == '(') {
    analogWrite(3, 51.652);
  }
  // note c octave 5
  if(strNote == ')') {
    analogWrite(3, 52.665);
  }
  // note c#/d| octave 5
  if(strNote == '_') {
    analogWrite(3, 53.678);
  }
  // note d octave 5
  if(strNote == '+') {
    analogWrite(3, 54.691);
  }
// note d#/e| octave 5
  if(strNote == 'Q') {
    analogWrite(3, 55.704);
  }
  // note e octave 5
  if(strNote == 'W') {
    analogWrite(3, 56.717);
  }
  // note f octave 5
  if(strNote == 'E') {
    analogWrite(3, 57.730);
  }
  // note f#/g| octave 5
  if(strNote == 'R') {
    analogWrite(3, 58.743);
  }
  // note g octave 5
  if(strNote == 'T') {
    analogWrite(3, 59.756);
  }
  // note g# octave 5/a| octave 6
  if(strNote == 'Y') {
    analogWrite(3, 60.769);
  }
  // note a octave 6
  if(strNote == 'U') {
    analogWrite(3, 61.782);
  }
  // note a#/b| octave 6
  if(strNote == 'I') {
    analogWrite(3, 62.795);
  }
  // note b octave 6
  if(strNote == 'O') {
    analogWrite(3, 63.808);
  }
  // note c octave 6
  if(strNote == 'P') {
    analogWrite(3, 64.821);
  }
  // note c#/d| octave 6
  if(strNote == '{') {
    analogWrite(3, 65.834);
  }
  // note d octave 6
  if(strNote == '}') {
    analogWrite(3, 66.847);
  }
// note d#/e| octave 6
  if(strNote == '|') {
    analogWrite(3, 67.860);
  }
  // note e octave 6
  if(strNote == 'A') {
    analogWrite(3, 68.873);
  }
  // note f octave 6
  if(strNote == 'S') {
    analogWrite(3, 69.886);
  }
  // note f#/g| octave 6
  if(strNote == 'D') {
    analogWrite(3, 70.899);
  }
  // note g octave 6
  if(strNote == 'F') {
    analogWrite(3, 71.912);
  }
  // note g# octave 6/a| octave 7
  if(strNote == 'G') {
    analogWrite(3, 72.925);
  }
  // note a octave 7
  if(strNote == 'H') {
    analogWrite(3, 73.935);
  }
  // note a#/b| octave 7
  if(strNote == 'J') {
    analogWrite(3, 74.935);
  }
  // note b octave 7
  if(strNote == 'K') {
    analogWrite(3, 75.948);
  }
  // note c octave 7
  if(strNote == 'L') {
    analogWrite(3, 76.961);
  }
  // note c#/d| octave 7
  if(strNote == ':') {
    analogWrite(3, 77.974);
  }
  // note d octave 7
  if(strNote == '"') {
    analogWrite(3, 78.987);
  }
// note d#/e| octave 7
  if(strNote == 'Z') {
    analogWrite(3, 80);
  }
  // note e octave 7
  if(strNote == 'X') {
    analogWrite(3, 81.13);
  }
  // note f octave 7
  if(strNote == 'V') {
    analogWrite(3, 82.26);
  }
  // note f#/g| octave 7
  if(strNote == 'B') {
    analogWrite(3, 83.39);
  }
  // note g octave 7
  if(strNote == 'N') {
    analogWrite(3, 84.52);
  }
  // note g# octave 7/a| octave 8
  if(strNote == 'M') {
    analogWrite(3, 85.65);
  }
  // note a octave 8
  if(strNote == '<') {
    analogWrite(3, 86.78);
  }
  // note a#/b| octave 8
  if(strNote == '>') {
    analogWrite(3, 87.91);
  }
  // note b octave 8
  if(strNote == '?') {
    analogWrite(3, 88.104);
  }
  // note c octave 8
  if(strNote == '9') {
    analogWrite(3, 89.117);
  }

}
void setup() {
  // put your setup code here, to run once:
  // starts serial connection at 9600 baud
  Serial.begin(57600);
}

void loop() {
  // put your main code here, to run repeatedly:
  // uses pin 3 on the arduino
  if(Serial.available() > 0){
    // input for note_data_to_instrument or user
    strNoteData = Serial.read();
    // function needed
    PlayNotes(strNoteData);
  }
}
