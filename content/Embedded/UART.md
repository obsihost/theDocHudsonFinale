## LPC2148 UART

### UART Features

#### Dual UARTs
- **UART0 and UART1**:
  - LPC2148 microcontroller features two inbuilt UARTs.
  - Enables connection with devices like GSM, GPS, or Bluetooth modules.
#### UART1 vs. UART0
- Both have similar features except:
  - **UART1** includes a modem interface.
#### Features of UART0
- **16-Byte FIFOs**: Separate buffers for transmit and receive operations.
- **Fractional Baud Rate Generator**: Supports autobauding.
- **Software Flow Control**: Controlled via the TXEN bit.
#### Features of UART1
- Inherits features of UART0 and the Modem Interface.
#### Modem Interface in UART1
The modem interface in UART1 enhances communication between the UART and external modems. It supports standard modem control signals, allowing seamless management of connections, data transfer, and readiness states. These signals are vital for reliable and efficient data communication.
##### Related Pins
- **RTS1 (Request to Send)**: An output signal from UART1 to the modem, indicating a request to initiate data transmission. Active low.
- **CTS1 (Clear to Send)**: An input signal from the modem to UART1, indicating the modem is ready to accept data. Active low.
- **DTR1 (Data Terminal Ready)**: An output signal showing UART1's readiness to establish a communication link with the modem. Active low.
- **DSR1 (Data Set Ready)**: An input signal from the modem, indicating it is ready to establish a link with UART1. Active low.
- **DCD1 (Data Carrier Detect)**: Indicates that the modem has successfully established a communication link with UART1. Active low.
- **RI1 (Ring Indicator)**: Signals the detection of a telephone ring signal by the modem. Active low\.s:
  - **Hardware Flow Control**: Auto-CTS/RTS flow control.
  - **Standard Modem Interface Signals**: Enhanced modem communication features.

#### UART Pins
##### UART0:
- **TXD0**: Transmit pin.
- **RXD0**: Receive pin.
##### UART1:
- **TXD1**: Transmit pin.
- **RXD1**: Receive pin.
- **RTS1**: Request to send.
- **CTS1**: Clear to send.
- **DTR1**: Data terminal ready.
- **DSR1**: Data set ready.
- **DCD1**: Data carrier detect.
- **RI1**: Ring indicator.

### LPC2148 UART Registers

#### 1. **U0RBR** (UART0 Receive Buffer Register)
- **Type**: 8-bit Read-only.
- **Purpose**: Stores the oldest byte of data received.
- **Details**:
  - Holds data fetched from the UART0 RX FIFO.
  - If fewer than 8 bits are received, unused MSBs are padded with zeroes.
  - Accessible only when **DLAB** is `0`.
#### 2. **U0THR** (UART0 Transmit Holding Register)

- **Type**: 8-bit Write-only.
- **Purpose**: Accepts data for transmission.
- **Details**:
  - Data written here enters the UART0 TX FIFO for transmission.
  - Accessible only when **DLAB** is `0`.
#### 3. **U0DLL** and **U0DLM** (Divisor Latch Registers)

- **Type**: 8-bit Read/Write.
- **Purpose**: Configures the baud rate.
- **Details**:
  - Divisor Latch is a combination of `U0DLL` (LSB) and `U0DLM` (MSB).
  - Formula:
$$\displaystyle \text{Baud Rate} = \frac{\text{PCLK}}{16 \times (256 \times \text{U0DLM} + \text{U0DLL})}$$
  - Requires **DLAB** to be `1` to modify.
#### 4. **U0FDR** (UART0 Fractional Divider Register)

- **Type**: 32-bit Read/Write.
- **Purpose**: Fine-tunes the baud rate using fractional values.
- **Details**:
  - Divides the clock by a multiplier (MULVAL) and an additive value (DIVADDVAL).
  - Formula:
$$\displaystyle \text{UART0 Baud Rate} = \frac{\text{PCLK}}{16 \times (256 \times \text{U0DLM} + \text{U0DLL}) \times \left(1 + \frac{\text{DIVADDVAL}}{\text{MULVAL}}\right)}$$
  - Constraints:
    - `MULVAL` must be >= 1.
    - `DIVADDVAL` must be in the range 0-15.
  - Avoid modifying this register during transmission or reception to prevent data corruption.
#### 5. **U0IER** (UART0 Interrupt Enable Register)
- **Type**: 32-bit Read/Write.
- **Purpose**: Enables or disables specific UART0 interrupt sources.
- **Details**:
  - **Bit 0**: Receive Data Available (RBR) interrupt enable.
  - **Bit 1**: Transmit Holding Register Empty (THRE) interrupt enable.
  - **Bit 2**: Receive Line Status (RX) interrupt enable.
  - **Bits 8-9**: Auto-baud interrupt enable (ABEO and ABTO).
<div style="page-break-after: always;"></div> 
#### 6. **U0IIR** (UART0 Interrupt Identification Register)
- **Type**: 32-bit Read-only.
- **Purpose**: Identifies the source and priority of pending interrupts.
- **Details**:
  - **Bit 0**: Interrupt pending (0 = pending, 1 = none).
  - **Bits 1-3**: Interrupt identification.
    - `011`: Receive Line Status.
    - `010`: Receive Data Available.
    - `110`: Character Timeout Indicator.
    - `001`: THRE interrupt.
  - **Bits 6-7**: FIFO Enable.
  - **Bit 8**: Auto-baud has finished successfully (if ABEO is enabled)
  - **Bit 9**: Auto-baud has timed out (if ABTO is enabled)
