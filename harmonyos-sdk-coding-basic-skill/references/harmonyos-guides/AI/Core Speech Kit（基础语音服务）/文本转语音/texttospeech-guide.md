---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/texttospeech-guide
title: 文本转语音
breadcrumb: 指南 > AI > Core Speech Kit（基础语音服务） > 文本转语音
category: harmonyos-guides
scraped_at: 2026-06-01T15:13:22+08:00
doc_updated_at: 2026-05-26
content_hash: sha256:383d28b19bd544e36ef89b37bc39099169afc69457680a05792958203a66e5de
---
Core Speech Kit支持将一篇不超过10000字符数的中英文文本（简体中文、繁体中文、数字、英文）合成为语音，并以选定音色进行播报。

开发者可对播报的策略进行设置，包括单词播报、数字播报、静音停顿、汉字发音策略。

## 场景介绍

手机/平板等设备在无网状态下，系统应用无障碍（屏幕朗读）接入文本转语音能力，为视障人士或不方便阅读场景提供播报能力。

## 约束与限制

| AI能力 | 约束 |
| --- | --- |
| 文本转语音 | - 支持的语种类型：中文、英文。（简体中文、繁体中文、中文语境下的英文）  - 支持的音色类型：聆小珊女声音色、英语（美国）劳拉女声音色、凌飞哲男声音色。  - 文本长度：不超过10000字符数。 |

## 开发步骤

