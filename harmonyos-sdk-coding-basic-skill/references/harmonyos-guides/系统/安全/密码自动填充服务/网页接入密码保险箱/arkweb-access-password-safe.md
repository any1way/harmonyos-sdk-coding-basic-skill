---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkweb-access-password-safe
title: 网页接入密码保险箱
breadcrumb: 指南 > 系统 > 安全 > 密码自动填充服务 > 网页接入密码保险箱
category: harmonyos-guides
scraped_at: 2026-06-11T14:40:26+08:00
doc_updated_at: 2026-06-09
content_hash: sha256:60f0c1068b823304263dadd54eb2837a7535109ccf38c2272f9d9759affc1bfa
---

网页中的登录表单，登录成功后，用户可将用户名和密码保存到系统密码保险箱中。再次打开该网页时，密码保险箱可以提供用户名、密码的自动填充。

## 手机使用场景

以下以<https://developer.huawei.com/>网站为例：

1. 在网站中输入用户名、密码，登录成功后，ArkWeb会提示将用户名和密码保存到密码保险箱中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/Fv4NeaWFT12DU1iQturaHg/zh-cn_image_0000002622858225.png?HW-CC-KV=V1&HW-CC-Date=20260611T064025Z&HW-CC-Expire=86400&HW-CC-Sign=04E9EC21CB4C8F6888C794C094CD7B75AB0675797B6FF38F6A81CDA6AB1B4A42)
2. 再次打开相同的网站，点击用户名或者密码框中时，会弹出密码保险箱的填充提示。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/u1Kh56UCS8SsNDSircUm8A/zh-cn_image_0000002622698347.png?HW-CC-KV=V1&HW-CC-Date=20260611T064025Z&HW-CC-Expire=86400&HW-CC-Sign=E06FAFEFC4363865D042515B940C672ACBBFF764FC3124B6C3B9A7B2C160357A)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/nVwbp5BaRNuZVuLADVqh5Q/zh-cn_image_0000002592218786.png?HW-CC-KV=V1&HW-CC-Date=20260611T064025Z&HW-CC-Expire=86400&HW-CC-Sign=46F777C81E15DA6F6D03B9B9FD9E99BCA7903A9D484A4CBB96280C93A320C22A)
3. 可以选择提示框中的用户名，通过认证，就能直接在网页中填入之前保存的用户名、密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/f2GfJs3-ToSYiP97T0i--w/zh-cn_image_0000002592378720.png?HW-CC-KV=V1&HW-CC-Date=20260611T064025Z&HW-CC-Expire=86400&HW-CC-Sign=6D288C648291E4C5AFDF6432E3F54A83C03A01BE26E57A723BB893F2F667A6C5)
4. 点击“使用其他账号”，选择密码保险箱中保存的其他账号。认证后在网页中填入选择的用户名、密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/kcXuVNsxRf2qWo4CNjojRQ/zh-cn_image_0000002622858227.png?HW-CC-KV=V1&HW-CC-Date=20260611T064025Z&HW-CC-Expire=86400&HW-CC-Sign=9DE9F029EF4811081D1855115CE5CAD191AC136679AE4337AB0DEBD05F2DCA82)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/KUhKgN9DT7KUClnAM5l9aQ/zh-cn_image_0000002622698349.png?HW-CC-KV=V1&HW-CC-Date=20260611T064025Z&HW-CC-Expire=86400&HW-CC-Sign=5D66A7C5A1ECA5872BDE1920CE98A04D3D618952469B6FFF9DD148651C2C687F)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/MGzeeMBBRPOx4MxeCVdZxA/zh-cn_image_0000002592218788.png?HW-CC-KV=V1&HW-CC-Date=20260611T064025Z&HW-CC-Expire=86400&HW-CC-Sign=6EA597DEB6182D65D6EDE0BB8233BB523E0EB79D039ECFD5E3627608EA7E2C95)
5. 点击“手动输入”或者提示框之外的地方，会弹出小艺输入法，会提示可用于密码填充的用户名和钥匙图标。

   点击用户名可触发在网页中填入用户名、密码；点击钥匙图标，进入选择账号的界面。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/BMad3VWvRuisC8b5iY0kug/zh-cn_image_0000002592378722.png?HW-CC-KV=V1&HW-CC-Date=20260611T064025Z&HW-CC-Expire=86400&HW-CC-Sign=871BD1BBE58024E389AB1495AE78261F583240A2A084E8B4482DD508FDB02729)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/4oW4lzHKS1eJWXWKnngKYA/zh-cn_image_0000002622858229.png?HW-CC-KV=V1&HW-CC-Date=20260611T064025Z&HW-CC-Expire=86400&HW-CC-Sign=1B5B820F5C3518F185D0A051E434753F58627FB0BD954392586DA309B5413D24)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/N3EHBPxdRbWdl9-VjfEW3A/zh-cn_image_0000002622698351.png?HW-CC-KV=V1&HW-CC-Date=20260611T064025Z&HW-CC-Expire=86400&HW-CC-Sign=7200D2CBB1D00C77B6F4DF26123962634C5A1F2DC19FCC2493118D894E38BE4A)

