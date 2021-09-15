import pandas as pd
import numpy as np
from glob import glob
import multiprocessing
import pickle


def preprocessing(tsalet_file):
    unique_pum = [
        "배추",
        "무",
        "양파",
        "건고추",
        "마늘",
        "대파",
        "얼갈이배추",
        "양배추",
        "깻잎",
        "시금치",
        "미나리",
        "당근",
        "파프리카",
        "새송이",
        "팽이버섯",
        "토마토",
    ]

    unique_kind = ["청상추", "백다다기", "애호박", "캠벨얼리", "샤인머스캇"]

    train_dict = {"data": []}

    for sub in unique_pum:
        train_dict[f"{sub}_거래량(kg)"] = []
        train_dict[f"{sub}_가격(원/kg)"] = []

    for sub in unique_kind:
        train_dict[f"{sub}_거래량(kg)"] = []
        train_dict[f"{sub}_가격(원/kg)"] = []

    tsalet_sample = pd.read_csv(tsalet_file)
    days = sorted(tsalet_sample["SALEDATE"].unique())
    for day in days:
        train_dict["date"].append(day)

        for sub in unique_pum:
            # 날짜별, 품목별, 거래량이 0 이상인 행만 선택
            c = tsalet_sample[
                (tsalet_sample["SALEDATE"] == day) & (tsalet_sample["PUM_NM"] == sub) & (tsalet_sample["TOT_QTY"] > 0)
            ]
            if c.shape[0] == 0:
                train_dict[f"{sub}_거래량(kg)"].append(0)
                train_dict[f"{sub}_가격(원/kg)"].append(0)
            else:
                tot_amt = c["TOT_AMT"].sum().astype(float)
                tot_qty = c["TOT_QTY"].sum().astype(float)
                mean_price = tot_amt / (tot_qty + 1e-20)
                train_dict[f"{sub}_거래량(kg)"].append(tot_qty)
                train_dict[f"{sub}_가격(원/kg)"].append(mean_price)

        for sub in unique_kind:
            # 날짜별, 품종별, 거래량이 0 이상인 행만 선택
            c = tsalet_sample[
                (tsalet_sample["SALEDATE"] == day) & (tsalet_sample["KIND_NM"] == sub) & (tsalet_sample["TOT_QTY"] > 0)
            ]
            if c.shape[0] == 0:
                train_dict[f"{sub}_거래량(kg)"].append(0)
                train_dict[f"{sub}_가격(원/kg)"].append(0)
            else:
                tot_amt = c["TOT_AMT"].sum().astype(float)
                tot_qty = c["TOT_QTY"].sum().astype(float)
                mean_price = round(tot_amt / (tot_qty + 1e-20))
                tot_qty = round(tot_qty, 1)
                train_dict[f"{sub}_거래량(kg)"].append(tot_qty)
                train_dict[f"{sub}_가격(원/kg)"].append(mean_price)

    with open(f'./data/public_data/dict/{tsalet_file.split("/")[-1].split(".")[0]}.pkl', "wb") as f:
        pickle.dump(train_dict, f)


tsalet_files = sorted(glob("./data/public_data/train_AT_TSALET_ALL/*"))

pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
pool.map(preprocessing, tsalet_files)
pool.close()
pool.join()

dict_files = sorted(glob("./data/public_data/dict/*.pkl"))

train_dict_list = []
for dict_file in dict_files:
    with open(dict_file, "rb") as f:
        train_dict = pickle.load(f)
    train_dict_list.append(train_dict)


train = None

for train_dcit in train_dict_list:
    if train is None:
        train = pd.DataFrame(train_dcit)
    else:
        train = pd.concat([train, pd.DataFrame(train_dcit)])


train["date"] = train.date.astype(str).str.replace("-", "")
train["date"] = pd.to_datetime(train.date, format="%Y%m%d")


train
