---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-codelinter-rules-change
title: 规则变更说明
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 规则变更说明
category: harmonyos-guides
scraped_at: 2026-06-01T15:19:16+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f0c481bb985ab6eb0f78e112b7a8f9bff170541fb0f63ec2441a1da18c0b144c
---
## 6.1.0.609

新增规则

* [@performance/custom-node-memory-leak-check](../性能规则@performance/@performancecustom-node-memory-leak-check/ide-custom-node-memory-leak-check.md)
* [@performance/state-variable-usage-in-ui-format-check](../性能规则@performance/@performancestate-variable-usage-in-ui-format-check/ide-state-variable-us_16038627.md)
* [@correctness/multimedia-use-stride-in-image-receiver](../正确性规则@correctness/@correctnessmultimedia-use-stride-in-image-receiver/ide-multimedia-use-s_02999470.md)
* [@correctness/v1-nested-object-property-change-format-check](../正确性规则@correctness/@correctnessv1-nested-object-property-change-format-check/ide-v1-nested-_75362271.md)
* [@correctness/v1-state-object-member-used-in-function-parameter-check](../正确性规则@correctness/@correctnessv1-state-object-member-used-in-function-parameter-check/ide-v1-_78277292.md)

## 6.0.2.636

新增规则

* [@correctness/redundant-dependency-check](../正确性规则@correctness/@correctnessredundant-dependency-check/ide-redundant-dependency-check.md)
* [@cross-device-app-dev/immersive-effect-check](../一次开发多端部署规则@cross-device-app-dev/@cross-device-app-devimmersive-effect-check/ide-immersive-effect-check.md)

## 6.0.1.246

新增规则

* [@compatibility/api-compatibility-check](../兼容性规则@compatibility/@compatibilityapi-compatibility-check/ide-api-compatibility-check.md)

## 6.0.0.848

新增规则

* [@security/no-unsafe-kdf](../安全规则@security/@securityno-unsafe-kdf/ide_no-unsafe-kdf.md)
* [@security/no-unsafe-sm4](../安全规则@security/@securityno-unsafe-sm4/ide_no-unsafe-sm4.md)
* [@security/no-unsafe-sm2-key](../安全规则@security/@securityno-unsafe-sm2-key/ide_no-unsafe-sm2-key.md)
* [@security/no-unsafe-sm2-cipher](../安全规则@security/@securityno-unsafe-sm2-cipher/ide_no-unsafe-sm2-cipher.md)
* [@security/no-unsafe-ecdh](../安全规则@security/@securityno-unsafe-ecdh/ide_no-unsafe-ecdh.md)
* [@security/no-unsafe-huks](../安全规则@security/@securityno-unsafe-huks/ide_no-unsafe-huks.md)

## 6.0.0.828

新增规则

* [@performance/no-use-any-import](../性能规则@performance/@performanceno-use-any-import/ide-no-use-any-import.md)
* [@performance/avoid-overusing-custom-component-check](../性能规则@performance/@performanceavoid-overusing-custom-component-check/ide-avoid-overusing-custom-component-check.md)
* [@performance/bad-deep-clone-check](../性能规则@performance/@performancebad-deep-clone-check/ide-bad-deep-clone-check.md)
* [@performance/reasonable-audio-use-check](../性能规则@performance/@performancereasonable-audio-use-check/ide-reasonable-audio-use-check.md)
* [@performance/reasonable-sensor-use-check](../性能规则@performance/@performancereasonable-sensor-use-check/ide-reasonable-sensor-use-check.md)
* [@performance/reasonable-gps-use-check](../性能规则@performance/@performancereasonable-gps-use-check/ide-reasonable-gps-use-check.md)
* [@performance/reuse-date-instances-check](../性能规则@performance/@performancereuse-date-instances-check/ide-reuse-date-instances-check.md)
* [@performance/crypto-replacement-check](../性能规则@performance/@performancecrypto-replacement-check/ide-crypto-replacement-check.md)
* [@performance/monitor-invisible-area-in-image-animation](../性能规则@performance/@performancemonitor-invisible-area-in-image-animation/ide-monitor-invisib_26216235.md)
* [@performance/datashare-query-unrelease-check](../性能规则@performance/@performancedatashare-query-unrelease-check/ide-datashare-query-unrelease-check.md)
* [@performance/dark-color-mode-check](../性能规则@performance/@performancedark-color-mode-check/ide-dark-color-mode-check.md)
* [@performance/update-state-var-between-animatetos-check](../性能规则@performance/@performanceupdate-state-var-between-animatetos-check/ide-update-state-va_37553175.md)
* [@performance/tabs-on-change-check](../性能规则@performance/@performancetabs-on-change-check/ide-tabs-on-change-check.md)
* [@performance/nested-post-frame-callback-check](../性能规则@performance/@performancenested-post-frame-callback-check/ide-nested-post-frame-callback-check.md)
* [@cross-device-app-dev/window-size-change-listener-check](../一次开发多端部署规则@cross-device-app-dev/@cross-device-app-devwindow-size-change-listener-check/ide-win_61812076.md)

