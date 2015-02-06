import re
import znc


class CloudToButt(znc.Module):
    description = "Cloud to Butt, for ZNC"
    module_types = [znc.CModInfo.UserModule, znc.CModInfo.NetworkModule, znc.CModInfo.GlobalModule]
    cloud_re = re.compile(r"cloud", re.I)

    def OnChanMsg(self, nick, chan, msg):
        if self.cloud_re.search(msg.s):
            new_msg = re.sub('Cloud', 'Butt', msg.s)
            new_msg = re.sub('CLOUD', 'BUTT', new_msg)
            new_msg = re.sub('cloud', 'butt', new_msg)
            self.PutUser(":{0}!{1}@{2} PRIVMSG {3} :{4}".format(
                nick.GetNick(),
                nick.GetIdent(),
                nick.GetHost(),
                chan,
                new_msg
            ))
            return znc.HALTCORE
