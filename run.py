import getPTTDB
import setSQL
import time

while True:
    try:
        getPTTDB.get_ptt_data()
        print('批次資料儲存成功!　' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        push = setSQL.auto_push_message()
        if push:
            for p in push:
                pass
        else:
            pass
    except Exception:
        print('批次資料儲存失敗，請檢查設定!' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    time.sleep(60)