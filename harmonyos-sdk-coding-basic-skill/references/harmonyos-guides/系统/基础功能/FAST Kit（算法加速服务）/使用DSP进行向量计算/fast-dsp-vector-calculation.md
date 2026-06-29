---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/fast-dsp-vector-calculation
title: 使用DSP进行向量计算
breadcrumb: 指南 > 系统 > 基础功能 > FAST Kit（算法加速服务） > 使用DSP进行向量计算
category: harmonyos-guides
scraped_at: 2026-06-01T11:22:24+08:00
doc_updated_at: 2026-05-28
content_hash: sha256:4e7b2a99eefe3e24a878476ca1c560ec9fbf0b2dc0534311226cf478d3a3656c
---
数字信号处理（DSP）中的向量计算功能，用于对实值向量和复数数据进行高效的统计运算、数学运算和格式转换。当开发者需要对传感器数据、音频信号或其他数值序列进行最大值查找、求和、点积、复数格式转换等计算时，可以使用向量计算接口。

向量计算支持单精度（float）和双精度（double）两种数据类型，并针对ARM NEON指令集进行了优化，在步长为 1 的连续存储场景下可获得显著性能提升。需要注意的是，为了提升性能，部分接口对浮点数的计算顺序进行了调整，可能影响结果精度。

## 接口说明

具体API说明详见[接口文档](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md>)。

### 最大值与索引计算

| 名称 | 描述 |
| --- | --- |
| float [HMS\_FAST\_DSP\_Maxmgv](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_dsp_maxmgv>) (const float\* input, size\_t stride, size\_t length) | 计算步长实值向量中的最大幅值（单精度）。 |
| double [HMS\_FAST\_DSP\_MaxmgvD](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_dsp_maxmgvd>) (const double\* input, size\_t stride, size\_t length) | 计算步长实值向量中的最大幅值（双精度）。 |
| void [HMS\_FAST\_DSP\_Maxvi](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_dsp_maxvi>) (const float\* input, size\_t stride, size\_t length, float\* value, size\_t\* index) | 查找步长实值向量中的最大值及其索引（单精度）。 |
| void [HMS\_FAST\_DSP\_MaxviD](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_dsp_maxvid>) (const double\* input, size\_t stride, size\_t length, double\* value, size\_t\* index) | 查找步长实值向量中的最大值及其索引（双精度）。 |

### 统计计算

| 名称 | 描述 |
| --- | --- |
| float [HMS\_FAST\_DSP\_Sve](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_dsp_sve>) (const float\* input, size\_t stride, size\_t length) | 计算步长实值向量的和（单精度）。 |
| double [HMS\_FAST\_DSP\_SveD](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_dsp_sved>) (const double\* input, size\_t stride, size\_t length) | 计算步长实值向量的和（双精度）。 |
| float [HMS\_FAST\_DSP\_Svemg](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_dsp_svemg>) (const float\* input, size\_t stride, size\_t length) | 计算步长向量的绝对值之和（L1范数）（单精度）。 |
| double [HMS\_FAST\_DSP\_SvemgD](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_dsp_svemgd>) (const double\* input, size\_t stride, size\_t length) | 计算步长向量的绝对值之和（L1范数）（双精度）。 |
| float [HMS\_FAST\_DSP\_Meamgv](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_dsp_meamgv>) (const float\* input, size\_t stride, size\_t length) | 计算步长实值向量绝对值的均值（单精度）。 |
| double [HMS\_FAST\_DSP\_MeamgvD](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_dsp_meamgvd>) (const double\* input, size\_t stride, size\_t length) | 计算步长实值向量绝对值的均值（双精度）。 |

### 向量运算

