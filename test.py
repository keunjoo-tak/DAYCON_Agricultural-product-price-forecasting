import glob
import multiprocessing

tsalet_files = sorted(glob("./data/public_data/train_AT_TSALET_ALL/*"))

pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
pool.map(preprocessing, tsalet_files)
pool.close()
pool.join()
