---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/batch-database-operations-guide
title: 批量数据写数据库场景
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 应用多线程开发实践案例 > 批量数据写数据库场景
category: harmonyos-guides
scraped_at: 2026-06-11T14:27:33+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:c38792b330008ced7b946c28147df165a66fefc4d88ed2df76cc04ec469538a3
---

## 使用TaskPool进行频繁数据库操作

对于需要频繁数据库操作的场景，由于读写数据库存在耗时，因此推荐在子线程中操作，避免阻塞UI线程。

通过ArkTS提供的TaskPool能力，可以将数据库操作任务移到子线程中，实现如下。

1. 创建多个子任务，支持数据库的创建、插入、查询和清除等操作。
2. UI主线程发起数据库操作请求，在子线程中完成数据库的增删改查等操作。

```
1. import { relationalStore, ValuesBucket } from '@kit.ArkData';
2. import { collections, taskpool } from '@kit.ArkTS';
3. import { IValueBucket, SharedValuesBucket } from './SharedValuesBucket';

5. @Concurrent
6. async function create(context: Context) {
7. const CONFIG: relationalStore.StoreConfig = {
8. name: 'Store.db',
9. securityLevel: relationalStore.SecurityLevel.S1,
10. };

12. // 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
13. let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
14. console.info(`Create Store.db successfully!`);

16. // 创建表
17. const CREATE_TABLE_SQL = 'CREATE TABLE IF NOT EXISTS test (' +
18. 'id INTEGER PRIMARY KEY AUTOINCREMENT, ' +
19. 'name TEXT NOT NULL, ' +
20. 'age INTEGER, ' +
21. 'salary REAL, ' +
22. 'blobType BLOB)';
23. await store.executeSql(CREATE_TABLE_SQL);
24. console.info(`Create table test successfully!`);
25. }

27. @Concurrent
28. async function insert(context: Context, valueBucketArray: Array<relationalStore.ValuesBucket>) {
29. const CONFIG: relationalStore.StoreConfig = {
30. name: 'Store.db',
31. securityLevel: relationalStore.SecurityLevel.S1,
32. };

34. // 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
35. let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
36. console.info(`Create Store.db successfully!`);

38. // 数据插入
39. await store.batchInsert('test', valueBucketArray as Object as Array<relationalStore.ValuesBucket>);
40. }

42. @Concurrent
43. async function query(context: Context): Promise<Array<relationalStore.ValuesBucket>> {
44. const CONFIG: relationalStore.StoreConfig = {
45. name: 'Store.db',
46. securityLevel: relationalStore.SecurityLevel.S1,
47. };

49. // 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
50. let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
51. console.info(`Create Store.db successfully!`);

53. // 获取结果集
54. let predicates: relationalStore.RdbPredicates = new relationalStore.RdbPredicates('test');
55. let resultSet = await store.query(predicates); // 查询所有数据
56. console.info(`Query data successfully! row count:${resultSet.rowCount}`);
57. let index = 0;
58. let result = new Array<relationalStore.ValuesBucket>(resultSet.rowCount);
59. resultSet.goToFirstRow();
60. do {
61. result[index++] = resultSet.getRow();
62. } while (resultSet.goToNextRow());
63. resultSet.close();
64. return result;
65. }

67. @Concurrent
68. async function clear(context: Context) {
69. const CONFIG: relationalStore.StoreConfig = {
70. name: 'Store.db',
71. securityLevel: relationalStore.SecurityLevel.S1,
72. };

74. // 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
75. await relationalStore.deleteRdbStore(context, CONFIG);
76. console.info(`Delete Store.db successfully!`);
77. }

79. @Entry
80. @Component
81. struct Index {
82. @State message: string = 'Hello World';

84. build() {
85. RelativeContainer() {
86. Text(this.message)
87. .id('HelloWorld')
88. .fontSize(50)
89. .fontWeight(FontWeight.Bold)
90. .alignRules({
91. center: { anchor: '__container__', align: VerticalAlign.Center },
92. middle: { anchor: '__container__', align: HorizontalAlign.Center }
93. })
94. .onClick(async () => {
95. let context: Context = this.getUIContext().getHostContext() as Context;

97. // 数据准备
98. const count = 5
99. let valueBucketArray = collections.Array.create<SharedValuesBucket | undefined>(count, undefined);
100. for (let i = 0; i < count; i++) {
101. let v: IValueBucket = {
102. id: i,
103. name: 'zhangsan' + i,
104. age: 20,
105. salary: 5000 + 50 * i
106. };
107. valueBucketArray[i] = new SharedValuesBucket(v);
108. }
109. await taskpool.execute(create, context);
110. await taskpool.execute(insert, context, valueBucketArray);
111. let index = 0;
112. let ret: collections.Array<SharedValuesBucket> =
113. await taskpool.execute(query, context) as collections.Array<SharedValuesBucket>;
114. for (let v of ret.values()) {
115. console.info(`Row[${index}].id = ${v.id}`)
116. console.info(`Row[${index}].name = ${v.name}`)
117. console.info(`Row[${index}].age = ${v.age}`)
118. console.info(`Row[${index}].salary = ${v.salary}`)
119. index++
120. };
121. await taskpool.execute(clear, context);
122. this.message = 'success';
123. })
124. }
125. .height('100%')
126. .width('100%')
127. }
128. }
```

