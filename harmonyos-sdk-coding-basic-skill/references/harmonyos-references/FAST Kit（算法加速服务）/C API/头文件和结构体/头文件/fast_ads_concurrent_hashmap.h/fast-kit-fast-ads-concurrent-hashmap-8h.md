---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/fast-kit-fast-ads-concurrent-hashmap-8h
title: fast_ads_concurrent_hashmap.h
breadcrumb: API参考 > 系统 > 基础功能 > FAST Kit（算法加速服务） > C API > 头文件和结构体 > 头文件 > fast_ads_concurrent_hashmap.h
category: harmonyos-references
scraped_at: 2026-06-01T16:11:53+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:1a0c42e8cb55a3f74aa1870098c2827c1b236292141ce8c648503f14e52122ab
---
## 概述

PhonePC/2in1Tablet

并发哈希表相关数据结构及函数定义。

**引用文件：** <FASTKit/fast\_ads\_concurrent\_hashmap.h>

**库：** libfast\_ads.so

**系统能力：** SystemCapability.FAST.Core

**起始版本：** 6.1.1(24)

**相关模块：** [FAST](../../../模块/FAST/fast-kit-fast.md)

## 汇总

PhonePC/2in1Tablet

### 类型定义

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| typedef void \* [FAST\_ConcurrentHashmapHandle](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle) | 并发哈希表句柄。 |
| typedef void \* [FAST\_ConcurrentHashmapKeyPtr](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmapkeyptr) | 并发哈希表键指针 |
| typedef void \* [FAST\_ConcurrentHashmapValuePtr](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmapvalueptr) | 并发哈希表的值指针 |
| typedef uint64\_t ([\*HMS\_FAST\_ConcurrentHashmap\_HashFunc](../../../模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_hashfunc)) (const [FAST\_ConcurrentHashmapKeyPtr](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmapkeyptr) key) | 开发者自定义的哈希值计算函数 |
| typedef int32\_t ([\*HMS\_FAST\_ConcurrentHashmap\_KeyEqualFunc](../../../模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_keyequalfunc)) (const [FAST\_ConcurrentHashmapKeyPtr](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmapkeyptr) leftKey, const [FAST\_ConcurrentHashmapKeyPtr](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmapkeyptr) rightKey) | 开发者自定义的键比较函数 |
| typedef int32\_t ([\*HMS\_FAST\_ConcurrentHashmap\_HookFunc](../../../模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_hookfunc)) (const [FAST\_ConcurrentHashmapKeyPtr](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmapkeyptr) key, [FAST\_ConcurrentHashmapValuePtr](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmapvalueptr) value, void\* context) | 开发者自定义的通用回调函数形式 |

### 函数

PhonePC/2in1Tablet

| 名称 | 描述 |
| --- | --- |
| [FAST\_ErrorCode](../../../模块/FAST/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_ConcurrentHashmap\_Create](../../../模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_create) ([FAST\_ConcurrentHashmapHandle](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle)\* handle, [HMS\_FAST\_ConcurrentHashmap\_HashFunc](../../../模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_hashfunc) hasher, [HMS\_FAST\_ConcurrentHashmap\_KeyEqualFunc](../../../模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_keyequalfunc) equaler, float maxLoadFac, size\_t numShards) | 使用给定配置创建并发哈希表 |
| void [HMS\_FAST\_ConcurrentHashmap\_Destroy](../../../模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_destroy) ([FAST\_ConcurrentHashmapHandle](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle) handle) | 销毁指定并发哈希表 |
| [FAST\_ErrorCode](../../../模块/FAST/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_ConcurrentHashmap\_Insert](../../../模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_insert) ([FAST\_ConcurrentHashmapHandle](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle) handle, const [FAST\_ConcurrentHashmapKeyPtr](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmapkeyptr) key, const [FAST\_ConcurrentHashmapValuePtr](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmapvalueptr) value, [FAST\_ConcurrentHashmapValuePtr](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmapvalueptr)\* originValue) | 将给定的键值对插入并发哈希表中，如果键已经存在、则使用value覆写原有的值，并将对应值的地址保存在originValue中 |
| [FAST\_ErrorCode](../../../模块/FAST/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_ConcurrentHashmap\_Find](../../../模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_find) ([FAST\_ConcurrentHashmapHandle](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle) handle, const [FAST\_ConcurrentHashmapKeyPtr](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmapkeyptr) key, [FAST\_ConcurrentHashmapValuePtr](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmapvalueptr)\* value) | 在给定并发哈希表中查找输入的键，并将对应的值保存在value中 |
| [FAST\_ErrorCode](../../../模块/FAST/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_ConcurrentHashmap\_Erase](../../../模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_erase) ([FAST\_ConcurrentHashmapHandle](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle) handle, const [FAST\_ConcurrentHashmapKeyPtr](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmapkeyptr) key, [FAST\_ConcurrentHashmapKeyPtr](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmapkeyptr)\* originKey, [FAST\_ConcurrentHashmapValuePtr](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmapvalueptr)\* originValue) | 在给定哈希表中删除输入的键，并将键和值对应的地址分别保存在originKey和originValue中 |
| [FAST\_ErrorCode](../../../模块/FAST/fast-kit-fast.md#fast_errorcode-1) [HMS\_FAST\_ConcurrentHashmap\_TryInsert](../../../模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_tryinsert) ([FAST\_ConcurrentHashmapHandle](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle) handle, const [FAST\_ConcurrentHashmapKeyPtr](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmapkeyptr) key, const [FAST\_ConcurrentHashmapValuePtr](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmapvalueptr) value) | 将给定的键值对插入并发哈希表中，如果键已经存在、则不做操作 |
| size\_t [HMS\_FAST\_ConcurrentHashmap\_Size](../../../模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_size) ([FAST\_ConcurrentHashmapHandle](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle) handle) | 返回给定哈希表当前的元素个数 |
| void [HMS\_FAST\_ConcurrentHashmap\_Clear](../../../模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_clear) ([FAST\_ConcurrentHashmapHandle](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle) handle) | 清空给定哈希表中维护的所有元素 |
| size\_t [HMS\_FAST\_ConcurrentHashmap\_EraseIf](../../../模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_eraseif) ([FAST\_ConcurrentHashmapHandle](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle) handle, [HMS\_FAST\_ConcurrentHashmap\_HookFunc](../../../模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_hookfunc) condFunc, void\* condCtx, [HMS\_FAST\_ConcurrentHashmap\_HookFunc](../../../模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_hookfunc) freeFunc, void\* freeCtx) | 删除哈希表中符合开发者定义条件的所有元素，并使用开发者定义的方式释放其内存 |
| void [HMS\_FAST\_ConcurrentHashmap\_Traverse](../../../模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_traverse) ([FAST\_ConcurrentHashmapHandle](../../../模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle) handle, [HMS\_FAST\_ConcurrentHashmap\_HookFunc](../../../模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_hookfunc) condFunc, void\* condCtx, [HMS\_FAST\_ConcurrentHashmap\_HookFunc](../../../模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_hookfunc) workFunc, void\* workCtx) | 遍历哈希表，将所有符合开发者输入条件的键值对按开发者给定的方式修改 |
