
# How to run the analysis scripts

Each TP has a `code/` folder with a small Python script that:
- loads CSVs from `../data/`
- recomputes the key results
- writes a `*_recomputed.csv`
- (TP1) produces a calibration plot under `../figures/`

Setup:
  pip install -r requirements.txt

Run examples:
  python measurements/determining-instrument-accuracy-class-voltmeter-and-ammeter/code/tp1_analysis.py
  python measurements/resistance-measurement-by-volt-ampere-method-short-and-long-connections/code/tp2_va_analysis.py
