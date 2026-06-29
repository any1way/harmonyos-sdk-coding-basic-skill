---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-napi-about-object
title: 使用Node-API接口进行object相关开发
breadcrumb: 指南 > NDK开发 > 代码开发 > 使用Node-API实现ArkTS/JS与C/C++语言交互 > Node-API使用指导 > 使用Node-API接口进行object相关开发
category: harmonyos-guides
scraped_at: 2026-06-01T15:15:18+08:00
doc_updated_at: 2026-05-28
content_hash: sha256:aad32f1ac34304b1f2422c350140d3fe78f9580d556dd0cd4624d1511b871ebe
---
## 简介

Node-API提供了相关接口对object进行基本操作，例如创建对象、获取原型、冻结和密封对象，检查对象的类型等。

## 基本概念

在Node-API接口开发中，经常需要定义和操作对象。例如，创建一个API接口，该接口接受一个对象作为输入参数，对该对象执行某些操作，并返回一个结果对象。在这个过程中，需要确保接口的定义清晰、规范，并且与对象的属性和方法相兼容。

* **接口（API）**：接口定义了组件之间的交互协议，包括输入参数、输出结果以及可能的错误处理。通过接口，组件可以相互调用和交换数据，而无需了解对方的内部实现细节。
* **对象（Object）**：在ArkTS中，对象是一种复合数据类型，允许存储多个不同类型的值作为一个单独的实体。对象是属性和方法的集合。属性是与对象相关联的值，而方法则是对象可以执行的操作。

## 场景和功能介绍

以下Node-API接口主要用于操作和管理ArkTS对象，使用场景介绍：

| 接口 | 描述 |
| --- | --- |
| napi\_get\_prototype | 当需要获取一个ArkTS对象的原型时，可以使用这个接口。通过这个接口可以在C/C++中获取到这个原型对象。 |
| napi\_create\_object | 在Node-API模块中创建一个默认的ArkTS对象。 |
| napi\_object\_freeze | 当需要确保一个对象不会被修改时（immutable），可以使用这个接口来冻结该对象，使其属性不可更改。 |
| napi\_object\_seal | 类似于napi\_object\_freeze，napi\_object\_seal用于密封给定的对象，使其属性不可添加或删除，但可以修改属性的值。 |
| napi\_typeof | 在处理传入的ArkTS值时，可以使用这个接口来获取其类型，以便进行相应的处理。 |
| napi\_instanceof | 当需要在Node-API模块中确定一个对象是否为特定构造函数的实例时，可以使用这个接口。 |
| napi\_type\_tag\_object | 可以将指针的特定值与ArkTS对象关联起来，这对于一些自定义的内部对象标记非常有用。 |
| napi\_check\_object\_type\_tag | 使用此接口可以检查给定的对象上是否关联了特定类型的标记。 |
| napi\_create\_symbol | 创建一个ArkTS Symbol对象。 |
| napi\_create\_external | 用于创建一个ArkTS外部对象，该对象可以用于将C/C++中的自定义数据结构或对象传递到ArkTS中，并且可以在ArkTS中访问其属性和方法。 |
| napi\_get\_value\_external | 用于获得napi\_create\_external创建的绑定了外部数据的ArkTS值，此函数可以在ArkTS和C/C++之间传递数据。 |

这些接口为开发人员提供了在Node-API模块中处理ArkTS对象的灵活性和功能性，可以实现从创建对象、管理对象属性和类型检查等多种操作。

## 使用示例

Node-API接口开发流程参考[使用Node-API实现跨语言交互开发流程](../../使用Node-API实现跨语言交互开发流程/use-napi-process.md)，本文仅对接口对应C++及ArkTS相关代码进行展示。

### napi\_get\_prototype

可以获得给定ArkTS对象的prototype。

cpp部分代码

