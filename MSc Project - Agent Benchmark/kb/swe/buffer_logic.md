# Buffer Alignment & Mirroring
* **Alignment**: `Aligned_Size = ((Requested_Size + 31) // 32) * 32`
* **Mirror**: `Shadow_Addr = Primary_Addr + 32768` (0x8000).