## 6.0.0.418

新增规则

* [@performance/web-on-active-check](../性能规则@performance/@performanceweb-on-active-check/ide-web-on-active-check.md)
* [@performance/gif-hardware-decoding-check](../性能规则@performance/@performancegif-hardware-decoding-check/ide-gif-hardware-decoding-check.md)
* [@cross-device-app-dev/one-multi-breakpoint-check](../一次开发多端部署规则@cross-device-app-dev/@cross-device-app-devone-multi-breakpoint-check/ide-one-multi-breakpoint-check.md)

变更规则

* [@typescript-eslint/explicit-function-return-type](../通用规则@typescript-eslint/@typescript-eslintexplicit-function-return-type/ide_explicit-function-return-type.md)规则新增额外选项allowArkTS（默认为false），配置为true时，支持对.ets文件进行检查。

## 5.1.0.828

新增规则

* [@performance/web-cache-mode-check](../性能规则@performance/@performanceweb-cache-mode-check/ide-performance-web-cache-mode-check.md)
* [@correctness/audio-interrupt-check](../正确性规则@correctness/@correctnessaudio-interrupt-check/ide-audio-interrupt-check.md)
* [@correctness/audio-pause-or-mute-check](../正确性规则@correctness/@correctnessaudio-pause-or-mute-check/ide-audio-pause-or-mute-check.md)
* [@correctness/avsession-metadata-check](../正确性规则@correctness/@correctnessavsession-metadata-check/ide-avsession-metadata-check.md)
* [@correctness/avsession-buttons-check](../正确性规则@correctness/@correctnessavsession-buttons-check/ide-avsession-buttons-check.md)
* [@correctness/image-interpolation-check](../正确性规则@correctness/@correctnessimage-interpolation-check/ide-image-interpolation-check.md)
* [@correctness/image-pixel-format-check](../正确性规则@correctness/@correctnessimage-pixel-format-check/ide-image-pixel-format-check.md)
* [@performance/hp-ffrt-no-use-std](../性能规则@performance/@performancehp-ffrt-no-use-std/ide-hp-ffrt-no-use-std.md)

变更规则

* [@performance/hp-arkui-use-taskpool-for-web-request](../性能规则@performance/@performancehp-arkui-use-taskpool-for-web-request/ide-hp-arkui-use-taskpool-for-web-request.md)所属规则集由recommended改为all。

## 5.0.7.100

新增规则

* [@performance/foreach-index-check](../性能规则@performance/@performanceforeach-index-check/ide-foreach-index-check.md)
* [@performance/js-code-cache-by-precompile-check](../性能规则@performance/@performancejs-code-cache-by-precompile-check/ide-js-code-cache-by-precompile-check.md)
* [@performance/js-code-cache-by-interception-check](../性能规则@performance/@performancejs-code-cache-by-interception-check/ide-js-code-cache-by-interception-check.md)
* [@performance/init-list-component](../性能规则@performance/@performanceinit-list-component/ide-init-list-component.md)
* [@correctness/listen-default-network-change](../正确性规则@correctness/@correctnesslisten-default-network-change/ide_listen-default-network-change.md)
* [@correctness/listen-multi-network-concurrent](../正确性规则@correctness/@correctnesslisten-multi-network-concurrent/ide_listen-multi-network-concurrent.md)
* [@security/no-unsafe-3des](../安全规则@security/@securityno-unsafe-3des/ide-no-unsafe-3des.md)