1. 在使用文本转语音时，将实现文本转语音相关的类添加至工程。

   ```
   1. import { textToSpeech } from '@kit.CoreSpeechKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 调用createEngine接口，创建[TextToSpeechEngine](<../../../../harmonyos-references/Core Speech Kit（基础语音服务）/ArkTS API/textToSpeech（文本转语音）/hms-ai-texttospeech.md#texttospeechengine>)实例。

   createEngine接口提供了两种调用形式，当前以其中一种作为示例，其他方式可参考[API参考](<../../../../harmonyos-references/Core Speech Kit（基础语音服务）/ArkTS API/textToSpeech（文本转语音）/hms-ai-texttospeech.md>)。

   ```
   1. let ttsEngine: textToSpeech.TextToSpeechEngine;

   3. // 设置创建引擎参数
   4. let extraParam: Record<string, Object> = {'style': 'interaction-broadcast', 'locate': 'CN', 'name': 'EngineName'};
   5. let initParamsInfo: textToSpeech.CreateEngineParams = {
   6. language: 'zh-CN',
   7. person: 0,
   8. online: 1,
   9. extraParams: extraParam
   10. };

   12. // 调用createEngine方法
   13. textToSpeech.createEngine(initParamsInfo, (err: BusinessError,
   14. textToSpeechEngine: textToSpeech.TextToSpeechEngine) => {
   15. if (!err) {
   16. console.info('Succeeded in creating engine');
   17. // 接收创建引擎的实例
   18. ttsEngine = textToSpeechEngine;
   19. } else {
   20. console.error(`Failed to create engine. Code: ${err.code}, message: ${err.message}.`);
   21. }
   22. });
   ```
3. 得到[TextToSpeechEngine](<../../../../harmonyos-references/Core Speech Kit（基础语音服务）/ArkTS API/textToSpeech（文本转语音）/hms-ai-texttospeech.md#texttospeechengine>)实例对象后，实例化[SpeakParams](<../../../../harmonyos-references/Core Speech Kit（基础语音服务）/ArkTS API/textToSpeech（文本转语音）/hms-ai-texttospeech.md#speakparams>)对象、[SpeakListener](<../../../../harmonyos-references/Core Speech Kit（基础语音服务）/ArkTS API/textToSpeech（文本转语音）/hms-ai-texttospeech.md#speaklistener>)对象，并传入待合成及播报的文本originalText，调用[speak](<../../../../harmonyos-references/Core Speech Kit（基础语音服务）/ArkTS API/textToSpeech（文本转语音）/hms-ai-texttospeech.md#speak>)接口进行播报。

   ```
   1. // 设置speak的回调信息
   2. let speakListener: textToSpeech.SpeakListener = {
   3. // 开始播报回调
   4. onStart(requestId: string, response: textToSpeech.StartResponse) {
   5. console.info(`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}`);
   6. },
   7. // 合成完成及播报完成回调
   8. onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
   9. console.info(`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}`);
   10. },
   11. // 停止播报回调
   12. onStop(requestId: string, response: textToSpeech.StopResponse) {
   13. console.info(`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}`);
   14. },
   15. // 返回音频流
   16. onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
   17. console.info(`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}`);
   18. },
   19. // 错误回调
   20. onError(requestId: string, errorCode: number, errorMessage: string) {
   21. console.error(`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
   22. }
   23. };
   24. // 设置回调
   25. ttsEngine.setListener(speakListener);
   26. // 设置播报内容
   27. let originalText: string = 'Hello HarmonyOS';
   28. // 设置播报相关参数
   29. let extraParam: Record<string, Object> = {
   30. 'queueMode': 0,
   31. 'speed': 1,
   32. 'volume': 2,
   33. 'pitch': 1,
   34. 'languageContext': 'zh-CN',
   35. 'audioType': 'pcm',
   36. 'soundChannel': 3,
   37. 'playType': 1
   38. };
   39. let speakParams: textToSpeech.SpeakParams = {
   40. requestId: '123456', // requestId在同一实例内仅能用一次，请勿重复设置
   41. extraParams: extraParam
   42. };
   43. // 调用播报方法
   44. // 开发者可以通过修改speakParams主动设置播报策略
   45. try {
   46. ttsEngine.speak(originalText, speakParams);
   47. } catch (err) {
   48. console.error(`error code: ${err.code}, message: ${err.message}.`);
   49. }
   ```
4. （可选）当需要停止合成及播报时，可调用[stop](<../../../../harmonyos-references/Core Speech Kit（基础语音服务）/ArkTS API/textToSpeech（文本转语音）/hms-ai-texttospeech.md#stop>)接口。

   ```
   1. ttsEngine.stop();
   ```
5. （可选）当需要查询文本转语音服务是否处于忙碌状态时，可调用[isBusy](<../../../../harmonyos-references/Core Speech Kit（基础语音服务）/ArkTS API/textToSpeech（文本转语音）/hms-ai-texttospeech.md#isbusy>)接口。

   ```
   1. ttsEngine.isBusy();
   ```
6. （可选）当需要查询支持的语种音色信息时，可调用[listVoices](<../../../../harmonyos-references/Core Speech Kit（基础语音服务）/ArkTS API/textToSpeech（文本转语音）/hms-ai-texttospeech.md#listvoices>)接口。

   listVoices接口提供了两种调用形式，当前以其中一种作为示例，其他方式可参考[API参考](<../../../../harmonyos-references/Core Speech Kit（基础语音服务）/ArkTS API/textToSpeech（文本转语音）/hms-ai-texttospeech.md>)。

   ```
   1. // 在组件中声明并初始化字符串voiceInfo
   2. @State voiceInfo: string = '';

   4. // 设置查询相关参数
   5. let voicesQuery: textToSpeech.VoiceQuery = {
   6. requestId: '12345678', // requestId在同一实例内仅能用一次，请勿重复设置
   7. online: 1
   8. };
   9. // 调用listVoices方法，以callback返回
   10. ttsEngine.listVoices(voicesQuery, (err: BusinessError, voiceInfo: textToSpeech.VoiceInfo[]) => {
   11. if (!err) {
   12. // 接收目前支持的语种音色等信息
   13. this.voiceInfo = JSON.stringify(voiceInfo);
   14. console.info(`Succeeded in listing voices, voiceInfo is ${this.voiceInfo}`);
   15. } else {
   16. console.error(`Failed to list voices. Code: ${err.code}, message: ${err.message}`);
   17. }
   18. });
   ```

## 设置播报策略

由于不同场景下，模型自动判断所选择的播报策略可能与实际需求不同，此章节提供对于播报策略进行主动设置的方法。

说明

以下取值说明均为有效取值，若所使用的数值在有效取值之外则播报结果可能与预期不符，并产生错误的播报结果。

### 设置单词播报方式

文本格式：[hN] (N=0/1/2)

N取值说明：

| 取值 | 说明 |
| --- | --- |
| 0 | 智能判断单词播放方式。默认值为0。 |
| 1 | 逐个字母进行播报。 |
| 2 | 以单词方式进行播报。 |

文本示例：

```
1. 'hello[h1] world'
```

hello使用单词发音，world及后续单词将会逐个字母进行发音。

### 设置数字播报策略

格式：[nN] (N=0/1/2)

N取值说明：

| 取值 | 说明 |
| --- | --- |
| 0 | 智能判断数字处理策略。默认值为0。 |
| 1 | 作为号码逐个数字播报。 |
| 2 | 作为数值播报。超过18位数字不支持，自动按逐个数字进行播报。 |

文本示例：

```
1. '[n2]123[n1]456[n0]'
```

其中，123将会按照数值播报，456则会按照号码播报，而后的文本中的数字，均会自动判断。

### 插入静音停顿

格式：[pN]

描述：N为无符号整数，单位为ms。

文本示例：

```
1. '你好[p500]小艺'
```

该句播报时，将会在“你好”后插入500ms的静音停顿。

### 指定汉字发音

汉字的声调，通过在拼音后接一位数字1~5分别表示阴平、阳平、上声、去声和轻声5个声调。

格式：[=MN]

描述：M表示拼音，N表示声调。

N取值说明：

| 取值 | 说明 |
| --- | --- |
| 1 | 阴平 |
| 2 | 阳平 |
| 3 | 上声 |
| 4 | 去声 |
| 5 | 轻声 |

文本示例：

```
1. '着[=zhuo2]手'
```

“着”字将读作“zhuó”。

## 开发实例

点击按钮，播报一段文本。

### Index.ets

```
1. import { textToSpeech } from '@kit.CoreSpeechKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { PromptAction, UIContext } from '@kit.ArkUI';
4. import { TreeMap } from '@kit.ArkTS';
5. import { fileIo } from '@kit.CoreFileKit';
6. import PcmPlayer from './PcmPlayer';
7. import { audio } from '@kit.AudioKit';
8. import { Context } from '@kit.AbilityKit';

10. const TAG: string = 'TtsDemo';
11. let ttsEngine: textToSpeech.TextToSpeechEngine;
12. let bufferLength: number = 0;
13. let engineCreated: boolean = false;

15. // 定义一个函数来拼接ArrayBuffer
16. function concatenateArrayBuffers(buffers: ArrayBuffer[]): ArrayBuffer {
17. const totalLength = buffers.reduce((sum, buffer) => sum + buffer.byteLength, 0);
18. const concatenatedBuffer = new ArrayBuffer(totalLength);
19. let offset = 0;
20. for (const buffer of buffers) {
21. const uint8Array = new Uint8Array(buffer);
22. new Uint8Array(concatenatedBuffer, offset, uint8Array.length).set(uint8Array);
23. offset += uint8Array.length;
24. }
25. return concatenatedBuffer;
26. }

28. @Entry
29. @Component
30. struct Index {
31. @State createCount: number = 0;
32. // 设置播报内容
33. @State originalText: string = '\n\t\t古人学问无遗力，少壮工夫老始成；\n\t\t' + '纸上得来终觉浅，绝知此事要躬行。\n\t\t';
34. @State uiContext: UIContext = this.getUIContext();
35. @State promptAction: PromptAction = this.uiContext.getPromptAction();
36. private pcmData: TreeMap<number, Uint8Array> = new TreeMap();
37. private pcmPlayer: PcmPlayer = new PcmPlayer();

39. build() {
40. Column() {
41. Scroll() {
42. Column() {
43. TextArea({ placeholder: 'Please enter tts original text', text: `${this.originalText}` })
44. .margin(20)
45. .focusable(false)
46. .border({ width: 5, color: 0x317AE7, radius: 10, style: BorderStyle.Dotted })
47. .onChange((value: string) => {
48. this.originalText = value;
49. console.info(TAG, 'original text: ' + this.originalText);
50. })

52. Button() {
53. Text('CreateEngine')
54. .fontColor(Color.White)
55. .fontSize(20)
56. }
57. .type(ButtonType.Capsule)
58. .backgroundColor('#0x317AE7')
59. .width('80%')
60. .height(50)
61. .margin(10)
62. .onClick(() => {
63. engineCreated = true;
64. this.createCount++;
65. console.info(`createByCallback: createCount:${this.createCount}`);
66. this.createByCallback();
67. try {
68. this.promptAction.showToast({
69. message: 'CreateEngine success!',
70. duration: 2000
71. });
72. } catch (error) {
73. let message = (error as BusinessError).message;
74. let code = (error as BusinessError).code;
75. console.error(`showToast args error code is ${code}, message is ${message}`);
76. }
77. })

79. Button() {
80. Text('speak')
81. .fontColor(Color.White)
82. .fontSize(20)
83. }
84. .type(ButtonType.Capsule)
85. .backgroundColor('#0x317AE7')
86. .width('80%')
87. .height(50)
88. .margin(10)
89. .onClick(() => {
90. if (engineCreated) {
91. try {
92. this.speak();
93. try {
94. this.promptAction.showToast({
95. message: 'start speaking',
96. duration: 2000
97. });
98. } catch (error) {
99. let message = (error as BusinessError).message;
100. let code = (error as BusinessError).code;
101. console.error(`showToast args error code is ${code}, message is ${message}`);
102. }
103. } catch (err) {
104. try {
105. this.promptAction.showToast({
106. message: 'start speaking failed',
107. duration: 2000
108. });
109. } catch (error) {
110. let message = (error as BusinessError).message;
111. let code = (error as BusinessError).code;
112. console.error(`showToast args error code is ${code}, message is ${message}`);
113. }
114. }
115. } else {
116. try {
117. this.promptAction.showToast({
118. message: 'The engine has not been created',
119. duration: 2000
120. });
121. } catch (error) {
122. let message = (error as BusinessError).message;
123. let code = (error as BusinessError).code;
124. console.error(`showToast args error code is ${code}, message is ${message}`);
125. }
126. }
127. })

129. Button() {
130. Text('speakOnData')
131. .fontColor(Color.White)
132. .fontSize(20)
133. }
134. .type(ButtonType.Capsule)
135. .backgroundColor('#0x317AE7')
136. .width('80%')
137. .height(50)
138. .margin(10)
139. .onClick(() => {
140. if (engineCreated) {
141. try {
142. void this.speakOnData();
143. try {
144. this.promptAction.showToast({
145. message: 'start speakOnData',
146. duration: 2000
147. });
148. } catch (error) {
149. let message = (error as BusinessError).message;
150. let code = (error as BusinessError).code;
151. console.error(`showToast args error code is ${code}, message is ${message}`);
152. }
153. } catch (err) {
154. try {
155. this.promptAction.showToast({
156. message: 'start speakOnData failed',
157. duration: 2000
158. });
159. } catch (error) {
160. let message = (error as BusinessError).message;
161. let code = (error as BusinessError).code;
162. console.error(`showToast args error code is ${code}, message is ${message}`);
163. }
164. }
165. } else {
166. try {
167. this.promptAction.showToast({
168. message: 'The engine has not been created',
169. duration: 2000
170. });
171. } catch (error) {
172. let message = (error as BusinessError).message;
173. let code = (error as BusinessError).code;
174. console.error(`showToast args error code is ${code}, message is ${message}`);
175. }
176. }
177. })

179. Button() {
180. Text('stop')
181. .fontColor(Color.White)
182. .fontSize(20)
183. }
184. .type(ButtonType.Capsule)
185. .backgroundColor('#0x317AE7')
186. .width('80%')
187. .height(50)
188. .margin(10)
189. .onClick(() => {
190. try {
191. let isBusy: boolean = ttsEngine.isBusy();
192. let isPlaying: boolean = this.pcmPlayer.isPlaying();
193. if (isBusy) {
194. ttsEngine.stop();
195. }
196. if (isPlaying) {
197. this.pcmPlayer.stop();
198. }
199. try {
200. this.promptAction.showToast({
201. message: 'stop!',
202. duration: 2000
203. });
204. } catch (error) {
205. let message = (error as BusinessError).message;
206. let code = (error as BusinessError).code;
207. console.error(`showToast args error code is ${code}, message is ${message}`);
208. }
209. } catch (err) {
210. try {
211. this.promptAction.showToast({
212. message: 'stop failed',
213. duration: 2000
214. });
215. } catch (error) {
216. let message = (error as BusinessError).message;
217. let code = (error as BusinessError).code;
218. console.error(`showToast args error code is ${code}, message is ${message}`);
219. }
220. }
221. })

223. Button() {
224. Text('isBusy')
225. .fontColor(Color.White)
226. .fontSize(20)
227. }
228. .type(ButtonType.Capsule)
229. .backgroundColor('#0x317AE7')
230. .width('80%')
231. .height(50)
232. .margin(10)
233. .onClick(() => {
234. try {
235. let isBusy: boolean = ttsEngine.isBusy();
236. let isPlaying: boolean = this.pcmPlayer.isPlaying();
237. console.info('isBusy :' + isBusy);
238. console.info('isPlaying :' + isPlaying);
239. try {
240. this.promptAction.showToast({
241. message: 'speak isBusy :' + isBusy + '\nspeakOnData isBusy :' + isPlaying,
242. duration: 2000
243. });
244. } catch (error) {
245. let message = (error as BusinessError).message;
246. let code = (error as BusinessError).code;
247. console.error(`showToast args error code is ${code}, message is ${message}`);
248. }
249. } catch (err) {
250. try {
251. this.promptAction.showToast({
252. message: 'isBusy failed',
253. duration: 2000
254. });
255. } catch (error) {
256. let message = (error as BusinessError).message;
257. let code = (error as BusinessError).code;
258. console.error(`showToast args error code is ${code}, message is ${message}`);
259. }
260. }
261. })

263. Button() {
264. Text('shutdown')
265. .fontColor(Color.White)
266. .fontSize(20)
267. }
268. .type(ButtonType.Capsule)
269. .backgroundColor('#0x317AA7')
270. .width('80%')
271. .height(50)
272. .margin(10)
273. .onClick(() => {
274. try {
275. this.pcmPlayer.release();
276. ttsEngine.shutdown();
277. engineCreated = false;
278. try {
279. this.promptAction.showToast({
280. message: 'shutdown success!',
281. duration: 2000
282. });
283. } catch (error) {
284. let message = (error as BusinessError).message;
285. let code = (error as BusinessError).code;
286. console.error(`showToast args error code is ${code}, message is ${message}`);
287. }
288. } catch (err) {
289. try {
290. this.promptAction.showToast({
291. message: 'shutdown failed',
292. duration: 2000
293. });
294. } catch (error) {
295. let message = (error as BusinessError).message;
296. let code = (error as BusinessError).code;
297. console.error(`showToast args error code is ${code}, message is ${message}`);
298. }
299. }
300. })

302. }
303. .layoutWeight(1)
304. }
305. .width('100%')
306. .height('100%')

308. }
309. }

311. // 创建引擎，通过callback形式返回
312. // 当引擎不存在、引擎资源不存在、初始化超时，返回错误码1002300005，引擎创建失败
313. private createByCallback() {
314. // 设置创建引擎参数
315. let extraParam: Record<string, Object> = { 'style': 'interaction-broadcast', 'locate': 'CN', 'name': 'EngineName' };
316. let initParamsInfo: textToSpeech.CreateEngineParams = {
317. language: 'zh-CN',
318. person: 0,
319. online: 1,
320. extraParams: extraParam
321. };
322. try {
323. // 调用createEngine方法
324. textToSpeech.createEngine(initParamsInfo, (err: BusinessError,
325. textToSpeechEngine: textToSpeech.TextToSpeechEngine) => {
326. if (!err) {
327. console.info('createEngine is success');
328. // 接收创建引擎的实例
329. ttsEngine = textToSpeechEngine;
330. } else {
331. console.error(`error code: ${err.code}, message: ${err.message}.`);
332. }
333. });
334. } catch (error) {
335. let message = (error as BusinessError).message;
336. let code = (error as BusinessError).code;
337. console.error(`createEngine failed, error code: ${code}, message: ${message}.`);
338. }
339. }

341. // 调用speak播报方法
342. private speak() {
343. let speakListener: textToSpeech.SpeakListener = {
344. // 开始播报回调
345. onStart(requestId: string, response: textToSpeech.StartResponse) {
346. console.info(`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}`);
347. },
348. // 完成播报回调
349. onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
350. console.info(`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}`);
351. },
352. // 停止播报完成回调，调用stop方法并完成时会触发此回调
353. onStop(requestId: string, response: textToSpeech.StopResponse) {
354. console.info(`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}`);
355. },
356. // 返回音频流
357. onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
358. console.info(`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}`);
359. },
360. // 错误回调，播报过程发生错误时触发此回调
361. onError(requestId: string, errorCode: number, errorMessage: string) {
362. if (errorCode === 1002300007) {
363. engineCreated = false;
364. }
365. console.error(`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}`);
366. }
367. };
368. // 设置回调
369. ttsEngine.setListener(speakListener);
370. // 设置播报相关参数
371. let extraParam: Record<string, Object> = {
372. 'queueMode': 0,
373. 'speed': 1,
374. 'volume': 2,
375. 'pitch': 1,
376. 'languageContext': 'zh-CN',
377. 'audioType': 'pcm',
378. 'soundChannel': 3,
379. 'playType':1
380. };
381. let speakParams: textToSpeech.SpeakParams = {
382. requestId: '123456' + Date.now(), // requestId在同一实例内仅能用一次，请勿重复设置
383. extraParams: extraParam
384. };
385. // 调用speak播报方法
386. try {
387. ttsEngine.speak(this.originalText, speakParams);
388. } catch (err) {
389. console.error(TAG, `error code: ${err.code}, message: ${err.message}.`);
390. }
391. }

393. private onStart = (utteranceId: string, response: textToSpeech.StartResponse) => {
394. bufferLength = 0;
395. // 初始化音频数据映射
396. console.info(TAG, `onStart | utteranceId: ${ utteranceId }, response: ${JSON.stringify(response)}`);
397. }

399. private onData = (utteranceId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) => {
400. // 将ArrayBuffer转换为Uint8Array
401. let uint8Array: Uint8Array = new Uint8Array(audio);
402. this.pcmData.set(response.sequence, uint8Array);
403. bufferLength += 1;
404. let str = '';
405. // 或者使用循环打印每个元素
406. for (let i = 0; i < uint8Array.length; i++) {
407. str = str + (',' + uint8Array[i]);
408. }
409. console.info(TAG, `onData | utteranceId: ${utteranceId}, sequence: ${JSON.stringify(response.sequence)}, length: ${uint8Array.length}, audio: ${JSON.stringify(str)}`);
410. }

412. private onComplete = (utteranceId: string, response: textToSpeech.CompleteResponse) => {
413. let buffers: ArrayBuffer[] = new Array();

415. console.info(TAG, `pcmData len: ${this.pcmData.length}`);
416. // 遍历Map，将ArrayBuffer添加到数组中
417. try {
418. this.pcmData?.forEach((value: Uint8Array) => {
419. buffers.push(value.buffer.slice(0));
420. })
421. } catch (forEachErr) {
422. console.error(TAG, 'pcmData forEach failed:', forEachErr);
423. }
424. console.info(TAG, `buffers len: ${buffers.length}`);

426. // 按照顺序拼接所有的ArrayBuffer
427. let audioData = concatenateArrayBuffers(buffers);
428. console.info(TAG, `audioData len: ${audioData.byteLength}`);

430. let context = this.uiContext.getHostContext() as Context;
431. let path = context.filesDir;
432. let filePath: string = `${path}/my.pcm`;
433. fileIo.createStream(filePath, 'w+')
434. .then(os => os.write(audioData).catch((e: BusinessError) => {
435. throw new Error(`Write failed: ${e}`)
436. }))
437. .then((): Promise<void> => {
438. try {
439. this.pcmPlayer.file = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY);
440. return this.pcmPlayer.prepare(audio.AudioSamplingRate.SAMPLE_RATE_16000);
441. } catch (e) {
442. throw new Error(`Open failed: ${e}`)
443. }
444. })
445. .then(() => this.pcmPlayer.play(audioData))
446. .catch((err: BusinessError) => console.error(TAG, `Error: ${err}`));

448. console.info(TAG, `onComplete | utteranceId: ${utteranceId}, response: ${JSON.stringify(response)}`);
449. }

451. // 调用speakOnData播报方法
452. // 未初始化引擎时调用speak方法，返回错误码1002300007，合成及播报失败
453. private speakOnData() {
454. // 设置播报相关参数
455. let extraParam: Record<string, Object> = {
456. 'queueMode': 0,
457. 'speed': 1.2,
458. 'volume': 2,
459. 'pitch': 1,
460. 'languageContext': 'zh-CN',
461. 'audioType': 'pcm',
462. 'soundChannel': 1,
463. 'playType':0
464. };
465. let speakParams: textToSpeech.SpeakParams = {
466. requestId: '1234567' + Date.now(),
467. extraParams: extraParam
468. };

470. try {
471. // 创建回调对象
472. let speakListener: textToSpeech.SpeakListener = {
473. // 开始识别成功回调
474. onStart: this.onStart,
475. // 识别完成回调
476. onComplete: this.onComplete,
477. // 停止播报回调
478. onStop(utteranceId: string, response: textToSpeech.StopResponse) {
479. console.info('speakListener onStop: ' + ' utteranceId: ' + utteranceId + ' response: ' + JSON.stringify(response));
480. },
481. // 返回音频流
482. onData: this.onData,
483. // 错误回调
484. onError(utteranceId: string, errorCode: number, errorMessage: string) {
485. if (errorCode === 1002300007) {
486. engineCreated = false;
487. }
488. console.error('speakListener onError: ' + ' utteranceId: ' + utteranceId + ' errorCode: ' + errorCode + ' errorMessage: ' + errorMessage);
489. }
490. };
491. // 设置回调
492. ttsEngine.setListener(speakListener);
493. try {
494. console.info(`speakListener before speak`);
495. // 调用speak播报方法
496. for (let i = 0; i < 1; i++) {
497. ttsEngine?.speak(this.originalText, speakParams);
498. }
499. console.info(`speakListener after speak`)
500. } catch (error) {
501. let message = (error as BusinessError).message;
502. let code = (error as BusinessError).code;
503. console.error(`speakListener speak failed, error code: ${code}, message: ${message}.`);
504. }
505. } catch (error) {
506. let message = (error as BusinessError).message;
507. let code = (error as BusinessError).code;
508. console.error(`speakListener setListener failed, error code: ${code}, message: ${message}.`);
509. }
510. }
511. }
```

