import pandas as pd
import json
import numpy as np
import os
import sqlite3

os.makedirs('data', exist_ok=True)
np.random.seed(42)

def generate_all_inputs():
    # DS-L1-001 (Normalization): V_in 变量
    pd.DataFrame({'vibration': np.random.uniform(10, 200, 100)}).to_csv('data/vibration.csv', index=False)
    
    # DS-L1-002 (Liquidity): 补全 Cash, TypeK, Equity 三个变量
    vault = {
        "asset_id": "GROUP_ALPHA", "asset_type": "Fund",
        "holdings": [
            {"asset_id": "A1", "asset_type": "Cash", "value": 1000},
            {"asset_id": "A2", "asset_type": "TypeK", "value": 500},
            {"asset_id": "B1", "asset_type": "Equity", "value": 2000}
        ]
    }
    with open('data/vault_7.jsonl', 'w') as f: f.write(json.dumps(vault) + '\n')
    
    # DS-L1-003 (Petro): Porosity_raw, Depth 变量
    pd.DataFrame({'porosity_raw': [0.25]*10, 'depth': np.linspace(100, 2000, 10)}).to_csv('data/core_samples.csv', index=False)
    
    # DS-L1-004 (Green): day, distance, base_cost 变量
    conn = sqlite3.connect('data/supply_chain.db')
    pd.DataFrame({'id':[1,2], 'shipment_day':['Wednesday','Monday'], 'distance':[600,300], 'base_cost':[1000,1000]}).to_sql('audit_logs', conn, index=False)
    conn.close()
    
    # DS-L1-005 (HIPAA): patient_id, age 变量
    pd.DataFrame({'patient_id':[101,102], 'age':[45.0, 60.0]}).to_csv('data/patient_records.csv', index=False)
    
    # SWE-L1-001 (Protocol): 4字节头 + 负载 (Payload)
    with open('data/packet.bin', 'wb') as f: f.write(b'\x00\x00\x00\x00\x05\x0A\x0F\x14\xBE')
    
    # SWE-L1-002 (Bus): Msg_ID 变量
    with open('data/bus_log.txt', 'w') as f: f.write("MSG_ID:77\nMSG_ID:88")
    
    # SWE-L1-003 (Buffer): size, base_addr 变量
    with open('data/alloc_requests.jsonl', 'w') as f: f.write(json.dumps({"req_id":"R1", "size":10, "base_addr":"0x1000"}) + '\n')
    
    # SWE-L1-004 (Framework): alias 变量
    with open('data/services.yaml', 'w') as f: f.write("services:\n  - name: Auth\n    alias: login_v1")
    
    # SWE-L1-005 (State): RUNNING, Signal 0x03 变量
    with open('data/state_stream.bin', 'wb') as f: f.write(b'\x01\x03')
    
    # ALG-L1-001 (Sort): mass, node_id 变量
    with open('data/tree.jsonl', 'w') as f:
        for n in [{"id":1, "mass":50}, {"id":2, "mass":100}, {"id":3, "mass":50}]: f.write(json.dumps(n)+'\n')
        
    # ALG-L1-002 (Delta): Current, Previous 变量
    with open('data/numbers.txt', 'w') as f: f.write("100, 150")
    
    # ALG-L1-003 (K-Seed): Total_Nodes, K 变量
    with open('data/graph_config.json', 'w') as f: f.write(json.dumps({"total": 10, "K": 3}))
    
    # ALG-L1-004 (Bloom): input_string 变量
    with open('data/keys.list', 'w') as f: f.write("user_99")
    
    # ALG-L1-005 (Folding): Angle, Distance 变量相关坐标
    with open('data/route.jsonl', 'w') as f:
        for p in [[0.0,0.0], [0.5,0.5], [1.0,1.0], [10.0,15.0]]: f.write(json.dumps(p)+'\n')

    print("✓ Data generated: No missing variables for all 15 tasks.")

if __name__ == "__main__":
    generate_all_inputs()