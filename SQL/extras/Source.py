import re
import time
from datetime import datetime
from IqArab import StartTime, iqthon
from IqArab.Config import Config
from IqArab.plugins import mention
help1 = ("**⁂ ⦙ كيفيه التنصيب :**")
help2 = ("**⁂ ⦙ قـائمـه الاوامـر :**\n**⁂ ⦙ قنـاه السـورس :** @dev_albrans\n**⁂ ⦙ شـرح اوامـر السـورس : @albrans00** \n\n**❕- اوامر الاونلاين تشتغل فقط في مجموعات التخزين لاغير\n - اذا كنت تريد الاوامر العادية أرسل (.م) **")
TG_BOT = Config.TG_BOT_USERNAME
TM = time.strftime("%I:%M")
Sour = f"**‎⿻┊My ⁂ {mention} ٫ **\n‌‎**⿻┊BoT ⁂ {TG_BOT} ٫**\n**‌‎⿻┊TimE ⁂ {TM} ٫**\n**‌‎⿻┊‌‎VeRsIoN ⁂ (8.3) ,** \n**⿻┊‌‎SoUrCe AlBrAnS ⁂** @dev_albrans"
