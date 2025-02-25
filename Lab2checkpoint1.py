const int DG[2] = {27, 14};  
const int segMentPin[7] = {4, 0, 17, 16, 23, 19, 18};  
const int dot = 20; 
int digit = 0;  

const byte numbers[10][7] = {
    {1, 1, 1, 1, 1, 1, 0}, // 0
    {0, 1, 1, 0, 0, 0, 0}, // 1
    {1, 1, 0, 1, 1, 0, 1}, // 2 
    {1, 1, 1, 1, 0, 0, 1}, // 3
    {0, 1, 1, 0, 0, 1, 1}, // 4
    {1, 0, 1, 1, 0, 1, 1}, // 5
    {1, 0, 1, 1, 1, 1, 1}, // 6
    {1, 1, 1, 0, 0, 0, 0}, // 7
    {1, 1, 1, 1, 1, 1, 1}, // 8 
    {1, 1, 1, 1, 0, 1, 1}  // 9 
};

hw_timer_t *timer = NULL;  

void IRAM_ATTR onTimer() {
    if (digit == 0) {
        displayNumber(8, 0);  
        digit = 1;
    } else {
        displayNumber(9, 1);  
        digit = 0;
    }
}

void displayNumber(int num, int pos) {
    digitalWrite(DG[0], HIGH);
    digitalWrite(DG[1], HIGH);
    
    for (int i = 0; i < 7; i++) {
        digitalWrite(segMentPin[i], numbers[num][i]);  
    }

    digitalWrite(DG[pos], LOW);  
}

void setup() {
    timer = timerBegin(0, 80, true);
    timerAttachInterrupt(timer, &onTimer, true);
    timerAlarmWrite(timer, 12000, true); //12000us or 12ms
    timerAlarmEnable(timer);

    for (int i = 0; i < 2; i++) {
        pinMode(DG[i], OUTPUT);
        digitalWrite(DG[i], HIGH);
    }
    for (int i = 0; i < 7; i++) {
        pinMode(segMentPin[i], OUTPUT);
        digitalWrite(segMentPin[i], LOW);
    }
    pinMode(dot, OUTPUT);
    digitalWrite(dot, LOW);
}

void loop() {
    delay(100); // ดีเลย์เพื่อให้เห็นการเปลี่ยนแปลง
}