```
1. // napi_get_prototype
2. static napi_value GetPrototype(napi_env env, napi_callback_info info)
3. {
4. // 获取并解析传参
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. napi_value result = nullptr;
9. // 获取此对象的原型对象，将结果返回到napi_value类型的变量result中
10. napi_get_prototype(env, args[0], &result);
11. return result;
12. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/cpp/napi_init.cpp#L21-L34)

接口声明

```
1. export const getPrototype: (object: Object) => Object; // napi_get_prototype
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/cpp/types/libentry/Index.d.ts#L16-L18)

ArkTS侧示例代码

```
1. class Person {
2. // 属性
3. name: string;
4. age: number;
5. // 构造函数
6. constructor(name: string, age: number) {
7. this.name = name;
8. this.age = age;
9. }
10. }
11. // 创建类的实例
12. const person = new Person('Alice', 30);
13. // 传入实例对象，获取该对象的原型
14. let applePrototype = testNapi.getPrototype(person);
15. // 判断通过testNapi.getPrototype()函数获取到的原型是不是apple的原型
16. // 在DevEco Studio 4.1及以后的版本中，由于ArkTS没有原型的概念，
17. // 因此尝试进行原型赋值或相关操作时，
18. // 将会触发错误提示'Prototype assignment is not supported (arkts-no-prototype-assignment)'，
19. // 以下代码需在ts文件中执行
20. if (applePrototype === Person.prototype) {
21. hilog.info(0x0000, 'Node-API', 'get_prototype_success');
22. } else {
23. hilog.error(0x0000, 'Node-API', 'get_prototype_fail');
24. }
```

