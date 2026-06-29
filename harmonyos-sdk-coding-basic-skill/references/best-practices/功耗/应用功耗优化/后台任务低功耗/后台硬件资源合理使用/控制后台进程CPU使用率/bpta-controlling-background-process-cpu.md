---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-controlling-background-process-cpu
title: 控制后台进程CPU使用率
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 后台任务低功耗 > 后台硬件资源合理使用 > 控制后台进程CPU使用率
category: best-practices
scraped_at: 2026-06-12T10:16:52+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:586fa81a8dca81d0e7bb492c01fd9085c2f761bd77f477703e65ca1b83592d80
---

CPU使用率表示进程在CPU上的运行时间占总时间的百分比，计算公式为：CPU使用率 = 运行时间 / 总时间。单核CPU使用率的最大值为100%，多核CPU使用率的最大值为核数乘以100%。例如，8核CPU使用率的最大值为800%。

系统将进程的任务调度到多个CPU核上，进程在所有核上运行的时间总和与总时间的比值即为该进程的CPU使用率。例如，1秒内进程在所有核上运行的总时间为1.1秒，则该进程的CPU使用率为110%。

## 约束

后台进程在10分钟内的单核CPU使用率不得超过80%。

短时任务后台进程CPU使用率约束：后台进程任务期间单核CPU使用率不得高于80%。

## 调测验证

1. 连接设备，打开命令行窗口，输入hdc shell进入设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/E2yicMOORfOzK62Z7_v8fA/zh-cn_image_0000002229450601.png?HW-CC-KV=V1&HW-CC-Date=20260612T021651Z&HW-CC-Expire=86400&HW-CC-Sign=ED861ABC2084A7F21B7AA131B11DC81DCAA88FB40A9F44E3AB8C7C03996D55C9 "点击放大")
2. 输入ps -ef | grep bundleName，查询应用使用率的进程号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/zNZ_riTWQ5ykrym_xNL7-Q/zh-cn_image_0000002229336117.png?HW-CC-KV=V1&HW-CC-Date=20260612T021651Z&HW-CC-Expire=86400&HW-CC-Sign=94D3A9DC8DCC9DFED8362AA2F122995E07EC33F23288F6E3A305C076E246345F "点击放大")
3. 输入：top -p xxx，查看对应进程的使用率。查询结果中，CPU列显示进程的实时使用率。其中，xxx是进程ID(PID)。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/-eyNeC2sR_6DUJQBkTvC9g/zh-cn_image_0000002194010320.png?HW-CC-KV=V1&HW-CC-Date=20260612T021651Z&HW-CC-Expire=86400&HW-CC-Sign=FF413BCD5A5821B1DC17D9BD42A2BFE457E2CC4BBED4CBFE877511F915891048 "点击放大")