#### 7. **U0LCR** (UART0 Line Control Register)
- **Type**: 8-bit Read/Write.
- **Purpose**: Configures the format of transmitted/received data.
- **Details**:
  - **Bits 0-1**: Word length select.
    - `00`: 5-bit character length.
    - `01`: 6-bit character length.
    - `10`: 7-bit character length.
    - `11`: 8-bit character length.
  - **Bit 2**: Stop bit select (1 or 2 stop bits).
	- `0`: 1 stop bit.
    - `1`: 2 stop bit.
  - **Bit 3**: Parity enable.
  - **Bits 4-5**: Parity select (odd, even, forced).
	- `00`: Odd Parity.
    - `01`: Even Parity.
    - `10`: Forced `1` Stick Parity (يعني ثابته).
    - `11`: Forced `0` Stick Parity.
  - **Bit 6**: Break control (enable/disable).
  - **Bit 7**: Divisor Latch Access Bit (DLAB).
#### 8. **U0LSR** (UART0 Line Status Register)
- **Type**: 8-bit Read-only.
- **Purpose**: Provides status information for UART0 RX and TX blocks.
- **Details**:
  - **Bit 0**: Receiver Data Ready (`1` if `U0RBR` contains data`.
  - **Bit 1**: Overrun Error.
  - **Bit 2**: Parity Error.
  - **Bit 3**: Framing Error.
  - **Bit 4**: Break Interrupt.
  - **Bit 5**: THR Empty (`1` if `U0THR` is empty).
  - **Bit 6**: Transmitter Empty (`0` if `U0THR` or/and `U0TSR` contains data).
  - **Bit 7**: Error in RX FIFO.
<div style="page-break-after: always;"></div> 
#### 9. **U0TER** (UART0 Transmit Enable Register)
- **Type**: 8-bit Read/Write.
- **Purpose**: Enables or disables the UART0 transmitter.
- **Details**:
  - **Bit 7**: TX Enable (0 = disabled, 1 = enabled).
  - Transmission halts when TXEN is cleared but completes the current character being transmitted.

### Code Example

#### Steps to Initialize UART0

1. **Configure UART0 Pins**:
   - Use the PINSEL0 register to set P0.0 as TXD0 (transmit) and P0.1 as RXD0 (receive).
   - Example:
     ```c
     PINSEL0 |= 0x00000005; // Enable UART0 Rx0 and Tx0 pins
     ```

2. **Set Frame Format**:
   - Use the U0LCR (UART Line Control Register) to configure the frame format.
   - Example:
     ```c
     U0LCR = 0x83; // DLAB = 1, 8-bit character length, 1 stop bit
     ```

3. **Set Baud Rate**:
   - Configure the Divisor Latch Registers (U0DLL and U0DLM) to set the desired baud rate.
   - Using the formula for baud rate calculation:

$$\text{Baud Rate} = \frac{PCLK}{16 \times (256 \times U0DLM + U0DLL)}$$

     For PCLK = 15 MHz and baud rate = 9600:

$$9600 = \frac{15000000}{16 \times (256 \times U0DLM + U0DLL)}$$

     Simplifying:
 $$
     256 \times U0DLM + U0DLL = \frac{15000000}{16 \times 9600} \approx 97.65
     $$

     Since 97.65 is close to 97, we set:
   - Example:
     ```c
     U0DLL = 97; // Example value for 9600 baud rate with 15MHz PCLK
     U0DLM = 0;
     U0LCR = 0x03; // DLAB = 0
     ```

4. **Enable UART0 Transmitter**:
   - Use the U0TER register to enable transmission.
   - Example:
     ```c
     U0TER = 0x80; // Enable transmission
     ```
<div style="page-break-after: always;"></div> 
#### Transmitting Data
To send a single character, write it to the U0THR register and wait for the THRE bit in U0LSR to be set.
##### Example Function:
```c
void UART0_TxChar(char ch) {
    U0THR = ch; // Write character to Transmit Holding Register
    while (!(U0LSR & 0x20)); // Wait for THRE bit to be set
}
```
#### Receiving Data
To receive a character, monitor the RDR bit in the U0LSR register and read from the U0RBR register when data is available.
##### Example Function:
```c
char UART0_RxChar(void) {
    while (!(U0LSR & 0x01)); // Wait for RDR bit to be set
    return U0RBR; // Return received character
}
```
#### Complete Example: Echoing Received Data

```c
#include <LPC214x.h>

void UART0_Init(void) {
    PINSEL0 |= 0x00000005; // Configure P0.0 as TXD0 and P0.1 as RXD0
    U0LCR = 0x83;          // DLAB = 1, 8-bit data, 1 stop bit
    U0DLL = 97;            // Set baud rate to 9600 (example value)
    U0DLM = 0;
    U0LCR = 0x03;          // DLAB = 0
    U0TER = 0x80;          // Enable transmission
}

void UART0_TxChar(char ch) {
    U0THR = ch;
    while (!(U0LSR & 0x20));
}

char UART0_RxChar(void) {
    while (!(U0LSR & 0x01));
    return U0RBR;
}

int main(void) {
    UART0_Init();
    char receivedChar;
    while (1) {
        receivedChar = UART0_RxChar(); // Receive character
        UART0_TxChar(receivedChar);   // Echo back received character
    }
}
```

