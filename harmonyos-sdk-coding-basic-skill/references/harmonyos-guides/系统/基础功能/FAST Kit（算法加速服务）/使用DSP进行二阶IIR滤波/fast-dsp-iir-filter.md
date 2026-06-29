---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-dsp-iir-filter
title: 使用DSP进行二阶IIR滤波
breadcrumb: 指南 > 系统 > 基础功能 > FAST Kit（算法加速服务） > 使用DSP进行二阶IIR滤波
category: harmonyos-guides
scraped_at: 2026-06-01T11:22:26+08:00
doc_updated_at: 2026-05-28
content_hash: sha256:746981f8b8bd167f495cdd0fa35f99ed5d484806691320b99c0eb8fab181be86
---
二阶IIR滤波器用于音频和信号处理中的滤波操作，例如实现低通、高通或带通滤波。

二阶IIR滤波器采用直接II型转置结构，支持多通道（如立体声）和多节级联（如高阶滤波器）配置。滤波器支持动态激活/旁路控制，允许运行时灵活调整滤波特性。

## 接口说明

具体API说明详见[接口文档](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md>)。

| 名称 | 描述 |
| --- | --- |
| [FAST\_ErrorCode](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_errorcode-1>) [HMS\_FAST\_Biquadm\_Create](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_biquadm_create>) (size\_t numChannels, size\_t numSections, size\_t maxFrames, FAST\_Biquadm\*\* filter) | 创建并初始化多通道多节二阶IIR滤波器组（单精度）。 |
| [FAST\_ErrorCode](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_errorcode-1>) [HMS\_FAST\_Biquadm\_CreateD](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_biquadm_created>) (size\_t numChannels, size\_t numSections, size\_t maxFrames, FAST\_BiquadmD\*\* filter) | 创建并初始化多通道多节二阶IIR滤波器组（双精度）。 |
| void [HMS\_FAST\_Biquadm\_Destroy](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_biquadm_destroy>) (FAST\_Biquadm\* filter) | 销毁二阶滤波器实例（单精度）。 |
| void [HMS\_FAST\_Biquadm\_DestroyD](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_biquadm_destroyd>) (FAST\_BiquadmD\* filter) | 销毁二阶滤波器实例（双精度）。 |
| [FAST\_ErrorCode](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_errorcode-1>) [HMS\_FAST\_Biquadm\_SetCoeffSingle](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_biquadm_setcoeffsingle>) (FAST\_Biquadm\* filter, const float\* coeff, size\_t stride) | 从单精度源数组设置所有二阶滤波器系数（单精度滤波器）。 |
| [FAST\_ErrorCode](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_errorcode-1>) [HMS\_FAST\_Biquadm\_SetCoeffDouble](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_biquadm_setcoeffdouble>) (FAST\_Biquadm\* filter, const double\* coeff, size\_t stride) | 从双精度源数组设置所有二阶滤波器系数（单精度滤波器）。 |
| [FAST\_ErrorCode](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_errorcode-1>) [HMS\_FAST\_Biquadm\_SetCoeffSingleD](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_biquadm_setcoeffsingled>) (FAST\_BiquadmD\* filter, const float\* coeff, size\_t stride) | 从单精度源数组设置所有二阶滤波器系数（双精度滤波器）。 |
| [FAST\_ErrorCode](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_errorcode-1>) [HMS\_FAST\_Biquadm\_SetCoeffDoubleD](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_biquadm_setcoeffdoubled>) (FAST\_BiquadmD\* filter, const double\* coeff, size\_t stride) | 从双精度源数组设置所有二阶滤波器系数（双精度滤波器）。 |
| [FAST\_ErrorCode](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_errorcode-1>) [HMS\_FAST\_Biquadm\_SetActiveFilters](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_biquadm_setactivefilters>) (FAST\_Biquadm\* filter, const uint8\_t\* activeMask) | 设置二阶滤波器节的激活掩码（单精度）。 |
| [FAST\_ErrorCode](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_errorcode-1>) [HMS\_FAST\_Biquadm\_SetActiveFiltersD](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_biquadm_setactivefiltersd>) (FAST\_BiquadmD\* filter, const uint8\_t\* activeMask) | 设置二阶滤波器节的激活掩码（双精度）。 |
| [FAST\_ErrorCode](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_errorcode-1>) [HMS\_FAST\_Biquadm](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_biquadm>) (FAST\_Biquadm\* filter, const float\*\* input, const size\_t strideInput, float\*\* output, const size\_t strideOutput, size\_t length) | 通过二阶滤波器组处理多通道音频（单精度）。 |
| [FAST\_ErrorCode](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#fast_errorcode-1>) [HMS\_FAST\_BiquadmD](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_biquadmd>) (FAST\_BiquadmD\* filter, const double\*\* input, const size\_t strideInput, double\*\* output, const size\_t strideOutput, size\_t length) | 通过二阶滤波器组处理多通道音频（双精度）。 |

## 开发步骤

1. 在CMake脚本中链接相关动态库。

   ```
   1. find_library(
   2. lib_fast_dsp
   3. NAMES fast_dsp
   4. )
   5. target_link_libraries(entry PRIVATE ${lib_fast_dsp})
   ```
2. 引入头文件。

   ```
   1. #include "FASTKit/fast_dsp_common.h"
   ```
3. 调用HMS\_FAST\_Biquadm\_Create创建滤波器实例（单精度）或HMS\_FAST\_Biquadm\_CreateD（双精度）。
4. 调用HMS\_FAST\_Biquadm\_SetCoeffSingle设置滤波器系数。
5. 可选：调用HMS\_FAST\_Biquadm\_SetActiveFilters设置滤波器节激活掩码。
6. 调用HMS\_FAST\_Biquadm进行滤波处理。
7. 调用HMS\_FAST\_Biquadm\_Destroy销毁滤波器实例。

## 代码示例

### 单通道滤波器示例

```
1. #include <cstdio>
2. #include <cstdlib>
3. #include "FASTKit/fast_dsp_common.h"

5. FAST_ErrorCode single_channel_filter_demo() {
6. // 滤波器参数：1通道，1节，最大100帧
7. size_t num_channels = 1;
8. size_t num_sections = 1;
9. size_t max_frames = 100;

11. FAST_Biquadm* filter = nullptr;
12. FAST_ErrorCode ret;

14. // 创建滤波器
15. ret = HMS_FAST_Biquadm_Create(num_channels, num_sections, max_frames, &filter);
16. if (ret != FAST_ERROR_CODE_SUCCESS) {
17. printf("Failed to create filter: %d\n", ret);
18. return ret;
19. }

21. // 设置滤波器系数 (b0, b1, b2, a1, a2)
22. // 低通滤波器示例系数
23. float coefficients[] = {
24. 0.049922035f,  // b0
25. 0.099844069f,  // b1
26. 0.049922035f,  // b2
27. -1.558153539f, // a1
28. 0.649003273f   // a2
29. };

31. ret = HMS_FAST_Biquadm_SetCoeffSingle(filter, coefficients, 1);
32. if (ret != FAST_ERROR_CODE_SUCCESS) {
33. printf("Failed to set coefficients: %d\n", ret);
34. HMS_FAST_Biquadm_Destroy(filter);
35. return ret;
36. }

38. // 准备输入输出数据
39. const size_t num_samples = 10;
40. float input[num_samples] = {1.0f, 1.0f, 1.0f, 1.0f, 1.0f,
41. 1.0f, 1.0f, 1.0f, 1.0f, 1.0f};
42. float output[num_samples];

44. const float* input_channels[] = {input};
45. float* output_channels[] = {output};

47. // 执行滤波
48. ret = HMS_FAST_Biquadm(filter, input_channels, 1, output_channels, 1, num_samples);
49. if (ret != FAST_ERROR_CODE_SUCCESS) {
50. printf("Failed to process: %d\n", ret);
51. HMS_FAST_Biquadm_Destroy(filter);
52. return ret;
53. }

55. printf("Filtered output:\n");
56. for (size_t i = 0; i < num_samples; ++i) {
57. printf("  output[%zu] = %f\n", i, output[i]);
58. }

60. // 销毁滤波器
61. HMS_FAST_Biquadm_Destroy(filter);

63. return FAST_ERROR_CODE_SUCCESS;
64. }
```

### 多通道滤波器示例

```
1. #include <cstdio>
2. #include <cstdlib>
3. #include <cmath>
4. #include "FASTKit/fast_dsp_common.h"

6. FAST_ErrorCode multi_channel_filter_demo() {
7. // 滤波器参数：2通道（立体声），2节级联，最大1000帧
8. size_t num_channels = 2;
9. size_t num_sections = 2;
10. size_t max_frames = 1000;

12. FAST_Biquadm* filter = nullptr;
13. FAST_ErrorCode ret;

15. // 创建滤波器
16. ret = HMS_FAST_Biquadm_Create(num_channels, num_sections, max_frames, &filter);
17. if (ret != FAST_ERROR_CODE_SUCCESS) {
18. printf("Failed to create filter: %d\n", ret);
19. return ret;
20. }

22. // 设置2节滤波器系数
23. float coefficients[] = {
24. // 第1节系数
25. 0.049922035f, 0.099844069f, 0.049922035f, -1.558153539f, 0.649003273f,
26. // 第2节系数
27. 0.049922035f, 0.099844069f, 0.049922035f, -1.558153539f, 0.649003273f
28. };

30. ret = HMS_FAST_Biquadm_SetCoeffSingle(filter, coefficients, 1);
31. if (ret != FAST_ERROR_CODE_SUCCESS) {
32. printf("Failed to set coefficients: %d\n", ret);
33. HMS_FAST_Biquadm_Destroy(filter);
34. return ret;
35. }

37. // 准备输入输出数据
38. const size_t num_samples = 100;
39. float input_left[num_samples];
40. float input_right[num_samples];
41. float output_left[num_samples];
42. float output_right[num_samples];

44. // 初始化输入数据（正弦波）
45. for (size_t i = 0; i < num_samples; ++i) {
46. input_left[i] = sinf(i * 0.1f);
47. input_right[i] = sinf(i * 0.1f + 0.5f);
48. }

50. const float* input_channels[] = {input_left, input_right};
51. float* output_channels[] = {output_left, output_right};

53. // 执行滤波
54. ret = HMS_FAST_Biquadm(filter, input_channels, 1, output_channels, 1, num_samples);
55. if (ret != FAST_ERROR_CODE_SUCCESS) {
56. printf("Failed to process: %d\n", ret);
57. HMS_FAST_Biquadm_Destroy(filter);
58. return ret;
59. }

61. printf("Multi-channel filter processed %zu samples\n", num_samples);

63. // 销毁滤波器
64. HMS_FAST_Biquadm_Destroy(filter);

66. return FAST_ERROR_CODE_SUCCESS;
67. }
```

### 动态激活滤波器节示例

```
1. #include <cstdio>
2. #include <cstdlib>
3. #include "FASTKit/fast_dsp_common.h"

5. FAST_ErrorCode dynamic_filter_activation_demo() {
6. // 滤波器参数：1通道，3节，最大100帧
7. size_t num_channels = 1;
8. size_t num_sections = 3;
9. size_t max_frames = 100;

11. FAST_Biquadm* filter = nullptr;
12. FAST_ErrorCode ret;

14. // 创建滤波器
15. ret = HMS_FAST_Biquadm_Create(num_channels, num_sections, max_frames, &filter);
16. if (ret != FAST_ERROR_CODE_SUCCESS) {
17. printf("Failed to create filter: %d\n", ret);
18. return ret;
19. }

21. // 设置3节滤波器系数
22. float coefficients[] = {
23. 0.049922035f, 0.099844069f, 0.049922035f, -1.558153539f, 0.649003273f,  // 节 0
24. 0.049922035f, 0.099844069f, 0.049922035f, -1.558153539f, 0.649003273f,  // 节 1
25. 0.049922035f, 0.099844069f, 0.049922035f, -1.558153539f, 0.649003273f   // 节 2
26. };

28. ret = HMS_FAST_Biquadm_SetCoeffSingle(filter, coefficients, 1);
29. if (ret != FAST_ERROR_CODE_SUCCESS) {
30. printf("Failed to set coefficients: %d\n", ret);
31. HMS_FAST_Biquadm_Destroy(filter);
32. return ret;
33. }

35. // 设置激活掩码：仅激活第0节和第2节，旁路第1节
36. uint8_t active_mask[] = {1, 0, 1};
37. ret = HMS_FAST_Biquadm_SetActiveFilters(filter, active_mask);
38. if (ret != FAST_ERROR_CODE_SUCCESS) {
39. printf("Failed to set active filters: %d\n", ret);
40. HMS_FAST_Biquadm_Destroy(filter);
41. return ret;
42. }

44. // 准备输入输出数据
45. const size_t num_samples = 10;
46. float input[num_samples] = {1.0f, 1.0f, 1.0f, 1.0f, 1.0f,
47. 1.0f, 1.0f, 1.0f, 1.0f, 1.0f};
48. float output[num_samples];

50. const float* input_channels[] = {input};
51. float* output_channels[] = {output};

53. // 执行滤波（仅通过第0节和第2节）
54. ret = HMS_FAST_Biquadm(filter, input_channels, 1, output_channels, 1, num_samples);
55. if (ret != FAST_ERROR_CODE_SUCCESS) {
56. printf("Failed to process: %d\n", ret);
57. HMS_FAST_Biquadm_Destroy(filter);
58. return ret;
59. }

61. printf("Filtered output with dynamic activation:\n");
62. for (size_t i = 0; i < num_samples; ++i) {
63. printf("  output[%zu] = %f\n", i, output[i]);
64. }

66. // 销毁滤波器
67. HMS_FAST_Biquadm_Destroy(filter);

69. return FAST_ERROR_CODE_SUCCESS;
70. }
```
