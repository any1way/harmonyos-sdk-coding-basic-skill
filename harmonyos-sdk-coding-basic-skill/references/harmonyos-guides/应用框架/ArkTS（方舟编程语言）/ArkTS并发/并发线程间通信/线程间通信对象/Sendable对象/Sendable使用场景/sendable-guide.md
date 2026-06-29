---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/sendable-guide
title: Sendable使用场景
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 并发线程间通信 > 线程间通信对象 > Sendable对象 > Sendable使用场景
category: harmonyos-guides
scraped_at: 2026-06-11T14:27:14+08:00
doc_updated_at: 2026-06-03
content_hash: sha256:79217a67294f47f7507991bc7e79d76d6772f78fc3ed8c12d6c7ff078bc33386
---
Sendable对象在不同并发实例间默认采用引用传递，这种方式比序列化更高效，且不会丢失类成员方法。因此，Sendable能够解决两个关键场景的问题：

* 跨并发实例传输大数据（例如达到100KB以上的数据）。
* 跨并发实例传递带方法的class实例对象。

## 跨并发实例传输大数据场景

由于跨并发实例序列化的开销随数据量线性增长，因此当传输数据量较大时（100KB的数据传输耗时约为1ms），跨并发实例的拷贝开销会影响应用性能。使用引用传递方式传输对象可提升性能。

**示例：**

```
1. import { taskpool } from '@kit.ArkTS';
2. import { TestTypeA, TestTypeB, Test } from './sendable';
3. import { BusinessError, emitter } from '@kit.BasicServicesKit';

5. // 在并发函数中模拟数据处理
6. @Concurrent
7. async function taskFunc(obj: Test) {
8. console.info('test task res1 is: ' + obj.data1.name + ' res2 is: ' + obj.data2.name);
9. }

11. async function test() {
12. // 使用taskpool传递数据
13. let a: TestTypeA = new TestTypeA('testTypeA');
14. let b: TestTypeB = new TestTypeB('testTypeB');
15. let obj: Test = new Test(a, b);
16. let task: taskpool.Task = new taskpool.Task(taskFunc, obj);
17. await taskpool.execute(task);
18. }

20. @Concurrent
21. function sensorListener() {
22. // 监听逻辑
23. // ...
24. console.info('Monitoring logic');
25. }

27. @Entry
28. @Component
29. struct Index {
30. @State listenerTask: string = 'Listener task';
31. @State dataProcessingTask: string = 'Data processing task';

33. build() {
34. Column() {
35. Text(this.listenerTask)
36. .id('Listener task')
37. .fontSize(50)
38. .fontWeight(FontWeight.Bold)
39. .onClick(() => {
40. let sensorTask = new taskpool.LongTask(sensorListener);
41. emitter.on({ eventId: 0 }, (data) => {
42. // Do something here
43. console.info(`Receive ACCELEROMETER data: {${data.data?.x}, ${data.data?.y}, ${data.data?.z}}`);
44. });
45. taskpool.execute(sensorTask).then(() => {
46. console.info('Add listener of ACCELEROMETER success');
47. }).catch((e: BusinessError) => {
48. // Process error
49. })
50. this.listenerTask = 'success';
51. })
52. Text(this.dataProcessingTask)
53. .id('Data processing task')
54. .fontSize(50)
55. .fontWeight(FontWeight.Bold)
56. .onClick(() => {
57. test();
58. this.dataProcessingTask = 'success';
59. })
60. }
61. .height('100%')
62. .width('100%')
63. }
64. }
```

```
1. // 将数据量较大的数据在Sendable class中组装
2. @Sendable
3. export class TestTypeA {
4. public name: string = 'A';
5. constructor(name: string) {
6. this.name = name;
7. }
8. }

10. @Sendable
11. export class TestTypeB {
12. public name: string = 'B';
13. constructor(name: string) {
14. this.name = name;
15. }
16. }

18. @Sendable
19. export class Test {
20. public data1: TestTypeA;
21. public data2: TestTypeB;
22. constructor(arg1: TestTypeA, arg2: TestTypeB) {
23. this.data1 = arg1;
24. this.data2 = arg2;
25. }
26. }
```

