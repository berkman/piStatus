piStatus
========

Display the current IP address of a Raspberry Pi on a LCD display

Parts
--------
Standard LCD 16x2 - 
http://www.ebay.com/itm/281030305673?ssPageName=STRK:MEWNX:IT&_trksid=p3984.m1439.l2649
http://www.adafruit.com/products/181
http://www.adafruit.com/datasheets/HD44780.pdf
http://en.wikipedia.org/wiki/Hitachi_HD44780_LCD_controller

Support
--------
http://learn.adafruit.com/character-lcds

LCD Pins
--------
1. Ground
2. VCC (+3.3 to +5V)
3. Contrast adjustment (VO)
4. Register Select (RS). RS=0: Command, RS=1: Data
5. Read/Write (R/W). R/W=0: Write, R/W=1: Read
6. Clock (Enable). Falling edge triggered
7. Bit 0 (Not used in 4-bit operation)
8. Bit 1 (Not used in 4-bit operation)
9. Bit 2 (Not used in 4-bit operation)
10. Bit 3 (Not used in 4-bit operation)
11. Bit 4
12. Bit 5
13. Bit 6
14. Bit 7
15. Backlight Anode (+)
16. Backlight Cathode (-)
