---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-concurrent-hashmap
title: 使用ConcurrentHashmap在多线程下完成键值信息的查找维护
breadcrumb: 指南 > 系统 > 基础功能 > FAST Kit（算法加速服务） > 使用ConcurrentHashmap在多线程下完成键值信息的查找维护
category: harmonyos-guides
scraped_at: 2026-06-11T14:50:15+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:b8d35eb852aa08a71ff2bc08150e5146b97f2337a48c712a9a4f9e7735cd9ebb
---
FAST Kit提供的Concurrent HashMap（并发哈希表）专为高并发场景下的键值对数据管理而设计。它通过细粒度的锁策略实现多线程环境下的安全存储、快速访问与高效更新，适用于对并发吞吐量和数据一致性要求较高的增删改查操作，典型场景包括单点插入、删除、查询及并发修改等。

## 接口说明

具体API说明详见[接口文档](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md>)。

| 名称 | 描述 |
| --- | --- |
| [FAST\_ErrorCode](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_errorcode-1>) [HMS\_FAST\_ConcurrentHashmap\_Create](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_create>) ([FAST\_ConcurrentHashmapHandle](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle>)\* handle, [HMS\_FAST\_ConcurrentHashmap\_HashFunc](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_hashfunc>) hasher, [HMS\_FAST\_ConcurrentHashmap\_KeyEqualFunc](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_keyequalfunc>) equaler, float maxLoadFac, size\_t numShards) | 使用给定配置创建并发哈希表。 |
| void [HMS\_FAST\_ConcurrentHashmap\_Destroy](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_destroy>) ([FAST\_ConcurrentHashmapHandle](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle>)\* handle) | 销毁指定并发哈希表。 |
| [FAST\_ErrorCode](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_errorcode-1>) [HMS\_FAST\_ConcurrentHashmap\_Insert](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_insert>) ([FAST\_ConcurrentHashmapHandle](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle>)\* handle, const [FAST\_ConcurrentHashmapKeyPtr](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_concurrenthashmapkeyptr>) key, const [FAST\_ConcurrentHashmapValuePtr](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_concurrenthashmapvalueptr>) value, [FAST\_ConcurrentHashmapValuePtr](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_concurrenthashmapvalueptr>)\* originValue) | 将给定的键值对插入并发哈希表中，如果键已经存在，则使用value覆写原有的值，并将对应值的地址保存在originValue中。 |
| [FAST\_ErrorCode](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_errorcode-1>) [HMS\_FAST\_ConcurrentHashmap\_Find](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_find>) ([FAST\_ConcurrentHashmapHandle](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle>)\* handle, const [FAST\_ConcurrentHashmapKeyPtr](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_concurrenthashmapkeyptr>) key, [FAST\_ConcurrentHashmapValuePtr](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_concurrenthashmapvalueptr>)\* value) | 在给定并发哈希表中查找输入的键，并将对应的值保存在value中。 |
| [FAST\_ErrorCode](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_errorcode-1>) [HMS\_FAST\_ConcurrentHashmap\_Erase](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_erase>) ([FAST\_ConcurrentHashmapHandle](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle>)\* handle, const [FAST\_ConcurrentHashmapKeyPtr](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_concurrenthashmapkeyptr>) key, [FAST\_ConcurrentHashmapKeyPtr](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_concurrenthashmapkeyptr>)\* originKey, [FAST\_ConcurrentHashmapValuePtr](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_concurrenthashmapvalueptr>)\* originValue) | 在给定哈希表中删除输入的键，并将键/值对应的地址保存在originKey和originValue中。 |
| [FAST\_ErrorCode](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_errorcode-1>) [HMS\_FAST\_ConcurrentHashmap\_TryInsert](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_tryinsert>) ([FAST\_ConcurrentHashmapHandle](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle>)\* handle, const [FAST\_ConcurrentHashmapKeyPtr](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_concurrenthashmapkeyptr>) key, const [FAST\_ConcurrentHashmapValuePtr](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_concurrenthashmapvalueptr>) value) | 将给定的键值对插入并发哈希表中，如果键已经存在、则不做操作。 |
| size\_t [HMS\_FAST\_ConcurrentHashmap\_Size](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_size>) ([FAST\_ConcurrentHashmapHandle](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle>)\* handle) | 返回给定哈希表当前的元素个数。 |
| void [HMS\_FAST\_ConcurrentHashmap\_Clear](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_clear>) ([FAST\_ConcurrentHashmapHandle](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle>)\* handle) | 清空给定哈希表中维护的所有元素。 |
| size\_t [HMS\_FAST\_ConcurrentHashmap\_EraseIf](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_eraseif>) ([FAST\_ConcurrentHashmapHandle](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle>)\* handle, [HMS\_FAST\_ConcurrentHashmap\_HookFunc](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_hookfunc>) condFunc, void\* condCtx, [HMS\_FAST\_ConcurrentHashmap\_HookFunc](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_hookfunc>) freeFunc, void\* freeCtx) | 删除哈希表中符合开发者定义条件的所有元素，并使用开发者定义的方式释放其内存。 |
| void [HMS\_FAST\_ConcurrentHashmap\_Traverse](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_traverse>) ([FAST\_ConcurrentHashmapHandle](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_concurrenthashmaphandle>)\* handle, [HMS\_FAST\_ConcurrentHashmap\_HookFunc](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_hookfunc>) condFunc, void\* condCtx, [HMS\_FAST\_ConcurrentHashmap\_HookFunc](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_concurrenthashmap_hookfunc>) workFunc, void\* workCtx) | 遍历哈希表，将所有符合开发者输入条件的键值对按开发者给定的方式修改。 |

