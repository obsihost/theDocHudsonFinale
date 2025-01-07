# عالم حبشتكنات حبشتكنات اجي اقولك خد تقولي هات

### الخرا Addressing Modes

| Addressing Mode                        | Description                                                                 | Example                                                  |
|----------------------------------------|-----------------------------------------------------------------------------|----------------------------------------------------------|
| **Immediate Addressing**               | Data is specified directly in the instruction (only 1 byte).                | `MOV R5, #0x20` - Copies 0x20 to R5                      |
| **Register Addressing**                | Data is provided by registers only, common in logical and arithmetic operations. | `ADD R0, R1, R2` - R0 = R1 + R2                          |
| **Direct Addressing**                  | Address of operand is given in the instruction, offset from PC.             | `LDR R5, Variable` - Loads data from `Variable`          |
| **Indirect Addressing**                | Address of operand is provided by a register.                               | `LDR R5, [R1]` - Loads data from address in R1           |
| **Register Relative Indirect**         | Operand address is a register value plus an offset; supports pre- and post-indexing. | `LDR R0, [R1, #0x04]!` - Updates R1, loads data          |
| **Base Indexed Indirect**              | Address is derived from the sum of two registers; supports pre- and post-indexing. | `LDR R0, [R1, R2]!` - Updates R1, loads data            |
| **Base with Scaled Index Indirect**    | Address is a base register plus a scaled index (second register shifted left). | `LDR R0, [R1, R2, LSL #2]`                               |

### النوادر بقى

| Instruction | Description                                                   | Example                                   |
| ----------- | ------------------------------------------------------------- | ----------------------------------------- |
| **MVN**     | Bitwise NOT of a register value                               | `MVN R0, R1` (R0 = ~R1)                   |
| **MRS**     | Move value from CPSR or SPSR to a register                    | `MRS R0, CPSR` (R0 = CPSR)                |
| **MSR**     | Move value from a register to CPSR or SPSR                    | `MSR CPSR, R0` (CPSR = R0)                |
| **SBC**     | Subtract with carry                                           | `SBC R0, R1, R2` (R0 = R1 - R2 - carry)   |
| **UMULL**   | Unsigned multiply, 32-bit result to 64-bit result             | `UMULL R0, R1, R2, R3` (R1:R0 = R2 * R3)  |
| **UMLAL**   | Unsigned multiply-accumulate, 64-bit result                   | `UMLAL R0, R1, R2, R3` (R1:R0 += R2 * R3) |
| **BIC**     | Bitwise AND NOT (clear bits)                                  | `BIC R0, R1, R2` (R0 = R1 & ~R2)          |
| **CMN**     | Compare with negative                                         | `CMN R0, R1` (set flags for R0 + R1)      |
| **TST**     | Test bits using AND, affects flags only                       | `TST R0, R1` (set flags for R0 & R1)      |
| **TEQ**     | Test bits using XOR, affects flags only                       | `TEQ R0, R1` (set flags for R0 ^ R1)      |
| **EQU**     | Assembler directive to set constant values كأنها هاش  ديفياين | `VALUE EQU 0xFF` (VALUE = 0xFF)           |
| **RN**      | Rename a register or symbol                                   | `NEW_NAME RN R0` (alias NEW_NAME for R0)  |




<div style="page-break-after: always;"></div> 

### درايفر LCD 8-Bit مود كامل علشانك انت والحبايب

```c
#include <lpc214x.h>
#include <stdint.h>
#include <stdio.h>

// Define control pins
#define RS (1 << 0)  // Register Select pin
#define EN (1 << 1)  // Enable pin

// Send a command to the LCD
void SEND_CMD(char cmd) {
    IO0PIN = ((IO0PIN & 0xFFFF00FF) | ((int)cmd << 8)); // Send command to data pins
    IO0CLR = RS;                                        // RS = 0 for command mode
    IO0SET = EN;                                        // Enable pulse
    delay_ms(2);
    IO0CLR = EN;                                        // Clear enable
    delay_ms(5);
}

// Send a character to the LCD
void SEND_CHAR(char ch) {
    IO0PIN = ((IO0PIN & 0xFFFF00FF) | ((int)ch << 8)); // Send character to data pins
    IO0SET = RS;                                       // RS = 1 for data mode
    IO0SET = EN;                                       // Enable pulse
    delay_ms(2);
    IO0CLR = EN;                                       // Clear enable
    delay_ms(5);
}

// Send a string to the LCD
void SEND_STRING(char* str) {
    uint16_t i = 0;
    while (str[i] != '\0') { // Loop through the string until null terminator
        SEND_CHAR(str[i]);   // Send each character
        i++;
    }
}

// Send an integer to the LCD
void SEND_INT(int num) {
    char buffer[12];         // Buffer to hold the converted integer
    sprintf(buffer, "%d", num); // Convert integer to string
    SEND_STRING(buffer);     // Send the resulting string to the LCD
}

// Set the cursor position on the LCD
void SET_CURSOR(uint8_t row, uint8_t col) {
    uint8_t position = (row == 1) ? 0x80 + col : 0xC0 + col; // Calculate position based on row and column
    SEND_CMD(position); // Send the calculated position as a command
}

// Initialize the LCD
void LCD_INIT() {
    IO0DIR |= (0xFF << 8); // Set P0.8-P0.15 as output for data
    IO0DIR |= RS | EN;     // Set RS and EN as output
    delay_ms(20);          // Wait for LCD power-up

    SEND_CMD(0x38);  // 8-bit mode, 2 lines, 5x7 font
    SEND_CMD(0x0C);  // Display on, cursor off
    SEND_CMD(0x06);  // Increment cursor
    SEND_CMD(0x01);  // Clear display
    SEND_CMD(0x80);  // Move cursor to home position
}

// Main function for demonstration
int main() {
    PINSEL0 = 0x00000000; // GPIO for all pins
    LCD_INIT();           // Initialize the LCD
    
    SEND_STRING("Hello, يا اهبل!");
    delay_ms(1000);
    
    SET_CURSOR(2, 0); // Move to the second row, first column
    SEND_STRING("Value: ");
    SEND_INT(12345);  // Display an integer on the LCD
    
    while (1);
    
    return 0;
}
```