[napiGetPrototype.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/ets/pages/napiGetPrototype.ts#L20-L45)

### napi\_create\_object

用于在Node-API模块中创建一个空的ArkTS对象。

cpp部分代码

```
1. // napi_create_object
2. napi_value NewObject(napi_env env, napi_callback_info info)
3. {
4. napi_value object = nullptr;
5. // 创建一个空对象
6. napi_create_object(env, &object);
7. // 设置对象的属性
8. napi_value name = nullptr;
9. // 设置属性名为"name"
10. napi_create_string_utf8(env, "name", NAPI_AUTO_LENGTH, &name);
11. napi_value value = nullptr;
12. // 设置属性值为"Hello from Node-API!"
13. napi_create_string_utf8(env, "Hello from Node-API!", NAPI_AUTO_LENGTH, &value);
14. // 将属性设置到对象上
15. napi_set_property(env, object, name, value);
16. return object;
17. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/cpp/napi_init.cpp#L36-L54)

接口声明

```
1. export const createObject: () => { name: string }; // napi_create_object
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/cpp/types/libentry/Index.d.ts#L20-L22)

ArkTS侧示例代码

```
1. // napi_create_object
2. try {
3. const myObject = testNapi.createObject();
4. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_object: %{public}s', myObject.name);
5. // ...
6. } catch (error) {
7. hilog.error(0x0000, 'testTag',
8. 'Test Node-API napi_create_object errorCode: %{public}s, errorMessage: %{public}s', error.code,
9. error.message);
10. // ...
11. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/ets/pages/Index.ets#L75-L91)

### napi\_object\_freeze

用于冻结给定的ArkTS对象。冻结对象后，无法再向对象添加新的属性或方法，也无法修改已有属性或方法的值。

cpp部分代码

```
1. // napi_object_freeze
2. static napi_value ObjectFreeze(napi_env env, napi_callback_info info)
3. {
4. // 接受一个ArkTS侧传入的object
5. size_t argc = 1;
6. napi_value argv[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);

9. // 调用接口napi_object_freeze将传入的object冻结
10. napi_value objFreeze = argv[0];
11. napi_status status = napi_object_freeze(env, objFreeze);
12. if (status == napi_ok) {
13. OH_LOG_INFO(LOG_APP, "Node-API napi_object_freeze success");
14. }
15. // 将冻结后的object传回ArkTS侧
16. return objFreeze;
17. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/cpp/napi_init.cpp#L56-L74)

接口声明

```
1. export interface Obj {
2. data: number
3. message: string
4. }

6. export const objectFreeze: (objFreeze: Object) => Obj; // napi_object_freeze
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/cpp/types/libentry/Index.d.ts#L24-L31)

ArkTS侧示例代码

```
1. // napi_object_freeze
2. try {
3. class Obj {
4. public data: number = 0
5. public message: string = ''
6. }

8. let obj: Obj = { data: 0, message: 'hello world' };
9. let objFreeze = testNapi.objectFreeze(obj);
10. hilog.info(0x0000, 'testTag', 'Test Node-API napi_object_freeze: %{public}s', (objFreeze.data = 1));
11. // ...
12. } catch (error) {
13. hilog.error(0x0000, 'testTag', 'Test Node-API napi_object_freeze error: %{public}s', error.message);
14. // ...
15. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/ets/pages/Index.ets#L93-L113)

### napi\_object\_seal

封闭一个对象后，无法向其添加新的属性，也无法删除或修改现有属性的可配置性。但是，可以继续修改已有属性的值。

cpp部分代码

```
1. // napi_object_seal
2. static napi_value ObjectSeal(napi_env env, napi_callback_info info)
3. {
4. // 接受一个ArkTS侧传入的object
5. size_t argc = 1;
6. napi_value argv[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
8. // 调用接口napi_object_seal将传入的object封闭，使其无法添加新的属性
9. napi_value objSeal = argv[0];
10. napi_status status = napi_object_seal(env, objSeal);
11. if (status == napi_ok) {
12. OH_LOG_INFO(LOG_APP, "Node-API napi_object_seal success");
13. } else {
14. napi_throw_error(env, nullptr, "Node-API napi_object_seal failed");
15. return nullptr;
16. }
17. // 将封闭后的object传回ArkTS侧
18. return objSeal;
19. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/cpp/napi_init.cpp#L76-L96)

接口声明

```
1. export interface Obj1 {
2. data: number
3. message: string
4. id: number
5. }

7. export const objectSeal: (objSeal: Object) => Obj1; // napi_object_seal
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/cpp/types/libentry/Index.d.ts#L33-L41)

ArkTS侧示例代码

```
1. // napi_object_seal
2. try {
3. class Obj {
4. public data: number = 0
5. public message: string = ''
6. // 可选属性
7. public address?: number = 0
8. }

10. let obj: Obj = { data: 0, message: 'hello world' };
11. let objSeal = testNapi.objectSeal(obj);
12. hilog.info(0x0000, 'testTag', 'Test Node-API napi_object_seal: %{public}s', objSeal.message);
13. objSeal.data = 1;
14. hilog.info(0x0000, 'testTag', 'Test Node-API napi_object_seal: %{public}d', objSeal.data);
15. hilog.info(0x0000, 'testTag', 'Test Node-API napi_object_seal: %{public}d', (objSeal.id = 1));
16. // ...
17. } catch (error) {
18. hilog.error(0x0000, 'testTag', 'Test Node-API napi_object_seal error: %{public}s', error.message);
19. // ...
20. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/ets/pages/Index.ets#L115-L140)

### napi\_typeof

这个接口用于获取给定ArkTS value的ArkTS Type。

\*\*注：\*\*napi\_typeof可以判断的类型包含：

| 类型 |
| --- |
| undefined |
| null |
| boolean |
| number |
| string |
| object |
| function |
| bigint |

cpp部分代码

```
1. // napi_typeof
2. static napi_value NapiTypeOf(napi_env env, napi_callback_info info)
3. {
4. // 接受一个入参
5. size_t argc = 1;
6. napi_value args[1] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

9. // 调用napi_typeof判断传入ArkTS参数类型
10. napi_valuetype valueType;
11. napi_status status = napi_typeof(env, args[0], &valueType);
12. if (status != napi_ok) {
13. napi_throw_error(env, nullptr, "Node-API napi_typeof fail");
14. return nullptr;
15. }
16. // 将结果转成napi_value类型返回。
17. napi_value returnValue = nullptr;
18. switch (valueType) {
19. case napi_undefined:
20. napi_create_string_utf8(env, "Input type is napi_undefined", NAPI_AUTO_LENGTH, &returnValue);
21. break;
22. case napi_null:
23. napi_create_string_utf8(env, "Input type is napi_null", NAPI_AUTO_LENGTH, &returnValue);
24. break;
25. case napi_boolean:
26. napi_create_string_utf8(env, "Input type is napi_boolean", NAPI_AUTO_LENGTH, &returnValue);
27. break;
28. case napi_number:
29. napi_create_string_utf8(env, "Input type is napi_number", NAPI_AUTO_LENGTH, &returnValue);
30. break;
31. case napi_string:
32. napi_create_string_utf8(env, "Input type is napi_string", NAPI_AUTO_LENGTH, &returnValue);
33. break;
34. case napi_object:
35. napi_create_string_utf8(env, "Input type is napi_object", NAPI_AUTO_LENGTH, &returnValue);
36. break;
37. case napi_function:
38. napi_create_string_utf8(env, "Input type is napi_function", NAPI_AUTO_LENGTH, &returnValue);
39. break;
40. case napi_bigint:
41. napi_create_string_utf8(env, "Input type is napi_bigint", NAPI_AUTO_LENGTH, &returnValue);
42. break;
43. default:
44. napi_create_string_utf8(env, "unknown", NAPI_AUTO_LENGTH, &returnValue);
45. }
46. return returnValue;
47. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/cpp/napi_init.cpp#L98-L146)

接口声明

```
1. export const napiTypeOf: <T>(value: T) => string | undefined; // napi_typeof
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/cpp/types/libentry/Index.d.ts#L43-L45)

ArkTS侧示例代码

```
1. // napi_typeof
2. try {
3. let varUndefined: undefined;
4. hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s',
5. testNapi.napiTypeOf(varUndefined));
6. let varNull: null = null;
7. hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s',
8. testNapi.napiTypeOf(varNull));
9. let varTrue = true;
10. hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s',
11. testNapi.napiTypeOf(varTrue));
12. let varNum = 1;
13. hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s',
14. testNapi.napiTypeOf(varNum));
15. let varString = 'str';
16. hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s',
17. testNapi.napiTypeOf(varString));