变更规则

* [@performance/high-frequency-log-check](../性能规则@performance/@performancehigh-frequency-log-check/ide-high-frequency-log-check.md)增加检测高频函数onWillScroll。
* [@typescript-eslint/prefer-readonly-parameter-types](../通用规则@typescript-eslint/@typescript-eslintprefer-readonly-parameter-types/ide_prefer-readonly-parameter-types.md)和[@typescript-eslint/no-magic-numbers](../通用规则@typescript-eslint/@typescript-eslintno-magic-numbers/ide_no-magic-numbers.md)中，规则的默认告警级别由error改为warn。
* [@typescript-eslint/lines-between-class-members](../通用规则@typescript-eslint/@typescript-eslintlines-between-class-members/ide_lines-between-class-members.md)默认检查规则从成员变量之间必须有空行分隔，变更为成员变量和成员变量之间不需要有空行分隔。
* [@security/no-unsafe-hash](../安全规则@security/@securityno-unsafe-hash/ide_no-unsafe-hash.md)新增对@ohos/crypto-js包中不安全Hash算法检查。
* [@security/no-unsafe-mac](../安全规则@security/@securityno-unsafe-mac/ide_no-unsafe-mac.md)新增对@ohos/crypto-js包中不安全Mac算法检查。

## 5.0.5.200

变更规则

* [@performance/hp-arkui-avoid-empty-callback](../性能规则@performance/@performancehp-arkui-avoid-empty-callback/ide_hp-arkui-avoid-empty-callback.md)所属规则集由recommended改为all。
* [@performance/hp-arkui-use-word-break-to-replace-zero-width-space](../性能规则@performance/@performancehp-arkui-use-word-break-to-replace-zero-width-space/ide_hp-ar_77809357.md)所属规则集由recommended改为all。
* [@performance/hp-arkui-remove-redundant-nest-container](../性能规则@performance/@performancehp-arkui-remove-redundant-nest-container/ide_hp-arkui-no-redundant-nest.md)所属规则集由recommended改为all。
* [@performance/hp-arkui-remove-container-without-property](../性能规则@performance/@performancehp-arkui-remove-container-without-property/ide_hp-arkui-remov_59621229.md)所属规则集由recommended改为all。
* [@performance/sparse-array-check](../性能规则@performance/@performancesparse-array-check/ide-sparse-array-check.md)所属规则集由recommended改为all。
* [@performance/number-init-check](../性能规则@performance/@performancenumber-init-check/ide-number-init-check.md)所属规则集由recommended改为all。
* [@performance/typed-array-check](../性能规则@performance/@performancetyped-array-check/ide-typed-array-check.md)所属规则集由recommended改为all。

## 5.0.3.800

**新增规则**

* [@performance/hp-arkui-reduce-pangesture-distance](../性能规则@performance/@performancehp-arkui-reduce-pangesture-distance/ide-hp-arkui-reduce-ges-distance.md)
* [@performance/hp-arkui-suggest-use-get-anonymousid-async](../性能规则@performance/@performancehp-arkui-suggest-use-get-anonymousid-async/ide-hp-arkui-sg-anonymousid-async.md)
* [@performance/multiple-associations-state-var-check](../性能规则@performance/@performancemultiple-associations-state-var-check/ide-multi-associations-state-var-check.md)
* [@performance/constant-property-referencing-check-in-loops](../性能规则@performance/@performanceconstant-property-referencing-check-in-loops/ide-constant-property-check-in-loops.md)
* [@performance/foreach-args-check](../性能规则@performance/@performanceforeach-args-check/ide-foreach-args-check.md)

