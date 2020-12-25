#!/usr/bin/python3

import getPTTDB
import setSQL
import time
from push_text import push_text

while True:
    try:
        getPTTDB.get_ptt_data()
        print('批次資料儲存成功!　' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        push = setSQL.auto_push_message()
        token = setSQL.get_alluser_token()
        if push and token:
            for p in push:
                for t in token:
                    push_text(t, p)
        else:
            pass
    except Exception:
        print('批次資料儲存失敗，請檢查設定!' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    time.sleep(60)