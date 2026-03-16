# Internal-Bus Message Routing
* **Logic**: `Target_Node = (Hash(Msg_ID) ^ Secret_Key) % 8`
* **Reference**: Secret_Key value is located in kb/swe/security_keys.md.