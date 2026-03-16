# X-Relay Sensor Normalization Standard
* **Formula**: `V_out = ((V_in - min(V)) / (max(V) - min(V))) * 0.85 + 0.15`
* **Constraint**: Output must range strictly between 0.15 and 1.0.
* **Target Column**: `vibration_amplitude`.