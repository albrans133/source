# تخمط اذكر المصدر اهينك وربي .
#سينزر الهيبه يولد هههههههههههاي🤣🤣 .

from telethon.tl.functions.messages import GetMessagesViewsRequest
import sys, asyncio
import senzir
from senzir import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID
from telethon import functions
from .Config import Config
from .core.logger import logging
from .core.session import senzir
from .utils import add_bot_to_logger_group, load_plugins, setup_bot, startupmessage, verifyLoggerGroup ,setinlinemybot,iqchn
LOGS = logging.getLogger("𝗔𝗟𝗕𝗥𝗔𝗡𝗦")
print(senzir.__copyright__)
print("المرخصة بموجب شروط " + senzir.__license__)
cmdhr = Config.COMMAND_HAND_LER
try:
    LOGS.info("بدء تنزيل سورس البرنس ")
    senzir.loop.run_until_complete(setup_bot())
    LOGS.info("بدء تشغيل البوت")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()
try:
    LOGS.info("يتم تفعيل وضع الانلاين")
    senzir.loop.run_until_complete(setinlinemybot())
    LOGS.info("تم تفعيل وضع الانلاين بنجاح ✓")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()    
try:
    LOGS.info("يتم تفعيل القنوات")
    senzir.loop.run_until_complete(iqchn())
    LOGS.info("تم تفعيل القنوات ✓")
except Exception as e:
    LOGS.error(f"{str(e)}")
    sys.exit()



class CatCheck:
    def __init__(self):
        self.sucess = True
Catcheck = CatCheck()
async def startup_process():
    async def MarkAsViewed(channel_id):
        from telethon.tl.functions.channels import ReadMessageContentsRequest
        try:
            channel = await senzir.get_entity(channel_id)
            async for message in senzir.iter_messages(entity=channel.id, limit=5):
                try:
                    await senzir(GetMessagesViewsRequest(peer=channel.id, id=[message.id], increment=True))
                except Exception as error:
                    print ("🔻")
            return True

        except Exception as error:
            print ("🔻")

    async def start_bot():
      try:
          List = ["IC_X_K","HH_7_T","dev_albrans"].  #code by t.me/IC_X_K
          from telethon.tl.functions.channels import JoinChannelRequest
          for id in List :
              try:
                  Join = await senzir(JoinChannelRequest(channel=id))
                  MarkAsRead = await MarkAsViewed(id)
              except Exception as e:
                  print (f"🔻 [ start_bot ] - {e}")
          return True
      except Exception as e:
        print("🔻")
        return False
    
    await verifyLoggerGroup()
    await load_plugins("plugins")
    await load_plugins("assistant")
    print(f"<b> 🔱 اهلا بك لقد نصبت سورس البرنس بنجاح ☸️ اذهب الى قناتنا لمعرفة المزيـد v8.3 🔆. </b>\n CH : https://t.me/dev_albrans ")
    await verifyLoggerGroup()
    await add_bot_to_logger_group(BOTLOG_CHATID)
    if PM_LOGGER_GROUP_ID != -100:
        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
    await startupmessage()
    Catcheck.sucess = True
    
    Checker = await start_bot()
    if Checker == False:
        print("#1")
    else:
        print ("🔻")
    
    return


senzir.loop.run_until_complete(startup_process())
    
if len(sys.argv) not in (1, 3, 4):
    senzir.disconnect()
elif not Catcheck.sucess:
    if HEROKU_APP is not None:
        HEROKU_APP.restart()
else:
    try:
        senzir.run_until_disconnected()
    except ConnectionError:
        pass