**变更规则**

* [@security/specified-interface-call-chain-check](../安全规则@security/@securityspecified-interface-call-chain-check/ide-specified-interface-call-chain-check.md)新增对命名空间namespace、类型别名type、接口interface、枚举enum和结构体struct的支持。namespace字段配置类型从字符串变更为数组。

* [@performance/high-frequency-log-check](../性能规则@performance/@performancehigh-frequency-log-check/ide-high-frequency-log-check.md)默认告警等级从suggestion变更为warn，该规则新增至all规则集中。
* [@performance/number-init-check](../性能规则@performance/@performancenumber-init-check/ide-number-init-check.md)默认告警等级从warn变更为suggestion，该规则新增至recommended规则集中。
* [@performance/start-window-icon-check](../性能规则@performance/@performancestart-window-icon-check/ide-start-window-icon-check.md)默认告警等级从warn变更为suggestion，该规则新增至recommended规则集中。
* [@performance/sparse-array-check](../性能规则@performance/@performancesparse-array-check/ide-sparse-array-check.md)默认告警等级从warn变更为suggestion，该规则新增至recommended规则集中。
* [@performance/typed-array-check](../性能规则@performance/@performancetyped-array-check/ide-typed-array-check.md)默认告警等级从warn变更为suggestion，该规则新增至recommended规则集中。
* [@performance/waterflow-data-preload-check](../性能规则@performance/@performancewaterflow-data-preload-check/ide-waterflow-data-preload-check.md)该规则新增至recommended规则集中。
* [@performance/hp-arkts-no-use-any-export-current](../性能规则@performance/@performancehp-arkts-no-use-any-export-current/ide-hp-arkts-no-use-any-export-current.md)告警级别由suggestion改为warn，该规则新增至recommended规则集中。
* [@performance/hp-arkts-no-use-any-export-other](../性能规则@performance/@performancehp-arkts-no-use-any-export-other/ide-hp-arkts-no-use-any-export-other.md)，该规则新增至recommended规则集中。
* [@performance/hp-arkui-avoid-empty-callback](../性能规则@performance/@performancehp-arkui-avoid-empty-callback/ide_hp-arkui-avoid-empty-callback.md)告警级别由warn改为suggestion。
* [@performance/hp-arkui-avoid-update-auto-state-var-in-aboutToReuse](../性能规则@performance/@performancehp-arkui-avoid-update-auto-state-var-in-aboutToReuse/ide_hp-arkui-abouttoreuse.md)，该规则新增至recommended规则集中。
* [@performance/hp-arkui-image-async-load](../性能规则@performance/@performancehp-arkui-image-async-load/ide_hp-arkui-image-async-load.md)所属规则集由recommend改为all。
* [@performance/hp-arkui-load-on-demand](../性能规则@performance/@performancehp-arkui-load-on-demand/ide_hp-arkui-load-on-demand.md)告警级别由suggestion改为warn。
* [@performance/hp-arkui-no-stringify-in-lazyforeach-key-generator](../性能规则@performance/@performancehp-arkui-no-stringify-in-lazyforeach-key-generator/ide_hp-ark_68283822.md)告警级别由suggestion改为warn，该规则新增至recommended规则集中。
* [@performance/hp-arkui-remove-container-without-property](../性能规则@performance/@performancehp-arkui-remove-container-without-property/ide_hp-arkui-remov_59621229.md)告警级别由warn改为suggestion。
* [@performance/hp-arkui-remove-redundant-nest-container](../性能规则@performance/@performancehp-arkui-remove-redundant-nest-container/ide_hp-arkui-no-redundant-nest.md)告警级别由warn改为suggestion。
* [@performance/hp-arkui-replace-nested-reusable-component-by-builder](../性能规则@performance/@performancehp-arkui-replace-nested-reusable-component-by-builder/ide_hp-_94301918.md)告警级别由suggestion改为warn，该规则新增至recommended规则集中。
* [@performance/hp-arkui-suggest-cache-avplayer](../性能规则@performance/@performancehp-arkui-suggest-cache-avplayer/ide-hp-arkui-suggest-cache-avplayer.md)告警级别由suggestion改为warn，该规则新增至recommended规则集中。
* [@performance/hp-arkui-suggest-reuseid-for-if-else-reusable-component](../性能规则@performance/@performancehp-arkui-suggest-reuseid-for-if-else-reusable-component/ide_hp-_66838745.md)告警级别由suggestion改为warn, 该规则新增至recommended规则集中。
* [@performance/hp-arkui-suggest-use-effectkit-blur](../性能规则@performance/@performancehp-arkui-suggest-use-effectkit-blur/ide-hp-arkui-suggest-use-effectkit-blur.md)，该规则新增至recommended规则集中。
* [@performance/hp-arkui-use-grid-layout-options](../性能规则@performance/@performancehp-arkui-use-grid-layout-options/ide_hp-arkui-use-grid-layout-options.md)告警级别由suggestion改为warn，该规则新增至recommended规则集中。
* [@performance/hp-arkui-use-local-var-to-replace-state-var](../性能规则@performance/@performancehp-arkui-use-local-var-to-replace-state-var/ide_hp-arkui-use-_79291313.md)告警级别由suggestion改为warn。
* [@performance/hp-arkui-use-onAnimationStart-for-swiper-preload](../性能规则@performance/@performancehp-arkui-use-onAnimationStart-for-swiper-preload/ide_hp-arkui_38224011.md)告警级别由suggestion改为warn，该规则新增至recommended规则集中。
* [@performance/hp-arkui-use-reusable-component](../性能规则@performance/@performancehp-arkui-use-reusable-component/ide_hp-arkui-use-reusable-component.md)告警级别由suggestion改为warn。
* [@performance/hp-arkui-use-row-column-to-replace-flex](../性能规则@performance/@performancehp-arkui-use-row-column-to-replace-flex/ide_hp-arkui-use-row-_08817323.md)，所属规则集由recommended改为all。
* [@performance/hp-arkui-use-scale-to-replace-attr-animateto](../性能规则@performance/@performancehp-arkui-use-scale-to-replace-attr-animateto/ide_hp-arkui-use_10529421.md)告警级别由suggestion改为warn，该规则新增至recommended规则集中。
* [@performance/hp-arkui-use-taskpool-for-web-request](../性能规则@performance/@performancehp-arkui-use-taskpool-for-web-request/ide-hp-arkui-use-taskpool-for-web-request.md)告警级别由suggestion改为warn，该规则新增至recommended规则集中。
* [@performance/hp-arkui-use-transition-to-replace-animateto](../性能规则@performance/@performancehp-arkui-use-transition-to-replace-animateto/ide_hp-arkui-use_47348746.md)告警级别由suggestion改为warn，该规则新增至recommended规则集中。
* [@performance/hp-arkui-use-word-break-to-replace-zero-width-space](../性能规则@performance/@performancehp-arkui-use-word-break-to-replace-zero-width-space/ide_hp-ar_77809357.md)该规则新增至recommended规则集中。
* [@performance/hp-arkui-set-cache-count-for-lazyforeach-grid](../性能规则@performance/@performancehp-arkui-set-cache-count-for-lazyforeach-grid/ide_hp-arkui-se_93975829.md)告警级别由warn改为suggestion。