[UsingSendable.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ApplicationMultithreadingDevelopment/PracticalCases/entry/src/main/ets/managers/UsingSendable.ets#L16-L145)

## 使用Sendable进行大容量数据库操作

由于数据库数据跨线程传递存在耗时，数据量较大时会占用UI主线程。推荐使用Sendable封装数据库数据，以降低跨线程开销。

1. 定义数据库中的数据格式，可以使用Sendable，以减少跨线程操作的耗时。

   ```
   1. export interface IValueBucket {
   2. id: number;
   3. name: string;
   4. age: number;
   5. salary: number;
   6. }

   8. @Sendable
   9. export class SharedValuesBucket implements IValueBucket {
   10. public id: number = 0;
   11. public name: string = '';
   12. public age: number = 0;
   13. public salary: number = 0;

   15. constructor(v: IValueBucket) {
   16. this.id = v.id;
   17. this.name = v.name;
   18. this.age = v.age;
   19. this.salary = v.salary;
   20. }
   21. }
   ```

   [SharedValuesBucket.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ApplicationMultithreadingDevelopment/PracticalCases/entry/src/main/ets/managers/SharedValuesBucket.ets#L16-L38)
2. UI主线程发起数据库操作请求，在子线程完成数据的增删改查等操作。

   ```
   1. import { relationalStore, ValuesBucket } from '@kit.ArkData';
   2. import { taskpool } from '@kit.ArkTS';

   4. @Concurrent
   5. async function create(context: Context) {
   6. const CONFIG: relationalStore.StoreConfig = {
   7. name: 'Store.db',
   8. securityLevel: relationalStore.SecurityLevel.S1,
   9. };

   11. // 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
   12. let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
   13. console.info(`Create Store.db successfully!`);

   15. // 创建表
   16. const CREATE_TABLE_SQL = 'CREATE TABLE IF NOT EXISTS test (' +
   17. 'id INTEGER PRIMARY KEY AUTOINCREMENT, ' +
   18. 'name TEXT NOT NULL, ' +
   19. 'age INTEGER, ' +
   20. 'salary REAL, ' +
   21. 'blobType BLOB)';
   22. await store.executeSql(CREATE_TABLE_SQL);
   23. console.info(`Create table test successfully!`);
   24. }

   26. @Concurrent
   27. async function insert(context: Context, valueBucketArray: Array<relationalStore.ValuesBucket>) {
   28. const CONFIG: relationalStore.StoreConfig = {
   29. name: 'Store.db',
   30. securityLevel: relationalStore.SecurityLevel.S1,
   31. };

   33. // 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
   34. let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
   35. console.info(`Create Store.db successfully!`);

   37. // 数据插入
   38. await store.batchInsert('test', valueBucketArray as Object as Array<relationalStore.ValuesBucket>);
   39. }

   41. @Concurrent
   42. async function query(context: Context): Promise<Array<relationalStore.ValuesBucket>> {
   43. const CONFIG: relationalStore.StoreConfig = {
   44. name: 'Store.db',
   45. securityLevel: relationalStore.SecurityLevel.S1,
   46. };

   48. // 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
   49. let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
   50. console.info(`Create Store.db successfully!`);

   52. // 获取结果集
   53. let predicates: relationalStore.RdbPredicates = new relationalStore.RdbPredicates('test');
   54. let resultSet = await store.query(predicates); // 查询所有数据
   55. console.info(`Query data successfully! row count:${resultSet.rowCount}`);
   56. let index = 0;
   57. let result = new Array<relationalStore.ValuesBucket>(resultSet.rowCount)
   58. resultSet.goToFirstRow()
   59. do {
   60. result[index++] = resultSet.getRow();
   61. } while (resultSet.goToNextRow());
   62. resultSet.close();
   63. return result;
   64. }

   66. @Concurrent
   67. async function clear(context: Context) {
   68. const CONFIG: relationalStore.StoreConfig = {
   69. name: 'Store.db',
   70. securityLevel: relationalStore.SecurityLevel.S1,
   71. };

   73. // 默认数据库文件路径为 context.databaseDir + rdb + StoreConfig.name
   74. await relationalStore.deleteRdbStore(context, CONFIG);
   75. console.info(`Delete Store.db successfully!`);
   76. }

   78. @Entry
   79. @Component
   80. struct Index {
   81. @State message: string = 'Hello World';

   83. build() {
   84. RelativeContainer() {
   85. Text(this.message)
   86. .id('HelloWorld')
   87. .fontSize(50)
   88. .fontWeight(FontWeight.Bold)
   89. .alignRules({
   90. center: { anchor: '__container__', align: VerticalAlign.Center },
   91. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   92. })
   93. .onClick(async () => {
   94. let context: Context = this.getUIContext().getHostContext() as Context;

   96. // 数据准备
   97. const count = 5
   98. let valueBucketArray = new Array<relationalStore.ValuesBucket>(count);
   99. for (let i = 0; i < count; i++) {
   100. let v: relationalStore.ValuesBucket = {
   101. id: i,
   102. name: 'zhangsan' + i,
   103. age: 20,
   104. salary: 5000 + 50 * i
   105. };
   106. valueBucketArray[i] = v;
   107. }
   108. await taskpool.execute(create, context);
   109. await taskpool.execute(insert, context, valueBucketArray);
   110. let index = 0;
   111. let ret = await taskpool.execute(query, context) as Array<relationalStore.ValuesBucket>;
   112. for (let v of ret) {
   113. console.info(`Row[${index}].id = ${v.id}`)
   114. console.info(`Row[${index}].name = ${v.name}`)
   115. console.info(`Row[${index}].age = ${v.age}`)
   116. console.info(`Row[${index}].salary = ${v.salary}`)
   117. index++
   118. };
   119. await taskpool.execute(clear, context);
   120. this.message = 'success';
   121. })
   122. }
   123. .height('100%')
   124. .width('100%')
   125. }
   126. }
   ```

   [UsingTaskPool.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ApplicationMultithreadingDevelopment/PracticalCases/entry/src/main/ets/managers/UsingTaskPool.ets#L16-L143)

## 复杂类实例对象使用Sendable进行大容量数据库操作

普通类实例对象的属性可持有Sendable类实例对象。

对于复杂的普通类实例对象，可以先将相应数据库数据字段封装为Sendable类实例对象，再由普通类实例对象持有，从而降低跨线程开销。

1. 定义数据库中的数据格式，采用Sendable，减少跨线程耗时。

   ```
   1. export interface IValueBucket {
   2. id: number;
   3. name: string;
   4. age: number;
   5. salary: number;
   6. }

   8. @Sendable
   9. export class SharedValuesBucket implements IValueBucket {
   10. public id: number = 0;
   11. public name: string = '';
   12. public age: number = 0;
   13. public salary: number = 0;

   15. constructor(v: IValueBucket) {
   16. this.id = v.id;
   17. this.name = v.name;
   18. this.age = v.age;
   19. this.salary = v.salary;
   20. }
   21. }
   ```

   [SharedValuesBucket.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ApplicationMultithreadingDevelopment/PracticalCases/entry/src/main/ets/managers/SharedValuesBucket.ets#L16-L38)
2. 定义普通类实例对象，持有Sendable类实例对象。

   ```
   1. import { SharedValuesBucket } from './SharedValuesBucket';
   2. import { collections } from '@kit.ArkTS';

   4. export class Material {
   5. public seq: number = 0;
   6. public materialName: string = '';
   7. // ... 省略其他属性
   8. public buckets: collections.Array<SharedValuesBucket | undefined>;

   10. constructor(seq: number, materialName: string, buckets: collections.Array<SharedValuesBucket | undefined>) {
   11. this.seq = seq;
   12. this.materialName = materialName;
   13. this.buckets = buckets;
   14. }

   16. getBuckets() : collections.Array<SharedValuesBucket | undefined>{
   17. return this.buckets;
   18. }

   20. setBuckets(buckets: collections.Array<SharedValuesBucket | undefined>) {
   21. this.buckets = buckets;
   22. }
   23. }
   ```

   [Material.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ApplicationMultithreadingDevelopment/PracticalCases/entry/src/main/ets/managers/Material.ets#L16-L40)
3. UI主线程发起数据库操作请求，在子线程进行数据的增删改查等操作。

   ```
   1. import { relationalStore, ValuesBucket } from '@kit.ArkData';
   2. import { collections, taskpool } from '@kit.ArkTS';
   3. import { IValueBucket, SharedValuesBucket } from './SharedValuesBucket';
   4. import { Material } from './Material';

   6. @Concurrent
   7. async function create(context: Context): Promise<boolean> {
   8. const CONFIG: relationalStore.StoreConfig = {
   9. name: 'Store.db',
   10. securityLevel: relationalStore.SecurityLevel.S1,
   11. };

   13. try {
   14. // 默认数据库文件路径为 context.databaseDir + "/rdb/" + StoreConfig.name
   15. let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
   16. console.info('Create Store.db successfully!');

   18. // 创建表
   19. const CREATE_TABLE_SQL = 'CREATE TABLE IF NOT EXISTS test (' +
   20. 'id INTEGER PRIMARY KEY AUTOINCREMENT, ' +
   21. 'name TEXT NOT NULL, ' +
   22. 'age INTEGER, ' +
   23. 'salary REAL, ' +
   24. 'blobType BLOB)';
   25. await store.executeSql(CREATE_TABLE_SQL);
   26. console.info('Create table test successfully!');
   27. return true;
   28. } catch (err) {
   29. console.error(`Create db failed, code: ${err.code}, message: ${err.message}`);
   30. return false;
   31. }
   32. }

   34. @Concurrent
   35. async function insert(context: Context, valueBucketArray: collections.Array<SharedValuesBucket | undefined>) {
   36. const CONFIG: relationalStore.StoreConfig = {
   37. name: 'Store.db',
   38. securityLevel: relationalStore.SecurityLevel.S1,
   39. };

   41. // 默认数据库文件路径为 context.databaseDir + "/rdb/" + StoreConfig.name
   42. let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
   43. console.info('Create Store.db successfully!');

   45. // 数据插入
   46. await store.batchInsert('test', valueBucketArray as Object as Array<ValuesBucket>);
   47. }

   49. @Concurrent
   50. async function query(context: Context): Promise<collections.Array<SharedValuesBucket | undefined>> {
   51. const CONFIG: relationalStore.StoreConfig = {
   52. name: 'Store.db',
   53. securityLevel: relationalStore.SecurityLevel.S1,
   54. };

   56. // 默认数据库文件路径为 context.databaseDir + "/rdb/" + StoreConfig.name
   57. let store: relationalStore.RdbStore = await relationalStore.getRdbStore(context, CONFIG);
   58. console.info('Create Store.db successfully!');

   60. // 获取用于查询的谓词
   61. let predicates: relationalStore.RdbPredicates = new relationalStore.RdbPredicates('test');
   62. // 查询所有数据
   63. let resultSet = await store.query(predicates);
   64. console.info(`Query data successfully! row count:${resultSet.rowCount}`);
   65. let index = 0;
   66. let result = collections.Array.create<SharedValuesBucket | undefined>(resultSet.rowCount, undefined);
   67. resultSet.goToFirstRow();
   68. do {
   69. let value: IValueBucket = {
   70. id: resultSet.getLong(resultSet.getColumnIndex('id')),
   71. name: resultSet.getString(resultSet.getColumnIndex('name')),
   72. age: resultSet.getLong(resultSet.getColumnIndex('age')),
   73. salary: resultSet.getLong(resultSet.getColumnIndex('salary'))
   74. };
   75. result[index++] = new SharedValuesBucket(value);
   76. } while (resultSet.goToNextRow());
   77. resultSet.close();
   78. return result;
   79. }

   81. @Concurrent
   82. async function deleteStore(context: Context) {
   83. const CONFIG: relationalStore.StoreConfig = {
   84. name: 'Store.db',
   85. securityLevel: relationalStore.SecurityLevel.S1,
   86. };

   88. // 默认数据库文件路径为 context.databaseDir + "/rdb/" + StoreConfig.name
   89. await relationalStore.deleteRdbStore(context, CONFIG);
   90. console.info('Delete Store.db successfully!');
   91. }

   93. function initMaterial(): Material {
   94. // 数据准备
   95. const count = 5;
   96. let valueBucketArray = collections.Array.create<SharedValuesBucket | undefined>(count, undefined);
   97. for (let i = 0; i < count; i++) {
   98. let value: IValueBucket = {
   99. id: i,
   100. name: 'zhangsan' + i,
   101. age: 20,
   102. salary: 5000 + 50 * i
   103. };
   104. valueBucketArray[i] = new SharedValuesBucket(value);
   105. }
   106. let material = new Material(1, 'test', valueBucketArray);
   107. return material;
   108. }

   110. @Entry
   111. @Component
   112. struct Index {
   113. @State message: string = 'Hello World';

   115. build() {
   116. RelativeContainer() {
   117. Text(this.message)
   118. .id('HelloWorld')
   119. .fontSize(50)
   120. .fontWeight(FontWeight.Bold)
   121. .alignRules({
   122. center: { anchor: '__container__', align: VerticalAlign.Center },
   123. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   124. })
   125. .onClick(async () => {
   126. let context: Context = this.getUIContext().getHostContext() as Context;
   127. let material = initMaterial();
   128. let ret = await taskpool.execute(create, context);
   129. if (!ret) {
   130. console.error('Create db failed.');
   131. return;
   132. }
   133. await taskpool.execute(insert, context, material.getBuckets());
   134. let index = 0;
   135. let resultSet: collections.Array<SharedValuesBucket> =
   136. await taskpool.execute(query, context) as collections.Array<SharedValuesBucket>;
   137. material.setBuckets(resultSet);
   138. for (let value of resultSet.values()) {
   139. console.info(`Row[${index}].id = ${value.id}`);
   140. console.info(`Row[${index}].name = ${value.name}`);
   141. console.info(`Row[${index}].age = ${value.age}`);
   142. console.info(`Row[${index}].salary = ${value.salary}`);
   143. index++;
   144. }
   145. await taskpool.execute(deleteStore, context);
   146. })
   147. }
   148. .height('100%')
   149. .width('100%')
   150. }
   151. }
   ```

   [ComplexClassInstanceObjectUsingSendable.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/ArkTsConcurrent/ApplicationMultithreadingDevelopment/PracticalCases/entry/src/main/ets/managers/ComplexClassInstanceObjectUsingSendable.ets#L16-L169)
