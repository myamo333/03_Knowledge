import os
import glob
import natsort
import cv2
import mmcv
from visualize_nusc import demo  # visualize_nusc.py 内の demo() を import

# ----- 設定 -----
results_file = './outputs/det/CRN_r50_256x704_128x128_4key/results_nusc.json'
infos_file = 'data/nuScenes/nuscenes_infos_val.pkl'
output_dir = './outputs/pngs'
os.makedirs(output_dir, exist_ok=True)

# ----- NuScenes mini の情報読み込み -----
infos = mmcv.load(infos_file)

# ----- 1. PNG をループで生成 -----
for idx, info in enumerate(infos):
    dump_file = os.path.join(output_dir, f'frame_{idx:03d}.png')
    print(f'Processing sample {idx} -> {dump_file}')
    demo(idx, results_file, dump_file)

# ----- 2. PNG を MP4 にまとめる -----
png_files = natsort.natsorted(glob.glob(os.path.join(output_dir, 'frame_*.png')))
if len(png_files) == 0:
    raise ValueError("PNG files not found in " + output_dir)

# 画像サイズ取得
frame = cv2.imread(png_files[0])
height, width, _ = frame.shape

# VideoWriter 初期化
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' で MP4
out = cv2.VideoWriter('output_video.mp4', fourcc, 5.0, (width, height))  # FPS=5

# PNG を順番に書き込み
for file in png_files:
    img = cv2.imread(file)
    out.write(img)

out.release()
print("MP4 動画作成完了: output_video.mp4")