**下线规则**

* [@performance/hp-arkui-wrap-waterflow-if-else-footer](../性能规则@performance/@performancehp-arkui-wrap-waterflow-if-else-footer（已下线）/ide-hp-arkui-wrap_11248948.md)

## 5.0.3.600

**新增规则**

* [@performance/hp-arkui-wrap-waterflow-if-else-footer](../性能规则@performance/@performancehp-arkui-wrap-waterflow-if-else-footer（已下线）/ide-hp-arkui-wrap_11248948.md)
* [@performance/hp-arkui-remove-unchanged-state-var](../性能规则@performance/@performancehp-arkui-remove-unchanged-state-var/ide-hp-arkui-remove-unchanged-state-var.md)
* [@performance/hp-arkts-no-use-any-export-current](../性能规则@performance/@performancehp-arkts-no-use-any-export-current/ide-hp-arkts-no-use-any-export-current.md)
* [@performance/hp-arkts-no-use-any-export-other](../性能规则@performance/@performancehp-arkts-no-use-any-export-other/ide-hp-arkts-no-use-any-export-other.md)
* [@performance/hp-arkui-suggest-cache-avplayer](../性能规则@performance/@performancehp-arkui-suggest-cache-avplayer/ide-hp-arkui-suggest-cache-avplayer.md)
* [@performance/hp-arkui-suggest-use-effectkit-blur](../性能规则@performance/@performancehp-arkui-suggest-use-effectkit-blur/ide-hp-arkui-suggest-use-effectkit-blur.md)
* [@performance/lottie-animation-destroy-check](../性能规则@performance/@performancelottie-animation-destroy-check/ide-lottie-animation-destroy-check.md)
* [@performance/timezone-interface-check](../性能规则@performance/@performancetimezone-interface-check/ide-timezone-interface-check.md)

