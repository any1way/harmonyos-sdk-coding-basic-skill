---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-evaluate-log
title: 打印表达式
breadcrumb: 指南 > 编写与调试应用 > 应用调试 > 代码调试 > ArkTS代码调试 > 打印表达式
category: harmonyos-guides
scraped_at: 2026-06-11T15:29:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7ce4a03e43dfb9094335b4806477c36b935ec68c2013f5859891d1a93c013b5c
---

开发者可以通过Evaluate and log能力在代码执行到断点行时打印开发者指定的表达式。

1. 在需要打印表达式结果的地方设置断点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/fTTVx-sGTxqNnyKyGvd1FQ/zh-cn_image_0000002571546726.png?HW-CC-KV=V1&HW-CC-Date=20260611T072902Z&HW-CC-Expire=86400&HW-CC-Sign=CFBC1D138DBB387AB9E091FC10B9182B359160F2595ECA5D1D6BC7908B597FBC)
2. 右键断点，然后点击**More**按钮。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/VS494_z1RrW2ukpAmgqQdQ/zh-cn_image_0000002571387090.png?HW-CC-KV=V1&HW-CC-Date=20260611T072902Z&HW-CC-Expire=86400&HW-CC-Sign=4518A54AA8B9FD77BB0D22E06A020457A2742A3B572195F1F4E05795418FA703)
3. 勾选**Evaluate and log**复选框，并在下方输入框输入要打印的表达式。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/HpVHkAs7S5uaOeb1ifA3yw/zh-cn_image_0000002602066205.png?HW-CC-KV=V1&HW-CC-Date=20260611T072902Z&HW-CC-Expire=86400&HW-CC-Sign=FE01A165D2710386C1C924C3996C83C0EE819BBA6BAF2E049F0FEC0B8BD34939)
4. 启动调试，程序运行到断点时，切换到调试的Console窗口，表达式的打印结果将在这里展示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/AKhAcYRiSxKShmyv3vwkIA/zh-cn_image_0000002602186259.png?HW-CC-KV=V1&HW-CC-Date=20260611T072902Z&HW-CC-Expire=86400&HW-CC-Sign=15FE17AB2D1E7FA3B5B63EB8DA662499ABD3B2250616F5CD7E3C4C092D756758)
