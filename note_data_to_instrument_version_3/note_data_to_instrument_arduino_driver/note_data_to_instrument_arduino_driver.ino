
String strNoteData;

void PlayNotes(String strNote) {
  // note off
  if(strNote == "0") {
    analogWrite(3, LOW);
  }
  // note c octave -1
  if(strNote == "1") {
    analogWrite(3, 1.9921875);
  }
  // note c#/d| octave -1
  if(strNote == "2") {
    analogWrite(3, 3.984375);
  }
  // note d octave -1
  if(strNote == "3") {
    analogWrite(3, 5.9765625);
  }
  // note d#/e| octave -1
  if(strNote == "4") {
    analogWrite(3, 7.96875);
  }
  // note e octave -1
  if(strNote == "5") {
    analogWrite(3, 9.9609375);
  }
  // note f octave -1
  if(strNote == "6") {
    analogWrite(3, 11.953125);
  }
  // note f#/g| octave -1
  if(strNote == "7") {
    analogWrite(3, 13.9453125);
  }
  // note g octave -1
  if(strNote == "8") {
    analogWrite(3, 15.9375);
  }
  // note g#/a| octave -1
  if(strNote == "9") {
    analogWrite(3, 17.9296875);
  }
  // note a octave -1
  if(strNote == "10") {
    analogWrite(3, 19.921875);
  }
  // note a#/b| octave -1
  if(strNote == "11") {
    analogWrite(3, 21.9140625);
  }
  // note b octave -1
  if(strNote == "12") {
    analogWrite(3, 23.90625);
  }
  // note c octave 0
  if(strNote == "13") {
    analogWrite(3, 25.8984375);
  }
  // note c#/b| octave 0
  if(strNote == "14") {
    analogWrite(3, 27.890625);
  }
  // note d octave 0
  if(strNote == "15") {
    analogWrite(3, 29.8828125);
  }
  // note d#/e| octave 0
  if(strNote == "16") {
    analogWrite(3, 31.875);
  }
  // note e octave 0
  if(strNote == "17") {
    analogWrite(3, 33.8671875);
  }
  // note f octave 0
  if(strNote == "18") {
    analogWrite(3, 35.859375);
  }
  // note f#/g| octave 0
  if(strNote == "19") {
    analogWrite(3, 37.8515625);
  }
  // note g octave 0
  if(strNote == "20") {
    analogWrite(3, 39.84375);
  }
  // note g#/a| octave 0
  if(strNote == "21") {
    analogWrite(3, 41.8359375);
  }
  // note a octave 0
  if(strNote == "22") {
    analogWrite(3, 43.828125);
  }
  // note a#/b| octave 0
  if(strNote == "23") {
    analogWrite(3, 45.8203125);
  }
  // note b octave 0
  if(strNote == "24") {
    analogWrite(3, 47.8125);
  }
  // note c octave 1
  if(strNote == "25") {
    analogWrite(3, 49.8046875);
  }
  // note c#/d| octave 1
  if(strNote == "26") {
    analogWrite(3, 51.796875);
  }
  // note d octave 1
  if(strNote == "27") {
    analogWrite(3, 53.7890625);
  }
// note d#/e| octave 1
  if(strNote == "28") {
    analogWrite(3, 55.78125);
  }
  // note e octave 1
  if(strNote == "29") {
    analogWrite(3, 57.734375);
  }
  // note f octave 1
  if(strNote == "30") {
    analogWrite(3, 59.765625);
  }
  // note f#/g| octave 1
  if(strNote == "31") {
    analogWrite(3, 61.7578125);
  }
  // note g octave 1
  if(strNote == "32") {
    analogWrite(3, 63.75);
  }
  // note g#/a| octave 1
  if(strNote == "33") {
    analogWrite(3, 65.7421875);
  }
  // note a octave 1
  if(strNote == "34") {
    analogWrite(3, 67.734375);
  }
  // note a#/b| octave 1
  if(strNote == "35") {
    analogWrite(3, 69.7265625);
  }
  // note b octave 1
  if(strNote == "36") {
    analogWrite(3, 71.71875);
  }
  // note c octave 2
  if(strNote == "37") {
    analogWrite(3, 73.7109375);
  }
  // note c#/d| octave 2
  if(strNote == "38") {
    analogWrite(3, 75.703125);
  }
  // note d octave 2
  if(strNote == "39") {
    analogWrite(3, 77.6953125);
  }
// note d#/e| octave 2
  if(strNote == "40") {
    analogWrite(3, 79.6875);
  }
  // note e octave 2
  if(strNote == "41") {
    analogWrite(3, 81.6796875);
  }
  // note f octave 2
  if(strNote == "42") {
    analogWrite(3, 83.671875);
  }
  // note f#/g| octave 2
  if(strNote == "43") {
    analogWrite(3, 85.6640625);
  }
  // note g octave 2
  if(strNote == "44") {
    analogWrite(3, 87.65625);
  }
  // note g#/a| octave 2
  if(strNote == "45") {
    analogWrite(3, 89.6484375);
  }
  // note a octave 2
  if(strNote == "46") {
    analogWrite(3, 91.640625);
  }
  // note a#/b| octave 2
  if(strNote == "47") {
    analogWrite(3, 93.6328125);
  }
  // note b octave 2
  if(strNote == "48") {
    analogWrite(3, 95.625);
  }
  // note c octave 3
  if(strNote == "49") {
    analogWrite(3, 97.6171875);
  }
  // note c#/d| octave 3
  if(strNote == "50") {
    analogWrite(3, 99.609375);
  }
  // note d octave 3
  if(strNote == "51") {
    analogWrite(3, 101.6015625);
  }
// note d#/e| octave 3
  if(strNote == "52") {
    analogWrite(3, 103.59375);
  }
  // note e octave 3
  if(strNote == "53") {
    analogWrite(3, 105.5859375);
  }
  // note f octave 3
  if(strNote == "54") {
    analogWrite(3, 107.578125);
  }
  // note f#/g| octave 3
  if(strNote == "55") {
    analogWrite(3, 109.5703125);
  }
  // note g octave 3
  if(strNote == "56") {
    analogWrite(3, 111.5625);
  }
  // note g#/a| octave 3
  if(strNote == "57") {
    analogWrite(3, 113.5546875);
  }
  // note a octave 3
  if(strNote == "58") {
    analogWrite(3, 115.546875);
  }
  // note a#/b| octave 3
  if(strNote == "59") {
    analogWrite(3, 117.5390625);
  }
  // note b octave 3
  if(strNote == "60") {
    analogWrite(3, 119.53125);
  }
  // note c octave 4
  if(strNote == "61") {
    analogWrite(3, 121.5234375);
  }
  // note c#/d| octave 4
  if(strNote == "62") {
    analogWrite(3, 123.515625);
  }
  // note d octave 4
  if(strNote == "63") {
    analogWrite(3, 125.5078125);
  }
// note d#/e| octave 4
  if(strNote == "64") {
    analogWrite(3, 127.5);
  }
  // note e octave 4
  if(strNote == "65") {
    analogWrite(3, 129.4921875);
  }
  // note f octave 4
  if(strNote == "66") {
    analogWrite(3, 131.484375);
  }
  // note f#/g| octave 4
  if(strNote == "67") {
    analogWrite(3, 133.4765625);
  }
  // note g octave 4
  if(strNote == "68") {
    analogWrite(3, 135.46875);
  }
  // note g#/a| octave 4
  if(strNote == "69") {
    analogWrite(3, 137.4609375);
  }
  // note a octave 4
  if(strNote == "70") {
    analogWrite(3, 139.453125);
  }
  // note a#/b| octave 4
  if(strNote == "71") {
    analogWrite(3, 141.4453125);
  }
  // note b octave 4
  if(strNote == "72") {
    analogWrite(3, 143.4375);
  }
  // note c octave 5
  if(strNote == "73") {
    analogWrite(3, 145.4296875);
  }
  // note c#/d| octave 5
  if(strNote == "74") {
    analogWrite(3, 147.421875);
  }
  // note d octave 5
  if(strNote == "75") {
    analogWrite(3, 149.4140625);
  }
// note d#/e| octave 5
  if(strNote == "76") {
    analogWrite(3, 151.40625);
  }
  // note e octave 5
  if(strNote == "77") {
    analogWrite(3, 153.3984375);
  }
  // note f octave 5
  if(strNote == "78") {
    analogWrite(3, 155.390625);
  }
  // note f#/g| octave 5
  if(strNote == "79") {
    analogWrite(3, 157.3828125);
  }
  // note g octave 5
  if(strNote == "80") {
    analogWrite(3, 159.375);
  }
  // note g#/a| octave 5
  if(strNote == "81") {
    analogWrite(3, 161.3671875);
  }
  // note a octave 5
  if(strNote == "82") {
    analogWrite(3, 163.359375);
  }
  // note a#/b| octave 5
  if(strNote == "83") {
    analogWrite(3, 165.3515625);
  }
  // note b octave 5
  if(strNote == "84") {
    analogWrite(3, 167.34375);
  }
  // note c octave 6
  if(strNote == "85") {
    analogWrite(3, 169.3359375);
  }
  // note c#/d| octave 6
  if(strNote == "86") {
    analogWrite(3, 171.328125);
  }
  // note d octave 6
  if(strNote == "87") {
    analogWrite(3, 173.3203125);
  }
// note d#/e| octave 6
  if(strNote == "88") {
    analogWrite(3, 175.3125);
  }
  // note e octave 6
  if(strNote == "89") {
    analogWrite(3, 177.3046875);
  }
  // note f octave 6
  if(strNote == "90") {
    analogWrite(3, 179.296875);
  }
  // note f#/g| octave 6
  if(strNote == "91") {
    analogWrite(3, 181.2890625);
  }
  // note g octave 6
  if(strNote == "92") {
    analogWrite(3, 183.28125);
  }
  // note g#/a| octave 6
  if(strNote == "93") {
    analogWrite(3, 185.2734375);
  }
  // note a octave 6
  if(strNote == "94") {
    analogWrite(3, 187.265625);
  }
  // note a#/b| octave 6
  if(strNote == "95") {
    analogWrite(3, 189.2578125);
  }
  // note b octave 6
  if(strNote == "96") {
    analogWrite(3, 191.25);
  }
  // note c octave 7
  if(strNote == "97") {
    analogWrite(3, 193.2421875);
  }
  // note c#/d| octave 7
  if(strNote == "98") {
    analogWrite(3, 195.234375);
  }
  // note d octave 7
  if(strNote == "99") {
    analogWrite(3, 197.2265625);
  }
// note d#/e| octave 7
  if(strNote == "100") {
    analogWrite(3, 199.21875);
  }
  // note e octave 7
  if(strNote == "101") {
    analogWrite(3, 201.2109375);
  }
  // note f octave 7
  if(strNote == "102") {
    analogWrite(3, 203.203125);
  }
  // note f#/g| octave 7
  if(strNote == "103") {
    analogWrite(3, 205.1953125);
  }
  // note g octave 7
  if(strNote == "104") {
    analogWrite(3, 207.1875);
  }
  // note g#/a| octave 7
  if(strNote == "105") {
    analogWrite(3, 209.1796875);
  }
  // note a octave 7
  if(strNote == "106") {
    analogWrite(3, 211.171875);
  }
  // note a#/b| octave 7
  if(strNote == "107") {
    analogWrite(3, 213.1640625);
  }
  // note b octave 7
  if(strNote == "108") {
    analogWrite(3, 215.15625);
  }
  // note c octave 8
  if(strNote == "109") {
    analogWrite(3, 217.1484375);
  }
  // note c#/d| octave 8
  if(strNote == "110") {
    analogWrite(3, 219.140625);
  }
  // note d octave 8
  if(strNote == "111") {
    analogWrite(3, 221.1328125);
  }
  // note d#/e| octave 8
  if(strNote == "112") {
    analogWrite(3, 223.125);
  }
  // note e octave 8
  if(strNote == "113") {
    analogWrite(3, 225.1171875);
  }
  // note f octave 8
  if(strNote == "114") {
    analogWrite(3, 227.109375);
  }
  // note f#/g| octave 8
  if(strNote == "115") {
    analogWrite(3, 229.1015625);
  }
  // note g octave 8
  if(strNote == "116") {
    analogWrite(3, 231.09375);
  }
  // note g#/a| octave 8
  if(strNote == "117") {
    analogWrite(3, 233.0859375);
  }
  // note a octave 8
  if(strNote == "118") {
    analogWrite(3, 235.078125);
  }
  // note a#/b| octave 8
  if(strNote == "119") {
    analogWrite(3, 237.0703125);
  }
  // note b octave 8
  if(strNote == "120") {
    analogWrite(3, 239.0625);
  }
  // note c octave 9
  if(strNote == "121") {
    analogWrite(3, 241.0546875);
  }
  // note c#/d| octave 9
  if(strNote == "122") {
    analogWrite(3, 243.046875);
  }
  // note d octave 9
  if(strNote == "123") {
    analogWrite(3, 245.0390625);
  }
  // note d#/e| octave 9
  if(strNote == "124") {
    analogWrite(3, 247.03125);
  }
  // note e octave 9
  if(strNote == "125") {
    analogWrite(3, 249.0234375);
  }
  // note f octave 9
  if(strNote == "126") {
    analogWrite(3, 251.015625);
  }
  // note f#/g| octave 9
  if(strNote == "127") {
    analogWrite(3, 253.0078125);
  }
  // note f octave 9
  if(strNote == "128") {
    analogWrite(3, HIGH);
  }


}
void setup() {
  // put your setup code here, to run once:
  // starts serial connection at 57600 baud
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
