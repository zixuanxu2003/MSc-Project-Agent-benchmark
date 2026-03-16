import os

# 定义文件夹路径
base_path = "kb"
folders = ["ds", "swe", "algo"]

# 定义 15 个任务的 KB 内容 (单行线性逻辑)
kb_content = {
    "ds/sensor_specs.md": """# X-Relay Sensor Normalization Standard
* **Formula**: `V_out = ((V_in - min(V)) / (max(V) - min(V))) * 0.85 + 0.15`
* **Constraint**: Output must range strictly between 0.15 and 1.0.
* **Target Column**: `vibration_amplitude`.""",

    "ds/finance_policy.md": """# Alpha-Liquidity Calculation Protocol
* **Formula**: `Liquidity = (Cash * 1.0) + (TypeK * 0.72) + (Equity * 0.45)`
* **Recursion**: If asset_type is 'Fund', sum its sub-assets liquidity. Max depth: 2.
* **Output**: Save as .jsonl with asset_id and liquidity_score.""",

    "ds/petro_manual.md": """# Petro-Physics Compaction Correction
* **Formula**: `Porosity_adj = Porosity_raw * (1 - 0.02 * log(Depth))`
* **Note**: Use natural logarithm (ln). Depth is in meters.""",

    "ds/green_standard.md": """# Green-Standard Supply Chain Audit
* **Rule**: If `shipment_day == "Wednesday"` and `distance > 500`, then `Total_Cost = Base_Cost * 1.12`.
* **Otherwise**: `Total_Cost = Base_Cost`.""",

    "ds/hipaa_internal.md": """# Internal HIPAA De-identification
* **Method**: Laplacian Noise with Epsilon = 0.1.
* **Requirement**: MUST call `numpy.random.seed(42)` before noise generation for consistency.""",

    "swe/v4_frame_spec.md": """# Star-Link-V4 Frame Spec (Advanced)
* **Structure**: [Header: 4 bytes][Payload: 4 bytes][Checksum: 1 byte]
* **Validation Logic**: 
    1. Calculate XOR sum of all 4 Payload bytes: S = B1 ^ B2 ^ B3 ^ B4.
    2. Apply offset: Checksum = (S + 0xAA) % 256.
* **Verification**: Calculated Checksum must match the 9th byte of the frame.""",

    "swe/internal_bus.md": """# Internal-Bus Message Routing
* **Logic**: `Target_Node = (Hash(Msg_ID) ^ Secret_Key) % 8`
* **Reference**: Secret_Key value is located in kb/swe/security_keys.md.""",

    "swe/security_keys.md": """# Internal Security Keys
* **Secret_Key**: `0xAF` (Use for XOR-hash routing logic).""",

    "swe/buffer_logic.md": """# Buffer Alignment & Mirroring
* **Alignment**: `Aligned_Size = ((Requested_Size + 31) // 32) * 32`
* **Mirror**: `Shadow_Addr = Primary_Addr + 32768` (0x8000).""",

    "swe/framework_v5.md": """# Framework-V5 Registration
* **Pattern**: Scan for `@InternalRegister(role="service")` decorator.
* **Action**: Extract `alias` parameter and save to service_registry.txt.""",

    "swe/protocol_z.md": """# Protocol-Z State Recovery
* **Trigger**: If State == "RUNNING" and Signal == 0x03.
* **Transition Path**: Log `RUNNING -> STANDBY -> RECOVERY` in sequence.""",

    "algo/traversal_standards.md": """# Gravity-Sort Priority
* **Rule 1**: Sort by `mass` attribute (Descending).
* **Rule 2**: If mass is equal, sort by `node_id` (Ascending).""",

    "algo/delta_varint_spec.md": """# Delta-VarInt Encoding
* **Logic**: `Encoded_Val = ~(Current_Val - Previous_Val)`
* **Storage**: Save as signed 16-bit binary (little-endian).""",

    "algo/balanced_cut.md": """# K-Seed Partitioning
* **Seed_Index**: `floor(Total_Nodes / K)`
* **Expansion**: Select clusters with the smallest edge-cut ratio.""",

    "algo/bloom_config.md": """# Salted Bloom Filter
* **Params**: m = 1024, k = 3.
* **Salting**: Append `"salt_v1"` to the end of the string before hashing.""",

    "algo/poly_folding.md": """# Poly-Folding Path Reduction
* **Condition**: `Angle_Deviation < 8.5` degrees AND `Segment_Distance < 1.5`.
* **Note**: `Angle_Deviation = 180 - Interior_Angle`."""
}

# 创建文件夹和文件
for folder in folders:
    os.makedirs(os.path.join(base_path, folder), exist_ok=True)

for file_path, content in kb_content.items():
    full_path = os.path.join(base_path, file_path)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Successfully generated 15+ KB files in /kb directory.")