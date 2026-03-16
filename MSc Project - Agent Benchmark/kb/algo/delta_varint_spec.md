# Delta-VarInt Encoding
* **Logic**: `Encoded_Val = ~(Current_Val - Previous_Val)`
* **Storage**: Save as signed 16-bit binary (little-endian).