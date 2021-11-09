Run_buffer 體溫偵測的緩衝
locks  鎖 控制Process 內fuction用   0(add Noise) , 1(default) ,3 (off)
sound_bools 接收Noise True 的次數 ,根據次數播放警告音

Process class:

1.Daemon_buffer  tempeature用
2.sound_deamon   Noise 用 
3.未設置停止訊號故每次只能從新要資源,多次後將會造成cpu 使用率過高。