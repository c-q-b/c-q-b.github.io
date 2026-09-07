# 陈庆标 · 神经工程设备作品集

纯 HTML / CSS / JavaScript 作品展示页，无需安装依赖或构建。页面顺序：

- 多通道脑电：背景、64 通道系统研发成果、硬件、闭眼 Alpha / 15 Hz SSVEP 验证方法与用途、演示视频。
- 经颅电刺激仪：背景、4 通道高电流高频原型机成果、监测与保护、实物和演示视频。

工程指标根据提供的简历整理。硬件与固件板块先介绍 ADS1299 菊花链采集板、STM32H743 数字处理板、通信接口与电源设计；区分 USB 2.0 HS 数据上传、CAN FD 命令控制及 UART 日志，并展示 USB / 5–12 V 电池和板载 DC-DC、LDO 供电结构。固件部分展示采集驱动、数据解析与 IIR 滤波、USB 上传流程，以及多设备同步、日志调试、IAP 升级恢复和低功耗管理。

Alpha / SSVEP 介绍嵌入脑电项目正文，每个实验依次展示“实验流程 → 实验结果分析 → 可以用来做什么”，采用大标题、18 px 正文和大幅结果图；参考资料可展开查看。不新增实验导航入口，不包含个人简介。图示为 Oz、O1、O2 三通道记录，不能替代 64 通道整机计量验证。SSVEP 不声称已完成多目标脑机接口；电刺激部分不作临床疗效推断。

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

所有页面链接使用相对路径，可直接打开或部署至 GitHub Pages。视频由原始 HEVC 转为 H.264 / AAC，并将 MP4 索引放在文件开头以支持快速起播；使用原生控件且不自动播放、不预加载。原视频备份保存在本地 `.preview/original-videos/`。图片使用 WebP 并支持点击放大。

简历 PDF 仅作为内容来源，已通过 `.gitignore` 排除，不随网站上传；网页不展示电话、年龄等个人信息。原始 PNG 与 `.preview/` 临时文件也不上传。`eeg-experiment.webp` 沿用已有的桌面证件区域模糊处理。
