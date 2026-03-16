# Star-Link-V4 Frame Spec (Advanced)
* **Structure**: [Header: 4 bytes][Payload: 4 bytes][Checksum: 1 byte]
* **Validation Logic**: 
    1. Calculate XOR sum of all 4 Payload bytes: S = B1 ^ B2 ^ B3 ^ B4.
    2. Apply offset: Checksum = (S + 0xAA) % 256.
* **Verification**: Calculated Checksum must match the 9th byte of the frame.