| 名称 | 描述 |
| --- | --- |
| float [HMS\_FAST\_DSP\_Dotpr](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_dsp_dotpr>) (const float\* inputA, size\_t strideA, const float\* inputB, size\_t strideB, size\_t length) | 计算两个步长实值向量的点积（单精度）。 |
| double [HMS\_FAST\_DSP\_DotprD](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_dsp_dotprd>) (const double\* inputA, size\_t strideA, const double\* inputB, size\_t strideB, size\_t length) | 计算两个步长实值向量的点积（双精度）。 |
| void [HMS\_FAST\_DSP\_Vsbsm](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_dsp_vsbsm>) (const float\* inputA, size\_t strideA, const float\* inputB, size\_t strideB, float scalar, float\* outputC, size\_t strideC, size\_t length) | 执行向量减法：outputC[i] = (inputA[i] - inputB[i]) \* scalar（单精度）。 |
| void [HMS\_FAST\_DSP\_VsbsmD](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_dsp_vsbsmd>) (const double\* inputA, size\_t strideA, const double\* inputB, size\_t strideB, double scalar, double\* outputC, size\_t strideC, size\_t length) | 执行向量减法：outputC[i] = (inputA[i] - inputB[i]) \* scalar（双精度）。 |

### 复数格式转换

| 名称 | 描述 |
| --- | --- |
| void [HMS\_FAST\_DSP\_Ctoz](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_dsp_ctoz>) (const float\* input, size\_t strideInput, FAST\_SplitComplex\* output, size\_t strideOutput, size\_t length) | 将交错复数数组转换为分离格式（单精度）。 |
| void [HMS\_FAST\_DSP\_CtozD](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_dsp_ctozd>) (const double\* input, size\_t strideInput, FAST\_SplitComplexD\* output, size\_t strideOutput, size\_t length) | 将交错复数数组转换为分离格式（双精度）。 |
| void [HMS\_FAST\_DSP\_Ztoc](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_dsp_ztoc>) (const FAST\_SplitComplex\* input, size\_t strideInput, float\* output, size\_t strideOutput, size\_t length) | 将分离复数数组转换为交错格式（单精度）。 |
| void [HMS\_FAST\_DSP\_ZtocD](<../../../../../harmonyos-references/基础功能/FAST Kit（算法加速服务）/C API/模块/FAST/fast-kit-fast.md#hms_fast_dsp_ztocd>) (const FAST\_SplitComplexD\* input, size\_t strideInput, double\* output, size\_t strideOutput, size\_t length) | 将分离复数数组转换为交错格式（双精度）。 |

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
3. 根据数据类型选择对应的函数（单精度无后缀，双精度带D后缀）。
4. 调用向量计算函数，注意设置正确的stride参数（连续存储时stride为1）。
5. 检查返回结果。

## 代码示例

### 最大值查找示例

```
1. #include <cstdio>
2. #include <cstdlib>
3. #include "FASTKit/fast_dsp_common.h"

5. FAST_ErrorCode max_value_demo() {
6. // 定义输入向量
7. float input[] = {1.0f, -2.0f, 3.0f, -4.0f, 5.0f};
8. size_t length = sizeof(input) / sizeof(float);
9. size_t stride = 1;

11. // 计算最大幅值（绝对值最大值）
12. float max_magnitude = HMS_FAST_DSP_Maxmgv(input, stride, length);
13. printf("Max magnitude: %f\n", max_magnitude);  // 输出5.0

15. // 查找最大值及其索引
16. float max_value = 0.0f;
17. size_t max_index = 0;
18. HMS_FAST_DSP_Maxvi(input, stride, length, &max_value, &max_index);
19. printf("Max value: %f at index %zu\n", max_value, max_index);  // 输出5.0 at index 4

21. return FAST_ERROR_CODE_SUCCESS;
22. }
```

### 统计计算示例

```
1. #include <cstdio>
2. #include <cstdlib>
3. #include "FASTKit/fast_dsp_common.h"

5. FAST_ErrorCode statistics_demo() {
6. // 定义输入向量
7. float input[] = {1.0f, -2.0f, 3.0f, -4.0f, 5.0f};
8. size_t length = sizeof(input) / sizeof(float);
9. size_t stride = 1;

11. // 计算向量总和
12. float sum = HMS_FAST_DSP_Sve(input, stride, length);
13. printf("Sum: %f\n", sum);  // 输出3.0

15. // 计算绝对值之和（L1范数）
16. float sum_abs = HMS_FAST_DSP_Svemg(input, stride, length);
17. printf("Sum of absolute values: %f\n", sum_abs);  // 输出15.0

19. // 计算绝对值均值
20. float mean_abs = HMS_FAST_DSP_Meamgv(input, stride, length);
21. printf("Mean of absolute values: %f\n", mean_abs);  // 输出3.0

23. return FAST_ERROR_CODE_SUCCESS;
24. }
```

### 向量运算示例

```
1. #include <cstdio>
2. #include <cstdlib>
3. #include "FASTKit/fast_dsp_common.h"

5. FAST_ErrorCode vector_operations_demo() {
6. // 定义两个输入向量
7. float inputA[] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f};
8. float inputB[] = {0.5f, 1.0f, 1.5f, 2.0f, 2.5f};
9. size_t length = 5;
10. size_t stride = 1;

12. // 计算点积
13. float dot_product = HMS_FAST_DSP_Dotpr(inputA, stride, inputB, stride, length);
14. printf("Dot product: %f\n", dot_product);  // 输出27.5

16. // 执行向量减法：outputC[i] = (inputA[i] - inputB[i]) * 2.0
17. float outputC[5];
18. float scalar = 2.0f;
19. HMS_FAST_DSP_Vsbsm(inputA, stride, inputB, stride, scalar, outputC, stride, length);

21. printf("Vector subtraction result:\n");
22. for (size_t i = 0; i < length; ++i) {
23. printf("  outputC[%zu] = %f\n", i, outputC[i]);
24. }
25. // 输出: 1.0, 2.0, 3.0, 4.0, 5.0

27. return FAST_ERROR_CODE_SUCCESS;
28. }
```

### 复数格式转换示例

```
1. #include <cstdio>
2. #include <cstdlib>
3. #include "FASTKit/fast_dsp_common.h"

5. FAST_ErrorCode complex_conversion_demo() {
6. // 定义交错格式复数输入 (real, imag, real, imag...)
7. float interleaved[] = {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f};
8. size_t length = 3;  // 3个复数
9. size_t stride_input = 1;

11. // 准备分离格式输出
12. float real_array[3];
13. float imag_array[3];
14. FAST_SplitComplex split_output = {
15. .real = real_array,
16. .imag = imag_array
17. };
18. size_t stride_output = 1;

20. // 转换为分离格式
21. HMS_FAST_DSP_Ctoz(interleaved, stride_input, &split_output, stride_output, length);

23. printf("Split format:\n");
24. for (size_t i = 0; i < length; ++i) {
25. printf("  Complex[%zu] = %f + %fi\n", i, real_array[i], imag_array[i]);
26. }
27. /* xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
28. Split format:
29. Complex[0] = 1.000000 + 2.000000i
30. Complex[1] = 3.000000 + 4.000000i
31. Complex[2] = 5.000000 + 6.000000i
32. */

34. // 转换回交错格式
35. float interleaved_output[6];
36. HMS_FAST_DSP_Ztoc(&split_output, stride_output, interleaved_output, stride_input, length);

38. printf("Interleaved format:\n");
39. for (size_t i = 0; i < length; ++i) {
40. printf("  Complex[%zu] = %f + %fi\n", i, interleaved_output[i * 2], interleaved_output[i * 2 + 1]);
41. }

43. return FAST_ERROR_CODE_SUCCESS;
44. }
```

### 非连续存储示例

```
1. #include <cstdio>
2. #include <cstdlib>
3. #include "FASTKit/fast_dsp_common.h"

5. FAST_ErrorCode strided_access_demo() {
6. // 定义交错存储的复数数据 (real, imag, real, imag...)
7. float interleaved[] = {1.0f, 10.0f, 2.0f, 20.0f, 3.0f, 30.0f, 4.0f, 40.0f, 5.0f, 50.0f};
8. size_t length = 5;  // 5个实数值
9. size_t stride = 2;  // 步长为2，跳过虚部

11. // 计算实部向量的最大幅值
12. float max_magnitude = HMS_FAST_DSP_Maxmgv(interleaved, stride, length);
13. printf("Max magnitude of real parts: %f\n", max_magnitude);  // 输出5.0

15. return FAST_ERROR_CODE_SUCCESS;
16. }
```