## 2in1使用场景

以下以<https://developer.huawei.com/>网站为例：

1. 在网站中输入用户名、密码，登录成功后，ArkWeb会提示将用户名和密码保存到密码保险箱中。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/-YRXz1ZCT02pg4Zs4Rybcg/zh-cn_image_0000002592218790.png?HW-CC-KV=V1&HW-CC-Date=20260611T064025Z&HW-CC-Expire=86400&HW-CC-Sign=5499C246599B6368E2E582755F8EF9FF1C484292F4AE377F23B626FEA3756FAF)
2. 再次打开相同的网站，点击用户名或者密码框中时，会弹出密码保险箱的下拉框。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/pABdOHPmSUSAsjm-QuI8nA/zh-cn_image_0000002592378724.png?HW-CC-KV=V1&HW-CC-Date=20260611T064025Z&HW-CC-Expire=86400&HW-CC-Sign=FB93ABA8F47368C6A57F041659DBA85500B447520C8CFCA772412399FC699358)
3. 选择下拉框中的用户名，通过认证，就能直接在网页中填入之前保存的用户名、密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/MX1ykfz1RkuN0GJwCSMRAQ/zh-cn_image_0000002622858231.png?HW-CC-KV=V1&HW-CC-Date=20260611T064025Z&HW-CC-Expire=86400&HW-CC-Sign=E99BF9ABD30CA36D8BCA1D00EBD5B9B077E8A1E7289B87BAD28EF5EB32BDCACC)
4. 也可以点击下拉框中的“使用其他账号”，选择密码保险箱中保存的其他账号。认证后在网页中填入选择的用户名、密码。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/j-ZJOBNzSYaob7DM3no9KQ/zh-cn_image_0000002622698353.png?HW-CC-KV=V1&HW-CC-Date=20260611T064025Z&HW-CC-Expire=86400&HW-CC-Sign=96CE13C142B38C28155872B8FB26F4F0EEA06C453C1678353398D5789F6A95C0)

## 网页密码保存规格

1、ArkWeb依赖密码表单提交成功后，触发页面跳转到其他页面，才能触发密码保存。

2、Native应用通过ArkWeb实现H5登录，登录成功后请勿立即销毁ArkWeb实例，否则将无法提示密码保存。

## 网页密码表单规格

ArkWeb使用Chromium智能算法，自动识别网页中的用户名、密码元素。算法对用户名、密码表单的设计，有一定的约束。

### 推荐的密码登录表单