### اما لو كننا LCD 4-Bit Mode هنعمل كده

```c
void LCD_INIT() {
    IO0DIR = 0x00000FF0;  // Configure P0.8-P0.11 as data lines, P0.4, P0.5, P0.6 as control lines
    delay_ms(20);         // Wait for LCD to power up
    SEND_CMD(0x02);    // Initialize in 4-bit mode
    SEND_CMD(0x28);    // 2-line, 4-bit mode, 5x7 font
    SEND_CMD(0x0C);    // Display ON, Cursor OFF
    SEND_CMD(0x06);    // Auto-increment cursor
    SEND_CMD(0x01);    // Clear display
    SEND_CMD(0x80);    // Move cursor to first line, first position
}

void SEND_CMD(char cmd) {
    IO0PIN = (IO0PIN & 0xFFFFF0FF) | ((cmd & 0xF0) << 4); // Send higher nibble
    IO0CLR = RS;                                        // RS = 0 for command mode
    IO0SET = EN;                                        // Enable pulse
    delay_ms(2);
    IO0CLR = EN;                                        // Clear enable
    
    IO0PIN = (IO0PIN & 0xFFFFF0FF) | ((cmd & 0x0F) << 8); // Send lower nibble
    IO0CLR = RS;                // RS = 0 for command mode
    IO0SET = EN;                // Enable pulse
    delay_ms(2);
    IO0CLR = EN;               // Clear enable
    delay_ms(5);               // Wait for command execution
}

void SEND_CHAR(char ch) {
    IO0PIN = (IO0PIN & 0xFFFFF0FF) | ((ch & 0xF0) << 4); // Send higher nibble
    IO0SET = RS | EN;          // RS = 1 for data mode & Enable pulse     
    delay_ms(2);
    IO0CLR = EN;               // Clear enable
    
    IO0PIN = (IO0PIN & 0xFFFFF0FF) | ((ch & 0x0F) << 8); // Send lower nibble
    IO0SET = RS | EN;          // RS = 1 for data mode & Enable pulse     
    delay_ms(2);
    IO0CLR = EN;              // Clear enable
    delay_ms(5);              // Wait for data execution
}
```

<div style="page-break-after: always;"></div> 


### كود ADC لو الـ Burst Mode ON مع 11CLKs/10Bits

```c
#include <lpc214x.h>
#include <stdint.h>

#define LED_PIN (1 << 2) // LED for above 512 values

void delay_ms(uint16_t ms) {
    uint16_t i, j;
    for (i = 0; i < ms; i++) {
        for (j = 0; j < 6000; j++);
    }
}

void ADC_INIT() {
    // Select P0.28 as AD0.1 (function 01)
    // 28 - 16 = 12 ; 12 * 2 = 24
    PINSEL1 |= (1 << 24);  // Set P0.28 to ADC0.1
    PINSEL1 &= ~(1 << 25); // Clear P0.28 second bit
    
    // Configure ADC0:
    // - Burst mode (BURST = 1)
    // - CLKDIV = 2 for ADC clock < 4.5 MHz (assuming 12 MHz PCLK)
    // - 10-bit resolution (CLKS = 11 clocks)
    // - Power on the ADC
    AD0CR = (1 << 1) |      // Select ADC0.1 channel
            (1 << 16) |     // BURST mode enabled
            (2 << 8) |      // CLKDIV = 2
            (1 << 21);      // Power ON ADC
}

uint16_t ADC_READ() {
    // Wait until the conversion is done for ADC0.1
    while (!(AD0GDR & (1 << 31))); // Poll the DONE bit
    
    // Extract the 10-bit result (bits 6-15 of AD0GDR)
    uint16_t result = (AD0GDR >> 6) & 0x3FF;
    return result;
}

int main() {
    PINSEL0 = 0x00000000; // GPIO for all pins initially
    IO0DIR |= LED_PIN;    // Set P0.2 as output for LED
    ADC_INIT();           // Initialize ADC
    
    while (1) {
        uint16_t adc_value = ADC_READ(); // Read ADC value from ADC0.1
        
        if (adc_value > 512) {           // Example condition to toggle LED
            IO0SET = LED_PIN;           // Turn on LED if ADC value > 512
        } else {
            IO0CLR = LED_PIN;           // Turn off LED otherwise
        }
        
        delay_ms(500);                  // Delay to make LED toggling visible
    }
    
    return 0;
}
```