---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/container-object
title: 容器类对象
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信对象 > 容器类对象
category: harmonyos-guides
scraped_at: 2026-06-01T11:01:10+08:00
doc_updated_at: 2026-05-28
content_hash: sha256:af16f74d4ac7e0104c9af6632a7a18310608555994c361c7f4d7aff46d714914
---
容器类对象在跨线程传递时，可通过序列化的机制，确保跨线程间的数据一致，从而实现跨线程数据传递。

支持序列化的容器类对象和支持的初始版本可以参考[容器类对象支持情况](container-object.md#容器类对象支持情况)。

容器类对象中的成员必须是序列化支持的类型，序列化支持类型可以参考[线程间通信对象概述](../线程间通信对象概述/serializable-overview.md)中的相关对象。

说明

* 容器类对象跨线程传递时，只能传递数据，自定义方法会丢失。如果需要自定义方法，则需要使用[@Sendable装饰器](../Sendable对象/Sendable对象简介/arkts-sendable.md#sendable装饰器)标识为Sendable function后，自定义方法可以跨线程传递。

## 容器类对象支持情况

以下仅针对容器类对象，普通对象（Array、Map、Set等）的支持情况请参考[普通对象](../普通对象/normal-object.md)。

| 容器类名称 | 支持版本 |
| --- | --- |
| [TreeSet](<../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util.TreeSet (非线性容器TreeSet)/js-apis-treeset.md>) | 搭载HarmonyOS 6.1.0及以上版本的设备支持 |
| [ArrayList](<../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util.ArrayList (线性容器ArrayList)/js-apis-arraylist.md>) | 暂不支持 |
| [List](<../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util.List (线性容器List)/js-apis-list.md>) | 暂不支持 |
| [LinkedList](<../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util.LinkedList (线性容器LinkedList)/js-apis-linkedlist.md>) | 暂不支持 |
| [Deque](<../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util.Deque (线性容器Deque)/js-apis-deque.md>) | 暂不支持 |
| [Queue](<../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util.Queue (线性容器Queue)/js-apis-queue.md>) | 暂不支持 |
| [Stack](<../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util.Stack (线性容器Stack)/js-apis-stack.md>) | 暂不支持 |
| [Vector](<../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/已停止维护的接口/@ohos.util.Vector (线性容器Vector)/js-apis-vector.md>) | 暂不支持 |
| [HashMap](<../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util.HashMap (非线性容器HashMap)/js-apis-hashmap.md>) | 暂不支持 |
| [HashSet](<../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util.HashSet (非线性容器HashSet)/js-apis-hashset.md>) | 暂不支持 |
| [TreeMap](<../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util.TreeMap (非线性容器TreeMap)/js-apis-treemap.md>) | 暂不支持 |
| [LightWeightMap](<../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util.LightWeightMap (非线性容器LightWeightMap)/js-apis-lightweightmap.md>) | 暂不支持 |
| [LightWeightSet](<../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util.LightWeightSet (非线性容器LightWeightSet)/js-apis-lightweightset.md>) | 暂不支持 |
| [PlainArray](<../../../../../../../harmonyos-references/ArkTS（方舟编程语言）/ArkTS API/@ohos.util.PlainArray (非线性容器PlainArray)/js-apis-plainarray.md>) | 暂不支持 |

## 使用示例

```
1. import { taskpool, TreeSet } from '@kit.ArkTS';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Sendable
5. function sendableCompareFunc(firstValue: number, secondValue: number): boolean {
6. return firstValue > secondValue;
7. }

9. @Concurrent
10. function treeSetTestFunc(treeSet: TreeSet<number>) {
11. for (let value of treeSet) {
12. console.info('value:', value);
13. }
14. }

16. @Entry
17. @Component
18. struct Index {
19. @State message: string = 'Hello World';

21. build() {
22. RelativeContainer() {
23. Text(this.message)
24. .id('HelloWorld')
25. .fontSize(50)
26. .fontWeight(FontWeight.Bold)
27. .alignRules({
28. center: { anchor: '__container__', align: VerticalAlign.Center },
29. middle: { anchor: '__container__', align: HorizontalAlign.Center }
30. })
31. .onClick(() => {
32. // 1. 创建TreeSet实例
33. let treeSet: TreeSet<number> = new TreeSet<number>(sendableCompareFunc);

35. treeSet.add(1);
36. treeSet.add(5);
37. treeSet.add(3);
38. treeSet.add(2);
39. // 2. 创建任务task，将treeSet传递给该任务，通过序列化传递给子线程
40. let task = new taskpool.Task(treeSetTestFunc, treeSet);
41. // 3. 执行任务
42. taskpool.execute(task).then(() => {
43. console.info('taskpool: execute task success!');
44. }).catch((e: BusinessError) => {
45. console.error(`taskpool: execute task: Code: ${e.code}, message: ${e.message}`);
46. })
47. this.message = 'success';
48. })
49. }
50. .height('100%')
51. .width('100%')
52. }
53. }
```

[ContainerObject.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ConcurrentThreadCommunication/InterThreadCommunicationObjects/CommunicationObjects/entry/src/main/ets/managers/ContainerObject.ets#L16-L70)