1. 使用静态的登录页面或登录表单元素，而不是通过js脚本在页面中动态插入<form>、<input>等表单元素。
2. 用户名密码输入框均使用<input>元素实现，并集成在同一个<form>内，默认可编辑，登录场景有且最多有一个type="password"类型的<input>元素。
3. 点击按钮触发登录，登录成功后，应当触发跳转到新的页面。
4. 用户名框携带autocomplete=“username”，携带id或name属性，并采用如下建议的值，便于算法推断用户名元素：

   ```
   1. const char* const kUsernameLatin[] = {
   2. "gatti",      "uzantonomo",   "solonanarana",    "nombredeusuario",
   3. "olumulo",    "nomenusoris",  "enwdefnyddiwr",   "nomdutilisateur",
   4. "lolowera",   "notandanafn",  "nomedeusuario",   "vartotojovardas",
   5. "username",   "ahanjirimara", "gebruikersnaam",  "numedeutilizator",
   6. "brugernavn", "benotzernumm", "jinalamtumiaji",  "erabiltzaileizena",
   7. "brukernavn", "benutzername", "sunanmaiamfani",  "foydalanuvchinomi",
   8. "mosebedisi", "kasutajanimi", "ainmcleachdaidh", "igamalomsebenzisi",
   9. "nomdusuari", "lomsebenzisi", "jenengpanganggo", "ingoakaiwhakamahi",
   10. "nomeutente", "namapengguna"};

   12. const char* const kUserLatin[] = {
   13. "user",   "wosuta",   "gebruiker",  "utilizator",
   14. "usor",   "notandi",  "gumagamit",  "vartotojas",
   15. "fammi",  "olumulo",  "maiamfani",  "cleachdaidh",
   16. "utent",  "pemakai",  "mpampiasa",  "umsebenzisi",
   17. "bruger", "usuario",  "panganggo",  "utilisateur",
   18. "bruker", "benotzer", "uporabnik",  "doutilizador",
   19. "numake", "benutzer", "covneegsiv", "erabiltzaile",
   20. "usuari", "kasutaja", "defnyddiwr", "kaiwhakamahi",
   21. "utente", "korisnik", "mosebedisi", "foydalanuvchi",
   22. "uzanto", "pengguna", "mushandisi"};

   24. const char* const kUsernameNonLatin[] = {
   25. "用户名", "کاتيجونالو", "用戶名", "የተጠቃሚስም",
   26. "логин", "اسمالمستخدم", "נאמען", "کاصارفکانام",
   27. "ユーザ名", "όνομα χρήστη", "brûkersnamme", "корисничкоиме",
   28. "nonitilizatè", "корисничкоиме", "ngaranpamaké", "ຊື່ຜູ້ໃຊ້",
   29. "användarnamn", "యూజర్పేరు", "korisničkoime", "пайдаланушыаты",
   30. "שםמשתמש", "ім'якористувача", "کارننوم", "хэрэглэгчийннэр",
   31. "nomedeusuário", "имяпользователя", "têntruynhập", "பயனர்பெயர்",
   32. "ainmúsáideora", "ชื่อผู้ใช้", "사용자이름", "імякарыстальніка", "lietotājvārds",
   33. "потребителскоиме", "uporabniškoime", "колдонуучунунаты", "kullanıcıadı",
   34. "පරිශීලකනාමය", "istifadəçiadı", "օգտագործողիանունը", "navêbikarhêner", "ಬಳಕೆದಾರಹೆಸರು",
   35. "emriipërdoruesit", "वापरकर्तानाव", "käyttäjätunnus", "વપરાશકર્તાનામ", "felhasználónév",
   36. "उपयोगकर्तानाम", "nazwaużytkownika", "ഉപയോക്തൃനാമം", "სახელი", "အသုံးပြုသူအမည်",
   37. "نامکاربری", "प्रयोगकर्तानाम", "uživatelskéjméno", "ব্যবহারকারীরনাম",
   38. "užívateľskémeno", "ឈ្មោះអ្នកប្រើប្រាស់"};

   40. const char* const kUserNonLatin[] = {
   41. "用户", "użytkownik", "tagatafaʻaaogā", "دکارونکيعکس",
   42. "用戶", "užívateľ", "корисник", "карыстальнік",
   43. "brûker", "kullanıcı", "истифода", "អ្នកប្រើ",
   44. "ọrụ", "ተጠቃሚ", "באַניצער", "хэрэглэгчийн",
   45. "يوزر", "istifadəçi", "ຜູ້ໃຊ້", "пользователь",
   46. "صارف", "meahoʻohana", "потребител", "वापरकर्ता",
   47. "uživatel", "ユーザー", "מִשׁתַמֵשׁ", "ผู้ใช้งาน",
   48. "사용자", "bikaranîvan", "колдонуучу", "વપરાશકર્તા",
   49. "përdorues", "ngườidùng", "корисникот", "उपयोगकर्ता",
   50. "itilizatè", "χρήστης", "користувач", "օգտվողիանձնագիրը",
   51. "használó", "faoiúsáideoir", "შესახებ", "ব্যবহারকারী",
   52. "lietotājs", "பயனர்", "ಬಳಕೆದಾರ", "ഉപയോക്താവ്",
   53. "کاربر", "యూజర్", "පරිශීලක", "प्रयोगकर्ता", "användare",
   54. "المستعمل", "пайдаланушы", "အသုံးပြုသူကို", "käyttäjä"};

   56. const char* const kTechnicalWords[] = {
   57. "uid",         "newtel",     "uaccount",   "regaccount",  "ureg",
   58. "loginid",     "laddress",   "accountreg", "regid",       "regname",
   59. "loginname",   "membername", "uname",      "ucreate",     "loginmail",
   60. "accountname", "umail",      "loginreg",   "accountid",   "loginaccount",
   61. "ulogin",      "regemail",   "newmobile",  "accountlogin"};

   63. const char* const kWeakWords[] = {"id", "login", "mail"};
   ```
5. 登录场景，密码框携带autocomplete=“current-password”。
6. 用户名框下面紧挨密码框，中间不要插入其他<input>元素（包括不可见的<input>）。
7. 静态页面中的用户名密码框不可见，则需要确保在静态页面中就存在，而不是跳转页面时插入密码表单。