## 跨并发实例传递带方法的class实例对象

在序列化传输实例对象时，会丢失方法。因此，若需调用实例方法，应使用引用传递。处理数据时，若需解析数据，可使用[ASON工具](../ASON解析与生成/ason-parsing-generation.md)。

**示例：**

```
1. import { taskpool, ArkTSUtils } from '@kit.ArkTS';
2. import { SendableTestClass, ISendable } from './sendable';

4. // 在并发函数中模拟数据处理
5. @Concurrent
6. async function taskFunc(sendableObj: SendableTestClass) {
7. console.info('SendableTestClass: name is: ' + sendableObj.printName() + ', age is: ' + sendableObj.printAge() +
8. ', sex is: ' + sendableObj.printSex());
9. sendableObj.setAge(28);
10. console.info('SendableTestClass: age is: ' + sendableObj.printAge());

12. // 解析sendableObj.arr数据生成JSON字符串
13. let str = ArkTSUtils.ASON.stringify(sendableObj.arr);
14. console.info('SendableTestClass: str is: ' + str);

16. // 解析该数据并生成ISendable数据
17. let jsonStr = '{"name": "Alexa", "age": 23, "sex": "female"}';
18. let obj = ArkTSUtils.ASON.parse(jsonStr) as ISendable;
19. console.info('SendableTestClass: type is: ' + typeof obj);
20. console.info('SendableTestClass: name is: ' + (obj as object)?.['name']); // 输出: 'Alexa'
21. console.info('SendableTestClass: age is: ' + (obj as object)?.['age']); // 输出: 23
22. console.info('SendableTestClass: sex is: ' + (obj as object)?.['sex']); // 输出: 'female'
23. }

25. async function test() {
26. // 使用taskpool传递数据
27. let obj: SendableTestClass = new SendableTestClass();
28. let task: taskpool.Task = new taskpool.Task(taskFunc, obj);
29. await taskpool.execute(task);
30. }

32. @Entry
33. @Component
34. struct Index {
35. @State message: string = 'Hello World';

37. build() {
38. RelativeContainer() {
39. Text(this.message)
40. .id('HelloWorld')
41. .fontSize(50)
42. .fontWeight(FontWeight.Bold)
43. .alignRules({
44. center: { anchor: '__container__', align: VerticalAlign.Center },
45. middle: { anchor: '__container__', align: HorizontalAlign.Center }
46. })
47. .onClick(() => {
48. test();
49. this.message = 'success';
50. })
51. }
52. .height('100%')
53. .width('100%')
54. }
55. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ConcurrentThreadCommunication/InterThreadCommunicationObjects/SendableObject/SendableScenarios/crossconcurrency/src/main/ets/pages/Index.ets#L16-L72)

```
1. // 定义模拟类Test，模仿开发过程中需传递带方法的class
2. import { lang, collections } from '@kit.ArkTS'

4. export type ISendable = lang.ISendable;

6. @Sendable
7. export class SendableTestClass {
8. public name: string = 'John';
9. public age: number = 20;
10. public sex: string = 'man';
11. public arr: collections.Array<number> = new collections.Array<number>(1, 2, 3);

13. constructor() {
14. }

16. setAge(age: number): void {
17. this.age = age;
18. }

20. printName(): string {
21. return this.name;
22. }

24. printAge(): number {
25. return this.age;
26. }

28. printSex(): string {
29. return this.sex;
30. }
31. }
```

[sendable.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ConcurrentThreadCommunication/InterThreadCommunicationObjects/SendableObject/SendableScenarios/crossconcurrency/src/main/ets/pages/sendable.ets#L16-L48)
