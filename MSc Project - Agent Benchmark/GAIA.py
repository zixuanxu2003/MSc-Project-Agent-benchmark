from datasets import load_dataset
from huggingface_hub import login

ds = load_dataset("gaia-benchmark/GAIA", "2023_all")

print(ds)

for split_name in ds.keys():
    file_name = f"gaia_{split_name}.csv"

    df = ds[split_name].to_pandas()

    ds[split_name].to_csv(file_name, index = False)
    print(f"已保存: {file_name}")