【案例1】：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/c3KgxOH6Tq2YfBUNtb_0aQ/zh-cn_image_0000002592218792.png?HW-CC-KV=V1&HW-CC-Date=20260611T064025Z&HW-CC-Expire=86400&HW-CC-Sign=B5F5E0217F4442C335F86B583F180E50DF33F705D4A4547C5E552DDB94A6E9D1)

【案例2】：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/b_3czQZYRzWz7XzPHVLh_w/zh-cn_image_0000002592378726.png?HW-CC-KV=V1&HW-CC-Date=20260611T064025Z&HW-CC-Expire=86400&HW-CC-Sign=95561C3982964864D92E32EB0B46AEA1B8356A5DCA14B287ED1DBC0FE2FBFE06)

### 不支持自动填充的密码登录表单类型

1. 初始页面内无用户名密码表单元素，点击登录跳转页面后，新增非<form>类型的用户名密码表单。
2. 密码输入框携带了autocomplete=“new-password”属性。
3. 用户名输入框type="number"，验证码输入框type="number"，无密码输入框。
4. 用户名和密码元素中间存在其他<input>元素，算法推断出的用户名元素，不符合用户预期。
5. 网页通过javascript脚本，变更了<input>元素的焦点或者修改<input>元素的value。
6. 用户名<input>元素上id、name、label内容中匹配到如下密码类型标识：

   ```
   1. const char* const kNegativeLatin[] = {
   2. "pin",    "parola",   "wagwoord",   "wachtwoord",
   3. "fake",   "parole",   "givenname",  "achinsinsi",
   4. "token",  "parool",   "firstname",  "facalfaire",
   5. "fname",  "lozinka",  "pasahitza",  "focalfaire",
   6. "lname",  "passord",  "pasiwedhi",  "iphasiwedi",
   7. "geslo",  "huahuna",  "passwuert",  "katalaluan",
   8. "heslo",  "fullname", "phasewete",  "adgangskode",
   9. "parol",  "optional", "wachtwurd",  "contrasenya",
   10. "sandi",  "lastname", "cyfrinair",  "contrasinal",
   11. "senha",  "kupuhipa", "katasandi",  "kalmarsirri",
   12. "password", "loluszais",  "tenimiafina",
   13. "second", "passwort", "middlename", "paroladordine",
   14. "codice", "pasvorto", "familyname", "inomboloyokuvula",
   15. "modpas", "salasana", "motdepasse", "numeraeleiloaesesi",
   16. "captcha"};

   18. const char* const kNegativeNonLatin[] = {
   19. "fjalëkalim", "የይለፍቃል", "كلمهالسر", "գաղտնաբառ",
   20. "пароль", "পাসওয়ার্ড", "парола", "密码", "密碼",
   21. "დაგავიწყდათ", "κωδικόςπρόσβασης", "પાસવર્ડ", "סיסמה",
   22. "पासवर्ड", "jelszó", "lykilorð", "paswọọdụ",
   23. "パスワード", "ಪಾಸ್ವರ್ಡ್", "пароль", "ការពាក្យសម្ងាត់",
   24. "암호", "şîfre", "купуясөз", "ລະຫັດຜ່ານ",
   25. "slaptažodis", "лозинка", "पासवर्ड", "нууцүг",
   26. "စကားဝှက်ကို", "पासवर्ड", "رمز", "کلمهعبور",
   27. "hasło", "пароль", "лозинка", "پاسورڊ",
   28. "මුරපදය", "contraseña", "lösenord", "гузарвожа",
   29. "கடவுச்சொல்", "పాస్వర్డ్", "รหัสผ่าน", "пароль",
   30. "پاسورڈ", "mậtkhẩu", "פּאַראָל", "ọrọigbaniwọle"};
   ```
7. 用户名<input>元素的autocomplete="one-time-code"或者"cc-\*"，或者id、name属性上能正则匹配到如下one-time-code或者信用卡标识：

   ```
   1. inline constexpr char16_t kOneTimePwdRe[] =
   2. u"one.?time|sms.?(code|token|password|pwd|pass)";

   4. inline constexpr char16_t kCardCvcRe[] =
   5. u"verification|card.?identification|security.?code|card.?code"
   6. u"|security.?value"
   7. u"|security.?number|card.?pin|c-v-v"
   8. u"|código de segurança"  // pt-BR
   9. u"|código de seguridad"  // es-MX
   10. u"|karten.?prüfn"        // de-DE
   11. u"|(?:cvn|cvv|cvc|csc|cvd|ccv)"
   12. // We used to match "cid", but it is a substring of "cidade" (Portuguese for
   13. // "city") and needs to be handled carefully.
   14. u"|\\bcid\\b|cccid";
   ```
8. 页面加载完成，<input>的type属性不是"password"，点击登录才变成"password"类型。
