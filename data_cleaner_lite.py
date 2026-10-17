#!/usr/bin/env python3
"""data_cleaner_lite.py - LITE: exact-duplicate removal, whitespace trim, empty-row removal, blanks report (CSV only).
Full version adds name/email/date/currency normalization, key-column dedupe, Excel in/out, parse-issue log.
Created with AI assistance, tested on sample data. Requires pandas."""
import sys, pandas as pd
from pathlib import Path
if len(sys.argv)<2: sys.exit("usage: python data_cleaner_lite.py input.csv")
src=Path(sys.argv[1]); df=pd.read_csv(src,dtype=str,encoding="utf-8-sig"); n=len(df)
df=df.apply(lambda s:s.str.strip().replace("",pd.NA)).dropna(how="all"); e=n-len(df)
d=df.duplicated(); df=df[~d]
out=src.with_name(src.stem+"_clean.csv"); df.to_csv(out,index=False)
print(f"rows in {n}, empty removed {e}, exact duplicates removed {int(d.sum())}, rows out {len(df)}")
print("Blanks per column:"); print(df.isna().sum().to_string()); print("Saved:",out)