## 开发步骤

1. 在CMake脚本中链接相关动态库。

   ```
   1. find_library(
   2. lib_fast_ads
   3. NAMES fast_ads
   4. )
   5. target_link_libraries(entry PRIVATE ${lib_fast_ads})
   ```
2. 调用相关接口能力完成键值信息的管理。

   ```
   1. #include "FASTKit/fast_ads_concurrent_hashmap.h"

   3. // 定义哈希值如何计算，键如何比较
   4. uint64_t custom_hash_int(const FAST_ConcurrentHashmapKeyPtr key) {
   5. static std::hash<int> hasher;
   6. int* intKey = (int*)key;
   7. return hasher(*intKey);
   8. }

   10. int32_t custom_equal_int(const FAST_ConcurrentHashmapKeyPtr key1, const FAST_ConcurrentHashmapKeyPtr key2) {
   11. int* intKey1 = (int*)key1;
   12. int* intKey2 = (int*)key2;
   13. return (*intKey1) == (*intKey2);
   14. }

   16. // 自定义删除条件
   17. int32_t custom_erase_cond(FAST_ConcurrentHashmapKeyPtr key, FAST_ConcurrentHashmapValuePtr val, void* context) {
   18. return 1;
   19. }

   21. // 释放键和值指针持有的内存
   22. int32_t custom_free(FAST_ConcurrentHashmapKeyPtr key, FAST_ConcurrentHashmapValuePtr val, void* context) {
   23. int* intKey = (int*)key;
   24. int* intVal = (int*)val;
   25. delete intKey;
   26. delete intVal;
   27. return 0;
   28. }

   30. // 自定义修改条件，也可传入nullptr以对所有元素执行修改
   31. int32_t custom_modify_cond(FAST_ConcurrentHashmapKeyPtr key, FAST_ConcurrentHashmapValuePtr val, void* context) {
   32. return 1;
   33. }

   35. int32_t custom_work(FAST_ConcurrentHashmapKeyPtr key, FAST_ConcurrentHashmapValuePtr val, void* context) {
   36. int* intVal = (int*)val;
   37. int* intCtx = (int*)context;
   38. *intVal += (*intCtx);
   39. return 1;
   40. }

   42. static napi_value RunConcurrentHashmap(napi_env env, napi_callback_info info)
   43. {
   44. // 使用合适的配置创建并发哈希表，负载因子（loadfac）和分段数（numShards）的典型值一般为0.8和64。
   45. // 负载因子主要作用于分段内部，更大的负载因子通常意味着更小的内存消耗和更大的操作开销；
   46. // 分段数主要作用域并发哈希表全局，更大的分段数通常意味着更好的并发性能和更大的内存消耗
   47. FAST_ConcurrentHashmapHandle handle;
   48. HMS_FAST_ConcurrentHashmap_HashFunc hasher = &custom_hash_int;
   49. HMS_FAST_ConcurrentHashmap_KeyEqualFunc equaler = &custom_equal_int;
   50. float loadfac = 0.8;
   51. size_t numShards = 64;
   52. int ret = HMS_FAST_ConcurrentHashmap_Create(&handle, hasher, equaler, loadfac, numShards);

   54. // 初始化空的哈希表并向其中插入元素
   55. const int size = 10;
   56. int keys[size] = {1,2,3,4,5,6,7,8,9,10};
   57. int vals[size] = {1,2,3,4,5,6,7,8,9,10};
   58. for (int i = 0; i < size; ++i) {
   59. ret = HMS_FAST_ConcurrentHashmap_Insert(
   60. handle,
   61. (FAST_ConcurrentHashmapKeyPtr)&(keys[i]),
   62. (FAST_ConcurrentHashmapValuePtr)&(vals[i]),
   63. nullptr
   64. );
   65. } // 完成插入后哈希表中应包含 {1: 1, 2: 2, ..., 10: 10}

   67. // 使用insert覆写已有的key，如果使用tryInsert则不会覆写
   68. int key2 = 1;
   69. int val2 = 2;
   70. int* originVal0;
   71. ret = HMS_FAST_ConcurrentHashmap_Insert(
   72. handle,
   73. (FAST_ConcurrentHashmapKeyPtr)&key2,
   74. (FAST_ConcurrentHashmapValuePtr)&val2,
   75. (FAST_ConcurrentHashmapValuePtr*)&originVal0
   76. ); // {1: 2, ...}, 且originVal0 == &vals[0]

   78. // 键查找对应的值，并将结果保存在输入指针中。开发者需注意在使用此接口时应校验返回值ret，
   79. // 如果ret值不等于FAST_ERROR_CODE_SUCCESS，则res获取到的值是无效的
   80. int targetKey = 1;
   81. int* res;
   82. ret = HMS_FAST_ConcurrentHashmap_Find(
   83. handle,
   84. (FAST_ConcurrentHashmapKeyPtr)&targetKey,
   85. (FAST_ConcurrentHashmapValuePtr*)&res
   86. ); // (*res) == 2

   88. // 键删除并发哈希表中对应的键值对，并获取关联内存的地址
   89. // 可以使用originKey/Val获得预先插入的元素地址，便于内存管理，可以使用nullptr作为入参
   90. int* originKey1;
   91. int* originVal1;
   92. int deleteKey = 1;
   93. ret = HMS_FAST_ConcurrentHashmap_Erase(
   94. handle,
   95. (FAST_ConcurrentHashmapKeyPtr)&deleteKey,
   96. (FAST_ConcurrentHashmapKeyPtr*)&originKey1,
   97. (FAST_ConcurrentHashmapValuePtr*)&originVal1
   98. ); // originKey1 == &keys[0] && originVal1 == &val2

   100. // 查询并发哈希表当前元素个数
   101. size_t curSize = HMS_FAST_ConcurrentHashmap_Size(handle); // curSize == 9

   103. // 清空并发哈希表中所有元素
   104. HMS_FAST_ConcurrentHashmap_Clear(handle);
   105. curSize = HMS_FAST_ConcurrentHashmap_Size(handle); // curSize == 0

   107. for (int i = 0; i < 6; i++) {
   108. int* key = new int{i};
   109. int* val = new int{i};
   110. ret = HMS_FAST_ConcurrentHashmap_Insert(
   111. handle,
   112. (FAST_ConcurrentHashmapKeyPtr)key,
   113. (FAST_ConcurrentHashmapValuePtr)val,
   114. nullptr
   115. );
   116. } // {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

   118. // 使用Traverse接口对符合custom_modify_cond的元素执行custom_work操作
   119. int context = 10;
   120. HMS_FAST_ConcurrentHashmap_Traverse(
   121. handle,
   122. (HMS_FAST_ConcurrentHashmap_HookFunc)&custom_modify_cond,
   123. nullptr,
   124. (HMS_FAST_ConcurrentHashmap_HookFunc)&custom_work,
   125. (void*)&context
   126. ); // {0: 10, 1: 11, 2: 12, 3: 13, 4: 14, 5: 15}

   128. // 使用EraseIf接口删除所有符合custom_erase_cond的键值对并使用custom_free清理相应的内存
   129. ret = HMS_FAST_ConcurrentHashmap_EraseIf(
   130. handle,
   131. (HMS_FAST_ConcurrentHashmap_HookFunc)&custom_erase_cond,
   132. nullptr,
   133. (HMS_FAST_ConcurrentHashmap_HookFunc)&custom_free,
   134. nullptr
   135. ); // size == 0 && ret == 6

   137. // 销毁并发哈希表
   138. HMS_FAST_ConcurrentHashmap_Destroy(handle);
   139. return 0;
   140. }
   ```
