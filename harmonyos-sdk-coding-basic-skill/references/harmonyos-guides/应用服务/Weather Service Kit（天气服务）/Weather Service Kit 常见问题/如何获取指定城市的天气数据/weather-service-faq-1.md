---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/weather-service-faq-1
title: 如何获取指定城市的天气数据
breadcrumb: 指南 > 应用服务 > Weather Service Kit（天气服务） > Weather Service Kit 常见问题 > 如何获取指定城市的天气数据
category: harmonyos-guides
scraped_at: 2026-06-01T15:12:22+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:a95e9c2a54b53043e0d5c83e18b4ae1f8d9c6a094ee5f93bbfce1914d48fbd77
---
先调用[getAddressesFromLocationName](<../../../../../harmonyos-references/Location Kit（位置服务）/ArkTS API/@ohos.geoLocationManager (位置服务)/js-apis-geolocationmanager.md#geolocationmanagergetaddressesfromlocationname-1>)方法获取指定城市的经纬度信息，然后根据返回的经纬度数据调用[getWeather](<../../../../../harmonyos-references/Weather Service Kit（天气服务）/ArkTS API/weatherService（天气数据服务）/weather-service-weatherservice.md#weatherservicegetweather>)方法获取天气数据。
