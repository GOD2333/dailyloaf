# dailyloaf  摸鱼人日历
一个很简单的每日摸鱼日报

## 安装方法
### 懒人法
&emsp;&emsp;将`dailyloaf.py`丢入任意一个已启用模块中然后重启hoshino
### 不是懒人法
* 在`HoshinoBot\hoshino\modules`下新建一个文件夹
* 将`dailyloaf.py`放入其中
* 在 `HoshinoBot\hoshino\config\__bot__.py` 文件的 `MODULES_ON` 里加入新建的文件夹的名字
* 重启hoshino
## 依赖要求
aiocqhttp>=1.4
>如果你的[Hoshino](https://github.com/Ice-Cirno/HoshinoBot)一直保持最新版本，那一定符合此要求

如果你在使用旧版本并且不愿意更新，可以将代码中两处使用`MessageSegment.image`的地方将`cache`参数去掉，该参数的作用是避免重复下载
## 使用方式
[启用 dailyloaf] 插件默认禁用，需要手动开启

启用后，将会在每天早上发送一份摸鱼日历

[@bot 今日摸鱼] （测试用）手动获取一份摸鱼日历
## 注意
* 自动推送偶尔会发生读取json出错的情况，推测可能是网络波动
## 鸣谢
[Hoshino](https://github.com/Ice-Cirno/HoshinoBot) <s>星乃真好玩</s>

## 感谢api作者
[https://api.emoao.com/api/moyu](https://api.emoao.com/api/moyu)返回格式：图片

[https://api.vvhan.com/api/moyu](https://api.vvhan.com/api/moyu)返回格式：图片

[https://api.emoao.com/api/moyu?type=json](https://api.emoao.com/api/moyu?type=json)返回格式：JSON

[https://api.j4u.ink/v1/store/other/proxy/remote/moyu.json](https://api.j4u.ink/v1/store/other/proxy/remote/moyu.json)返回格式：JSON




![预览图片](https://static.4ce.cn/star3/origin/3fc3e7792b64aef3eb398c0fd3089828.png?rw=540&rh=804&_fileSize=864236&_orientation=1 "摸鱼人日历 预览图")

## License
This project is licensed under [GLWTPL](https://github.com/me-shaon/GLWTPL/blob/master/LICENSE)