### PcmPlayer.ets

```
1. import { audio } from '@kit.AudioKit';
2. import { fileIo } from '@kit.CoreFileKit';

4. const TAG = 'PCM_audio';

6. class Options {
7. offset?: number;
8. length?: number;
9. }

11. export default class PcmPlayer {

13. public file: fileIo.File | undefined;
14. private writeDataCallback = (buffer: ArrayBuffer) => {
15. let options: Options = {
16. offset: this.bufferSize,
17. length: buffer.byteLength
18. };

20. try {
21. fileIo.readSync(this.file?.fd, buffer, options);
22. this.bufferSize += buffer.byteLength;
23. if (this.audioDataSize < this.bufferSize) {
24. this.renderModel?.off('writeData');
25. void this.stop()
26. }
27. console.info(TAG, 'reading file success');
28. // 系统会判定buffer有效，正常播放。
29. return audio.AudioDataCallbackResult.VALID;
30. } catch (error) {
31. console.error(TAG, `Reading file failed, error code: ${error.code}, message: ${error.message}.`);
32. // 系统会判定buffer无效，不播放。
33. return audio.AudioDataCallbackResult.INVALID;
34. }
35. };
36. /**
37. * 缓存大小
38. */
39. private bufferSize: number = 0;
40. /**
41. * 音频总大小
42. */
43. private audioDataSize: number = 0;
44. /**
45. * 播放器
46. */
47. private renderModel: audio.AudioRenderer | null = null;
48. /**
49. * 播放状态
50. */
51. private audioStreamInfo: audio.AudioStreamInfo = {
52. samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_16000, // 采样率
53. channels: audio.AudioChannel.CHANNEL_1, // 通道
54. sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式
55. encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式
56. };
57. private audioRendererInfo: audio.AudioRendererInfo = {
58. usage: audio.StreamUsage.STREAM_USAGE_ACCESSIBILITY, // 音频流使用类型
59. rendererFlags: 0 // 音频渲染器标志
60. };
61. private audioRendererOptions: audio.AudioRendererOptions = {
62. streamInfo: this.audioStreamInfo,
63. rendererInfo: this.audioRendererInfo
64. };

66. public async prepare(sampleRate: number) {
67. this.audioRendererOptions.streamInfo.samplingRate = sampleRate;
68. this.audioRendererOptions.rendererInfo.usage = audio.StreamUsage.STREAM_USAGE_MUSIC;
69. if (this.renderModel != null) {
70. await this.renderModel.release();
71. }
72. let renderModel = await audio.createAudioRenderer(this.audioRendererOptions);
73. if (!renderModel) {
74. console.error(TAG, `failed to create audio renderer`);
75. }
76. console.info(TAG, 'creating AudioRenderer success');
77. this.renderModel = renderModel;
78. this.bufferSize = await this.renderModel.getBufferSize();
79. }

81. public async play(data: ArrayBuffer): Promise<number> {
82. this.audioDataSize = data.byteLength
83. if (this.renderModel != null) {
84. try {
85. this.renderModel.on('writeData', this.writeDataCallback);
86. } catch (err) {
87. console.error(`error code: ${err.code}, message: ${err.message}.`);
88. }
89. // 启动渲染
90. await this.renderModel.start();
91. console.info(TAG, 'start AudioRenderer success');
92. }
93. return -1;
94. }

96. public async stop() {
97. console.info(TAG, 'Renderer begin stop');
98. if (this.renderModel == null) {
99. return;
100. }

102. // 只有渲染器状态为running或paused的时候才可以停止
103. if (this.renderModel.state !== audio.AudioState.STATE_RUNNING
104. && this.renderModel.state !== audio.AudioState.STATE_PAUSED) {
105. console.error(TAG, 'Renderer is not running or paused');
106. return;
107. }
108. await this.renderModel.stop(); // 停止渲染
109. console.info(TAG, 'Renderer stopped');
110. }

112. public async release() {
113. // 渲染器状态不是released状态，才能release
114. if (this.renderModel != null) {
115. if (this.renderModel.state === audio.AudioState.STATE_RELEASED) {
116. console.error(TAG, 'Renderer already released');
117. return;
118. }
119. await this.renderModel.release(); // 释放资源
120. this.renderModel = null;
121. console.info(TAG, 'Renderer released');
122. }
123. }

125. /**
126. * 判断当前渲染状态
127. *
128. * @returns running返回true，否则返回false
129. */
130. public isPlaying() {
131. if (this.renderModel != null) {
132. console.info(TAG, 'player.state:' + this.renderModel.state);
133. return this.renderModel.state == audio.AudioState.STATE_RUNNING;
134. } else {
135. return false;
136. }
137. }

139. /**
140. * 获取当前渲染状态
141. *
142. * @returns running返回true，否则返回false
143. */
144. public getRenderState(): number {
145. if (this.renderModel != null) {
146. console.info(TAG, 'player.state:' + this.renderModel.state);
147. return this.renderModel.state;
148. } else {
149. return audio.AudioState.STATE_INVALID;
150. }
151. }

153. /**
154. * 获取音频渲染器的最小缓冲区大小
155. */
156. public getBufferSize(): number {
157. return this.bufferSize;
158. }
159. }
```
