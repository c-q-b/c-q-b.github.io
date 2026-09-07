# 陈庆标 · 神经工程设备作品集

纯 HTML / CSS / JavaScript 作品展示页，无需安装依赖或构建。页面顺序：

- 多通道脑电：背景、64 通道系统研发成果、硬件、Alpha / SSVEP 实验及演示视频。
- 经颅电刺激仪：背景、4 通道高电流高频原型机成果、监测与保护、实物和演示视频。
- 个人简介与技术能力。

工程指标和个人经历根据提供的简历整理，实验图仅展示素材中已有结果。64 通道是设备规格，Alpha / SSVEP 图中展示的是 Oz、O1、O2 三个通道。电刺激部分展示工程开发成果，不作临床疗效推断。

## 本地预览

直接打开 `index.html` 即可浏览。为避免浏览器对本地资源的限制，也可以在本目录运行：

```powershell
python -m http.server 8000
```

然后访问 `http://localhost:8000`。

## 部署

远程仓库：`https://github.com/c-q-b/c-q-b.github.io.git`。后续修改可运行：

```powershell
python tools/check_site.py
git add index.html styles.css script.js README.md assets/images/*.webp assets/video/*.mp4
git commit -m "Update neurotechnology portfolio"
git push -u origin main
```

GitHub 仓库的 **Settings → Pages → Build and deployment** 选择 **Deploy from a branch**，分支 **main**，目录 **/ (root)**。GitHub Pages 生效后访问 `https://c-q-b.github.io/`。`.nojekyll` 保证静态资源直接发布。

## 目录

```text
assets/
  images/        网页优化后的实验图片
  video/         脑电与电刺激设备演示视频
tools/
  prepare_assets.py
  check_site.py
index.html
styles.css
script.js
```

所有页面链接使用相对路径，可直接打开或部署至 GitHub Pages。视频使用原生控件且不自动播放、不预加载；图片使用 WebP 并支持点击放大。

简历 PDF 仅作为内容来源，已通过 `.gitignore` 排除，不随网站上传；网页不展示电话、年龄等个人信息。原始 PNG 与 `.preview/` 临时文件也不上传。`eeg-experiment.webp` 沿用已有的桌面证件区域模糊处理。
