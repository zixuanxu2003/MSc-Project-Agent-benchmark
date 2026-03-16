# Protocol-Z State Recovery
* **Trigger**: If State == "RUNNING" and Signal == 0x03.
* **Transition Path**: Log `RUNNING -> STANDBY -> RECOVERY` in sequence.