**变更规则**

以下规则的部分场景，在5.0.3.600之前的版本检查执行Codelinter检查时不报错，升级至DevEco Studio 5.0.3.600版本后执行Codelinter检查将报错。

* [@typescript-eslint/no-unnecessary-condition](../通用规则@typescript-eslint/@typescript-eslintno-unnecessary-condition/ide_no-unnecessary-condition.md)

```
1. // 场景一：支持逻辑表达式的检查
2. interface GeneratedTypeLiteralInterface {}
3. declare let foo: GeneratedTypeLiteralInterface;
4. foo ??= 1; // 升级前不报错，升级后报错
5. // 场景二：链式表达式中可以推断为非空的场景下，不需要增加判空
6. interface GeneratedTypeLiteralInterface {
7. bar: () => number;
8. }
9. type Foo = GeneratedTypeLiteralInterface | null;
10. declare const foo: Foo;
11. foo?.bar()?.toExponential(); // 升级前不报错，升级后报错
```

* [@typescript-eslint/promise-function-async](../通用规则@typescript-eslint/@typescript-eslintpromise-function-async/ide_promise-function-async.md)

```
1. // 函数返回值没有显式定义类型，并且返回值可能为Promise的场景下，函数需要定义为async
2. function promiseInUnionWithoutExplicitReturnType(p: boolean) { // 升级前不报错，升级后报错
3. return p ? Promise.resolve(5) : 5;
4. }
```

* [@typescript-eslint/member-ordering](../通用规则@typescript-eslint/@typescript-eslintmember-ordering/ide_member-ordering.md)

```
1. // 配置了optionalityOrder选项，并且类属性中不包含可选变量的场景下，规则中配置的order选项在历史版本中失效了
2. // 规则配置为"@typescript-eslint/member-ordering": ["error", {"default": {"memberTypes": 'never', "order": 'natural-case-insensitive', "optionalityOrder": 'required-first',}}]
3. class X {
4. b: string = '';
5. a: string = ''; // 升级前不报错，升级后报错
6. }
```

* [@typescript-eslint/naming-convention](../通用规则@typescript-eslint/@typescript-eslintnaming-convention/ide_naming-convention.md)

```
1. // 支持检查interface中的typeMethod
2. // 规则配置为："@typescript-eslint/naming-convention": ["error", {selector: 'typeMethod', format: ['PascalCase']}]
3. interface SOME_INTERFACE {
4. someMethod: () => void; // 升级前不报错，升级后报错
5. some_property: string;
6. }
```

* [@typescript-eslint/ban-types](../通用规则@typescript-eslint/@typescript-eslintban-types/ide_ban-types.md)

```
1. // 支持检查extend、implements后的类型
2. // 规则配置为："@typescript-eslint/ban-types": ["error",{"types": {"Bar": {"message": ""}}}]
3. interface Bar {}
4. interface Baz {}
5. interface Foo extends Bar, Baz {} // 升级前不报错，升级后报错
```