19. class Obj {
20. public id: number = 0
21. public name: string = ''
22. }

24. let varObject: Obj = { id: 1, name: 'LiLei' };
25. hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s',
26. testNapi.napiTypeOf(varObject));
27. const addNum = (a: number, b: number): number => a * b;
28. hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s',
29. testNapi.napiTypeOf(addNum));
30. let varBigint = BigInt('1234567890123456789012345678901234567890');
31. hilog.info(0x0000, 'testTag', 'Test Node-API napi_typeof: %{public}s',
32. testNapi.napiTypeOf(varBigint));
33. // ...
34. } catch (error) {
35. hilog.error(0x0000, 'testTag', 'Test Node-API napi_typeof error: %{public}s', error.message);
36. // ...
37. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/ets/pages/Index.ets#L142-L184)

### napi\_instanceof

用于检查一个对象是否是指定构造函数的实例。

cpp部分代码

```
1. // napi_instanceof
2. static napi_value NapiInstanceOf(napi_env env, napi_callback_info info)
3. {
4. // 接受两个入参
5. size_t argc = 2;
6. napi_value args[2] = {nullptr};
7. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
8. // 调用napi_instanceof接口判断给定object是否为给定constructor的实例
9. bool result = true;
10. napi_status status = napi_instanceof(env, args[0], args[1], &result);
11. if (status != napi_ok) {
12. napi_throw_error(env, nullptr, "Node-API napi_instanceof fail");
13. return nullptr;
14. }
15. // 将结果转成napi_value类型返回
16. napi_value returnValue = nullptr;
17. napi_get_boolean(env, result, &returnValue);

19. return returnValue;
20. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/cpp/napi_init.cpp#L148-L169)

接口声明

```
1. export const napiInstanceOf: (date: Object, construct: Object) => boolean | undefined; // napi_instanceof
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/cpp/types/libentry/Index.d.ts#L47-L49)

ArkTS侧示例代码

```
1. // napi_instanceof
2. try {
3. class Person {
4. public name: string;
5. public age: number;

7. constructor(name: string, age: number) {
8. this.name = name;
9. this.age = age;
10. }
11. }

13. const person = new Person('Alice', 30);

15. class Obj {
16. public data: number = 0
17. public message: string = ''
18. }

20. let obj: Obj = { data: 0, message: 'hello world' };
21. hilog.info(0x0000, 'testTag', 'Test Node-API napi_instanceof: %{public}s',
22. testNapi.napiInstanceOf(person, Person));
23. hilog.info(0x0000, 'testTag', 'Test Node-API napi_instanceof: %{public}s',
24. testNapi.napiInstanceOf(obj, Person));
25. // ...
26. } catch (error) {
27. hilog.error(0x0000, 'testTag', 'Test Node-API napi_instanceof error: %{public}s', error.message);
28. // ...
29. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/ets/pages/Index.ets#L186-L220)

### napi\_type\_tag\_object

使用类型标签type\_tag来标记ArkTS对象，后续可以更精确地识别ArkTS对象。

ArkTS版本中，napi\_type\_tag\_object接口没有使用private symbol，导致type\_tag有被改写的风险，开发者应避免在关键安全场景中使用该接口。

### napi\_check\_object\_type\_tag

验证一个ArkTS对象是否带有特定类型标签。

类型标签提供了一种在Node-API模块和ArkTS对象之间建立强类型关联的机制，使得原生代码能够更准确地识别和处理特定的ArkTS对象。

cpp部分代码

```
1. #define NUMBERINT_FOUR 4
2. // 定义一个静态常量napi_type_tag数组存储类型标签
3. static const napi_type_tag TagsData[NUMBERINT_FOUR] = {
4. {0x9e4b2449547061b3, 0x33999f8a6516c499},
5. {0x1d55a794c53a726d, 0x43633f509f9c944e},
6. // 用于表示无标签或默认标签
7. {0, 0},
8. {0x6a971439f5b2e5d7, 0x531dc28a7e5317c0},
9. };
10. // napi_type_tag_object
11. static napi_value SetTypeTagToObject(napi_env env, napi_callback_info info)
12. {
13. // 获取函数调用信息和参数
14. size_t argc = 2;
15. napi_value args[2] = {nullptr};
16. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
17. // 获取索引数字转换为napi_value
18. int32_t index = 0;
19. napi_get_value_int32(env, args[1], &index);
20. // 给参数（对象）设置类型标签
21. napi_status status = napi_type_tag_object(env, args[0], &TagsData[index]);
22. if (status != napi_ok) {
23. napi_throw_error(env, "Reconnect error", "napi_type_tag_object failed");
24. return nullptr;
25. }
26. // 将bool结果转换为napi_value并返回
27. napi_value result = nullptr;
28. napi_get_boolean(env, true, &result);
29. return result;
30. }
31. // napi_check_object_type_tag
32. static napi_value CheckObjectTypeTag(napi_env env, napi_callback_info info)
33. {
34. // 获取函数调用信息和参数
35. size_t argc = 2;
36. napi_value args[2] = {nullptr};
37. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
38. // 获取索引数字转换为napi_value
39. int32_t index = 0;
40. napi_get_value_int32(env, args[1], &index);
41. // 检查对象的类型标签
42. bool checkResult = true;
43. napi_check_object_type_tag(env, args[0], &TagsData[index], &checkResult);
44. // 将bool结果转换为napi_value并返回
45. napi_value checked = nullptr;
46. napi_get_boolean(env, checkResult, &checked);

48. return checked;
49. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/cpp/napi_init.cpp#L171-L221)

接口声明

```
1. export const setTypeTagToObject: (obj: Object, index: number) => boolean | undefined; // napi_type_tag_object

3. export const checkObjectTypeTag: (obj: Object, index: number) => boolean; // napi_check_object_type_tag
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/cpp/types/libentry/Index.d.ts#L51-L55)

```
1. // napi_type_tag_object and napi_check_object_type_tag
2. class Obj {
3. public data: number = 0
4. public message: string = ''
5. }

7. let objA: Obj = { data: 0, message: 'hello world' };
8. let objB: Obj = { data: 10, message: 'typeTag' };
9. hilog.info(0x0000, 'testTag', 'Test Node-API napi_type_tag_object objA -> 0: %{public}s',
10. testNapi.setTypeTagToObject(objA, 0));
11. hilog.info(0x0000, 'testTag', 'Test Node-API napi_type_tag_object objB -> 0: %{public}s',
12. testNapi.setTypeTagToObject(objB, 0));
13. hilog.info(0x0000, 'testTag', 'Test Node-API napi_check_object_type_tag objA -> 0: %{public}s',
14. testNapi.checkObjectTypeTag(objA, 0));
15. hilog.info(0x0000, 'testTag', 'Test Node-API napi_check_object_type_tag objB -> 1: %{public}s',
16. testNapi.checkObjectTypeTag(objB, 1));
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/ets/pages/Index.ets#L222-L239)

### napi\_create\_external

创建自定义的C/C++对象并将其公开给ArkTS代码。这种情况下，我们可以使用napi\_create\_external来创建一个包含指向自定义对象的指针的Node-API值，以便让ArkTS代码能够访问和操作该对象。

cpp部分代码

```
1. // 用于释放外部数据的回调函数
2. void finalizeCallback(napi_env env, void *data, void *hint)
3. {
4. // 释放外部数据
5. free(data);
6. }
7. // napi_create_external
8. static napi_value GetExternalType(napi_env env, napi_callback_info info)
9. {
10. size_t argc = 1;
11. napi_value args[1] = {nullptr};
12. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);
13. // 获取参数的数据类型
14. napi_valuetype valueType;
15. napi_typeof(env, args[0], &valueType);
16. napi_value returnValue = nullptr;
17. if (valueType == napi_external) {
18. // 如果数据类型是napi_external,则返回true
19. napi_get_boolean(env, true, &returnValue);
20. } else {
21. napi_get_boolean(env, false, &returnValue);
22. }
23. return returnValue;
24. }

26. static napi_value CreateExternal(napi_env env, napi_callback_info info)
27. {
28. // 设置外部数据大小为10
29. const size_t dataSize = 10;
30. // 分配外部数据
31. void *data = malloc(dataSize);
32. if (data == nullptr) {
33. OH_LOG_ERROR(LOG_APP, "malloc failed");
34. return nullptr;
35. }
36. // 初始化外部数据
37. memset(data, 0, dataSize);
38. napi_value result = nullptr;
39. // 返回带有外部数据的对象
40. napi_status status = napi_create_external(env, data, finalizeCallback, nullptr, &result);
41. if (status != napi_ok) {
42. OH_LOG_ERROR(LOG_APP, " Node-API Failed to create external data");
43. return nullptr;
44. }
45. return result;
46. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/cpp/napi_init.cpp#L223-L270)

接口声明

```
1. export const createExternal: () => Object; // napi_create_external

3. export const getExternalType: (externalData: Object) => boolean; // napi_create_external
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/cpp/types/libentry/Index.d.ts#L57-L61)

ArkTS侧示例代码

```
1. // napi_create_external
2. const externalData = testNapi.createExternal();
3. hilog.info(0x0000, 'testTag', 'Test Node-API napi_create_external:%{public}s',
4. testNapi.getExternalType(externalData));
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/ets/pages/Index.ets#L242-L247)

### napi\_get\_value\_external

napi\_create\_external可以创建包装自定义的C/C++对象并将其公开给ArkTS代码，而napi\_get\_value\_external就是用来获得napi\_create\_external所创建的外部对象的。

cpp部分代码

```
1. // napi_get_value_external
2. static int g_external = 5;
3. static napi_value GetValueExternal(napi_env env, napi_callback_info info)
4. {
5. // 创建外部数据
6. int *data = &g_external;
7. napi_value setExternal = nullptr;
8. napi_create_external(env, data, nullptr, nullptr, &setExternal);
9. // 获得外部数据的值
10. void *getExternal;
11. napi_get_value_external(env, setExternal, &getExternal);
12. // 返回获得到的外部数据
13. napi_value result = nullptr;
14. napi_create_int32(env, *(int *)getExternal, &result);
15. return result;
16. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/cpp/napi_init.cpp#L272-L289)

接口声明

```
1. export const getValueExternal: () => number; // napi_get_value_external
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/cpp/types/libentry/Index.d.ts#L63-L65)

ArkTS侧示例代码

```
1. // napi_get_value_external
2. hilog.info(0x0000, 'Node-API', 'get_value_external:%{public}d', testNapi.getValueExternal());
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/ets/pages/Index.ets#L250-L253)

### napi\_create\_symbol

用于创建一个新的Symbol。Symbol是一种特殊的数据类型，用于表示唯一的标识符。与字符串或数字不同，符号的值是唯一的，即使两个符号具有相同的描述，它们也是不相等的。符号通常用作对象属性的键，以确保属性的唯一性。

cpp部分代码

```
1. // napi_create_symbol
2. static napi_value CreateSymbol(napi_env env, napi_callback_info info)
3. {
4. napi_value result = nullptr;
5. const char *des = "only";
6. // 使用napi_create_string_utf8创建描述字符串
7. napi_status status = napi_create_string_utf8(env, des, NAPI_AUTO_LENGTH, &result);
8. if (status != napi_ok) {
9. OH_LOG_ERROR(LOG_APP, "Node-API napi_create_string_utf8 failed");
10. return nullptr;
11. }
12. napi_value returnSymbol = nullptr;
13. // 创建一个symbol类型，并返回
14. status = napi_create_symbol(env, result, &returnSymbol);
15. if (status != napi_ok) {
16. OH_LOG_ERROR(LOG_APP, "Node-API napi_create_symbol failed");
17. return nullptr;
18. }
19. return returnSymbol;
20. }
```

[napi\_init.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/cpp/napi_init.cpp#L291-L312)

```
1. export const createSymbol: () => symbol; // napi_create_symbol
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/cpp/types/libentry/Index.d.ts#L67-L69)

ArkTS侧示例代码

```
1. // napi_create_symbol
2. let varSymbol = testNapi.createSymbol();
3. hilog.info(0x0000, 'Node-API', 'createSymbol:%{public}s', typeof varSymbol);
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260402/ArkTS/NodeAPI/NodeAPIUse/NodeAPIObject/entry/src/main/ets/pages/Index.ets#L256-L260)

以上代码如果要在native cpp中打印日志，需在CMakeLists.txt文件中添加以下配置信息（并添加头文件：#include "hilog/log.h"）：

```
1. // CMakeLists.txt
2. add_definitions( "-DLOG_DOMAIN=0xd0d0" )
3. add_definitions( "-DLOG_TAG=\"testTag\"" )
4. target_link_libraries(entry PUBLIC libace_napi.z.so libhilog_ndk.z.so)
```
