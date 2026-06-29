---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-58
title: 使用HiLog打印日志是否有长度限制
breadcrumb: FAQ > 应用质量 > 技术质量 > 运维 > 使用HiLog打印日志是否有长度限制
category: harmonyos-faqs
scraped_at: 2026-06-12T10:19:57+08:00
doc_updated_at: 2026-05-22
content_hash: sha256:79e128eb966392381959cb86824e952d70da63d3ee701041a0d99ff6900bebd5
---

使用HiLog进行日志打印时，最多支持4096字节，超出部分将被截断。

利用HiLog封装日志打印工具类，解决日志信息过长的问题。

示例如下：

封装LogUtil类：

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const HILOG_MAX_BYTES = 4096;

5. // Split the string by byte limit.
6. function splitByByteLimit(str: string, limit: number): string[] {
7. const result: string[] = [];
8. let start = 0;
9. while (start < str.length) {
10. let end = start;
11. let byteLen = 0;
12. while (end < str.length) {
13. const code = str.charCodeAt(end);
14. let charBytes: number;
15. if (code < 0x80) {
16. charBytes = 1;
17. } else if (code < 0x800) {
18. charBytes = 2;
19. } else if (code < 0xD800 || code > 0xDFFF) {
20. charBytes = 3;
21. } else {
22. charBytes = 4;
23. end++;
24. }
25. if (byteLen + charBytes > limit) break;
26. byteLen += charBytes;
27. end++;
28. }
29. result.push(str.substring(start, end));
30. start = end;
31. }
32. return result;
33. }

35. function printSegments(level: string, logTag: string, content: string): void {
36. const segments = splitByByteLimit(content, HILOG_MAX_BYTES);
37. for (const seg of segments) {
38. switch (level) {
39. case 'error':
40. hilog.error(0x0000, logTag, '%{public}s', seg);
41. break;
42. case 'debug':
43. hilog.debug(0x0000, logTag, '%{public}s', seg);
44. break;
45. case 'info':
46. hilog.info(0x0000, logTag, '%{public}s', seg);
47. break;
48. }
49. }
50. }

52. class LogUtil {
53. private static instance: LogUtil;

55. private constructor() {
56. }

58. public static getInstance(): LogUtil {
59. if (!LogUtil.instance) {
60. LogUtil.instance = new LogUtil();
61. }
62. return LogUtil.instance;
63. }

65. public logError(logTag: string, content: string) {
66. printSegments('error', logTag, content);
67. }

69. public logDebug(logTag: string, content: string) {
70. printSegments('debug', logTag, content);
71. }

73. public logInfo(logTag: string, content: string) {
74. printSegments('info', logTag, content);
75. }
76. }

78. export default LogUtil;
```

[LogUtilClass.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AnalysisKit/entry/src/main/ets/pages/LogUtilClass.ets#L21-L98)

使用：

```
1. import LogUtil from './LogUtilClass';

3. @Entry
4. @Component
5. struct HiLogIsThereALengthLimit {

7. build() {
8. Row() {
9. Column() {
10. Button('hilog util')
11. .onClick(() => {
12. let str = 'Long log content';
13. let utilInfo = LogUtil.getInstance();
14. utilInfo.logInfo('testTag', str);
15. })
16. }
17. .width('100%')
18. }
19. .height('100%')
20. }
21. }
```

[HiLogIsThereALengthLimit.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AnalysisKit/entry/src/main/ets/pages/HiLogIsThereALengthLimit.ets#L21-L41)
