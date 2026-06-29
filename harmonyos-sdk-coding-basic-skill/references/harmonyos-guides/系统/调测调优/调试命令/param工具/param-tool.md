---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/param-tool
title: param工具
breadcrumb: 指南 > 系统 > 调测调优 > 调试命令 > param工具
category: harmonyos-guides
scraped_at: 2026-06-11T14:53:12+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:bc68a7e7d36f5f9b5cad807f43b855c9602ead47166c49127df3a3852a74401c
---

param是为开发人员提供用于操作系统参数的工具，该工具只支持标准系统。

## 环境要求

* 获取hdc工具，执行hdc shell。
* 正常连接设备。

## param工具命令列表

| 选项 | 说明 |
| --- | --- |
| -h | 获取param支持的命令。 |
| ls [-r] [name] | 显示匹配name的系统参数信息。带"-r"则根据参数权限获取信息，不带"-r"则直接获取参数信息。 |
| get [name] | 获取指定name系统参数的值；若不指定任何name，则返回所有系统参数。 |
| set name value | 设置指定name系统参数的值为value。 |
| wait name [value] [timeout] | 同步等待指定name系统参数与指定值value匹配。value支持模糊匹配，如"\*"表示任何值，"val\*"表示只匹配前三个val字符。timeout为等待时间（单位：s），不设置则默认为30s。 |
| save | 保存persist参数到工作空间。 |

## 获取param支持的命令

* 获取param支持的命令，命令格式如下：

  ```
  1. param -h
  ```

## 获取系统参数信息

* 显示匹配name的系统参数信息，命令格式如下：

  ```
  1. param ls [-r] [name]
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/54529PVrQBOVwLzLj2LY-g/zh-cn_image_0000002592378876.png?HW-CC-KV=V1&HW-CC-Date=20260611T065311Z&HW-CC-Expire=86400&HW-CC-Sign=BCE29968649320C2F61D4544608F184C7BD6BF694D2B3454C0A07024375DD94B)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/MlgI-_4qQUSXN5kq3e2N6A/zh-cn_image_0000002622858383.png?HW-CC-KV=V1&HW-CC-Date=20260611T065311Z&HW-CC-Expire=86400&HW-CC-Sign=B64F4ADC8971C7E149038C286B3324760BBC1657CEDCA3D5A3EF63F271032176)

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/kxx7m96GTRyOtynovSJTHQ/zh-cn_image_0000002622698505.png?HW-CC-KV=V1&HW-CC-Date=20260611T065311Z&HW-CC-Expire=86400&HW-CC-Sign=A1F6A2B10C1778B3AF33362C901C90FB9ABD08CCAEFD59F4BD3C6183638B7FC7)

## 获取系统参数的值

* 获取指定name系统参数的值，命令格式如下：

  ```
  1. param get [name]
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/eEzkZRfdRZC_TtQUPzjZyg/zh-cn_image_0000002592218944.png?HW-CC-KV=V1&HW-CC-Date=20260611T065311Z&HW-CC-Expire=86400&HW-CC-Sign=6D2FCC0CC6BDE51CD73224D6B7D4445D0EB380AD50A4868FC257781E0159EEFB)

## 设置系统参数的值

* 设置指定name系统参数的值为value，命令格式如下：

  ```
  1. param set name value
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/T8sBzX2PTASXMUMzq4kSbA/zh-cn_image_0000002592378878.png?HW-CC-KV=V1&HW-CC-Date=20260611T065311Z&HW-CC-Expire=86400&HW-CC-Sign=470B5B53E89A801D3ACD784098682A6F53FD3BBA816BD37B9253E37409B1CB29)

## 等待系统参数值匹配

* 同步等待指定name系统参数与指定值value匹配，命令格式如下：

  ```
  1. param wait name [value] [timeout]
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/pCG6hup0SXWq5OGBaGGASQ/zh-cn_image_0000002622858385.png?HW-CC-KV=V1&HW-CC-Date=20260611T065311Z&HW-CC-Expire=86400&HW-CC-Sign=33C1D3FB7955F8664882BD324F306EB0A4C26A6AF73387C00F48C81779160ABB)

## 保存persist(可持久化)参数

* 保存persist(可持久化)参数到工作空间，命令格式如下：

  ```
  1. param save
  ```

  **示例**

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/BmGACkkQTKqrFRoFENYqyg/zh-cn_image_0000002622698507.png?HW-CC-KV=V1&HW-CC-Date=20260611T065311Z&HW-CC-Expire=86400&HW-CC-Sign=AAFB2297C93ACDCC64D4570965E82B481EF240771F78F75E446192DD67CF6C1B)

## 系统参数错误码说明

**错误码说明**

错误码详情参考[系统参数](https://gitcode.com/openharmony/docs/blob/weekly_20260309/zh-cn/device-dev/subsystems/subsys-boot-init-sysparam.md#系统参数错误码说明)文档描述