* [@typescript-eslint/no-floating-promises](../通用规则@typescript-eslint/@typescript-eslintno-floating-promises/ide_no-floating-promises.md)

```
1. // 场景一：.finally()被认为是没有有效处理Promise中可能发生的异常
2. Promise.reject().finally(() => {}) // 升级前不报错，升级后报错
3. // 场景二：.then()中的第二个参数如果是undefined或者null，被认为是没有有效处理Promise中可能发生的异常
4. Promise.resolve().then(() => {}, undefined); // 升级前不报错，升级后报错
5. Promise.resolve().then(() => {}, null); // 升级前不报错，升级后报错
```

* [@typescript-eslint/no-inferrable-types](../通用规则@typescript-eslint/@typescript-eslintno-inferrable-types/ide_no-inferrable-types.md)

```
1. // 支持检查构造函数中的参数类型
2. class Foo {
3. constructor(param: boolean = true) {} // 升级前不报错，升级后报错
4. }
```

* [@typescript-eslint/prefer-readonly](../通用规则@typescript-eslint/@typescript-eslintprefer-readonly/ide_prefer-readonly.md)

```
1. interface GeneratedObjectLiteralInterface {
2. prop?: string
3. }

5. class Test {
6. // 支持检查私有属性
7. #testObj: GeneratedObjectLiteralInterface = {}; // 升级前不报错，升级后报错

9. public test(): void {
10. this.#testObj?.prop;
11. }
12. }
```

## 5.0.3.500

**新增规则**

* [@security/no-unsafe-dh-key](../安全规则@security/@securityno-unsafe-dh-key/ide_no-unsafe-dh-key.md)
* [@security/no-unsafe-dsa-key](../安全规则@security/@securityno-unsafe-dsa-key/ide_no-unsafe-dsa-key.md)
* [@security/no-unsafe-rsa-key](../安全规则@security/@securityno-unsafe-rsa-key/ide_no-unsafe-rsa-key.md)
* [@performance/hp-arkui-use-attributeUpdater-control-refresh-scope](../性能规则@performance/@performancehp-arkui-use-attributeUpdater-control-refresh-scope/ide-hp-at_24736549.md)
* [@performance/hp-arkui-use-id-in-get-resource-sync-api](../性能规则@performance/@performancehp-arkui-use-id-in-get-resource-sync-api/ide_hp-arkui-use-id-_33597197.md)
* [@performance/hp-arkui-use-transition-to-replace-animateto](../性能规则@performance/@performancehp-arkui-use-transition-to-replace-animateto/ide_hp-arkui-use_47348746.md)
* [@performance/hp-arkui-remove-redundant-state-var](../性能规则@performance/@performancehp-arkui-remove-redundant-state-var/ide-hp-arkui-remove-redundant-state-var.md)
* [@performance/hp-arkui-use-taskpool-for-web-request](../性能规则@performance/@performancehp-arkui-use-taskpool-for-web-request/ide-hp-arkui-use-taskpool-for-web-request.md)
* [@security/specified-interface-call-chain-check](../安全规则@security/@securityspecified-interface-call-chain-check/ide-specified-interface-call-chain-check.md)
* [@hw-stylistic/file-naming-convention](../ArkTS代码风格规则@hw-stylistic/@hw-stylisticfile-naming-convention/ide-file-naming-convention.md)

**变更规则**

* @performance/high-frequency-log-check所属规则集由all变更为recommended。

**下线规则**

* [@performance/object-creation-check](../性能规则@performance/@performanceobject-creation-check（已下线）/ide-object-creation-check.md)
* [@performance/hp-arkui-limit-refresh-scope](../性能规则@performance/@performancehp-arkui-limit-refresh-scope（已下线）/ide_hp-arkui-limit-refresh-scope.md)
* [@performance/lazyforeach-args-check](../性能规则@performance/@performancelazyforeach-args-check（已下线）/ide-lazyforeach-args-check.md)
