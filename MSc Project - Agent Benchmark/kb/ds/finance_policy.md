# Alpha-Liquidity Calculation Protocol
* **Formula**: `Liquidity = (Cash * 1.0) + (TypeK * 0.72) + (Equity * 0.45)`
* **Recursion**: If asset_type is 'Fund', sum its sub-assets liquidity. Max depth: 2.
* **Output**: Save as .jsonl with asset_id and liquidity_score.