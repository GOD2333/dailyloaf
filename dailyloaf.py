from hoshino import Service, util
from hoshino.typing import MessageSegment, CQHttpError, CQEvent, HoshinoBot
from hoshino import aiorequests
sv = Service('摸鱼人日历', enable_on_default=False, help_='''每日摸鱼
启用后会在每天早上发送一份摸鱼日历
[@bot 今日摸鱼] （测试用）手动发送一份早报''')


@sv.scheduled_job('cron', hour='8', minute='40', jitter=50)
async def autoloaf():
    try:
        info = await aiorequests.get('https://api.j4u.ink/v1/store/other/proxy/remote/moyu.json')
        try:
            info = await info.json()
        except:
            print(await info.text)
            raise
        if info['message'] == 'success':
            await sv.broadcast(
                MessageSegment.image(info['data']['moyu_url'], cache=True), 'dailyloaf')
        else:
            sv.logger.error(f'daily loaf error {info["msg"]}')
    except CQHttpError as e:
        sv.logger.error(f'daily loaf error {e}')
        raise


@sv.on_fullmatch('今日摸鱼', only_to_me=True)
async def handloaf(bot: HoshinoBot, ev: CQEvent):
    info = await aiorequests.get('https://api.j4u.ink/v1/store/other/proxy/remote/moyu.json')
    info = await info.json()
    if info['message'] == 'success':
        await bot.send(ev, MessageSegment.image(info['data']['moyu_url'], cache=True))
    else:
        sv.logger.error(f'error {info["message"]}')
